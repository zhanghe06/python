# encoding: utf-8
__author__ = 'zhanghe'


from password import tc_58
from js_58 import get_p
import requests
import random
import time
import os
import re
import json
import logging

# logging.basicConfig(level=logging.DEBUG, filename='58.log', filemode='w')
logging.basicConfig(level=logging.DEBUG)

s = requests.session()
# 伪装成浏览器
s.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'}


def get_login_hidden_form():
    """
    获取登录隐藏域表单
    """
    url = 'http://passport.58.com/login'
    login_form = {}
    response = s.get(url)
    html = response.text
    form_path = re.compile(ur'<input type="hidden" name="path" value="(.*?)"/>')
    form_ptk = re.compile(ur'<input type="hidden" id="ptk" name="ptk" id="ptk" value="(.*?)"/>')
    form_cd = re.compile(ur'<input type="hidden" id="cd" name="cd" id="cd" value="(.*?)"/>')
    login_form['path'] = form_path.findall(html)[0].encode('utf-8')  # unicode
    login_form['ptk'] = form_ptk.findall(html)[0].encode('utf-8')  # unicode
    login_form['cd'] = form_cd.findall(html)[0].encode('utf-8')  # unicode
    print login_form
    return login_form


def get_login_encrypt_form():
    """
    获取登录加密表单
    """
    # 模拟22-38秒内登录
    timespan = 1411093327735
    timesign = '%13s' % (timespan + random.randint(22000, 36000))
    data = get_p(tc_58['password'], timesign)
    print data
    return data


def login():
    """
    登录
    """
    hidden_form = get_login_hidden_form()
    url = 'http://passport.58.com/dounionlogin'
    p = get_login_encrypt_form()

    # 登录需要提交的表单
    form_data = {
        'isweak': 0,
        'path': hidden_form['path'],
        'p1': p['p1'],
        'p2': p['p2'],
        'p3': p['p3'],
        'timesign': '%13s' % '',
        'ptk': hidden_form['ptk'],
        'cd': hidden_form['cd'],
        'username': tc_58['username'],
        'password': '',
        'source': 'pc-login',
        'mrisktype': '1',
        'pptmobilecodeloginmobile': '请输入手机号',
        'pptmobilecodeloginmobilecode': '',
        'mcresult': None,
    }
    print form_data
    login_response = s.post(url, data=form_data)
    print login_response.text
    login_status = check_login_status(login_response.text)
    print login_status
    return login_status


def check_login_status(login_response_text):
    """
    登录状态检查
    """
    if u'window.parent.location="http://' in login_response_text:
        return 'login_ok'
    if u'您输入的密码与账户名不符' in login_response_text:
        return 'name_or_pass_error'
    return 'login_error'


if __name__ == '__main__':
    # get_login_hidden_form()
    # get_login_encrypt_form()
    login()


"""
登录成功页面：
<script type="text/javascript">
document.domain='58.com';
	parent.clearPassportTimeout();
	window.parent.location="http://my.58.com/?pts=1449556514157";
parent.clearPassportTimeout();
parent.$.formValidator.subfalse('submitForm', 'btnSubmit', '登录');
</script>

登录失败页面：
<script type="text/javascript">
document.domain='58.com';
										//验证码存在，则刷新
		parent.refreshvalidcode();
		parent.$.c.Error.setErrorTip('您输入的密码与账户名不符','tipDiv');
								parent.clearform();
parent.clearPassportTimeout();
parent.$.formValidator.subfalse('submitForm', 'btnSubmit', '登录');
</script>
"""


"""
$("#p1").val(getm32str($("#password").val(), timesign + ""));
$("#p2").val(getm16str($("#password").val(), timesign + ""));
$("#p3").val(encryptString(timesign + encodeURIComponent($("#password").val()), "010001", "008baf14121377fc76eaf7794b8a8af17085628c3590df47e6534574efcfd81ef8635fcdc67d141c15f51649a89533df0db839331e30b8f8e4440ebf7ccbcc494f4ba18e9f492534b8aafc1b1057429ac851d3d9eb66e86fce1b04527c7b95a2431b07ea277cde2365876e2733325df04389a9d891c5d36b7bc752140db74cb69f"));
"""


"""
<form name="submitForm" method="post" action="/dounionlogin" id="submitForm" target="formSubmitFrame">
<input type="hidden" name="isweak" id="isweak" value="0"/>
<input type="hidden" name="path" value="http://my.58.com/?pts=1449541205022"/>
<input type="hidden" name="p1" id="p1" />
<input type="hidden" name="p2" id="p2" />
<input type="hidden" name="p3" id="p3" />
<input type="hidden" name="timesign" id="timesign" />
<input type="hidden" id="ptk" name="ptk" id="ptk" value="ff846067b4604273aa77aeb956fd4629"/>
<input type="hidden" id="cd" name="cd" id="cd" value="1025"/>
"""



"""
fun : function() {
    var wrongTimes = 0;
    if (GetCookieValue('wrongtimes') != null) {
        wrongTimes = parseInt(GetCookieValue('wrongtimes'));
    }
    if (wrongTimes > 4) {
        alert("您密码输入错误次数太多,请过一段时间再试");
        return false;
    }
    var timesign = new Date().getTime() + timespan;
    if (timesign - 1411093327735 > 1800000) {
        alert("页面已过期，请刷新后再提交");
        window.location.href = window.location.href;
        return false;
    }
    if (passwordIsWeak($("#username").val(), $("#password").val()))
        $("#isweak").val("1");
    else
        $("#isweak").val("0");
    $("#timesign").val(timesign);
    $("#p1").val(getm32str($("#password").val(), timesign + ""));
    $("#p2").val(getm16str($("#password").val(), timesign + ""));
    $("#p3").val(encryptString(timesign + encodeURIComponent($("#password").val()), "010001", "008baf14121377fc76eaf7794b8a8af17085628c3590df47e6534574efcfd81ef8635fcdc67d141c15f51649a89533df0db839331e30b8f8e4440ebf7ccbcc494f4ba18e9f492534b8aafc1b1057429ac851d3d9eb66e86fce1b04527c7b95a2431b07ea277cde2365876e2733325df04389a9d891c5d36b7bc752140db74cb69f"));
    $("#username").addClass("c_ccc").attr("readonly", "readonly");
    $("#password").val("").addClass("c_ccc").attr("readonly", "readonly");
    passporttimeout = setTimeout(function() {
        //	alert("服务器繁忙，请稍后再试");
        $("#password").val(upwd);
        $.formValidator.subfalse('submitForm', 'btnSubmit', '登录');
    }, 10000);
    return true;
    },
"""

"""
58加密js
http://j2.58cdn.com.cn/js/v6/source/f01f02dc906c8e6734ed04749e5db7cb_102.js

// 1411093327.735 >> 2014/9/19 10:22:7
var timespan = 1411093327735 - new Date().getTime();
var timesign = new Date().getTime() + timespan;
// 30分钟后过期 （1800000/1000/60=30）
// 页面加载到登录过程必须在30分钟内完成
if (timesign - 1411093327735 > 1800000) {
    alert("页面已过期，请刷新后再提交");
    window.location.href = window.location.href;
    return false;
}

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
注释：
js语法
charCodeAt() 方法可返回指定位置的字符的 Unicode 编码。这个返回值是 0 - 65535 之间的整数。
charAt() 方法可返回指定位置的字符。
encodeURIComponent() 函数可把字符串作为 URI 组件进行编码。


关键的方法encryptString全站都无法搜索到，关于加密的线索只有下面这个链接：
http://passport.58.com/rsa/ppt_security.js
需要工具解密：
工具链接：http://www.jb51.net/tools/eval/
需要了解：eval解密 eval加密


Request URL:http://passport.58.com/dounionlogin
Request Method:POST

Host:passport.58.com
Origin:http://passport.58.com
Referer:http://passport.58.com/login?path=http%3A//sh.58.com/&PGTID=0d100000-0000-28f4-530d-7d16a8b52935&ClickID=1
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36


isweak:1
path:http://sh.58.com/?pts=1449473332235
p1:78106e820110e70c090f21490ae606df
p2:94ab635ef656ec13c96676b1bd437ffc
p3:0d99893d3f9805827f42cf7d93450d1e1de5038a1e0666c5e83e9585e94f2d29bbb7b033ed7b7297513184e75c86cca0e5bbf64d6c8f0c0587a412b761f04e4d8e3b29c0e8be00e256b3e25ceada4697de248969099d81c47616ace91adc0c2fa97d7e726e835ee73a2b36ce8ef7c69e03b6d0fb25af91c2c6ea6912dc96e5ab
timesign:1411093354064
ptk:a9b701b52e70403e80239c5c57026b76
cd:9864
username:abcdefg
password:
source:pc-login
mrisktype:1
pptmobilecodeloginmobile:请输入手机号
pptmobilecodeloginmobilecode:
mcresult:undefined

"""