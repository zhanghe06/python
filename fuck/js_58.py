# encoding: utf-8
__author__ = 'zhanghe'

import execjs
from urllib import quote

# 修改：window 改为 global
# encryptString 方法中的RSAUtils  替换为  global.RSAUtils

ctx = execjs.compile("""
var hexcase=0;
var b64pad="";
var chrsz = 8;

function safe_add(a, e) {
    var d = (a & 65535) + (e & 65535);
    var c = (a >> 16) + (e >> 16) + (d >> 16);
    return (c << 16) | (d & 65535);
}
function bit_rol(a, c) {
    return (a << c) | (a >>> (32 - c));
}
function md5_cmn(h, e, d, c, g, f) {
    return safe_add(bit_rol(safe_add(safe_add(e, h), safe_add(c, f)), g), d);
}
function md5_ff(g, f, l, k, e, j, h) {
    return md5_cmn((f & l) | ((~f) & k), g, f, e, j, h);
}
function md5_gg(g, f, l, k, e, j, h) {
    return md5_cmn((f & k) | (l & (~k)), g, f, e, j, h);
}
function md5_hh(g, f, l, k, e, j, h) {
    return md5_cmn(f ^ l ^ k, g, f, e, j, h);
}
function md5_ii(g, f, l, k, e, j, h) {
    return md5_cmn(l ^ (f | (~k)), g, f, e, j, h);
}
function core_md5(r, k) {
    r[k >> 5] |= 128 << ((k) % 32);
    r[(((k + 64) >>> 9) << 4) + 14] = k;
    var q = 1732584193;
    var p = -271733879;
    var m = -1732584194;
    var l = 271733878;
    for (var g = 0; g < r.length; g += 16) {
        var j = q;
        var h = p;
        var f = m;
        var e = l;
        q = md5_ff(q, p, m, l, r[g + 0], 7, -680876936);
        l = md5_ff(l, q, p, m, r[g + 1], 12, -389564586);
        m = md5_ff(m, l, q, p, r[g + 2], 17, 606105819);
        p = md5_ff(p, m, l, q, r[g + 3], 22, -1044525330);
        q = md5_ff(q, p, m, l, r[g + 4], 7, -176418897);
        l = md5_ff(l, q, p, m, r[g + 5], 12, 1200080426);
        m = md5_ff(m, l, q, p, r[g + 6], 17, -1473231341);
        p = md5_ff(p, m, l, q, r[g + 7], 22, -45705983);
        q = md5_ff(q, p, m, l, r[g + 8], 7, 1770035416);
        l = md5_ff(l, q, p, m, r[g + 9], 12, -1958414417);
        m = md5_ff(m, l, q, p, r[g + 10], 17, -42063);
        p = md5_ff(p, m, l, q, r[g + 11], 22, -1990404162);
        q = md5_ff(q, p, m, l, r[g + 12], 7, 1804603682);
        l = md5_ff(l, q, p, m, r[g + 13], 12, -40341101);
        m = md5_ff(m, l, q, p, r[g + 14], 17, -1502002290);
        p = md5_ff(p, m, l, q, r[g + 15], 22, 1236535329);
        q = md5_gg(q, p, m, l, r[g + 1], 5, -165796510);
        l = md5_gg(l, q, p, m, r[g + 6], 9, -1069501632);
        m = md5_gg(m, l, q, p, r[g + 11], 14, 643717713);
        p = md5_gg(p, m, l, q, r[g + 0], 20, -373897302);
        q = md5_gg(q, p, m, l, r[g + 5], 5, -701558691);
        l = md5_gg(l, q, p, m, r[g + 10], 9, 38016083);
        m = md5_gg(m, l, q, p, r[g + 15], 14, -660478335);
        p = md5_gg(p, m, l, q, r[g + 4], 20, -405537848);
        q = md5_gg(q, p, m, l, r[g + 9], 5, 568446438);
        l = md5_gg(l, q, p, m, r[g + 14], 9, -1019803690);
        m = md5_gg(m, l, q, p, r[g + 3], 14, -187363961);
        p = md5_gg(p, m, l, q, r[g + 8], 20, 1163531501);
        q = md5_gg(q, p, m, l, r[g + 13], 5, -1444681467);
        l = md5_gg(l, q, p, m, r[g + 2], 9, -51403784);
        m = md5_gg(m, l, q, p, r[g + 7], 14, 1735328473);
        p = md5_gg(p, m, l, q, r[g + 12], 20, -1926607734);
        q = md5_hh(q, p, m, l, r[g + 5], 4, -378558);
        l = md5_hh(l, q, p, m, r[g + 8], 11, -2022574463);
        m = md5_hh(m, l, q, p, r[g + 11], 16, 1839030562);
        p = md5_hh(p, m, l, q, r[g + 14], 23, -35309556);
        q = md5_hh(q, p, m, l, r[g + 1], 4, -1530992060);
        l = md5_hh(l, q, p, m, r[g + 4], 11, 1272893353);
        m = md5_hh(m, l, q, p, r[g + 7], 16, -155497632);
        p = md5_hh(p, m, l, q, r[g + 10], 23, -1094730640);
        q = md5_hh(q, p, m, l, r[g + 13], 4, 681279174);
        l = md5_hh(l, q, p, m, r[g + 0], 11, -358537222);
        m = md5_hh(m, l, q, p, r[g + 3], 16, -722521979);
        p = md5_hh(p, m, l, q, r[g + 6], 23, 76029189);
        q = md5_hh(q, p, m, l, r[g + 9], 4, -640364487);
        l = md5_hh(l, q, p, m, r[g + 12], 11, -421815835);
        m = md5_hh(m, l, q, p, r[g + 15], 16, 530742520);
        p = md5_hh(p, m, l, q, r[g + 2], 23, -995338651);
        q = md5_ii(q, p, m, l, r[g + 0], 6, -198630844);
        l = md5_ii(l, q, p, m, r[g + 7], 10, 1126891415);
        m = md5_ii(m, l, q, p, r[g + 14], 15, -1416354905);
        p = md5_ii(p, m, l, q, r[g + 5], 21, -57434055);
        q = md5_ii(q, p, m, l, r[g + 12], 6, 1700485571);
        l = md5_ii(l, q, p, m, r[g + 3], 10, -1894986606);
        m = md5_ii(m, l, q, p, r[g + 10], 15, -1051523);
        p = md5_ii(p, m, l, q, r[g + 1], 21, -2054922799);
        q = md5_ii(q, p, m, l, r[g + 8], 6, 1873313359);
        l = md5_ii(l, q, p, m, r[g + 15], 10, -30611744);
        m = md5_ii(m, l, q, p, r[g + 6], 15, -1560198380);
        p = md5_ii(p, m, l, q, r[g + 13], 21, 1309151649);
        q = md5_ii(q, p, m, l, r[g + 4], 6, -145523070);
        l = md5_ii(l, q, p, m, r[g + 11], 10, -1120210379);
        m = md5_ii(m, l, q, p, r[g + 2], 15, 718787259);
        p = md5_ii(p, m, l, q, r[g + 9], 21, -343485551);
        q = safe_add(q, j);
        p = safe_add(p, h);
        m = safe_add(m, f);
        l = safe_add(l, e);
    }
    return Array(q, p, m, l);
}
function hex_md5(a) {
    return binl2hex(core_md5(str2binl(a), a.length * chrsz));
}
function reverse(d) {
    var a = "";
    for (var c = d.length - 1; c >= 0; c--) {
        a += d.charAt(c);
    }
    return a;
}
function hex_md5_16(c) {
    var a = hex_md5(c);
    a = a.substring(8, 24);
    return reverse(a);
}
function str2binl(e) {
    var d = Array();
    var a = (1 << chrsz) - 1;
    for (var c = 0; c < e.length * chrsz; c += chrsz) {
        d[c >> 5] |= (e.charCodeAt(c / chrsz) & a) << (c % 32);
    }
    return d;
}
function binl2hex(d) {
    var c = hexcase ? "0123456789ABCDEF" : "0123456789abcdef";
    var e = "";
    for (var a = 0; a < d.length * 4; a++) {
        e += c.charAt((d[a >> 2] >> ((a % 4) * 8 + 4)) & 15) + c.charAt((d[a >> 2] >> ((a % 4) * 8)) & 15);
    }
    return e;
}
function getm32str(c, a) {
    if (a.length != 13) {
        //alert("timesign error !!!");
        return "";
    }
    return hex_md5(hex_md5(c) + a.substring(5, 11));
}
function getm16str(c, a) {
    if (a.length != 13) {
        //alert("timesign error !!!");
        return "";
    }
    return hex_md5(hex_md5_16(c) + a.substring(5, 11));
}
(function($w) {
    if (typeof $w.RSAUtils === 'undefined') var RSAUtils = $w.RSAUtils = {};
    var biRadixBase = 2;
    var biRadixBits = 16;
    var bitsPerDigit = biRadixBits;
    var biRadix = 1 << 16;
    var biHalfRadix = biRadix >>> 1;
    var biRadixSquared = biRadix * biRadix;
    var maxDigitVal = biRadix - 1;
    var maxInteger = 9999999999999998;
    var maxDigits;
    var ZERO_ARRAY;
    var bigZero, bigOne;
    var BigInt = $w.BigInt = function(flag) {
        if (typeof flag == "boolean" && flag == true) {
            this.digits = null
        } else {
            this.digits = ZERO_ARRAY.slice(0)
        }
        this.isNeg = false
    };
    RSAUtils.setMaxDigits = function(value) {
        maxDigits = value;
        ZERO_ARRAY = new Array(maxDigits);
        for (var iza = 0; iza < ZERO_ARRAY.length; iza++) ZERO_ARRAY[iza] = 0;
        bigZero = new BigInt();
        bigOne = new BigInt();
        bigOne.digits[0] = 1
    };
    RSAUtils.setMaxDigits(20);
    var dpl10 = 15;
    RSAUtils.biFromNumber = function(i) {
        var result = new BigInt();
        result.isNeg = i < 0;
        i = Math.abs(i);
        var j = 0;
        while (i > 0) {
            result.digits[j++] = i & maxDigitVal;
            i = Math.floor(i / biRadix)
        }
        return result
    };
    var lr10 = RSAUtils.biFromNumber(1000000000000000);
    RSAUtils.biFromDecimal = function(s) {
        var isNeg = s.charAt(0) == '-';
        var i = isNeg ? 1 : 0;
        var result;
        while (i < s.length && s.charAt(i) == '0')++i;
        if (i == s.length) {
            result = new BigInt()
        } else {
            var digitCount = s.length - i;
            var fgl = digitCount % dpl10;
            if (fgl == 0) fgl = dpl10;
            result = RSAUtils.biFromNumber(Number(s.substr(i, fgl)));
            i += fgl;
            while (i < s.length) {
                result = RSAUtils.biAdd(RSAUtils.biMultiply(result, lr10), RSAUtils.biFromNumber(Number(s.substr(i, dpl10))));
                i += dpl10
            }
            result.isNeg = isNeg
        }
        return result
    };
    RSAUtils.biCopy = function(bi) {
        var result = new BigInt(true);
        result.digits = bi.digits.slice(0);
        result.isNeg = bi.isNeg;
        return result
    };
    RSAUtils.reverseStr = function(s) {
        var result = "";
        for (var i = s.length - 1; i > -1; --i) {
            result += s.charAt(i)
        }
        return result
    };
    var hexatrigesimalToChar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
    RSAUtils.biToString = function(x, radix) {
        var b = new BigInt();
        b.digits[0] = radix;
        var qr = RSAUtils.biDivideModulo(x, b);
        var result = hexatrigesimalToChar[qr[1].digits[0]];
        while (RSAUtils.biCompare(qr[0], bigZero) == 1) {
            qr = RSAUtils.biDivideModulo(qr[0], b);
            digit = qr[1].digits[0];
            result += hexatrigesimalToChar[qr[1].digits[0]]
        }
        return (x.isNeg ? "-": "") + RSAUtils.reverseStr(result)
    };
    RSAUtils.biToDecimal = function(x) {
        var b = new BigInt();
        b.digits[0] = 10;
        var qr = RSAUtils.biDivideModulo(x, b);
        var result = String(qr[1].digits[0]);
        while (RSAUtils.biCompare(qr[0], bigZero) == 1) {
            qr = RSAUtils.biDivideModulo(qr[0], b);
            result += String(qr[1].digits[0])
        }
        return (x.isNeg ? "-": "") + RSAUtils.reverseStr(result)
    };
    var hexToChar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'];
    RSAUtils.digitToHex = function(n) {
        var mask = 0xf;
        var result = "";
        for (i = 0; i < 4; ++i) {
            result += hexToChar[n & mask];
            n >>>= 4
        }
        return RSAUtils.reverseStr(result)
    };
    RSAUtils.biToHex = function(x) {
        var result = "";
        var n = RSAUtils.biHighIndex(x);
        for (var i = RSAUtils.biHighIndex(x); i > -1; --i) {
            result += RSAUtils.digitToHex(x.digits[i])
        }
        return result
    };
    RSAUtils.charToHex = function(c) {
        var ZERO = 48;
        var NINE = ZERO + 9;
        var littleA = 97;
        var littleZ = littleA + 25;
        var bigA = 65;
        var bigZ = 65 + 25;
        var result;
        if (c >= ZERO && c <= NINE) {
            result = c - ZERO
        } else if (c >= bigA && c <= bigZ) {
            result = 10 + c - bigA
        } else if (c >= littleA && c <= littleZ) {
            result = 10 + c - littleA
        } else {
            result = 0
        }
        return result
    };
    RSAUtils.hexToDigit = function(s) {
        var result = 0;
        var sl = Math.min(s.length, 4);
        for (var i = 0; i < sl; ++i) {
            result <<= 4;
            result |= RSAUtils.charToHex(s.charCodeAt(i))
        }
        return result
    };
    RSAUtils.biFromHex = function(s) {
        var result = new BigInt();
        var sl = s.length;
        for (var i = sl,
        j = 0; i > 0; i -= 4, ++j) {
            result.digits[j] = RSAUtils.hexToDigit(s.substr(Math.max(i - 4, 0), Math.min(i, 4)))
        }
        return result
    };
    RSAUtils.biFromString = function(s, radix) {
        var isNeg = s.charAt(0) == '-';
        var istop = isNeg ? 1 : 0;
        var result = new BigInt();
        var place = new BigInt();
        place.digits[0] = 1;
        for (var i = s.length - 1; i >= istop; i--) {
            var c = s.charCodeAt(i);
            var digit = RSAUtils.charToHex(c);
            var biDigit = RSAUtils.biMultiplyDigit(place, digit);
            result = RSAUtils.biAdd(result, biDigit);
            place = RSAUtils.biMultiplyDigit(place, radix)
        }
        result.isNeg = isNeg;
        return result
    };
    RSAUtils.biDump = function(b) {
        return (b.isNeg ? "-": "") + b.digits.join(" ")
    };
    RSAUtils.biAdd = function(x, y) {
        var result;
        if (x.isNeg != y.isNeg) {
            y.isNeg = !y.isNeg;
            result = RSAUtils.biSubtract(x, y);
            y.isNeg = !y.isNeg
        } else {
            result = new BigInt();
            var c = 0;
            var n;
            for (var i = 0; i < x.digits.length; ++i) {
                n = x.digits[i] + y.digits[i] + c;
                result.digits[i] = n % biRadix;
                c = Number(n >= biRadix)
            }
            result.isNeg = x.isNeg
        }
        return result
    };
    RSAUtils.biSubtract = function(x, y) {
        var result;
        if (x.isNeg != y.isNeg) {
            y.isNeg = !y.isNeg;
            result = RSAUtils.biAdd(x, y);
            y.isNeg = !y.isNeg
        } else {
            result = new BigInt();
            var n, c;
            c = 0;
            for (var i = 0; i < x.digits.length; ++i) {
                n = x.digits[i] - y.digits[i] + c;
                result.digits[i] = n % biRadix;
                if (result.digits[i] < 0) result.digits[i] += biRadix;
                c = 0 - Number(n < 0)
            }
            if (c == -1) {
                c = 0;
                for (var i = 0; i < x.digits.length; ++i) {
                    n = 0 - result.digits[i] + c;
                    result.digits[i] = n % biRadix;
                    if (result.digits[i] < 0) result.digits[i] += biRadix;
                    c = 0 - Number(n < 0)
                }
                result.isNeg = !x.isNeg
            } else {
                result.isNeg = x.isNeg
            }
        }
        return result
    };
    RSAUtils.biHighIndex = function(x) {
        var result = x.digits.length - 1;
        while (result > 0 && x.digits[result] == 0)--result;
        return result
    };
    RSAUtils.biNumBits = function(x) {
        var n = RSAUtils.biHighIndex(x);
        var d = x.digits[n];
        var m = (n + 1) * bitsPerDigit;
        var result;
        for (result = m; result > m - bitsPerDigit; --result) {
            if ((d & 0x8000) != 0) break;
            d <<= 1
        }
        return result
    };
    RSAUtils.biMultiply = function(x, y) {
        var result = new BigInt();
        var c;
        var n = RSAUtils.biHighIndex(x);
        var t = RSAUtils.biHighIndex(y);
        var u, uv, k;
        for (var i = 0; i <= t; ++i) {
            c = 0;
            k = i;
            for (j = 0; j <= n; ++j, ++k) {
                uv = result.digits[k] + x.digits[j] * y.digits[i] + c;
                result.digits[k] = uv & maxDigitVal;
                c = uv >>> biRadixBits
            }
            result.digits[i + n + 1] = c
        }
        result.isNeg = x.isNeg != y.isNeg;
        return result
    };
    RSAUtils.biMultiplyDigit = function(x, y) {
        var n, c, uv;
        result = new BigInt();
        n = RSAUtils.biHighIndex(x);
        c = 0;
        for (var j = 0; j <= n; ++j) {
            uv = result.digits[j] + x.digits[j] * y + c;
            result.digits[j] = uv & maxDigitVal;
            c = uv >>> biRadixBits
        }
        result.digits[1 + n] = c;
        return result
    };
    RSAUtils.arrayCopy = function(src, srcStart, dest, destStart, n) {
        var m = Math.min(srcStart + n, src.length);
        for (var i = srcStart,
        j = destStart; i < m; ++i, ++j) {
            dest[j] = src[i]
        }
    };
    var highBitMasks = [0x0000, 0x8000, 0xC000, 0xE000, 0xF000, 0xF800, 0xFC00, 0xFE00, 0xFF00, 0xFF80, 0xFFC0, 0xFFE0, 0xFFF0, 0xFFF8, 0xFFFC, 0xFFFE, 0xFFFF];
    RSAUtils.biShiftLeft = function(x, n) {
        var digitCount = Math.floor(n / bitsPerDigit);
        var result = new BigInt();
        RSAUtils.arrayCopy(x.digits, 0, result.digits, digitCount, result.digits.length - digitCount);
        var bits = n % bitsPerDigit;
        var rightBits = bitsPerDigit - bits;
        for (var i = result.digits.length - 1,
        i1 = i - 1; i > 0; --i, --i1) {
            result.digits[i] = ((result.digits[i] << bits) & maxDigitVal) | ((result.digits[i1] & highBitMasks[bits]) >>> (rightBits))
        }
        result.digits[0] = ((result.digits[i] << bits) & maxDigitVal);
        result.isNeg = x.isNeg;
        return result
    };
    var lowBitMasks = [0x0000, 0x0001, 0x0003, 0x0007, 0x000F, 0x001F, 0x003F, 0x007F, 0x00FF, 0x01FF, 0x03FF, 0x07FF, 0x0FFF, 0x1FFF, 0x3FFF, 0x7FFF, 0xFFFF];
    RSAUtils.biShiftRight = function(x, n) {
        var digitCount = Math.floor(n / bitsPerDigit);
        var result = new BigInt();
        RSAUtils.arrayCopy(x.digits, digitCount, result.digits, 0, x.digits.length - digitCount);
        var bits = n % bitsPerDigit;
        var leftBits = bitsPerDigit - bits;
        for (var i = 0,
        i1 = i + 1; i < result.digits.length - 1; ++i, ++i1) {
            result.digits[i] = (result.digits[i] >>> bits) | ((result.digits[i1] & lowBitMasks[bits]) << leftBits)
        }
        result.digits[result.digits.length - 1] >>>= bits;
        result.isNeg = x.isNeg;
        return result
    };
    RSAUtils.biMultiplyByRadixPower = function(x, n) {
        var result = new BigInt();
        RSAUtils.arrayCopy(x.digits, 0, result.digits, n, result.digits.length - n);
        return result
    };
    RSAUtils.biDivideByRadixPower = function(x, n) {
        var result = new BigInt();
        RSAUtils.arrayCopy(x.digits, n, result.digits, 0, result.digits.length - n);
        return result
    };
    RSAUtils.biModuloByRadixPower = function(x, n) {
        var result = new BigInt();
        RSAUtils.arrayCopy(x.digits, 0, result.digits, 0, n);
        return result
    };
    RSAUtils.biCompare = function(x, y) {
        if (x.isNeg != y.isNeg) {
            return 1 - 2 * Number(x.isNeg)
        }
        for (var i = x.digits.length - 1; i >= 0; --i) {
            if (x.digits[i] != y.digits[i]) {
                if (x.isNeg) {
                    return 1 - 2 * Number(x.digits[i] > y.digits[i])
                } else {
                    return 1 - 2 * Number(x.digits[i] < y.digits[i])
                }
            }
        }
        return 0
    };
    RSAUtils.biDivideModulo = function(x, y) {
        var nb = RSAUtils.biNumBits(x);
        var tb = RSAUtils.biNumBits(y);
        var origYIsNeg = y.isNeg;
        var q, r;
        if (nb < tb) {
            if (x.isNeg) {
                q = RSAUtils.biCopy(bigOne);
                q.isNeg = !y.isNeg;
                x.isNeg = false;
                y.isNeg = false;
                r = biSubtract(y, x);
                x.isNeg = true;
                y.isNeg = origYIsNeg
            } else {
                q = new BigInt();
                r = RSAUtils.biCopy(x)
            }
            return [q, r]
        }
        q = new BigInt();
        r = x;
        var t = Math.ceil(tb / bitsPerDigit) - 1;
        var lambda = 0;
        while (y.digits[t] < biHalfRadix) {
            y = RSAUtils.biShiftLeft(y, 1); ++lambda; ++tb;
            t = Math.ceil(tb / bitsPerDigit) - 1
        }
        r = RSAUtils.biShiftLeft(r, lambda);
        nb += lambda;
        var n = Math.ceil(nb / bitsPerDigit) - 1;
        var b = RSAUtils.biMultiplyByRadixPower(y, n - t);
        while (RSAUtils.biCompare(r, b) != -1) {++q.digits[n - t];
            r = RSAUtils.biSubtract(r, b)
        }
        for (var i = n; i > t; --i) {
            var ri = (i >= r.digits.length) ? 0 : r.digits[i];
            var ri1 = (i - 1 >= r.digits.length) ? 0 : r.digits[i - 1];
            var ri2 = (i - 2 >= r.digits.length) ? 0 : r.digits[i - 2];
            var yt = (t >= y.digits.length) ? 0 : y.digits[t];
            var yt1 = (t - 1 >= y.digits.length) ? 0 : y.digits[t - 1];
            if (ri == yt) {
                q.digits[i - t - 1] = maxDigitVal
            } else {
                q.digits[i - t - 1] = Math.floor((ri * biRadix + ri1) / yt)
            }
            var c1 = q.digits[i - t - 1] * ((yt * biRadix) + yt1);
            var c2 = (ri * biRadixSquared) + ((ri1 * biRadix) + ri2);
            while (c1 > c2) {--q.digits[i - t - 1];
                c1 = q.digits[i - t - 1] * ((yt * biRadix) | yt1);
                c2 = (ri * biRadix * biRadix) + ((ri1 * biRadix) + ri2)
            }
            b = RSAUtils.biMultiplyByRadixPower(y, i - t - 1);
            r = RSAUtils.biSubtract(r, RSAUtils.biMultiplyDigit(b, q.digits[i - t - 1]));
            if (r.isNeg) {
                r = RSAUtils.biAdd(r, b); --q.digits[i - t - 1]
            }
        }
        r = RSAUtils.biShiftRight(r, lambda);
        q.isNeg = x.isNeg != origYIsNeg;
        if (x.isNeg) {
            if (origYIsNeg) {
                q = RSAUtils.biAdd(q, bigOne)
            } else {
                q = RSAUtils.biSubtract(q, bigOne)
            }
            y = RSAUtils.biShiftRight(y, lambda);
            r = RSAUtils.biSubtract(y, r)
        }
        if (r.digits[0] == 0 && RSAUtils.biHighIndex(r) == 0) r.isNeg = false;
        return [q, r]
    };
    RSAUtils.biDivide = function(x, y) {
        return RSAUtils.biDivideModulo(x, y)[0]
    };
    RSAUtils.biModulo = function(x, y) {
        return RSAUtils.biDivideModulo(x, y)[1]
    };
    RSAUtils.biMultiplyMod = function(x, y, m) {
        return RSAUtils.biModulo(RSAUtils.biMultiply(x, y), m)
    };
    RSAUtils.biPow = function(x, y) {
        var result = bigOne;
        var a = x;
        while (true) {
            if ((y & 1) != 0) result = RSAUtils.biMultiply(result, a);
            y >>= 1;
            if (y == 0) break;
            a = RSAUtils.biMultiply(a, a)
        }
        return result
    };
    RSAUtils.biPowMod = function(x, y, m) {
        var result = bigOne;
        var a = x;
        var k = y;
        while (true) {
            if ((k.digits[0] & 1) != 0) result = RSAUtils.biMultiplyMod(result, a, m);
            k = RSAUtils.biShiftRight(k, 1);
            if (k.digits[0] == 0 && RSAUtils.biHighIndex(k) == 0) break;
            a = RSAUtils.biMultiplyMod(a, a, m)
        }
        return result
    };
    $w.BarrettMu = function(m) {
        this.modulus = RSAUtils.biCopy(m);
        this.k = RSAUtils.biHighIndex(this.modulus) + 1;
        var b2k = new BigInt();
        b2k.digits[2 * this.k] = 1;
        this.mu = RSAUtils.biDivide(b2k, this.modulus);
        this.bkplus1 = new BigInt();
        this.bkplus1.digits[this.k + 1] = 1;
        this.modulo = BarrettMu_modulo;
        this.multiplyMod = BarrettMu_multiplyMod;
        this.powMod = BarrettMu_powMod
    };
    function BarrettMu_modulo(x) {
        var $dmath = RSAUtils;
        var q1 = $dmath.biDivideByRadixPower(x, this.k - 1);
        var q2 = $dmath.biMultiply(q1, this.mu);
        var q3 = $dmath.biDivideByRadixPower(q2, this.k + 1);
        var r1 = $dmath.biModuloByRadixPower(x, this.k + 1);
        var r2term = $dmath.biMultiply(q3, this.modulus);
        var r2 = $dmath.biModuloByRadixPower(r2term, this.k + 1);
        var r = $dmath.biSubtract(r1, r2);
        if (r.isNeg) {
            r = $dmath.biAdd(r, this.bkplus1)
        }
        var rgtem = $dmath.biCompare(r, this.modulus) >= 0;
        while (rgtem) {
            r = $dmath.biSubtract(r, this.modulus);
            rgtem = $dmath.biCompare(r, this.modulus) >= 0
        }
        return r
    }
    function BarrettMu_multiplyMod(x, y) {
        var xy = RSAUtils.biMultiply(x, y);
        return this.modulo(xy)
    }
    function BarrettMu_powMod(x, y) {
        var result = new BigInt();
        result.digits[0] = 1;
        var a = x;
        var k = y;
        while (true) {
            if ((k.digits[0] & 1) != 0) result = this.multiplyMod(result, a);
            k = RSAUtils.biShiftRight(k, 1);
            if (k.digits[0] == 0 && RSAUtils.biHighIndex(k) == 0) break;
            a = this.multiplyMod(a, a)
        }
        return result
    }
    var RSAKeyPair = function(encryptionExponent, decryptionExponent, modulus) {
        var $dmath = RSAUtils;
        this.e = $dmath.biFromHex(encryptionExponent);
        this.d = $dmath.biFromHex(decryptionExponent);
        this.m = $dmath.biFromHex(modulus);
        this.chunkSize = 2 * $dmath.biHighIndex(this.m);
        this.radix = 16;
        this.barrett = new $w.BarrettMu(this.m)
    };
    RSAUtils.getKeyPair = function(encryptionExponent, decryptionExponent, modulus) {
        return new RSAKeyPair(encryptionExponent, decryptionExponent, modulus)
    };
    if (typeof $w.twoDigit === 'undefined') {
        $w.twoDigit = function(n) {
            return (n < 10 ? "0": "") + String(n)
        }
    }
    RSAUtils.encryptedString = function(key, s) {
        var a = [];
        var sl = s.length;
        var i = 0;
        while (i < sl) {
            a[i] = s.charCodeAt(i);
            i++
        }
        while (a.length % key.chunkSize != 0) {
            a[i++] = 0
        }
        var al = a.length;
        var result = "";
        var j, k, block;
        for (i = 0; i < al; i += key.chunkSize) {
            block = new BigInt();
            j = 0;
            for (k = i; k < i + key.chunkSize; ++j) {
                block.digits[j] = a[k++];
                block.digits[j] += a[k++] << 8
            }
            var crypt = key.barrett.powMod(block, key.e);
            var text = key.radix == 16 ? RSAUtils.biToHex(crypt) : RSAUtils.biToString(crypt, key.radix);
            result += text + " "
        }
        return result.substring(0, result.length - 1)
    };
    RSAUtils.decryptedString = function(key, s) {
        var blocks = s.split(" ");
        var result = "";
        var i, j, block;
        for (i = 0; i < blocks.length; ++i) {
            var bi;
            if (key.radix == 16) {
                bi = RSAUtils.biFromHex(blocks[i])
            } else {
                bi = RSAUtils.biFromString(blocks[i], key.radix)
            }
            block = key.barrett.powMod(bi, key.d);
            for (j = 0; j <= RSAUtils.biHighIndex(block); ++j) {
                result += String.fromCharCode(block.digits[j] & 255, block.digits[j] >> 8)
            }
        }
        if (result.charCodeAt(result.length - 1) == 0) {
            result = result.substring(0, result.length - 1)
        }
        return result
    };
    RSAUtils.setMaxDigits(130)
})(global);
function encryptString(str, e, m) {
    var key = global.RSAUtils.getKeyPair(e, '', m);
    return global.RSAUtils.encryptedString(key, str)
}
""")


def get_p(password, timesign):
    """
    获取加密表单数值
    :param password:
    :param timesign:
    :return:
    """
    data = {
        'p1': ctx.call("getm32str", password, timesign),
        'p2': ctx.call("getm16str", password, timesign),
        'p3': ctx.call("encryptString", timesign+quote(password), "010001", "008baf14121377fc76eaf7794b8a8af17085628c3590df47e6534574efcfd81ef8635fcdc67d141c15f51649a89533df0db839331e30b8f8e4440ebf7ccbcc494f4ba18e9f492534b8aafc1b1057429ac851d3d9eb66e86fce1b04527c7b95a2431b07ea277cde2365876e2733325df04389a9d891c5d36b7bc752140db74cb69f")
    }
    return data
