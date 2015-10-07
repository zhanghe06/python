# encoding: utf-8
__author__ = 'zhanghe'

"""
The MIT License
Copyright (c) 2005 hoxide
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
QQ Crypt module.
"""

from struct import pack as _pack
from struct import unpack as _unpack
from binascii import b2a_hex, a2b_hex

from random import seed
from random import randint as _randint

__all__ = ['encrypt', 'decrypt']

seed()

op = 0xffffffffL


def xor(a, b):
    a1, a2 = _unpack('>LL', a[0:8])
    b1, b2 = _unpack('>LL', b[0:8])
    r = _pack('>LL', (a1 ^ b1) & op, (a2 ^ b2) & op)
    return r


def code(v, k):
    n = 16  # qq use 16
    delta = 0x9e3779b9L
    k = _unpack('>LLLL', k[0:16])
    y, z = _unpack('>LL', v[0:8])
    s = 0
    for i in xrange(n):
        s += delta
        y += (op & (z << 4)) + k[0] ^ z + s ^ (op & (z >> 5)) + k[1];
        y &= op
        z += (op & (y << 4)) + k[2] ^ y + s ^ (op & (y >> 5)) + k[3];
        z &= op
    r = _pack('>LL', y, z)
    return r


def encrypt(v, k):
    END_CHAR = '\0'
    FILL_N_OR = 0xF8
    vl = len(v)
    filln = ((8 - (vl + 2)) % 8) + 2
    fills = ''
    for i in xrange(filln):
        fills += chr(_randint(0, 0xff))
    v = (chr((filln - 2) | FILL_N_OR)
         + fills
         + v
         + END_CHAR * 7)
    tr = '\0' * 8
    to = '\0' * 8
    r = ''
    o = '\0' * 8
    for i in xrange(0, len(v), 8):
        o = xor(v[i:i + 8], tr)
        tr = xor(code(o, k), to)
        to = o
        r += tr
    return r


if __name__ == "__main__":
    print b2a_hex(encrypt(a2b_hex(
        '0018001600010000044800000001000014fb02dda52300000000030900080001b73c38560002003600120002000100000000000000000000000000000114001d01020019034c4f55458f7948953c5a2256af39efaf21a0b75a7385f34100000000'),
        b2a_hex('b537a06cf3bcb33206237d7149c27bc3')))
    # print b2a_hex(decrypt(a2b_hex('16F793BD36D4F53A23DD329198E6BBBE0FC493AF02FE46148A1A63A8C2232FBD13ABB080CDC617F3D25CB3138A512042ED3D46514FDD340A04A68C3BAD8CF35BF8C8AD8CAE4AE682B4C7DAB3947B7625D077F6021971DC06DA8BA0391A247F813C5A7B310C236536'), a2b_hex('E6992970E51D5CD9DFC7D061DD52EB27')))