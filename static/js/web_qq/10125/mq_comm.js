/**
 * Created by zhanghe on 15-6-13.
 */

String.prototype.trim = function() {
    return this.replace(/(^\s*)|(\s*$)/g, "")
};
var sys = {$: function(a) {
        return document.getElementById(a)
    },onload: function(b) {
        var a = window.onload;
        window.onload = function() {
            if (typeof (a) == "function") {
                a()
            }
            if (typeof (b) == "function") {
                b()
            }
        }
    },getQueryValue: function(c, b) {
        var a = "";
        if (b) {
            a = "&" + b
        } else {
            a = window.location.search.replace(/(^\?+)|(#\S*$)/g, "")
        }
        a = a.match(new RegExp("(^|&)" + c + "=([^&]*)(&|$)"));
        return !a ? "" : decodeURIComponent(a[2])
    }};
function getCookie(a) {
    return pt.cookie.get(a)
}
function setCookie(a, b) {
    pt.cookie.set(a.value)
}
var _ua = navigator.userAgent;
var isMobile = _ua.indexOf("Android") > -1 || _ua.indexOf("iPhone") > -1 || _ua.indexOf("iPad") > -1 || _ua.indexOf("iPod") > -1;
var canLogin = true;
var loginButton = document.getElementById("login_button");
var pt = {uin: 0,salt: "",ckNum: {},action: [0, 0],submitN: {},err_m: null,isHttps: false,isIpad: false,mibao_css: "",needAt: "",t_appid: 46000101,seller_id: 703010802,needCodeTip: false,regmaster: 0,qrlogin_step: 0,qrlogin_clock: 0,qrlogin_timeout: 0,qrlogin_timeout_time: 120000,isQrLogin: false,qr_uin: "",qr_nick: "",dftImg: "http://imgcache.qq.com/ptlogin/face/1.png",js_type: 0,pt_verifysession: "",cntCheckTimeout: 0,nlog: function(e, b) {
        var d = location.protocol == "https:" ? "https://ssl.qq.com/ptlogin/cgi-bin/ptlogin_report?" : "http://log.wtlogin.qq.com/cgi-bin/ptlogin_report?";
        var c = encodeURIComponent(e + "|_|" + location.href + "|_|" + window.navigator.userAgent);
        b = b ? b + "-487131" : 0;
        d += ("id=" + b + "&msg=" + c + "&v=" + Math.random());
        var a = new Image();
        a.src = d
    },is_weibo_appid: function(a) {
        if (a == 46000101 || a == 607000101) {
            return true
        }
        return false
    },is_mibao: function(a) {
        return /^http(s)?:\/\/ui.ptlogin2.(\S)+\/cgi-bin\/mibao_vry/.test(a)
    },chkUin: function(a) {
        a = a.trim();
        if (a.length == 0) {
            return false
        }
        if (window.location.hostname.match(/paipai.com$/)) {
            if (a.length < 64 && (new RegExp(/^[A-Za-z0-9]+@{1}[A-Za-z0-9]+$/).test(a))) {
                return true
            }
        }
        if (g_appid == pt.seller_id && a.length < 64 && (new RegExp(/^[A-Za-z0-9]+@{1}[0-9]+$/).test(a))) {
            return true
        }
        pt.needAt = "";
        var b = pt.chkAccount;
        if (pt.is_weibo_appid(g_appid)) {
            if (b.isQQ(a) || b.isMail(a)) {
                return true
            } else {
                if (b.isNick(a) || b.isName(a)) {
                    pt.needAt = "@" + encodeURIComponent(a);
                    return true
                } else {
                    if (b.isPhone(a)) {
                        pt.needAt = "@" + a.replace(/^(86|886)/, "");
                        return true
                    } else {
                        if (b.isSeaPhone(a)) {
                            pt.needAt = "@00" + a.replace(/^(00)/, "");
                            if (/^(@0088609)/.test(pt.needAt)) {
                                pt.needAt = pt.needAt.replace(/^(@0088609)/, "@008869")
                            }
                            return true
                        }
                    }
                }
            }
            pt.needAt = ""
        } else {
            if (b.isQQ(a) || b.isMail(a)) {
                return true
            }
            if (b.isPhone(a)) {
                pt.needAt = "@" + a.replace(/^(86|886)/, "");
                return true
            }
            if (b.isNick(a)) {
                sys.$("u").value = a + "@qq.com";
                return true
            }
        }
        if (b.isForeignPhone(a)) {
            pt.needAt = "@" + a;
            return true
        }
        return false
    },chkAccount: {isQQ: function(a) {
            return /^[1-9]{1}\d{4,9}$/.test(a)
        },isNick: function(a) {
            return /^[a-zA-Z]{1}([a-zA-Z0-9]|[-_]){0,19}$/.test(a)
        },isName: function(a) {
            if (a == "<请输入帐号>") {
                return false
            }
            return /[\u4E00-\u9FA5]/.test(a) ? (a.length > 8 ? false : true) : false
        },isPhone: function(a) {
            return /^(?:86|886|)1\d{10}\s*$/.test(a)
        },isDXPhone: function(a) {
            return /^(?:86|886|)1(?:33|53|80|81|89)\d{8}$/.test(a)
        },isSeaPhone: function(a) {
            return /^(00)?(?:852|853|886(0)?\d{1})\d{8}$/.test(a)
        },isMail: function(a) {
            return /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/.test(a)
        },isForeignPhone: function(a) {
            return /^00\d{7,}/.test(a)
        }},cookie: {get: function(b) {
            var a = document.cookie.match(new RegExp("(^| )" + b + "=([^;]*)(;|$)"));
            return a ? a[2] : ""
        },set: function(c, e) {
            var a = arguments;
            var h = arguments.length;
            var b = (2 < h) ? a[2].toGMTString() : "";
            var g = (3 < h) ? a[3] : "";
            var d = (4 < h) ? a[4] : "";
            var f = (5 < h) ? a[5] : false;
            document.cookie = c + "=" + escape(e) + ";expires =" + b + ";path = " + g + ";domain =" + d + ((f == true) ? ";secure" : " ")
        }},html: {encode: function(b) {
            var a = "";
            if (b.length == 0) {
                return ""
            }
            a = b.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/  /g, "&nbsp; ").replace(/'/g, "&apos;").replace(/"/g, "&quot;");
            return a
        }},init: function() {
        var a = Date.now();
        if (pt.t_appid == g_appid) {
            if (sys.$("u")) {
                sys.$("u").setAttribute("style", "")
            }
            sys.$("u").style.cssText = ""
        }
        pt.isHttps = (/^https/g.test(window.location));
        sys.onload(function() {
            var f = Date.now();
            var m = new Image();
            if (isMobile) {
                m.src = "http://isdspeed.qq.com/cgi-bin/r.cgi?flag1=170&flag2=126&flag3=1&4=" + (f - g_begTime) + "&2=" + (f - a) + "&t=" + f
            } else {
                m.src = "http://isdspeed.qq.com/cgi-bin/r.cgi?flag1=7812&flag2=2&flag3=1&5=" + (f - g_begTime) + "&3=" + (f - a) + "&t=" + f
            }
            if (sys.$("u").value) {
                check()
            }
            pt.err_m = sys.$("err_m");
            if (g_appid != 1003903 && g_appid != 501004106) {
                document.body.onclick = function(t) {
                    t = t | window.event;
                    pt.action[0]++
                }
            }
            document.body.onkeydown = function(t) {
                t = t | window.event;
                pt.action[1]++
            };
            if (Math.random() < 0.1 && !pt.isHttps) {
                pt.loadScript("http://mat1.gtimg.com/www/js/common.js", function() {
                    if (typeof checkNonTxDomain == "function") {
                        checkNonTxDomain(1, 5)
                    }
                })
            }
            window.setTimeout(function() {
                ptui_reportAttr2("313790&union=256038", 0.05);
                if (!window.g_login_sig) {
                    pt.nlog("旧版登录框login_sig为空|_|" + window.g_pt_version, "291551")
                }
            }, 1000);
            try {
                var n = sys.getQueryValue("s_url");
                var i = sys.getQueryValue("style");
                var d = sys.getQueryValue("appid");
                var h = /paipai.com$/.test(window.location.hostname);
                var r = sys.getQueryValue("regmaster");
                var l = sys.getQueryValue("enable_qlogin");
                if (i == 5) {
                    var j = /\?/g.test(n) ? "&" : "?";
                    j += "login2qq=1&webqq_type=10";
                    n += j
                }
                var p = sys.getQueryValue("hide_close_icon") == 1 || sys.getQueryValue("hide_title_bar") == 1;
                var g = document.createElement("h4");
                g.innerHTML = '<input type="button" class="btn_close" id="close" name="close" onclick="javascript:onPageClose();" title="关闭" /><u id="label_login_title">用户登录</u>';
                if (window.g_href && location.href.indexOf(g_href) == -1 && /^ui.ptlogin2./.test(location.hostname)) {
                    if (location.protocol == "http:") {
                        if (window.g_jumpname == "aqjump" && i != 5 && r != 3 && r != 2) {
                            if (!p && !sys.$("close")) {
                                sys.$("login").insertBefore(g, sys.$("normal_login"));
                                sys.$("login").style.border = "1px"
                            }
                            var v = document.createElement("div");
                            v.style.textAlign = "center";
                            v.innerHTML = '<div style="position:relative;">							<br/>							<p style="line-height:20px;text-align:left;width:220px;margin:0 auto;">您当前的网络存在链路层劫持，为了确保您的帐号安全，请使用安全登录。</p></div>							<input id="safe_login" value="安全登录"" type="button" class="btn" style="text-align:center;"/>							</div>							<div style="margin-top:10px;margin-left:10px; height:20px;">							<span style="float:left;height:15px;width:14px; background: url(https://ui.ptlogin2.qq.com/style/14/images/help.png) no-repeat scroll right center transparent;"></span>							<a style="float:left; margin-left:5px;" href="http://kf.qq.com/info/80861.html" target="_blank" >什么是链路层劫持</a>							</div>';
                            sys.$("loginform").style.display = "none";
                            sys.$("web_login").appendChild(v);
                            ptui_notifySize("login");
                            ptui_reportAttr2(245663);
                            var u = new Image();
                            var s = encodeURIComponent(window.g_href + "|_|" + location.href + "|_|" + window.g_jumpname + "|_|mid=245663");
                            u.src = "http://log.wtlogin.qq.com/cgi-bin/ptlogin_report?msg=" + s + "&v=" + Math.random()
                        } else {
                            var u = new Image();
                            var s = encodeURIComponent(window.g_href + "|_|" + location.href + "|_|" + window.g_jumpname + "|_|mid=245580");
                            u.src = "http://log.wtlogin.qq.com/cgi-bin/ptlogin_report??id=245580&msg=" + s + "&v=" + Math.random()
                        }
                    } else {
                        if (window.g_jumpname == "aqjump") {
                            ptui_reportAttr2(245582)
                        } else {
                            ptui_reportAttr2(245581)
                        }
                    }
                    g_jumpname = sys.getQueryValue("jumpname");
                    g_target = sys.getQueryValue("target");
                    switch (g_target) {
                        case "self":
                            document.forms[0].ptredirect.value = 0;
                            break;
                        case "top":
                            document.forms[0].ptredirect.value = 1;
                            break;
                        case "parent":
                            document.forms[0].ptredirect.value = 2;
                            break;
                        default:
                            document.forms[0].ptredirect.value = 1
                    }
                    g_qtarget = sys.getQueryValue("qtarget");
                    switch (g_qtarget) {
                        case "self":
                            g_qtarget = 0;
                            break;
                        case "top":
                            g_qtarget = 1;
                            break;
                        case "parent":
                            g_qtarget = 2;
                            break;
                        default:
                            g_qtarget = 1
                    }
                    var q = 1;
                    if (g_jumpname != "") {
                        if (g_qtarget != -1) {
                            q = g_qtarget
                        }
                    } else {
                        switch (g_target) {
                            case "self":
                                q = 0;
                                break;
                            case "top":
                                q = 1;
                                break;
                            case "parent":
                                q = 2;
                                break;
                            default:
                                q = 1
                        }
                    }
                    if (sys.$("safe_login")) {
                        sys.$("safe_login").onclick = function() {
                            if (q != 1) {
                                try {
                                    n = top.location.href
                                } catch (w) {
                                }
                            }
                            n = encodeURIComponent(n);
                            var t = "https://ui.ptlogin2.qq.com/cgi-bin/login";
                            window.open(t + "?style=14&pt_safe=1&appid=" + d + "&s_url=" + n + "&regmaster=" + r + "&enable_qlogin=" + l, "_top");
                            ptui_reportAttr2(247563)
                        };
                        if (sys.$("switch").style.display == "none") {
                            ptui_reportAttr2(248671)
                        } else {
                            sys.$("switch").onclick = function() {
                                if (!pt.hasShowSafeTips) {
                                    pt.hasShowSafeTips = true;
                                    ptui_reportAttr2(248671)
                                }
                            }
                        }
                    }
                    document.forms[0].u1.value = n;
                    if (r == 3 || r == 2) {
                        pt.regmaster = r
                    }
                    var k = (g_jumpname == "jump" || g_jumpname == "") ? encodeURIComponent("u1=" + encodeURIComponent(document.forms[0].u1.value)) : "";
                    sys.$("xui") && (sys.$("xui").src = sys.$("xui").src + "&jumpname=" + g_jumpname + "&param=" + k + "&qtarget=" + q + "&regmaster" + r)
                }
            } catch (o) {
            }
        });
        pt.mibao_css = window.g_mibao_css;
        var b = navigator.userAgent.toLowerCase();
        pt.isIpad = /ipad/i.test(b);
        pt.needCodeTip = window.needCodeTip ? needCodeTip : false;
        var c = document.loginform.regmaster ? document.loginform.regmaster.value : "";
        if ((c == 2 || c == 3) && !pt.isHttps) {
            pt.regmaster = c
        }
        pt.dftImg = pt.ishttps ? "https://ui.ptlogin2.qq.com/face/1.png" : "http://imgcache.qq.com/ptlogin/face/1.png"
    },show_err: function(b) {
        canLogin = true;
        loginButton.value = "登  录";
        loginButton.style.opacity = 1;
        if (pt.isQrLogin) {
            return
        }
        var a = pt.html.encode(sys.$("u").value);
        if (pt.err_m && (typeof ptui_notifySize == "function")) {
            b += '<a href="http://support.qq.com/write.shtml?guest=1&fid=713&SSTAG=10011-' + a + '" target="_blank">' + str_yjfk + "</a>";
            pt.err_m.innerHTML = b;
            pt.err_m.style.display = "block";
            ptui_notifySize("login");
            return
        } else {
            alert(b)
        }
    },hide_err: function() {
        if (pt.err_m && (typeof ptui_notifySize == "function")) {
            pt.err_m.innerHTML = "";
            pt.err_m.style.display = "none";
            ptui_notifySize("login");
            return
        }
    },setHeader: function(a) {
        for (var b in a) {
            if (b != "") {
                if (sys.$("qr_head")) {
                    sys.$("qr_head").src = a[b]
                }
            }
        }
    },imgErr: function(a) {
        a.onerror = null;
        if (a.src != pt.dftImg) {
            a.src = pt.dftImg
        }
        return false
    },setFeeds: function(a) {
        for (var b in a) {
            if (b != "") {
                if (sys.$("qr_feeds")) {
                    pt.getShortWord(sys.$("qr_feeds"), a[b], 120)
                }
            }
        }
    },get_qrlogin_pic: function() {
        var b = "ptqrshow";
        var a = (pt.isHttps ? "https://ssl." : "http://") + "ptlogin2." + g_domain + "/" + b + "?";
        if (pt.regmaster == 2) {
            a = "http://ptlogin2.function.qq.com/" + b + "?regmaster=2&"
        } else {
            if (pt.regmaster == 3) {
                a = "http://ptlogin2.crm2.qq.com/" + b + "?regmaster=3&"
            }
        }
        a += "appid=" + g_appid + "&e=0&l=M&s=5&d=72&v=4&t=" + Math.random();
        return a
    },animate: function(b, c, h, s, g) {
        if (!b) {
            return
        }
        if (!b.effect) {
            b.effect = {}
        }
        if (typeof (b.effect.animate) == "undefined") {
            b.effect.animate = 0
        }
        for (var n in c) {
            c[n] = parseInt(c[n]) || 0
        }
        window.clearInterval(b.effect.animate);
        var h = h || 10, s = s || 20, j = function(v) {
            var i = {left: v.offsetLeft,top: v.offsetTop};
            return i
        }, u = j(b), f = {width: b.clientWidth,height: b.clientHeight,left: u.left,top: u.top}, d = [], r = window.navigator.userAgent.toLowerCase();
        if (!(r.indexOf("msie") != -1 && document.compatMode == "BackCompat")) {
            var l = document.defaultView ? document.defaultView.getComputedStyle(b, null) : b.currentStyle;
            var e = c.width || c.width == 0 ? parseInt(c.width) : null, t = c.height || c.height == 0 ? parseInt(c.height) : null;
            if (typeof (e) == "number") {
                d.push("width");
                c.width = e - l.paddingLeft.replace(/\D/g, "") - l.paddingRight.replace(/\D/g, "")
            }
            if (typeof (t) == "number") {
                d.push("height");
                c.height = t - l.paddingTop.replace(/\D/g, "") - l.paddingBottom.replace(/\D/g, "")
            }
            if (s < 15) {
                h = Math.floor((h * 15) / s);
                s = 15
            }
        }
        var q = c.left || c.left == 0 ? parseInt(c.left) : null, m = c.top || c.top == 0 ? parseInt(c.top) : null;
        if (typeof (q) == "number") {
            d.push("left");
            b.style.position = "absolute"
        }
        if (typeof (m) == "number") {
            d.push("top");
            b.style.position = "absolute"
        }
        var k = [], p = d.length;
        for (var n = 0; n < p; n++) {
            k[d[n]] = f[d[n]] < c[d[n]] ? 1 : -1
        }
        var o = b.style;
        var a = function() {
            var v = true;
            for (var w = 0; w < p; w++) {
                f[d[w]] = f[d[w]] + k[d[w]] * Math.abs(c[d[w]] - Math.floor(f[d[w]]) * h / 100);
                if ((Math.round(f[d[w]]) - c[d[w]]) * k[d[w]] >= 0) {
                    v = v && true;
                    o[d[w]] = c[d[w]] + "px"
                } else {
                    v = v && false;
                    o[d[w]] = f[d[w]] + "px"
                }
            }
            if (v) {
                window.clearInterval(b.effect.animate);
                if (typeof (g) == "function") {
                    g(b)
                }
            }
        };
        b.effect.animate = window.setInterval(a, s)
    },go_qrlogin_step: function(a) {
        switch (a) {
            case 1:
                sys.$("qrlogin_step1").style.display = "block";
                sys.$("qrlogin_step2").style.display = "none";
                sys.$("qrlogin_step3").style.display = "none";
                break;
            case 2:
                sys.$("qrlogin_step1").style.display = "none";
                sys.$("qrlogin_step2").style.display = "block";
                sys.$("qrlogin_step3").style.display = "none";
                break;
            case 3:
                sys.$("qr_nick").innerHTML = pt.html.encode(pt.qr_nick);
                sys.$("qr_uin").innerHTML = pt.qr_uin;
                sys.$("qrlogin_step2").style.display = "none";
                break;
            default:
                break
        }
    },switch_qrlogin: function(a) {
        if (a) {
            ptui_reportAttr2(228433);
            sys.$("normal_login").style.display = "none";
            pt.go_qrlogin_step(1);
            sys.$("qrlogin_img").src = pt.get_qrlogin_pic();
            window.clearInterval(pt.qrlogin_clock);
            pt.qrlogin_clock = window.setInterval("qrlogin_submit();", 2000);
            window.clearTimeout(pt.qrlogin_timeout);
            pt.qrlogin_timeout = window.setTimeout(function() {
                pt.switch_qrlogin(false)
            }, pt.qrlogin_timeout_time)
        } else {
            sys.$("qr_mask_wrap").style.display = "block";
            pt.go_qrlogin_step(1);
            window.clearInterval(pt.qrlogin_clock);
            window.clearTimeout(pt.qrlogin_timeout)
        }
        ptui_notifySize("login")
    },force_qrlogin: function() {
        $("login_button").disabled = true
    },no_force_qrlogin: function() {
        $("login_button").disabled = false
    },getShortWord: function(d, g, f) {
        f = d.getAttribute("w") || f;
        g = g ? g : "";
        var b = "...";
        d.innerHTML = pt.html.encode(g);
        if (d.clientWidth <= f) {
        } else {
            var a = Math.min(g.length, 20);
            for (var c = a; c > 0; c--) {
                var e = g.substring(0, c);
                d.innerHTML = pt.html.encode(e + b);
                if (d.clientWidth <= f) {
                    break
                }
            }
        }
        d.style.width = f + "px"
    },bind_account: function() {
        window.open("http://id.qq.com/index.html#account");
        ptui_reportAttr2("234964")
    },loadScript: function(b, c) {
        var a = document.createElement("script");
        a.charset = "UTF-8";
        a.onload = a.onreadystatechange = function() {
            if (!this.readyState || this.readyState === "loaded" || this.readyState === "complete") {
                if (typeof c == "function") {
                    c(a)
                }
                a.onload = a.onreadystatechange = null;
                if (a.parentNode) {
                    a.parentNode.removeChild(a)
                }
            }
        };
        a.src = b;
        document.getElementsByTagName("head")[0].appendChild(a)
    },clearScript: function(a) {
        window.setTimeout(function() {
            a.parentNode.removeChild(a)
        }, 5000)
    },winName: {set: function(c, a) {
            var b = window.name || "";
            if (b.match(new RegExp(";" + c + "=([^;]*)(;|$)"))) {
                window.name = b.replace(new RegExp(";" + c + "=([^;]*)"), ";" + c + "=" + a)
            } else {
                window.name = b + ";" + c + "=" + a
            }
        },get: function(c) {
            var b = window.name || "";
            var a = b.match(new RegExp(";" + c + "=([^;]*)(;|$)"));
            return a ? a[1] : ""
        },clear: function(b) {
            var a = window.name || "";
            window.name = a.replace(new RegExp(";" + b + "=([^;]*)"), "")
        }}};
pt.init();
var checkClock = 0;
var lastUin = 1;
var t_appid = 46000101;
var g_changeNum = 0;
var changeimg = false;
var defaultuin = "";
var login_param = g_href.substring(g_href.indexOf("?") + 1);
function ptui_onEnableLLogin(b) {
    var a = b.low_login_enable;
    var c = b.low_login_hour;
    if (a != null && c != null) {
        c.disabled = !a.checked
    }
}
function ptui_setDefUin(c, b) {
    if (!b) {
        var b = unescape(pt.cookie.get("ptui_loginuin"));
        var a = pt.chkAccount;
        if (g_appid != t_appid && (a.isNick(b) || a.isName(b))) {
            b = pt.cookie.get("pt2gguin").replace(/^o/, "") - 0;
            b = b == 0 ? "" : b
        }
        defaultuin = b
    }
    if (b) {
        c.u.value = b
    }
}
var g_ptredirect = -1;
var g_xmlhttp;
var g_loadcheck = true;
var g_submitting = false;
function ptui_needVC(b, c) {
    if (pt.chkAccount.isQQ(b)) {
        document.cookie = "chkuin=" + b + ";domain=ptlogin2." + g_domain + ";path=/"
    }
    b = pt.needAt ? pt.needAt : b;
    if (pt.ckNum[b]) {
        if (pt.ckNum[b] == 2) {
            pt.show_err(str_net_error);
            return
        }
        pt.ckNum[b]++
    } else {
        pt.ckNum = {};
        pt.ckNum[b] = 1
    }
    var a = (pt.isHttps ? "https://ssl." : "http://check.") + "ptlogin2." + g_domain + "/check?";
    if (pt.regmaster == 2) {
        a = "http://check.ptlogin2.function.qq.com/check?regmaster=2&"
    } else {
        if (pt.regmaster == 3) {
            a = "http://check.ptlogin2.crm2.qq.com/check?regmaster=3&"
        }
    }
    a += "pt_tea=1&uin=" + b + "&appid=" + c + "&js_ver=" + window.g_pt_version + "&js_type=" + pt.js_type + "&login_sig=" + window.g_login_sig + "&u1=" + encodeURIComponent(document.forms[0].u1.value) + "&r=" + Math.random();
    pt.loadScript(a);
    g_loadcheck = true;
    return
}
function ptui_checkVC(a, d, b, e, c) {
    clearTimeout(checkClock);
    if (!b) {
        g_uin = "0";
        check();
        return
    }
    pt.ckNum[pt.needAt ? pt.needAt : sys.$("u").value.trim()] = 0;
    if (b == "\x00\x00\x00\x00\x00\x00\x27\x10") {
        g_uin = "0";
        pt.show_err(str_inv_uin);
        return
    }
    pt.isRandSalt = c;
    pt.salt = b;
    pt.uin = b;
    if (!pt.submitN[pt.uin]) {
        pt.submitN[pt.uin] = 1
    }
    var g = new Date();
    g_time.time7 = g;
    var f = {"12": g_time.time7 - g_time.time6};
    if (!curXui) {
        ptui_speedReport(f)
    }
    g_loadcheck = false;
    if (g_submitting) {
        return
    }
    if (a == "0") {
        $("verifycode").value = d;
        loadVC(false)
    } else {
        if (a == "1") {
            pt.cap_cd = d;
            $("verifycode").value = pt.needCodeTip ? str_codetip : "";
            loadVC(true)
        }
    }
    pt.pt_verifysession = e
}
function ptui_changeImg(f, d, i) {
    d = window.g_appid;
    changeimg = true;
    var h = pt.needAt ? pt.needAt : g_uin;
    var b = (pt.isHttps ? "https://ssl." : "http://") + "captcha." + f + "/getimage?&uin=" + h + "&aid=" + d + "&" + Math.random() + "&cap_cd=" + pt.cap_cd;
    var a = $("imgVerify");
    try {
        if (a != null) {
            a.src = b;
            var c = $("verifycode");
            if (c != null && c.disabled == false && i) {
                c.focus();
                c.select()
            }
        }
    } catch (g) {
    }
}
function ptui_initFocus(b) {
    if (pt.isIpad) {
        return
    }
    try {
        var a = b.u;
        var d = b.p;
        var f = b.verifycode;
        if (a.value == "" || str_uintip == a.value) {
            a.focus();
            return
        }
        if (d.value == "") {
            d.focus();
            return
        }
        if (f.value == "") {
            f.focus()
        }
    } catch (c) {
    }
}
function getSubmitUrl(h) {
    var e = true;
    var c = document.forms[0];
    var a = (pt.isHttps ? "https://ssl." : "http://") + "ptlogin2." + g_domain + "/" + h + "?";
    var b = document.getElementById("login2qq");
    if (pt.regmaster == 2) {
        a = "http://ptlogin2.function.qq.com/" + h + "?regmaster=2&"
    } else {
        if (pt.regmaster == 3) {
            a = "http://ptlogin2.crm2.qq.com/" + h + "?regmaster=3&"
        }
    }
    for (var g = 0; g < c.length; g++) {
        if (h == "ptqrlogin" && (c[g].name == "u" || c[g].name == "p" || c[g].name == "verifycode" || c[g].name == "h")) {
            continue
        }
        if (c[g].name == "ipFlag" && !c[g].checked) {
            a += c[g].name + "=-1&";
            continue
        }
        if (c[g].name == "fp" || c[g].type == "submit") {
            continue
        }
        if (c[g].name == "ptredirect") {
            g_ptredirect = c[g].value
        }
        if (c[g].name == "low_login_enable" && (!c[g].checked)) {
            e = false;
            continue
        }
        if (c[g].name == "low_login_hour" && (!e)) {
            continue
        }
        if (c[g].name == "webqq_type" && !b && (!c[g].checked)) {
            continue
        }
        a += c[g].name;
        a += "=";
        if (c[g].name == "u" && pt.needAt) {
            a += pt.needAt + "&";
            continue
        }
        if (c[g].name == "p") {
            a += $.Encryption.getEncryption(c.p.value, pt.salt, c.verifycode.value)
        } else {
            if (c[g].name == "u1" || c[g].name == "ep") {
                var d = c[g].value;
                var j = "";
                if ((g_appid == "1003903" || g_appid == "501004106") && b) {
                    j = /\?/g.test(d) ? "&" : "?";
                    var f = document.getElementById("webqq_type").value;
                    j += "login2qq=" + b.value + "&webqq_type=" + f
                }
                a += encodeURIComponent(d + j)
            } else {
                a += c[g].value
            }
        }
        a += "&"
    }
    a += "fp=loginerroralert&action=" + pt.action.join("-") + "-" + (new Date() - g_begTime) + "&mibao_css=" + pt.mibao_css + "&t=" + pt.submitN[pt.uin] + "&g=1";
    a += "&js_type=" + pt.js_type + "&js_ver=" + window.g_pt_version + "&login_sig=" + window.g_login_sig;
    a += "&pt_randsalt=" + (pt.isRandSalt || 0);
    if (h == "login") {
        a += "&pt_vcode_v1=0";
        a += ("&pt_verifysession_v1=" + (pt.pt_verifysession || pt.cookie.get("verifysession")))
    }
    return a
}
function ajax_Submit() {
    if (pt.cntCheckTimeout >= 2) {
        pt.show_err("网络繁忙，请尝试刷新页面重试");
        return
    }
    var a = getSubmitUrl("login");
    pt.winName.set("login_param", encodeURIComponent(login_param));
    pt.loadScript(a);
    return
}
function qrlogin_submit() {
    var a = getSubmitUrl("ptqrlogin");
    pt.winName.set("login_param", encodeURIComponent(login_param));
    pt.loadScript(a);
    return
}
function ptuiCB(k, l, b, i, c, a) {
    function g() {
        var m = pt.cookie.get("uin");
        var e = pt.cookie.get("skey");
        if (m == "" || e == "") {
            ptui_reportAttr2("240601")
        }
    }
    function d() {
        if (i != "0") {
            g()
        }
        pt.hide_err();
        switch (i) {
            case "0":
                if (pt.is_mibao(b)) {
                    b += "#login_param=" + encodeURIComponent(login_param)
                }
                window.location.href = b;
                break;
            case "1":
                top.location.href = b;
                break;
            case "2":
                parent.location.href = b;
                break;
            default:
                top.location.href = b
        }
    }
    g_time.time13 = new Date();
    var f = {"15": g_time.time13 - g_time.time12};
    ptui_speedReport(f);
    g_submitting = false;
    if (k == 65) {
        pt.switch_qrlogin(false);
        return
    }
    if (k == 66) {
        return
    }
    if (k == 67) {
        pt.go_qrlogin_step(2);
        window.clearInterval(pt.qrlogin_clock);
        pt.qrlogin_clock = window.setInterval("qrlogin_submit();", 1000);
        return
    }
    if (k == 10005) {
        pt.force_qrlogin()
    }
    if (k == 10006) {
        pt.force_qrlogin()
    }
    if (k == 0) {
        var h = 0;
        if (pt.isQrLogin && !pt.is_mibao(b)) {
            window.clearInterval(pt.qrlogin_clock);
            pt.qr_uin = pt.cookie.get("uin");
            pt.qr_uin = parseInt(pt.qr_uin.substring(1, pt.qr_uin.length), 10);
            pt.qr_nick = a;
            if (!pt.isHttps) {
                pt.loadScript("http://ptlogin2." + g_domain + "/getface?appid=" + g_appid + "&imgtype=3&encrytype=0&devtype=0&keytpye=0&uin=" + pt.qr_uin + "&js=1&r=" + Math.random())
            } else {
                sys.$("qr_head").src = pt.dftImg
            }
            pt.loadScript((pt.isHttps ? "https://ssl." : "http://") + "ptlogin2." + g_domain + "/getlongnick?appid=" + g_appid + "&js=1&r=" + Math.random());
            pt.go_qrlogin_step(3);
            window.setTimeout(function() {
                d()
            }, 4000)
        } else {
            d()
        }
    } else {
        if (pt.submitN[pt.uin]) {
            pt.submitN[pt.uin]++
        }
        if (l == 0) {
            if (c && c != "") {
                pt.show_err(c)
            } else {
                pt.show_err(str_input_error)
            }
        } else {
            pt.show_err(c);
            $("p").value = "";
            $("p").focus();
            $("p").select()
        }
        if (isLoadVC) {
            ptui_changeImg(g_domain, g_appid, true);
            $("verifycode").value = pt.needCodeTip ? str_codetip : "";
            loadVC(true);
            $("verifycode").focus();
            $("verifycode").select()
        } else {
            if (l == 0) {
                g_uin = 0
            }
        }
        if (k == 3 || k == 4) {
            if (navigator.userAgent.toLowerCase().indexOf("webkit") > -1) {
                $("u").focus()
            }
            if (k == 3) {
                $("p").value = ""
            }
            $("p").focus();
            $("p").select();
            if (k == 4) {
                check();
                try {
                    $("verifycode").focus();
                    $("verifycode").select()
                } catch (j) {
                }
            }
            if (l != 0 && l != 102) {
                $("verifycode").value = pt.needCodeTip ? str_codetip : "";
                loadVC(true);
                g_submitting = true
            }
        }
    }
}
function browser_version() {
    var a = navigator.userAgent.toLowerCase();
    return a.match(/msie ([\d.]+)/) ? 1 : a.match(/firefox\/([\d.]+)/) ? 3 : a.match(/chrome\/([\d.]+)/) ? 5 : a.match(/opera.([\d.]+)/) ? 9 : a.match(/version\/([\d.]+).*safari/) ? 7 : 1
}
function ptui_reportSpeed(e, d) {
    if (pt.isHttps || (window.flag2 && Math.random() > 0.5) || (!window.flag2 && Math.random() > 0.05)) {
        return
    }
    var a = browser_version();
    url = "http://isdspeed.qq.com/cgi-bin/r.cgi?flag1=6000&flag2=" + (window.flag2 ? window.flag2 : 1) + "&flag3=" + a;
    for (var c = 0; c < g_speedArray.length; c++) {
        url += "&" + g_speedArray[c][0] + "=" + (g_speedArray[c][1] - e)
    }
    if (d != 0) {
        url += "&4=" + (e - d)
    }
    imgSendTimePoint = new Image();
    imgSendTimePoint.src = url + "&24=" + g_appid
}
function ptui_reportAttr(a) {
    if (Math.random() > 0.05) {
        return
    }
    url = (pt.isHttps ? "https" : "http") + "://ui.ptlogin2." + g_domain + "/cgi-bin/report?id=" + a + "&t=" + Math.random();
    imgAttr = new Image();
    imgAttr.src = url;
    imgAttr = null
}
function ptui_reportAttr2(b, a) {
    if (Math.random() > (a || 1)) {
        return
    }
    url = (pt.isHttps ? "https" : "http") + "://ui.ptlogin2." + g_domain + "/cgi-bin/report?id=" + b + "&t=" + Math.random();
    imgAttr = new Image();
    imgAttr.src = url;
    imgAttr = null
}
function ptui_reportNum(b) {
    if (Math.random() > 0.05) {
        return
    }
    url = (pt.isHttps ? "https" : "http") + "://ui.ptlogin2." + g_domain + "/cgi-bin/report?id=1000&n=" + b;
    var a = new Image();
    a.src = url
}
function imgLoadReport() {
    if (changeimg) {
        return
    }
    g_time.time8 = new Date();
    var a = {"11": g_time.time8 - g_time.time7};
    if (!curXui) {
        ptui_speedReport(a)
    }
}
function webLoginReport() {
    var a = {};
    if (g_time.time0 && g_time.time0 > 0 && g_time.time1 && g_time.time1 > 0 && g_time.time2 && g_time.time2 > 0 && g_time.time3 && g_time.time3 > 0) {
        a["18"] = g_time.time1 - g_time.time0;
        a["19"] = g_time.time2 - g_time.time0;
        a["20"] = g_time.time4 - g_time.time0;
        a["21"] = g_time.time5 - g_time.time0;
        a["7"] = g_time.time4 - g_time.time3;
        a["26"] = g_time.time5 - g_time.time3;
        ptui_speedReport(a)
    }
}
function ptui_speedReport(e) {
    if (pt.isHttps || (window.flag2 && Math.random() > 0.5) || (!window.flag2 && Math.random() > 0.1)) {
        return
    }
    var b = "http://isdspeed.qq.com/cgi-bin/r.cgi?flag1=6000&flag2=" + (window.flag2 ? window.flag2 : 1) + "&flag3=" + browser_version();
    var c = 0;
    for (var d in e) {
        if (e[d] > 300000 || e[d] < 0) {
            continue
        }
        b += "&" + d + "=" + e[d];
        c++
    }
    if (c == 0) {
        return
    }
    var a = new Image();
    a.src = b + "&24=" + g_appid
}
function ptui_notifyClose() {
    try {
        window.clearInterval(pt.qrlogin_clock);
        if (parent.ptlogin2_onClose) {
            parent.ptlogin2_onClose()
        } else {
            if (top == this) {
                window.close()
            }
        }
    } catch (a) {
        window.close()
    }
}
function ptui_setUinColor(d, b, a) {
    var c = $(d);
    if (str_uintip == c.value) {
        c.style.color = a
    } else {
        c.style.color = b
    }
}
function ptui_checkPwdOnInput() {
    if ($("p").value.length >= 16) {
        return false
    }
    return true
}
function ptui_onLogin(a) {
    if (!canLogin) {
        return
    }
    canLogin = false;
    loginButton.value = "登录中..";
    loginButton.style.opacity = 0.6;
    return ptui_checkValidate(a)
}
function ptui_onLoginEx(b, c) {
    g_time.time12 = new Date();
    if (ptui_onLogin(b)) {
        var a = new Date();
        a.setHours(a.getHours() + 24 * 30);
        pt.cookie.set("ptui_loginuin", b.u.value, a, "/", c)
    }
    return false
}
function ptui_onReset(a) {
    try {
        if (parent.ptlogin2_onReset) {
            if (!parent.ptlogin2_onReset()) {
                return false
            }
        }
    } catch (b) {
    }
    return true
}
function ptui_checkValidate(b) {
    var a = b.u;
    var d = b.p;
    var f = b.verifycode;
    if (a.value == "" || str_uintip == a.value) {
        pt.show_err(str_no_uin);
        a.focus();
        return false
    }
    a.value = a.value.trim();
    if (!pt.chkUin(a.value)) {
        pt.show_err(str_inv_uin);
        a.focus();
        a.select();
        return false
    }
    if (d.value == "") {
        pt.show_err(str_no_pwd);
        d.focus();
        return false
    }
    if (f.value == "") {
        if (!isLoadVC) {
            check();
            return false
        }
        pt.show_err(str_no_vcode);
        try {
            f.focus()
        } catch (c) {
        }
        if (!g_loadcheck) {
            ptui_reportAttr(78028)
        } else {
            ptui_reportAttr(78029)
        }
        return false
    }
    if (f.value.length < 4) {
        pt.show_err(str_inv_vcode);
        f.focus();
        f.select();
        return false
    }
    d.setAttribute("maxlength", "32");
    ajax_Submit();
    ptui_reportNum(g_changeNum);
    g_changeNum = 0;
    return true
}
function uin2hex(str) {
    var maxLength = 16;
    var hex = parseInt(str).toString(16);
    var len = hex.length;
    for (var i = len; i < maxLength; i++) {
        hex = "0" + hex
    }
    var arr = [];
    for (var j = 0; j < maxLength; j += 2) {
        arr.push("\\x" + hex.substr(j, 2))
    }
    var result = arr.join("");
    eval('result="' + result + '"');
    return result
}
isAbleSubmit = true;
function checkTimeout() {
    var a = $("u").value.trim();
    if (pt.chkAccount.isQQ(a)) {
        pt.uin = pt.salt = uin2hex(a);
        $("verifycode").value = "";
        loadVC(true);
        pt.cntCheckTimeout++;
        if (pt.cntCheckTimeout >= 2) {
            pt.show_err("网络繁忙，请尝试刷新页面重试")
        }
    }
    ptui_reportAttr2(216082)
}
function check() {
    g_time.time6 = new Date();
    g_changeNum++;
    var a = $("u").value.trim();
    $("u").value = a;
    if ((g_uin == a || (!pt.chkUin(a))) && pt.cntCheckTimeout == 0) {
        return
    }
    clearTimeout(checkClock);
    checkClock = setTimeout("checkTimeout()", 5000);
    g_uin = $("u").value.trim();
    try {
        if (parent.ptui_uin) {
            parent.ptui_uin(g_uin)
        }
    } catch (b) {
    }
    ptui_needVC(g_uin, g_appid)
}
function loadVC(a) {
    if (isLoadVC == a && (lastUin == g_uin)) {
        return
    }
    lastUin = g_uin;
    isLoadVC = a;
    if (a == true) {
        var b = $("imgVerify");
        var g = pt.needAt ? pt.needAt : g_uin;
        var f = (pt.isHttps ? "https://ssl." : "http://") + "captcha." + g_domain + "/getimage?aid=" + g_appid + "&r=" + Math.random() + "&uin=" + g + "&cap_cd=" + pt.cap_cd;
        var d = new Date();
        b.src = f;
        $("verifyinput").style.display = "";
        $("verifytip").style.display = "";
        $("verifyshow").style.display = "";
        ptui_notifySize("login");
        try {
            $("p").focus()
        } catch (c) {
        }
    } else {
        $("verifyinput").style.display = "none";
        $("verifytip").style.display = "none";
        $("verifyshow").style.display = "none";
        ptui_notifySize("login");
        try {
            $("p").focus()
        } catch (c) {
        }
    }
}
function onPageClose() {
    ptui_notifyClose()
}
function onFormReset(a) {
    if (ptui_onReset(a)) {
        a.u.style.color = "#CCCCCC";
        return true
    }
    return false
}
function onClickForgetPwd() {
    var b = $("u");
    var a = $("label_forget_pwd");
    if (sys.getQueryValue("fgt") == 2052) {
        g_forget = g_forget.replace("1028", 2052)
    }
    a.href = g_forget;
    if (b != null && b.value != str_uintip) {
        if (a.href.indexOf("?") == -1) {
            a.href += "?"
        } else {
            a.href += "&"
        }
        a.href += "aquin=" + b.value
    }
    return true
}
var _ua = navigator.userAgent;
var $$ = function(a) {
    return document.querySelectorAll(a)
};
if (_ua.indexOf("Android") > -1 || _ua.indexOf("iPhone") > -1 || _ua.indexOf("iPad") > -1 || _ua.indexOf("iPod") > -1) {
    $$(".input_login_text")[0].innerHTML = "手机QQ 网页版";
    pt.switch_qrlogin = function() {
    }
}
$ = window.$ || {};
$pt = window.$pt || {};
$.RSA = $pt.RSA = function() {
    function g(z, t) {
        return new ar(z, t)
    }
    function ah(aA, aB) {
        var t = "";
        var z = 0;
        while (z + aB < aA.length) {
            t += aA.substring(z, z + aB) + "\n";
            z += aB
        }
        return t + aA.substring(z, aA.length)
    }
    function r(t) {
        if (t < 16) {
            return "0" + t.toString(16)
        } else {
            return t.toString(16)
        }
    }
    function af(aB, aE) {
        if (aE < aB.length + 11) {
            uv_alert("Message too long for RSA");
            return null
        }
        var aD = new Array();
        var aA = aB.length - 1;
        while (aA >= 0 && aE > 0) {
            var aC = aB.charCodeAt(aA--);
            aD[--aE] = aC
        }
        aD[--aE] = 0;
        var z = new ad();
        var t = new Array();
        while (aE > 2) {
            t[0] = 0;
            while (t[0] == 0) {
                z.nextBytes(t)
            }
            aD[--aE] = t[0]
        }
        aD[--aE] = 2;
        aD[--aE] = 0;
        return new ar(aD)
    }
    function L() {
        this.n = null;
        this.e = 0;
        this.d = null;
        this.p = null;
        this.q = null;
        this.dmp1 = null;
        this.dmq1 = null;
        this.coeff = null
    }
    function o(z, t) {
        if (z != null && t != null && z.length > 0 && t.length > 0) {
            this.n = g(z, 16);
            this.e = parseInt(t, 16)
        } else {
            uv_alert("Invalid RSA public key")
        }
    }
    function W(t) {
        return t.modPowInt(this.e, this.n)
    }
    function p(aA) {
        var t = af(aA, (this.n.bitLength() + 7) >> 3);
        if (t == null) {
            return null
        }
        var aB = this.doPublic(t);
        if (aB == null) {
            return null
        }
        var z = aB.toString(16);
        if ((z.length & 1) == 0) {
            return z
        } else {
            return "0" + z
        }
    }
    L.prototype.doPublic = W;
    L.prototype.setPublic = o;
    L.prototype.encrypt = p;
    var aw;
    var ai = 244837814094590;
    var Z = ((ai & 16777215) == 15715070);
    function ar(z, t, aA) {
        if (z != null) {
            if ("number" == typeof z) {
                this.fromNumber(z, t, aA)
            } else {
                if (t == null && "string" != typeof z) {
                    this.fromString(z, 256)
                } else {
                    this.fromString(z, t)
                }
            }
        }
    }
    function h() {
        return new ar(null)
    }
    function b(aC, t, z, aB, aE, aD) {
        while (--aD >= 0) {
            var aA = t * this[aC++] + z[aB] + aE;
            aE = Math.floor(aA / 67108864);
            z[aB++] = aA & 67108863
        }
        return aE
    }
    function ay(aC, aH, aI, aB, aF, t) {
        var aE = aH & 32767, aG = aH >> 15;
        while (--t >= 0) {
            var aA = this[aC] & 32767;
            var aD = this[aC++] >> 15;
            var z = aG * aA + aD * aE;
            aA = aE * aA + ((z & 32767) << 15) + aI[aB] + (aF & 1073741823);
            aF = (aA >>> 30) + (z >>> 15) + aG * aD + (aF >>> 30);
            aI[aB++] = aA & 1073741823
        }
        return aF
    }
    function ax(aC, aH, aI, aB, aF, t) {
        var aE = aH & 16383, aG = aH >> 14;
        while (--t >= 0) {
            var aA = this[aC] & 16383;
            var aD = this[aC++] >> 14;
            var z = aG * aA + aD * aE;
            aA = aE * aA + ((z & 16383) << 14) + aI[aB] + aF;
            aF = (aA >> 28) + (z >> 14) + aG * aD;
            aI[aB++] = aA & 268435455
        }
        return aF
    }
    if (Z && (navigator.appName == "Microsoft Internet Explorer")) {
        ar.prototype.am = ay;
        aw = 30
    } else {
        if (Z && (navigator.appName != "Netscape")) {
            ar.prototype.am = b;
            aw = 26
        } else {
            ar.prototype.am = ax;
            aw = 28
        }
    }
    ar.prototype.DB = aw;
    ar.prototype.DM = ((1 << aw) - 1);
    ar.prototype.DV = (1 << aw);
    var aa = 52;
    ar.prototype.FV = Math.pow(2, aa);
    ar.prototype.F1 = aa - aw;
    ar.prototype.F2 = 2 * aw - aa;
    var ae = "0123456789abcdefghijklmnopqrstuvwxyz";
    var ag = new Array();
    var ap, v;
    ap = "0".charCodeAt(0);
    for (v = 0; v <= 9; ++v) {
        ag[ap++] = v
    }
    ap = "a".charCodeAt(0);
    for (v = 10; v < 36; ++v) {
        ag[ap++] = v
    }
    ap = "A".charCodeAt(0);
    for (v = 10; v < 36; ++v) {
        ag[ap++] = v
    }
    function az(t) {
        return ae.charAt(t)
    }
    function A(z, t) {
        var aA = ag[z.charCodeAt(t)];
        return (aA == null) ? -1 : aA
    }
    function Y(z) {
        for (var t = this.t - 1; t >= 0; --t) {
            z[t] = this[t]
        }
        z.t = this.t;
        z.s = this.s
    }
    function n(t) {
        this.t = 1;
        this.s = (t < 0) ? -1 : 0;
        if (t > 0) {
            this[0] = t
        } else {
            if (t < -1) {
                this[0] = t + DV
            } else {
                this.t = 0
            }
        }
    }
    function c(t) {
        var z = h();
        z.fromInt(t);
        return z
    }
    function w(aE, z) {
        var aB;
        if (z == 16) {
            aB = 4
        } else {
            if (z == 8) {
                aB = 3
            } else {
                if (z == 256) {
                    aB = 8
                } else {
                    if (z == 2) {
                        aB = 1
                    } else {
                        if (z == 32) {
                            aB = 5
                        } else {
                            if (z == 4) {
                                aB = 2
                            } else {
                                this.fromRadix(aE, z);
                                return
                            }
                        }
                    }
                }
            }
        }
        this.t = 0;
        this.s = 0;
        var aD = aE.length, aA = false, aC = 0;
        while (--aD >= 0) {
            var t = (aB == 8) ? aE[aD] & 255 : A(aE, aD);
            if (t < 0) {
                if (aE.charAt(aD) == "-") {
                    aA = true
                }
                continue
            }
            aA = false;
            if (aC == 0) {
                this[this.t++] = t
            } else {
                if (aC + aB > this.DB) {
                    this[this.t - 1] |= (t & ((1 << (this.DB - aC)) - 1)) << aC;
                    this[this.t++] = (t >> (this.DB - aC))
                } else {
                    this[this.t - 1] |= t << aC
                }
            }
            aC += aB;
            if (aC >= this.DB) {
                aC -= this.DB
            }
        }
        if (aB == 8 && (aE[0] & 128) != 0) {
            this.s = -1;
            if (aC > 0) {
                this[this.t - 1] |= ((1 << (this.DB - aC)) - 1) << aC
            }
        }
        this.clamp();
        if (aA) {
            ar.ZERO.subTo(this, this)
        }
    }
    function O() {
        var t = this.s & this.DM;
        while (this.t > 0 && this[this.t - 1] == t) {
            --this.t
        }
    }
    function q(z) {
        if (this.s < 0) {
            return "-" + this.negate().toString(z)
        }
        var aA;
        if (z == 16) {
            aA = 4
        } else {
            if (z == 8) {
                aA = 3
            } else {
                if (z == 2) {
                    aA = 1
                } else {
                    if (z == 32) {
                        aA = 5
                    } else {
                        if (z == 4) {
                            aA = 2
                        } else {
                            return this.toRadix(z)
                        }
                    }
                }
            }
        }
        var aC = (1 << aA) - 1, aF, t = false, aD = "", aB = this.t;
        var aE = this.DB - (aB * this.DB) % aA;
        if (aB-- > 0) {
            if (aE < this.DB && (aF = this[aB] >> aE) > 0) {
                t = true;
                aD = az(aF)
            }
            while (aB >= 0) {
                if (aE < aA) {
                    aF = (this[aB] & ((1 << aE) - 1)) << (aA - aE);
                    aF |= this[--aB] >> (aE += this.DB - aA)
                } else {
                    aF = (this[aB] >> (aE -= aA)) & aC;
                    if (aE <= 0) {
                        aE += this.DB;
                        --aB
                    }
                }
                if (aF > 0) {
                    t = true
                }
                if (t) {
                    aD += az(aF)
                }
            }
        }
        return t ? aD : "0"
    }
    function R() {
        var t = h();
        ar.ZERO.subTo(this, t);
        return t
    }
    function al() {
        return (this.s < 0) ? this.negate() : this
    }
    function G(t) {
        var aA = this.s - t.s;
        if (aA != 0) {
            return aA
        }
        var z = this.t;
        aA = z - t.t;
        if (aA != 0) {
            return aA
        }
        while (--z >= 0) {
            if ((aA = this[z] - t[z]) != 0) {
                return aA
            }
        }
        return 0
    }
    function j(z) {
        var aB = 1, aA;
        if ((aA = z >>> 16) != 0) {
            z = aA;
            aB += 16
        }
        if ((aA = z >> 8) != 0) {
            z = aA;
            aB += 8
        }
        if ((aA = z >> 4) != 0) {
            z = aA;
            aB += 4
        }
        if ((aA = z >> 2) != 0) {
            z = aA;
            aB += 2
        }
        if ((aA = z >> 1) != 0) {
            z = aA;
            aB += 1
        }
        return aB
    }
    function u() {
        if (this.t <= 0) {
            return 0
        }
        return this.DB * (this.t - 1) + j(this[this.t - 1] ^ (this.s & this.DM))
    }
    function aq(aA, z) {
        var t;
        for (t = this.t - 1; t >= 0; --t) {
            z[t + aA] = this[t]
        }
        for (t = aA - 1; t >= 0; --t) {
            z[t] = 0
        }
        z.t = this.t + aA;
        z.s = this.s
    }
    function X(aA, z) {
        for (var t = aA; t < this.t; ++t) {
            z[t - aA] = this[t]
        }
        z.t = Math.max(this.t - aA, 0);
        z.s = this.s
    }
    function s(aF, aB) {
        var z = aF % this.DB;
        var t = this.DB - z;
        var aD = (1 << t) - 1;
        var aC = Math.floor(aF / this.DB), aE = (this.s << z) & this.DM, aA;
        for (aA = this.t - 1; aA >= 0; --aA) {
            aB[aA + aC + 1] = (this[aA] >> t) | aE;
            aE = (this[aA] & aD) << z
        }
        for (aA = aC - 1; aA >= 0; --aA) {
            aB[aA] = 0
        }
        aB[aC] = aE;
        aB.t = this.t + aC + 1;
        aB.s = this.s;
        aB.clamp()
    }
    function l(aE, aB) {
        aB.s = this.s;
        var aC = Math.floor(aE / this.DB);
        if (aC >= this.t) {
            aB.t = 0;
            return
        }
        var z = aE % this.DB;
        var t = this.DB - z;
        var aD = (1 << z) - 1;
        aB[0] = this[aC] >> z;
        for (var aA = aC + 1; aA < this.t; ++aA) {
            aB[aA - aC - 1] |= (this[aA] & aD) << t;
            aB[aA - aC] = this[aA] >> z
        }
        if (z > 0) {
            aB[this.t - aC - 1] |= (this.s & aD) << t
        }
        aB.t = this.t - aC;
        aB.clamp()
    }
    function ab(z, aB) {
        var aA = 0, aC = 0, t = Math.min(z.t, this.t);
        while (aA < t) {
            aC += this[aA] - z[aA];
            aB[aA++] = aC & this.DM;
            aC >>= this.DB
        }
        if (z.t < this.t) {
            aC -= z.s;
            while (aA < this.t) {
                aC += this[aA];
                aB[aA++] = aC & this.DM;
                aC >>= this.DB
            }
            aC += this.s
        } else {
            aC += this.s;
            while (aA < z.t) {
                aC -= z[aA];
                aB[aA++] = aC & this.DM;
                aC >>= this.DB
            }
            aC -= z.s
        }
        aB.s = (aC < 0) ? -1 : 0;
        if (aC < -1) {
            aB[aA++] = this.DV + aC
        } else {
            if (aC > 0) {
                aB[aA++] = aC
            }
        }
        aB.t = aA;
        aB.clamp()
    }
    function D(z, aB) {
        var t = this.abs(), aC = z.abs();
        var aA = t.t;
        aB.t = aA + aC.t;
        while (--aA >= 0) {
            aB[aA] = 0
        }
        for (aA = 0; aA < aC.t; ++aA) {
            aB[aA + t.t] = t.am(0, aC[aA], aB, aA, 0, t.t)
        }
        aB.s = 0;
        aB.clamp();
        if (this.s != z.s) {
            ar.ZERO.subTo(aB, aB)
        }
    }
    function Q(aA) {
        var t = this.abs();
        var z = aA.t = 2 * t.t;
        while (--z >= 0) {
            aA[z] = 0
        }
        for (z = 0; z < t.t - 1; ++z) {
            var aB = t.am(z, t[z], aA, 2 * z, 0, 1);
            if ((aA[z + t.t] += t.am(z + 1, 2 * t[z], aA, 2 * z + 1, aB, t.t - z - 1)) >= t.DV) {
                aA[z + t.t] -= t.DV;
                aA[z + t.t + 1] = 1
            }
        }
        if (aA.t > 0) {
            aA[aA.t - 1] += t.am(z, t[z], aA, 2 * z, 0, 1)
        }
        aA.s = 0;
        aA.clamp()
    }
    function E(aI, aF, aE) {
        var aO = aI.abs();
        if (aO.t <= 0) {
            return
        }
        var aG = this.abs();
        if (aG.t < aO.t) {
            if (aF != null) {
                aF.fromInt(0)
            }
            if (aE != null) {
                this.copyTo(aE)
            }
            return
        }
        if (aE == null) {
            aE = h()
        }
        var aC = h(), z = this.s, aH = aI.s;
        var aN = this.DB - j(aO[aO.t - 1]);
        if (aN > 0) {
            aO.lShiftTo(aN, aC);
            aG.lShiftTo(aN, aE)
        } else {
            aO.copyTo(aC);
            aG.copyTo(aE)
        }
        var aK = aC.t;
        var aA = aC[aK - 1];
        if (aA == 0) {
            return
        }
        var aJ = aA * (1 << this.F1) + ((aK > 1) ? aC[aK - 2] >> this.F2 : 0);
        var aR = this.FV / aJ, aQ = (1 << this.F1) / aJ, aP = 1 << this.F2;
        var aM = aE.t, aL = aM - aK, aD = (aF == null) ? h() : aF;
        aC.dlShiftTo(aL, aD);
        if (aE.compareTo(aD) >= 0) {
            aE[aE.t++] = 1;
            aE.subTo(aD, aE)
        }
        ar.ONE.dlShiftTo(aK, aD);
        aD.subTo(aC, aC);
        while (aC.t < aK) {
            aC[aC.t++] = 0
        }
        while (--aL >= 0) {
            var aB = (aE[--aM] == aA) ? this.DM : Math.floor(aE[aM] * aR + (aE[aM - 1] + aP) * aQ);
            if ((aE[aM] += aC.am(0, aB, aE, aL, 0, aK)) < aB) {
                aC.dlShiftTo(aL, aD);
                aE.subTo(aD, aE);
                while (aE[aM] < --aB) {
                    aE.subTo(aD, aE)
                }
            }
        }
        if (aF != null) {
            aE.drShiftTo(aK, aF);
            if (z != aH) {
                ar.ZERO.subTo(aF, aF)
            }
        }
        aE.t = aK;
        aE.clamp();
        if (aN > 0) {
            aE.rShiftTo(aN, aE)
        }
        if (z < 0) {
            ar.ZERO.subTo(aE, aE)
        }
    }
    function N(t) {
        var z = h();
        this.abs().divRemTo(t, null, z);
        if (this.s < 0 && z.compareTo(ar.ZERO) > 0) {
            t.subTo(z, z)
        }
        return z
    }
    function K(t) {
        this.m = t
    }
    function V(t) {
        if (t.s < 0 || t.compareTo(this.m) >= 0) {
            return t.mod(this.m)
        } else {
            return t
        }
    }
    function ak(t) {
        return t
    }
    function J(t) {
        t.divRemTo(this.m, null, t)
    }
    function H(t, aA, z) {
        t.multiplyTo(aA, z);
        this.reduce(z)
    }
    function au(t, z) {
        t.squareTo(z);
        this.reduce(z)
    }
    K.prototype.convert = V;
    K.prototype.revert = ak;
    K.prototype.reduce = J;
    K.prototype.mulTo = H;
    K.prototype.sqrTo = au;
    function B() {
        if (this.t < 1) {
            return 0
        }
        var t = this[0];
        if ((t & 1) == 0) {
            return 0
        }
        var z = t & 3;
        z = (z * (2 - (t & 15) * z)) & 15;
        z = (z * (2 - (t & 255) * z)) & 255;
        z = (z * (2 - (((t & 65535) * z) & 65535))) & 65535;
        z = (z * (2 - t * z % this.DV)) % this.DV;
        return (z > 0) ? this.DV - z : -z
    }
    function f(t) {
        this.m = t;
        this.mp = t.invDigit();
        this.mpl = this.mp & 32767;
        this.mph = this.mp >> 15;
        this.um = (1 << (t.DB - 15)) - 1;
        this.mt2 = 2 * t.t
    }
    function aj(t) {
        var z = h();
        t.abs().dlShiftTo(this.m.t, z);
        z.divRemTo(this.m, null, z);
        if (t.s < 0 && z.compareTo(ar.ZERO) > 0) {
            this.m.subTo(z, z)
        }
        return z
    }
    function at(t) {
        var z = h();
        t.copyTo(z);
        this.reduce(z);
        return z
    }
    function P(t) {
        while (t.t <= this.mt2) {
            t[t.t++] = 0
        }
        for (var aA = 0; aA < this.m.t; ++aA) {
            var z = t[aA] & 32767;
            var aB = (z * this.mpl + (((z * this.mph + (t[aA] >> 15) * this.mpl) & this.um) << 15)) & t.DM;
            z = aA + this.m.t;
            t[z] += this.m.am(0, aB, t, aA, 0, this.m.t);
            while (t[z] >= t.DV) {
                t[z] -= t.DV;
                t[++z]++
            }
        }
        t.clamp();
        t.drShiftTo(this.m.t, t);
        if (t.compareTo(this.m) >= 0) {
            t.subTo(this.m, t)
        }
    }
    function am(t, z) {
        t.squareTo(z);
        this.reduce(z)
    }
    function y(t, aA, z) {
        t.multiplyTo(aA, z);
        this.reduce(z)
    }
    f.prototype.convert = aj;
    f.prototype.revert = at;
    f.prototype.reduce = P;
    f.prototype.mulTo = y;
    f.prototype.sqrTo = am;
    function i() {
        return ((this.t > 0) ? (this[0] & 1) : this.s) == 0
    }
    function x(aF, aG) {
        if (aF > 4294967295 || aF < 1) {
            return ar.ONE
        }
        var aE = h(), aA = h(), aD = aG.convert(this), aC = j(aF) - 1;
        aD.copyTo(aE);
        while (--aC >= 0) {
            aG.sqrTo(aE, aA);
            if ((aF & (1 << aC)) > 0) {
                aG.mulTo(aA, aD, aE)
            } else {
                var aB = aE;
                aE = aA;
                aA = aB
            }
        }
        return aG.revert(aE)
    }
    function an(aA, t) {
        var aB;
        if (aA < 256 || t.isEven()) {
            aB = new K(t)
        } else {
            aB = new f(t)
        }
        return this.exp(aA, aB)
    }
    ar.prototype.copyTo = Y;
    ar.prototype.fromInt = n;
    ar.prototype.fromString = w;
    ar.prototype.clamp = O;
    ar.prototype.dlShiftTo = aq;
    ar.prototype.drShiftTo = X;
    ar.prototype.lShiftTo = s;
    ar.prototype.rShiftTo = l;
    ar.prototype.subTo = ab;
    ar.prototype.multiplyTo = D;
    ar.prototype.squareTo = Q;
    ar.prototype.divRemTo = E;
    ar.prototype.invDigit = B;
    ar.prototype.isEven = i;
    ar.prototype.exp = x;
    ar.prototype.toString = q;
    ar.prototype.negate = R;
    ar.prototype.abs = al;
    ar.prototype.compareTo = G;
    ar.prototype.bitLength = u;
    ar.prototype.mod = N;
    ar.prototype.modPowInt = an;
    ar.ZERO = c(0);
    ar.ONE = c(1);
    var m;
    var U;
    var ac;
    function d(t) {
        U[ac++] ^= t & 255;
        U[ac++] ^= (t >> 8) & 255;
        U[ac++] ^= (t >> 16) & 255;
        U[ac++] ^= (t >> 24) & 255;
        if (ac >= M) {
            ac -= M
        }
    }
    function T() {
        d(new Date().getTime())
    }
    if (U == null) {
        U = new Array();
        ac = 0;
        var I;
        if (navigator.appName == "Netscape" && navigator.appVersion < "5" && window.crypto && window.crypto.random) {
            var F = window.crypto.random(32);
            for (I = 0; I < F.length; ++I) {
                U[ac++] = F.charCodeAt(I) & 255
            }
        }
        while (ac < M) {
            I = Math.floor(65536 * Math.random());
            U[ac++] = I >>> 8;
            U[ac++] = I & 255
        }
        ac = 0;
        T()
    }
    function C() {
        if (m == null) {
            T();
            m = ao();
            m.init(U);
            for (ac = 0; ac < U.length; ++ac) {
                U[ac] = 0
            }
            ac = 0
        }
        return m.next()
    }
    function av(z) {
        var t;
        for (t = 0; t < z.length; ++t) {
            z[t] = C()
        }
    }
    function ad() {
    }
    ad.prototype.nextBytes = av;
    function k() {
        this.i = 0;
        this.j = 0;
        this.S = new Array()
    }
    function e(aC) {
        var aB, z, aA;
        for (aB = 0; aB < 256; ++aB) {
            this.S[aB] = aB
        }
        z = 0;
        for (aB = 0; aB < 256; ++aB) {
            z = (z + this.S[aB] + aC[aB % aC.length]) & 255;
            aA = this.S[aB];
            this.S[aB] = this.S[z];
            this.S[z] = aA
        }
        this.i = 0;
        this.j = 0
    }
    function a() {
        var z;
        this.i = (this.i + 1) & 255;
        this.j = (this.j + this.S[this.i]) & 255;
        z = this.S[this.i];
        this.S[this.i] = this.S[this.j];
        this.S[this.j] = z;
        return this.S[(z + this.S[this.i]) & 255]
    }
    k.prototype.init = e;
    k.prototype.next = a;
    function ao() {
        return new k()
    }
    var M = 256;
    function S(aB, aA, z) {
        aA = "F20CE00BAE5361F8FA3AE9CEFA495362FF7DA1BA628F64A347F0A8C012BF0B254A30CD92ABFFE7A6EE0DC424CB6166F8819EFA5BCCB20EDFB4AD02E412CCF579B1CA711D55B8B0B3AEB60153D5E0693A2A86F3167D7847A0CB8B00004716A9095D9BADC977CBB804DBDCBA6029A9710869A453F27DFDDF83C016D928B3CBF4C7";
        z = "3";
        var t = new L();
        t.setPublic(aA, z);
        return t.encrypt(aB)
    }
    return {rsa_encrypt: S}
}();
(function(r) {
    var s = "", a = 0, g = [], x = [], y = 0, u = 0, m = [], t = [], n = true;
    function e() {
        return Math.round(Math.random() * 4294967295)
    }
    function i(C, D, z) {
        if (!z || z > 4) {
            z = 4
        }
        var A = 0;
        for (var B = D; B < D + z; B++) {
            A <<= 8;
            A |= C[B]
        }
        return (A & 4294967295) >>> 0
    }
    function b(A, B, z) {
        A[B + 3] = (z >> 0) & 255;
        A[B + 2] = (z >> 8) & 255;
        A[B + 1] = (z >> 16) & 255;
        A[B + 0] = (z >> 24) & 255
    }
    function w(C) {
        if (!C) {
            return ""
        }
        var z = "";
        for (var A = 0; A < C.length; A++) {
            var B = Number(C[A]).toString(16);
            if (B.length == 1) {
                B = "0" + B
            }
            z += B
        }
        return z
    }
    function v(A) {
        var B = "";
        for (var z = 0; z < A.length; z += 2) {
            B += String.fromCharCode(parseInt(A.substr(z, 2), 16))
        }
        return B
    }
    function c(C, z) {
        if (!C) {
            return ""
        }
        if (z) {
            C = k(C)
        }
        var B = [];
        for (var A = 0; A < C.length; A++) {
            B[A] = C.charCodeAt(A)
        }
        return w(B)
    }
    function k(C) {
        var B, D, A = [], z = C.length;
        for (B = 0; B < z; B++) {
            D = C.charCodeAt(B);
            if (D > 0 && D <= 127) {
                A.push(C.charAt(B))
            } else {
                if (D >= 128 && D <= 2047) {
                    A.push(String.fromCharCode(192 | ((D >> 6) & 31)), String.fromCharCode(128 | (D & 63)))
                } else {
                    if (D >= 2048 && D <= 65535) {
                        A.push(String.fromCharCode(224 | ((D >> 12) & 15)), String.fromCharCode(128 | ((D >> 6) & 63)), String.fromCharCode(128 | (D & 63)))
                    }
                }
            }
        }
        return A.join("")
    }
    function h(B) {
        g = new Array(8);
        x = new Array(8);
        y = u = 0;
        n = true;
        a = 0;
        var z = B.length;
        var C = 0;
        a = (z + 10) % 8;
        if (a != 0) {
            a = 8 - a
        }
        m = new Array(z + a + 10);
        g[0] = ((e() & 248) | a) & 255;
        for (var A = 1; A <= a; A++) {
            g[A] = e() & 255
        }
        a++;
        for (var A = 0; A < 8; A++) {
            x[A] = 0
        }
        C = 1;
        while (C <= 2) {
            if (a < 8) {
                g[a++] = e() & 255;
                C++
            }
            if (a == 8) {
                p()
            }
        }
        var A = 0;
        while (z > 0) {
            if (a < 8) {
                g[a++] = B[A++];
                z--
            }
            if (a == 8) {
                p()
            }
        }
        C = 1;
        while (C <= 7) {
            if (a < 8) {
                g[a++] = 0;
                C++
            }
            if (a == 8) {
                p()
            }
        }
        return m
    }
    function q(D) {
        var C = 0;
        var A = new Array(8);
        var z = D.length;
        t = D;
        if (z % 8 != 0 || z < 16) {
            return null
        }
        x = l(D);
        a = x[0] & 7;
        C = z - a - 10;
        if (C < 0) {
            return null
        }
        for (var B = 0; B < A.length; B++) {
            A[B] = 0
        }
        m = new Array(C);
        u = 0;
        y = 8;
        a++;
        var E = 1;
        while (E <= 2) {
            if (a < 8) {
                a++;
                E++
            }
            if (a == 8) {
                A = D;
                if (!f()) {
                    return null
                }
            }
        }
        var B = 0;
        while (C != 0) {
            if (a < 8) {
                m[B] = (A[u + a] ^ x[a]) & 255;
                B++;
                C--;
                a++
            }
            if (a == 8) {
                A = D;
                u = y - 8;
                if (!f()) {
                    return null
                }
            }
        }
        for (E = 1; E < 8; E++) {
            if (a < 8) {
                if ((A[u + a] ^ x[a]) != 0) {
                    return null
                }
                a++
            }
            if (a == 8) {
                A = D;
                u = y;
                if (!f()) {
                    return null
                }
            }
        }
        return m
    }
    function p() {
        for (var z = 0; z < 8; z++) {
            if (n) {
                g[z] ^= x[z]
            } else {
                g[z] ^= m[u + z]
            }
        }
        var A = j(g);
        for (var z = 0; z < 8; z++) {
            m[y + z] = A[z] ^ x[z];
            x[z] = g[z]
        }
        u = y;
        y += 8;
        a = 0;
        n = false
    }
    function j(A) {
        var B = 16;
        var G = i(A, 0, 4);
        var F = i(A, 4, 4);
        var I = i(s, 0, 4);
        var H = i(s, 4, 4);
        var E = i(s, 8, 4);
        var D = i(s, 12, 4);
        var C = 0;
        var J = 2654435769 >>> 0;
        while (B-- > 0) {
            C += J;
            C = (C & 4294967295) >>> 0;
            G += ((F << 4) + I) ^ (F + C) ^ ((F >>> 5) + H);
            G = (G & 4294967295) >>> 0;
            F += ((G << 4) + E) ^ (G + C) ^ ((G >>> 5) + D);
            F = (F & 4294967295) >>> 0
        }
        var K = new Array(8);
        b(K, 0, G);
        b(K, 4, F);
        return K
    }
    function l(A) {
        var B = 16;
        var G = i(A, 0, 4);
        var F = i(A, 4, 4);
        var I = i(s, 0, 4);
        var H = i(s, 4, 4);
        var E = i(s, 8, 4);
        var D = i(s, 12, 4);
        var C = 3816266640 >>> 0;
        var J = 2654435769 >>> 0;
        while (B-- > 0) {
            F -= ((G << 4) + E) ^ (G + C) ^ ((G >>> 5) + D);
            F = (F & 4294967295) >>> 0;
            G -= ((F << 4) + I) ^ (F + C) ^ ((F >>> 5) + H);
            G = (G & 4294967295) >>> 0;
            C -= J;
            C = (C & 4294967295) >>> 0
        }
        var K = new Array(8);
        b(K, 0, G);
        b(K, 4, F);
        return K
    }
    function f() {
        var z = t.length;
        for (var A = 0; A < 8; A++) {
            x[A] ^= t[y + A]
        }
        x = l(x);
        y += 8;
        a = 0;
        return true
    }
    function o(D, C) {
        var B = [];
        if (C) {
            for (var A = 0; A < D.length; A++) {
                B[A] = D.charCodeAt(A) & 255
            }
        } else {
            var z = 0;
            for (var A = 0; A < D.length; A += 2) {
                //解析十六进制，转为整数
                B[z++] = parseInt(D.substr(A, 2), 16)
            }
        }
        return B
    }
    r.TEA = {encrypt: function(C, B) {
            var A = o(C, B);
            var z = h(A);
            return w(z)
        },enAsBase64: function(E, D) {
            var C = o(E, D);//十六进制转为十进制整数
            var B = h(C);
            var z = "";
            for (var A = 0; A < B.length; A++) {
                z += String.fromCharCode(B[A])
            }
            return btoa(z)
        },decrypt: function(B) {
            var A = o(B, false);
            var z = q(A);
            return w(z)
        },initkey: function(z, A) {
            s = o(z, A)
        },bytesToStr: v,strToBytes: c,bytesInStr: w,dataFromStr: o};
    var d = {};
    d.PADCHAR = "=";
    d.ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    d.getbyte = function(B, A) {
        var z = B.charCodeAt(A);
        if (z > 255) {
            throw "INVALID_CHARACTER_ERR: DOM Exception 5"
        }
        return z
    };
    d.encode = function(D) {
        if (arguments.length != 1) {
            throw "SyntaxError: Not enough arguments"
        }
        var A = d.PADCHAR;
        var F = d.ALPHA;
        var E = d.getbyte;
        var C, G;
        var z = [];
        D = "" + D;
        var B = D.length - D.length % 3;
        if (D.length == 0) {
            return D
        }
        for (C = 0; C < B; C += 3) {
            G = (E(D, C) << 16) | (E(D, C + 1) << 8) | E(D, C + 2);
            z.push(F.charAt(G >> 18));
            z.push(F.charAt((G >> 12) & 63));
            z.push(F.charAt((G >> 6) & 63));
            z.push(F.charAt(G & 63))
        }
        switch (D.length - B) {
            case 1:
                G = E(D, C) << 16;
                z.push(F.charAt(G >> 18) + F.charAt((G >> 12) & 63) + A + A);
                break;
            case 2:
                G = (E(D, C) << 16) | (E(D, C + 1) << 8);
                z.push(F.charAt(G >> 18) + F.charAt((G >> 12) & 63) + F.charAt((G >> 6) & 63) + A);
                break
        }
        return z.join("")
    };
    if (!window.btoa) {
        window.btoa = d.encode
    }
})(window);
$ = window.$ || {};
$pt = window.$pt || {};
$.Encryption = $pt.Encryption = function() {
    var hexcase = 1;
    var b64pad = "";
    var chrsz = 8;
    var mode = 32;
    function md5(s) {
        return hex_md5(s)
    }
    function hex_md5(s) {
        return binl2hex(core_md5(str2binl(s), s.length * chrsz))
    }
    function str_md5(s) {
        return binl2str(core_md5(str2binl(s), s.length * chrsz))
    }
    function hex_hmac_md5(key, data) {
        return binl2hex(core_hmac_md5(key, data))
    }
    function b64_hmac_md5(key, data) {
        return binl2b64(core_hmac_md5(key, data))
    }
    function str_hmac_md5(key, data) {
        return binl2str(core_hmac_md5(key, data))
    }
    function core_md5(x, len) {
        x[len >> 5] |= 128 << ((len) % 32);
        x[(((len + 64) >>> 9) << 4) + 14] = len;
        var a = 1732584193;
        var b = -271733879;
        var c = -1732584194;
        var d = 271733878;
        for (var i = 0; i < x.length; i += 16) {
            var olda = a;
            var oldb = b;
            var oldc = c;
            var oldd = d;
            a = md5_ff(a, b, c, d, x[i + 0], 7, -680876936);
            d = md5_ff(d, a, b, c, x[i + 1], 12, -389564586);
            c = md5_ff(c, d, a, b, x[i + 2], 17, 606105819);
            b = md5_ff(b, c, d, a, x[i + 3], 22, -1044525330);
            a = md5_ff(a, b, c, d, x[i + 4], 7, -176418897);
            d = md5_ff(d, a, b, c, x[i + 5], 12, 1200080426);
            c = md5_ff(c, d, a, b, x[i + 6], 17, -1473231341);
            b = md5_ff(b, c, d, a, x[i + 7], 22, -45705983);
            a = md5_ff(a, b, c, d, x[i + 8], 7, 1770035416);
            d = md5_ff(d, a, b, c, x[i + 9], 12, -1958414417);
            c = md5_ff(c, d, a, b, x[i + 10], 17, -42063);
            b = md5_ff(b, c, d, a, x[i + 11], 22, -1990404162);
            a = md5_ff(a, b, c, d, x[i + 12], 7, 1804603682);
            d = md5_ff(d, a, b, c, x[i + 13], 12, -40341101);
            c = md5_ff(c, d, a, b, x[i + 14], 17, -1502002290);
            b = md5_ff(b, c, d, a, x[i + 15], 22, 1236535329);
            a = md5_gg(a, b, c, d, x[i + 1], 5, -165796510);
            d = md5_gg(d, a, b, c, x[i + 6], 9, -1069501632);
            c = md5_gg(c, d, a, b, x[i + 11], 14, 643717713);
            b = md5_gg(b, c, d, a, x[i + 0], 20, -373897302);
            a = md5_gg(a, b, c, d, x[i + 5], 5, -701558691);
            d = md5_gg(d, a, b, c, x[i + 10], 9, 38016083);
            c = md5_gg(c, d, a, b, x[i + 15], 14, -660478335);
            b = md5_gg(b, c, d, a, x[i + 4], 20, -405537848);
            a = md5_gg(a, b, c, d, x[i + 9], 5, 568446438);
            d = md5_gg(d, a, b, c, x[i + 14], 9, -1019803690);
            c = md5_gg(c, d, a, b, x[i + 3], 14, -187363961);
            b = md5_gg(b, c, d, a, x[i + 8], 20, 1163531501);
            a = md5_gg(a, b, c, d, x[i + 13], 5, -1444681467);
            d = md5_gg(d, a, b, c, x[i + 2], 9, -51403784);
            c = md5_gg(c, d, a, b, x[i + 7], 14, 1735328473);
            b = md5_gg(b, c, d, a, x[i + 12], 20, -1926607734);
            a = md5_hh(a, b, c, d, x[i + 5], 4, -378558);
            d = md5_hh(d, a, b, c, x[i + 8], 11, -2022574463);
            c = md5_hh(c, d, a, b, x[i + 11], 16, 1839030562);
            b = md5_hh(b, c, d, a, x[i + 14], 23, -35309556);
            a = md5_hh(a, b, c, d, x[i + 1], 4, -1530992060);
            d = md5_hh(d, a, b, c, x[i + 4], 11, 1272893353);
            c = md5_hh(c, d, a, b, x[i + 7], 16, -155497632);
            b = md5_hh(b, c, d, a, x[i + 10], 23, -1094730640);
            a = md5_hh(a, b, c, d, x[i + 13], 4, 681279174);
            d = md5_hh(d, a, b, c, x[i + 0], 11, -358537222);
            c = md5_hh(c, d, a, b, x[i + 3], 16, -722521979);
            b = md5_hh(b, c, d, a, x[i + 6], 23, 76029189);
            a = md5_hh(a, b, c, d, x[i + 9], 4, -640364487);
            d = md5_hh(d, a, b, c, x[i + 12], 11, -421815835);
            c = md5_hh(c, d, a, b, x[i + 15], 16, 530742520);
            b = md5_hh(b, c, d, a, x[i + 2], 23, -995338651);
            a = md5_ii(a, b, c, d, x[i + 0], 6, -198630844);
            d = md5_ii(d, a, b, c, x[i + 7], 10, 1126891415);
            c = md5_ii(c, d, a, b, x[i + 14], 15, -1416354905);
            b = md5_ii(b, c, d, a, x[i + 5], 21, -57434055);
            a = md5_ii(a, b, c, d, x[i + 12], 6, 1700485571);
            d = md5_ii(d, a, b, c, x[i + 3], 10, -1894986606);
            c = md5_ii(c, d, a, b, x[i + 10], 15, -1051523);
            b = md5_ii(b, c, d, a, x[i + 1], 21, -2054922799);
            a = md5_ii(a, b, c, d, x[i + 8], 6, 1873313359);
            d = md5_ii(d, a, b, c, x[i + 15], 10, -30611744);
            c = md5_ii(c, d, a, b, x[i + 6], 15, -1560198380);
            b = md5_ii(b, c, d, a, x[i + 13], 21, 1309151649);
            a = md5_ii(a, b, c, d, x[i + 4], 6, -145523070);
            d = md5_ii(d, a, b, c, x[i + 11], 10, -1120210379);
            c = md5_ii(c, d, a, b, x[i + 2], 15, 718787259);
            b = md5_ii(b, c, d, a, x[i + 9], 21, -343485551);
            a = safe_add(a, olda);
            b = safe_add(b, oldb);
            c = safe_add(c, oldc);
            d = safe_add(d, oldd)
        }
        if (mode == 16) {
            return Array(b, c)
        } else {
            return Array(a, b, c, d)
        }
    }
    function md5_cmn(q, a, b, x, s, t) {
        return safe_add(bit_rol(safe_add(safe_add(a, q), safe_add(x, t)), s), b)
    }
    function md5_ff(a, b, c, d, x, s, t) {
        return md5_cmn((b & c) | ((~b) & d), a, b, x, s, t)
    }
    function md5_gg(a, b, c, d, x, s, t) {
        return md5_cmn((b & d) | (c & (~d)), a, b, x, s, t)
    }
    function md5_hh(a, b, c, d, x, s, t) {
        return md5_cmn(b ^ c ^ d, a, b, x, s, t)
    }
    function md5_ii(a, b, c, d, x, s, t) {
        return md5_cmn(c ^ (b | (~d)), a, b, x, s, t)
    }
    function core_hmac_md5(key, data) {
        var bkey = str2binl(key);
        if (bkey.length > 16) {
            bkey = core_md5(bkey, key.length * chrsz)
        }
        var ipad = Array(16), opad = Array(16);
        for (var i = 0; i < 16; i++) {
            ipad[i] = bkey[i] ^ 909522486;
            opad[i] = bkey[i] ^ 1549556828
        }
        var hash = core_md5(ipad.concat(str2binl(data)), 512 + data.length * chrsz);
        return core_md5(opad.concat(hash), 512 + 128)
    }
    function safe_add(x, y) {
        var lsw = (x & 65535) + (y & 65535);
        var msw = (x >> 16) + (y >> 16) + (lsw >> 16);
        return (msw << 16) | (lsw & 65535)
    }
    function bit_rol(num, cnt) {
        return (num << cnt) | (num >>> (32 - cnt))
    }
    function str2binl(str) {
        var bin = Array();
        var mask = (1 << chrsz) - 1;
        for (var i = 0; i < str.length * chrsz; i += chrsz) {
            bin[i >> 5] |= (str.charCodeAt(i / chrsz) & mask) << (i % 32)
        }
        return bin
    }
    function binl2str(bin) {
        var str = "";
        var mask = (1 << chrsz) - 1;
        for (var i = 0; i < bin.length * 32; i += chrsz) {
            str += String.fromCharCode((bin[i >> 5] >>> (i % 32)) & mask)
        }
        return str
    }
    function binl2hex(binarray) {
        var hex_tab = hexcase ? "0123456789ABCDEF" : "0123456789abcdef";
        var str = "";
        for (var i = 0; i < binarray.length * 4; i++) {
            str += hex_tab.charAt((binarray[i >> 2] >> ((i % 4) * 8 + 4)) & 15) + hex_tab.charAt((binarray[i >> 2] >> ((i % 4) * 8)) & 15)
        }
        return str
    }
    function binl2b64(binarray) {
        var tab = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
        var str = "";
        for (var i = 0; i < binarray.length * 4; i += 3) {
            var triplet = (((binarray[i >> 2] >> 8 * (i % 4)) & 255) << 16) | (((binarray[i + 1 >> 2] >> 8 * ((i + 1) % 4)) & 255) << 8) | ((binarray[i + 2 >> 2] >> 8 * ((i + 2) % 4)) & 255);
            for (var j = 0; j < 4; j++) {
                if (i * 8 + j * 6 > binarray.length * 32) {
                    str += b64pad
                } else {
                    str += tab.charAt((triplet >> 6 * (3 - j)) & 63)
                }
            }
        }
        return str
    }
    function hexchar2bin(str) {
        var arr = [];
        for (var i = 0; i < str.length; i = i + 2) {
            arr.push("\\x" + str.substr(i, 2))
        }
        arr = arr.join("");
        eval("var temp = '" + arr + "'");
        return temp
    }
    function __monitor(mid, probability) {
        if (Math.random() > (probability || 1)) {
            return
        }
        try {
            var url = location.protocol + "//ui.ptlogin2.qq.com/cgi-bin/report?id=" + mid;
            var s = document.createElement("img");
            s.src = url
        } catch (e) {
        }
    }
    function getEncryption(password, salt, vcode, isMd5) {
        vcode = vcode || "";
        password = password || "";
        var md5Pwd = isMd5 ? password : md5(password), h1 = hexchar2bin(md5Pwd), s2 = md5(h1 + salt), rsaH1 = $pt.RSA.rsa_encrypt(h1), rsaH1Len = (rsaH1.length / 2).toString(16), hexVcode = TEA.strToBytes(vcode.toUpperCase(), true), vcodeLen = Number(hexVcode.length / 2).toString(16);
        while (vcodeLen.length < 4) {
            vcodeLen = "0" + vcodeLen
        }
        while (rsaH1Len.length < 4) {
            rsaH1Len = "0" + rsaH1Len
        }
        TEA.initkey(s2);
        var saltPwd = TEA.enAsBase64(rsaH1Len + rsaH1 + TEA.strToBytes(salt) + vcodeLen + hexVcode);
        TEA.initkey("");
        setTimeout(function() {
            __monitor(488358, 1)
        }, 0);
        return saltPwd.replace(/[\/\+=]/g, function(a) {
            return {"/": "-","+": "*","=": "_"}[a]
        })
    }
    function getRSAEncryption(password, vcode, isMd5) {
        var str1 = isMd5 ? password : md5(password);
        var str2 = str1 + vcode.toUpperCase();
        var str3 = $.RSA.rsa_encrypt(str2);
        return str3
    }
    return {getEncryption: getEncryption,getRSAEncryption: getRSAEncryption,md5: md5}
}();
