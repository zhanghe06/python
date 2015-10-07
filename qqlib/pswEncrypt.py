# encoding: utf-8
__author__ = 'zhanghe'

import hashlib
import rsa
import Tea
import base64


# RSA 公钥
pubkey = "F20CE00BAE5361F8FA3AE9CEFA495362FF7DA1BA628F64A347F0A8C012BF0B254A30CD92ABFFE7A6EE0DC424CB6166F8819EFA5BCCB20EDFB4AD02E412CCF579B1CA711D55B8B0B3AEB60153D5E0693A2A86F3167D7847A0CB8B00004716A9095D9BADC977CBB804DBDCBA6029A9710869A453F27DFDDF83C016D928B3CBF4C7"
rsa_public_key = int(pubkey, 16)
key = rsa.PublicKey(rsa_public_key, 3)


def get_tea_pass(q, p, v):
    # MD5 密码
    md5 = hashlib.md5()
    md5.update(p)
    p = md5.digest()

    # TEA 的KEY
    md5 = hashlib.md5()
    md5.update(p + ("%0.16X" % q).decode('hex'))
    m = md5.digest()

    # RSA的加密结果
    n = rsa.encrypt(p, key)

    # RSA 结果的长度
    d = ("%0.4X" % len(n)).decode('hex')

    # RSA 加密结果
    d += n

    # salt
    d += ("%0.16X" % q).decode('hex')

    # 验证码长度
    d += ("%0.4X" % len(v)).decode('hex')

    # 验证码
    d += v.upper()

    # TEA 加密并Base64编码
    r = base64.b64encode(Tea.encrypt(d, m))

    # 对特殊字符进行替换
    return r.replace('/', '-').replace('+', '*').replace('=', '_')
