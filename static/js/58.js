/**
 * Created by zhanghe on 15-12-7.
 */

//58加密js 版本v6
//http://j2.58cdn.com.cn/js/v6/source/f01f02dc906c8e6734ed04749e5db7cb_102.js
//
//1411093327.735 >> 2014/9/19 10:22:7
//var timespan = 1411093327735 - new Date().getTime();
//var timesign = new Date().getTime() + timespan;
//30分钟后过期 （1800000/1000/60=30）
//页面加载到登录过程必须在30分钟内完成
//if (timesign - 1411093327735 > 1800000) {
//    alert("页面已过期，请刷新后再提交");
//    window.location.href = window.location.href;
//    return false;
//}

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
        alert("timesign error !!!");
        return "";
    }
    return hex_md5(hex_md5(c) + a.substring(5, 11));
}
function getm16str(c, a) {
    if (a.length != 13) {
        alert("timesign error !!!");
        return "";
    }
    return hex_md5(hex_md5_16(c) + a.substring(5, 11));
}
