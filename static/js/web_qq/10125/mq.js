/**
 * Created by zhanghe on 15-6-22.
 */

 /*
 almond 0.3.0 Copyright (c) 2011-2014, The Dojo Foundation All Rights Reserved.
 Available via the MIT or new BSD license.
 see: http://github.com/jrburke/almond for details
*/
var requirejs, require, define;
(function(g) {
    function a(o, v) {
        var D, p, y, F, H, M, P, E, G, O = v && v.split("/"), u = z.map, s = u && u["*"] || {};
        if (o && o.charAt(0) === ".")
            if (v) {
                O = O.slice(0, O.length - 1);
                o = o.split("/");
                H = o.length - 1;
                if (z.nodeIdCompat && h.test(o[H]))
                    o[H] = o[H].replace(h, "");
                o = O.concat(o);
                for (H = 0; H < o.length; H += 1) {
                    D = o[H];
                    if (D === ".") {
                        o.splice(H, 1);
                        H -= 1
                    } else if (D === "..")
                        if (H === 1 && (o[2] === ".." || o[0] === ".."))
                            break;
                        else if (H > 0) {
                            o.splice(H - 1, 2);
                            H -= 2
                        }
                }
                o = o.join("/")
            } else if (o.indexOf("./") === 0)
                o = o.substring(2);
        if ((O || s) && u) {
            D = o.split("/");
            for (H = D.length; H >
            0; H -= 1) {
                p = D.slice(0, H).join("/");
                if (O)
                    for (G = O.length; G > 0; G -= 1)
                        if (y = u[O.slice(0, G).join("/")])
                            if (y = y[p]) {
                                F = y;
                                M = H;
                                break
                            }
                if (F)
                    break;
                if (!P && s && s[p]) {
                    P = s[p];
                    E = H
                }
            }
            if (!F && P) {
                F = P;
                M = E
            }
            if (F) {
                D.splice(0, M, F);
                o = D.join("/")
            }
        }
        return o
    }
    function b(o, v) {
        return function() {
            var D = C.call(arguments, 0);
            typeof D[0] !== "string" && D.length === 1 && D.push(null);
            return r.apply(g, D.concat([o, v]))
        }
    }
    function c(o) {
        return function(v) {
            return a(v, o)
        }
    }
    function e(o) {
        return function(v) {
            t[o] = v
        }
    }
    function j(o) {
        if (w.call(B, o)) {
            var v = B[o];
            delete B[o];
            q[o] = true;
            m.apply(g, v)
        }
        if (!w.call(t, o) && !w.call(q, o))
            throw Error("No " + o);
        return t[o]
    }
    function f(o) {
        var v, D = o ? o.indexOf("!") : -1;
        if (D > -1) {
            v = o.substring(0, D);
            o = o.substring(D + 1, o.length)
        }
        return [v, o]
    }
    function n(o) {
        return function() {
            return z && z.config && z.config[o] || {}
        }
    }
    var m, r, k, d, t = {}, B = {}, z = {}, q = {}, w = Object.prototype.hasOwnProperty, C = [].slice, h = /\.js$/;
    k = function(o, v) {
        var D, p = f(o), y = p[0];
        o = p[1];
        if (y) {
            y = a(y, v);
            D = j(y)
        }
        if (y)
            o = D && D.normalize ? D.normalize(o, c(v)) : a(o, v);
        else {
            o = a(o, v);
            p = f(o);
            y = p[0];
            o = p[1];
            if (y)
                D = j(y)
        }
        return {f: y ? y + "!" + o : o,n: o,pr: y,p: D}
    };
    d = {require: function(o) {
            return b(o)
        },exports: function(o) {
            var v = t[o];
            return typeof v !== "undefined" ? v : t[o] = {}
        },module: function(o) {
            return {id: o,uri: "",exports: t[o],config: n(o)}
        }};
    m = function(o, v, D, p) {
        var y, F, H, M, P = [];
        F = typeof D;
        var E;
        p = p || o;
        if (F === "undefined" || F === "function") {
            v = !v.length && D.length ? ["require", "exports", "module"] : v;
            for (M = 0; M < v.length; M += 1) {
                H = k(v[M], p);
                F = H.f;
                if (F === "require")
                    P[M] = d.require(o);
                else if (F === "exports") {
                    P[M] = d.exports(o);
                    E = true
                } else if (F ===
                "module")
                    y = P[M] = d.module(o);
                else if (w.call(t, F) || w.call(B, F) || w.call(q, F))
                    P[M] = j(F);
                else if (H.p) {
                    H.p.load(H.n, b(p, true), e(F), {});
                    P[M] = t[F]
                } else
                    throw Error(o + " missing " + F);
            }
            v = D ? D.apply(t[o], P) : undefined;
            if (o)
                if (y && y.exports !== g && y.exports !== t[o])
                    t[o] = y.exports;
                else if (v !== g || !E)
                    t[o] = v
        } else if (o)
            t[o] = D
    };
    requirejs = require = r = function(o, v, D, p, y) {
        if (typeof o === "string") {
            if (d[o])
                return d[o](v);
            return j(k(o, v).f)
        } else if (!o.splice) {
            z = o;
            z.deps && r(z.deps, z.callback);
            if (!v)
                return;
            if (v.splice) {
                o = v;
                v = D;
                D = null
            } else
                o =
                g
        }
        v = v || function() {
        };
        if (typeof D === "function") {
            D = p;
            p = y
        }
        p ? m(g, o, v, D) : setTimeout(function() {
            m(g, o, v, D)
        }, 4);
        return r
    };
    r.config = function(o) {
        return r(o)
    };
    requirejs._defined = t;
    define = function(o, v, D) {
        if (!v.splice) {
            D = v;
            v = []
        }
        if (!w.call(t, o) && !w.call(B, o))
            B[o] = [o, v, D]
    };
    define.amd = {jQuery: true}
})();
define("requireLib", function() {
});
(function() {
    var g = {$namespace: function(a) {
            if (!a)
                return window;
            nsArr = a.split(".");
            a = window;
            i = 0;
            for (l = nsArr.length; i < l; i++) {
                var b = nsArr[i];
                a[b] = a[b] || {};
                a = a[b]
            }
            return a
        },$package: function(a, b) {
            var c;
            if (typeof a == "function") {
                b = a;
                c = window
            } else if (typeof a == "string")
                c = this.$namespace(a);
            else if (typeof a == "object")
                c = a;
            b.call(c, this)
        },extend: function(a, b) {
            for (var c in b)
                if (b.hasOwnProperty(c))
                    a[c] = b[c];
            return a
        },bind: function(a, b) {
            var c = [].slice, e = c.call(arguments, 2);
            return function() {
                return a.apply(b, e.concat(c.call(arguments)))
            }
        },
        Class: function() {
            var a = arguments.length, b = arguments[a - 1];
            b.init = b.init || function() {
            };
            if (a === 2) {
                a = arguments[0].extend;
                var c = function() {
                };
                c.prototype = a.prototype;
                var e = function() {
                    return new e.prototype._init(arguments)
                };
                e.superClass = a.prototype;
                e.callSuper = function(f, n) {
                    var m = Array.prototype.slice, r = m.call(arguments, 2);
                    (n = e.superClass[n]) && n.apply(f, r.concat(m.call(arguments)))
                };
                e.prototype = new c;
                e.prototype.constructor = e;
                g.extend(e.prototype, b);
                e.prototype._init = function(f) {
                    this.init.apply(this, f)
                };
                e.prototype._init.prototype = e.prototype;
                return e
            } else if (a === 1) {
                var j = function() {
                    return new j.prototype._init(arguments)
                };
                j.prototype = b;
                j.prototype._init = function(f) {
                    this.init.apply(this, f)
                };
                j.prototype.constructor = j;
                j.prototype._init.prototype = j.prototype;
                return j
            }
        },toArray: function(a) {
            var b = [], c, e;
            try {
                return b.slice.call(a)
            } catch (j) {
                b = [];
                c = 0;
                for (e = a.length; c < e; ++c)
                    b[c] = a[c];
                return b
            }
        },indexOf: function(a, b) {
            var c = g.type;
            if (a.length)
                return [].indexOf.call(a, b);
            else if (c.isObject(a))
                for (var e in a)
                    if (a.hasOwnProperty(e) &&
                    a[e] === b)
                        return e
        },every: function(a, b) {
            if (a.length)
                return [].every.call(a, b);
            else if ($T.isObject(a)) {
                var c = true;
                this.each(a, function(e, j, f) {
                    b(e, j, f) || (c = false)
                });
                return c
            }
        },some: function(a, b) {
            if (a.length)
                return [].some.call(a, b);
            else if ($T.isObject(a)) {
                var c = false;
                this.each(a, function(e, j, f) {
                    if (b(e, j, f))
                        c = true
                });
                return c
            }
        },each: function(a, b) {
            var c = g.type;
            if (a.length)
                return [].forEach.call(a, b);
            else if (c.isObject(a))
                for (var e in a)
                    if (a.hasOwnProperty(e))
                        if (b.call(a[e], a[e], e, a) === false)
                            break
        },map: function(a,
        b) {
            var c = g.type;
            if (a.length)
                [].map.call(a, b);
            else if (c.isObject(a))
                for (var e in a)
                    if (a.hasOwnProperty(e))
                        a[e] = b.call(a[e], a[e], e, a)
        },filter: function(a, b) {
            var c = g.type;
            if (a.length)
                return [].filter.call(a, b);
            else if (c.isObject(a)) {
                var e = {};
                this.each(a, function(j, f) {
                    if (b(j, f))
                        e[f] = j
                });
                return e
            }
        },isEmptyObject: function(a) {
            for (var b in a)
                return false;
            return true
        },random: function(a, b) {
            return Math.floor(Math.random() * (b - a + 1) + a)
        },$default: function(a, b) {
            if (typeof a === "undefined")
                return b;
            return a
        }};
    window.JM =
    window.J = g
})();
J.$package(function(g) {
    g.connectType = ["unknow", "ethernet", "wifi", "cell_2g", "cell_3g"][(navigator.connection || {type: 0}).type]
});
J.$package(function(g) {
    var a = Object.prototype.toString;
    g.type = {isArray: function(b) {
            return b && (b.constructor === Array || a.call(b) === "[object Array]")
        },isObject: function(b) {
            return b && (b.constructor === Object || a.call(b) === "[object Object]")
        },isBoolean: function(b) {
            return (b === false || b) && b.constructor === Boolean
        },isNumber: function(b) {
            return (b === 0 || b) && b.constructor === Number
        },isUndefined: function(b) {
            return typeof b === "undefined"
        },isNull: function(b) {
            return b === null
        },isFunction: function(b) {
            return b && b.constructor ===
            Function
        },isString: function(b) {
            return (b === "" || b) && b.constructor === String
        }}
});
J.$package(function(g) {
    var a = navigator.userAgent, b = {};
    b.ieVersion = function() {
        var c = -1, e, j;
        if (navigator.appName === "Microsoft Internet Explorer") {
            e = navigator.userAgent;
            j = /MSIE ([0-9]{1,})/;
            if (j.exec(e) !== null)
                c = parseInt(RegExp.$1)
        }
        return c
    }();
    b.ie = b.ieVersion !== -1;
    b.android = a.match(/Android/i) === null ? false : true;
    b.iPhone = a.match(/iPhone/i) === null ? false : true;
    b.iPad = a.match(/iPad/i) === null ? false : true;
    b.iPod = a.match(/iPod/i) === null ? false : true;
    b.winPhone = a.match(/Windows Phone/i) === null ? false : true;
    b.IOS =
    b.iPad || b.iPhone;
    b.touchDevice = "ontouchstart" in window;
    g.platform = b
});
J.$package(function(g) {
    var a, b, c = navigator.userAgent.toLowerCase(), e = navigator.plugins, j = function(f, n) {
        f = ("" + f).replace(/_/g, ".");
        n = n || 1;
        f = String(f).split(".");
        f = f[0] + "." + (f[1] || "0");
        return f = Number(f).toFixed(n)
    };
    b = {features: {xpath: !!document.evaluate,air: !!window.runtime,query: !!document.querySelector},plugins: {flash: function() {
                var f = 0;
                if (e && e.length) {
                    var n = e["Shockwave Flash"];
                    if (n && n.description)
                        f = j(n.description.match(/\b(\d+)\.\d+\b/)[1], 1) || f
                } else
                    for (n = 13; n--; )
                        try {
                            new ActiveXObject("ShockwaveFlash.ShockwaveFlash." +
                            n);
                            f = j(n);
                            break
                        } catch (m) {
                        }
                return f
            }()},getUserAgent: function() {
            return c
        },name: "unknown",version: 0,ie: 0,firefox: 0,chrome: 0,opera: 0,safari: 0,mobileSafari: 0,adobeAir: 0,set: function(f, n) {
            this.name = f;
            this.version = n;
            this[f] = n
        }};
    (a = c.match(/msie ([\d.]+)/)) ? b.set("ie", j(a[1])) : (a = c.match(/firefox\/([\d.]+)/)) ? b.set("firefox", j(a[1])) : (a = c.match(/chrome\/([\d.]+)/)) ? b.set("chrome", j(a[1])) : (a = c.match(/opera.([\d.]+)/)) ? b.set("opera", j(a[1])) : (a = c.match(/adobeair\/([\d.]+)/)) ? b.set("adobeAir", j(a[1])) : (a =
    c.match(/version\/([\d.]+).*safari/)) && b.set("safari", j(a[1]));
    g.browser = b
});
J.$package(function(g) {
    var a, b;
    if (window.getComputedStyle) {
        a = window.getComputedStyle(document.documentElement, "");
        a = (Array.prototype.slice.call(a).join("").match(/-(moz|webkit|ms)-/) || a.OLink === "" && ["", "o"])[1];
        b = "WebKit|Moz|MS|O".match(RegExp("(" + a + ")", "i"))[1];
        g.prefix = {dom: b,lowercase: a,css: "-" + a + "-",js: a}
    } else
        g.prefix = {dom: "",lowercase: "",css: "",js: ""}
});
J.$package(function(g) {
    var a = document, b = g.type, c = /^[\w-]+$/, e = /^#([\w-]*)$/, j = /^\.([\w-]+)$/, f = "classList" in document.documentElement, n = ["o", "ms", "moz", "webkit"], m = document.createElement("div"), r = {$: function(k, d) {
            var t;
            d = d || a;
            if (e.test(k))
                return (t = this.id(k.replace("#", ""))) ? [t] : [];
            else
                t = c.test(k) ? this.tagName(k, d) : j.test(k) ? this.className(k.replace(".", ""), d) : d.querySelectorAll(k);
            return g.toArray(t)
        },id: function(k) {
            return a.getElementById(k)
        },tagName: function(k, d) {
            d = d || a;
            return d.getElementsByTagName(k)
        },
        node: function(k) {
            return a.createElement(k)
        },className: function(k, d) {
            var t, B, z, q, w;
            d = d || a;
            if (d.getElementsByClassName)
                return d.getElementsByClassName(k);
            else {
                t = d.getElementsByTagName("*");
                B = [];
                z = 0;
                for (q = t.length; z < q; ++z)
                    if (w = t[z].className && g.indexOf(w.split(" "), k) >= 0)
                        B.push(t[z]);
                return B
            }
        },remove: function(k) {
            var d = k.parentNode;
            d && d.removeChild(k)
        },setSelectorEngine: function() {
        },matchesSelector: function(k, d) {
            if (k && d) {
                var t = k.webkitMatchesSelector || k.mozMatchesSelector || k.oMatchesSelector || k.matchesSelector;
                if (t)
                    return t.call(k, d);
                t = this.$(d);
                if (g.indexOf(t, k) > 0)
                    return true;
                return false
            }
        },closest: function(k, d) {
            for (; k; ) {
                if (r.matchesSelector(k, d))
                    return k;
                k = k.parentNode
            }
        },toDomStyle: function(k) {
            if (b.isString(k))
                return k.replace(/\-[a-z]/g, function(d) {
                    return d.charAt(1).toUpperCase()
                })
        },toCssStyle: function(k) {
            if (b.isString(k))
                return k.replace(/[A-Z]/g, function(d) {
                    return "-" + d.toLowerCase()
                })
        },setStyle: function(k, d, t) {
            var B = this;
            if (k.length)
                g.each(k, function(q) {
                    B.setStyle(q, d, t)
                });
            else if (b.isObject(d))
                for (var z in d) {
                    if (d.hasOwnProperty(z))
                        k.style[z] =
                        d[z]
                }
            else if (b.isString(d))
                k.style[d] = t
        },getStyle: function(k, d) {
            if (k) {
                if (d === "float")
                    d = "cssFloat";
                if (k.style[d])
                    return k.style[d];
                else if (window.getComputedStyle)
                    return window.getComputedStyle(k, null)[d];
                else if (document.defaultView && document.defaultView.getComputedStyle) {
                    d = d.replace(/([/A-Z])/g, "-$1");
                    d = d.toLowerCase();
                    var t = document.defaultView.getComputedStyle(k, "");
                    return t && t.getPropertyValue(d)
                } else if (k.currentStyle)
                    return k.currentStyle[d]
            }
        },getVendorPropertyName: function(k) {
            var d = m.style;
            if (k in d)
                return k;
            k = k.charAt(0).toUpperCase() + k.substr(1);
            for (var t = n.length; t--; ) {
                var B = n[t] + k;
                if (B in d)
                    return B
            }
        },isSupprot3d: function() {
            var k = r.getVendorPropertyName("perspective");
            return k && k in m.style
        },filterSelector: function(k, d) {
            return g.filter(k, function(t) {
                return r.matchesSelector(t, d)
            })
        },addClass: function() {
            return f ? function(k, d) {
                !k || !d || r.hasClass(k, d) || k.classList.add(d)
            } : function(k, d) {
                !k || !d || r.hasClass(k, d) || (k.className += " " + d)
            }
        }(),hasClass: function() {
            return f ? function(k, d) {
                if (!k ||
                !d)
                    return false;
                return k.classList.contains(d)
            } : function(k, d) {
                if (!k || !d)
                    return false;
                return -1 < (" " + k.className + " ").indexOf(" " + d + " ")
            }
        }(),removeClass: function() {
            return f ? function(k, d) {
                !k || !d || !r.hasClass(k, d) || k.classList.remove(d)
            } : function(k, d) {
                if (!(!k || !d || !r.hasClass(k, d)))
                    k.className = k.className.replace(RegExp("(?:^|\\s)" + d + "(?:\\s|$)"), " ")
            }
        }(),toggleClass: function(k, d) {
            r.hasClass(k, d) ? r.removeClass(k, d) : r.addClass(k, d)
        },insertAfter: function(k, d, t) {
            (t = t.nextSibling) ? k.insertBefore(d, t) : k.appendChild(d);
            return d
        }};
    g.dom = r
});
J.$package(function(g) {
    var a = {}, b = function(e, j) {
        var f = !/\W/.test(e) ? a[e] = a[e] || b(document.getElementById(e).innerHTML) : new Function("obj", "var p=[],print=function(){p.push.apply(p,arguments);};with(obj){p.push('" + e.replace(/[\r\t\n]/g, " ").split("<%").join("\t").replace(/((^|%>)[^\t]*)'/g, "$1\r").replace(/\t=(.*?)%>/g, "',$1,'").split("\t").join("');").split("%>").join("p.push('").split("\r").join("\\'") + "');}return p.join('');");
        return j ? f(j) : f
    };
    g.string = g.string || {};
    g.string.template = b;
    g.string.encodeHtml =
    function(e) {
        e = e.replace(/&/g, "&amp;");
        e = e.replace(/>/g, "&gt;");
        e = e.replace(/</g, "&lt;");
        e = e.replace(/"/g, "&quot;");
        return e = e.replace(/'/g, "&#39;")
    };
    var c = function(e) {
        var j = null;
        if (null !== (j = c.RE.exec(e))) {
            e = {};
            for (var f = 0, n = c.SPEC.length; f < n; f++)
                e[c.SPEC[f]] = j[f + 1];
            j = e
        }
        return j
    };
    c.SPEC = ["scheme", "user", "pass", "host", "port", "path", "query", "fragment"];
    c.RE = /^([^:]+):\/\/(?:([^:@]+):?([^@]*)@)?(?:([^/?#:]+):?(\d*))([^?#]*)(?:\?([^#]+))?(?:#(.+))?$/;
    g.string.parseURL = c;
    g.string.buildURL = function(e) {
        for (var j =
        "", f = {}, n = {}, m = 0, r = c.SPEC.length; m < r; m++) {
            var k = c.SPEC[m];
            if (e[k]) {
                switch (k) {
                    case "scheme":
                        n[k] = "://";
                        break;
                    case "pass":
                        f[k] = ":";
                    case "user":
                        f.host = "@";
                        break;
                    case "port":
                        f[k] = ":";
                        break;
                    case "query":
                        f[k] = "?";
                        break;
                    case "fragment":
                        f[k] = "#"
                }
                if (k in f)
                    j += f[k];
                if (k in e)
                    j += e[k];
                if (k in n)
                    j += n[k]
            }
        }
        return j
    }
});
J.$package(function(g) {
    g.format = g.format || {};
    g.format.date = function(a, b) {
        var c = {"M+": a.getMonth() + 1,"D+": a.getDate(),"h+": a.getHours(),"m+": a.getMinutes(),"s+": a.getSeconds(),"q+": Math.floor((a.getMonth() + 3) / 3),S: a.getMilliseconds()};
        if (/(Y+)/.test(b))
            b = b.replace(RegExp.$1, (a.getFullYear() + "").substr(4 - RegExp.$1.length));
        for (var e in c)
            if (RegExp("(" + e + ")").test(b))
                b = b.replace(RegExp.$1, RegExp.$1.length == 1 ? c[e] : ("00" + c[e]).substr(("" + c[e]).length));
        return b
    }
});
J.$package(function(g) {
    var a = window, b = a.document, c = a.navigator, e = g.dom, j = {fixed: function() {
            var f = document.body, n = e.node("div");
            e.setStyle(n, {position: "fixed",top: "100px"});
            f.appendChild(n);
            var m = f.style.height, r = f.scrollTop;
            e.setStyle(f, "height", "3000px");
            f.scrollTop = 500;
            var k = n.getBoundingClientRect().top;
            m ? e.setStyle(f, "height", m + "px") : e.setStyle(f, "height", "");
            f.removeChild(n);
            f.scrollTop = r;
            return k === 100
        }(),transitionend: function() {
            var f, n, m, r;
            if ("ontransitionend" in a)
                return "transitionend";
            else if ("onwebkittransitionend" in
            a)
                return "webkitTransitionEnd";
            else if ("transition" in b.body.style)
                return "transitionend";
            else if ("addEventListener" in a) {
                f = ["transitionend", "webkitTransitionEnd", "MozTransitionEnd", "MSTransitionEnd", "otransitionend", "oTransitionEnd"];
                n = b.createElement("div");
                m = function(k) {
                    for (var d = f.length; d--; )
                        this.removeEventListener(f[d], m);
                    j.transitionend = k.type;
                    m = null
                };
                e.setStyle(n, {position: "absolute",top: "0px",left: "-99999px",transition: "top 1ms",WebkitTransition: "top 1ms",MozTransition: "top 1ms",MSTransitionEnd: "top 1ms",
                    OTransitionEnd: "top 1ms"});
                for (r = f.length; r--; )
                    n.addEventListener(f[r], m, false);
                b.documentElement.appendChild(n);
                setTimeout(function() {
                    n.style.top = "100px";
                    setTimeout(function() {
                        n.parentNode.removeChild(n);
                        m = n = null
                    }, 100)
                }, 0)
            }
            return false
        }(),audio: function() {
            var f = document.createElement("audio"), n, m = /^no$/i;
            try {
                if (f.canPlayType) {
                    n = {};
                    n.mp3 = f.canPlayType("audio/mpeg;").replace(m, "");
                    n.wav = f.canPlayType('audio/wav; codecs="1"').replace(m, "");
                    n.ogg = f.canPlayType('audio/ogg; codecs="vorbis"').replace(m,
                    "");
                    n.m4a = (f.canPlayType("audio/x-m4a;") || f.canPlayType("audio/aac;")).replace(m, "")
                }
            } catch (r) {
            }
            return n
        }(),flash: function() {
            if (c.plugins && c.plugins.length && c.plugins["Shockwave Flash"])
                return true;
            else if (c.mimeTypes && c.mimeTypes.length) {
                var f = c.mimeTypes["application/x-shockwave-flash"];
                return f && f.enabledPlugin
            } else
                try {
                    if (ActiveXObject) {
                        new ActiveXObject("ShockwaveFlash.ShockwaveFlash");
                        return true
                    }
                } catch (n) {
                }
            return false
        }()};
    g.support = j
});
J.$package(function(g) {
    var a = g.type, b = g.support, c = window, e = function(q, w) {
        if (("on" + w).toLowerCase() in q)
            return w;
        else if (b.transitionend && (w === "transitionend" || w === b.transitionend))
            return b.transitionend;
        return false
    }, j = function(q, w, C) {
        var h;
        if (q.addEventListener)
            q.addEventListener(w, C, false);
        else {
            w = w.toLowerCase();
            if (q.attachEvent)
                q.attachEvent("on" + w, C);
            else {
                h = q["on" + w];
                q["on" + w] = function() {
                    h && h.apply(this, arguments);
                    return C.apply(this, arguments)
                }
            }
        }
    }, f = function(q, w, C) {
        if (q.removeEventListener)
            q.removeEventListener(w,
            C, false);
        else {
            w = w.toLowerCase();
            if (q.detachEvent)
                q.detachEvent("on" + w, C);
            else
                q["on" + w] = null
        }
    }, n = {on: function(q, w, C) {
            var h;
            if (a.isArray(q))
                for (h = q.length; h--; )
                    n.on(q[h], w, C);
            else if (a.isString(w) && w.indexOf(" ") > 0) {
                w = w.split(" ");
                for (h = w.length; h--; )
                    n.on(q, w[h], C)
            } else if (a.isArray(C))
                for (h = C.length; h--; )
                    n.on(q, w, C[h]);
            else if (a.isObject(w))
                for (h in w)
                    n.on(q, h, w[h]);
            else if (h = e(q, w)) {
                w = h;
                j(q, w, C)
            } else if (q.elem && (h = e(q.elem, w))) {
                w = h;
                j(q.elem, w, C)
            } else if (z[w])
                z[w](q, C);
            else {
                if (!q.events)
                    q.events =
                    {};
                q.events[w] || (q.events[w] = []);
                q.events[w].push(C)
            }
        },once: function(q, w, C) {
            var h = function() {
                C.apply(c, arguments);
                n.off(q, w, h)
            };
            n.on(q, w, h)
        },off: function(q, w, C) {
            if (a.isString(w) && w.indexOf(" ") > 0) {
                w = w.split(" ");
                for (var h = w.length; h--; )
                    n.off(q, w[h], C)
            } else if (a.isArray(C))
                for (h = C.length; h--; )
                    n.off(q, w, C[h]);
            else if (a.isObject(w))
                for (h in w)
                    n.off(q, h, w[h]);
            else if (tmpEvtType = e(q, w)) {
                w = tmpEvtType;
                f(q, w, C)
            } else if (q.elem && (tmpEvtType = e(q.elem, w))) {
                w = tmpEvtType;
                f(q.elem, w, C)
            } else if (z[w])
                z._off(q, w, C);
            else if (w) {
                if (q.events)
                    if (C) {
                        if (q.events[w]) {
                            q = q.events[w];
                            for (h = q.length; h--; )
                                if (q[h] == C) {
                                    q.splice(h, 1);
                                    break
                                }
                        }
                    } else
                        q.events[w] = []
            } else
                q.events = {}
        },fire: function(q, w) {
            var C = [].slice.call(arguments, 2), h;
            if (h = e(q, w)) {
                w = h;
                C = document.createEvent("HTMLEvents");
                C.initEvent(w, true, true);
                q.dispatchEvent(C)
            } else if (q.elem && (h = e(q.elem, w))) {
                w = h;
                C = document.createEvent("HTMLEvents");
                C.initEvent(w, true, true);
                q.elem.dispatchEvent(C)
            } else if (q.events && q.events[w]) {
                h = q.events[w];
                for (var o = 0, v = h.length; o < v; o++)
                    h[o].apply(window,
                    C)
            }
        },getActionTarget: function(q, w, C, h) {
            q = q.target;
            var o = w || 3;
            w = w !== -1;
            C = C || "cmd";
            h = h || document.body;
            if (q === h)
                return q.getAttribute(C) ? q : null;
            for (; q && q !== h && (w ? o-- > 0 : true); )
                if (q.getAttribute(C))
                    return q;
                else
                    q = q.parentNode;
            return null
        },bindCommands: function(q, w, C, h) {
            var o = g.platform.touchDevice ? "tap" : "click";
            if (arguments.length === 1) {
                C = q;
                q = document.body;
                w = o
            } else if (arguments.length === 2) {
                C = w;
                w = o
            }
            if (!q._commends)
                q._commends = {};
            if (q._commends[w])
                g.extend(q._commends[w], C);
            else {
                q._commends[w] = C;
                h = h || "cmd";
                q.getAttribute(h) || q.setAttribute(h, "void");
                g.event.on(q, w, function(v) {
                    var D = g.event.getActionTarget(v, -1, h, this.parentNode);
                    if (D) {
                        var p = D.getAttribute(h), y = D.getAttribute("param");
                        D.href && D.getAttribute("href").indexOf("#") === 0 && v.preventDefault();
                        this._commends[w][p] && this._commends[w][p](y, D, v)
                    }
                })
            }
        }}, m, r, k;
    if (g.platform.touchDevice) {
        m = "touchstart";
        r = "touchmove";
        k = "touchend"
    } else {
        m = "mousedown";
        r = "mousemove";
        k = "mouseup"
    }
    var d = function(q) {
        var w = q.touches;
        if (w && w[0])
            return {x: w[0].clientX,y: w[0].clientY};
        return {x: q.clientX,y: q.clientY}
    }, t = function(q, w) {
        if (!q || !w)
            return 0;
        return Math.sqrt((q.x - w.x) * (q.x - w.x) + (q.y - w.y) * (q.y - w.y))
    }, B = [], z = {_fire: function(q, w, C) {
            g.each(B, function(h) {
                h.ele == q && w == h.evtType && C == h.handler && C.call(q, {type: w})
            })
        },_off: function(q, w, C) {
            g.each(B, function(h, o) {
                var v = h.actions;
                if (h.ele == q && w == h.evtType && C == h.handler) {
                    for (var D in v) {
                        var p = v[D];
                        a.isObject(p) ? n.off(p.ele, D, p.handler) : n.off(q, D, p)
                    }
                    B.splice(o, 1)
                }
            })
        },tap: function(q, w) {
            var C, h, o, v, D, p = function(M) {
                var P = M.touches;
                if (!P ||
                P.length == 1)
                    h = C = d(M)
            }, y = function(M) {
                M.preventDefault();
                h = d(M)
            }, F = function(M) {
                var P = Date.now(), E = t(h, C), G = t(h, o);
                if (E < 20) {
                    D = v && P - v < 300 && G < 20 ? "doubletap" : "tap";
                    w.call(q, {target: M.target,oriEvt: M,type: D})
                }
                o = h;
                v = P
            };
            n.on(q, m, p);
            n.on(q, r, y);
            n.on(q, k, F);
            var H = {ele: q,evtType: "tap",handler: w};
            H.actions = {};
            H.actions[m] = p;
            H.actions[r] = y;
            H.actions[k] = F;
            B.push(H)
        },hold: function(q, w) {
            var C, h, o, v = function(F) {
                F.stopPropagation();
                var H = F.touches;
                if (!H || H.length == 1) {
                    h = o = d(F);
                    pt_time = Date.now();
                    C = setTimeout(function() {
                        H &&
                        H.length != 1 || t(h, o) < 20 && w.call(q, {oriEvt: F,target: F.target,type: "hold"})
                    }, 2E3)
                }
            }, D = function(F) {
                F.stopPropagation();
                F.preventDefault();
                o = d(F)
            }, p = function(F) {
                F.stopPropagation();
                clearTimeout(C)
            };
            n.on(q, m, v);
            n.on(q, r, D);
            n.on(q, k, p);
            var y = {ele: q,evtType: "hold",handler: w};
            y.actions = {};
            y.actions[m] = v;
            y.actions[r] = D;
            y.actions[k] = p;
            B.push(y)
        },swipe: function(q, w) {
            var C, h, o, v, D, p = function(P, E) {
                var G = Math.atan2(-P.y + E.y, P.x - E.x) * 180 / Math.PI;
                if (G < 45 && G > -45)
                    return "right";
                if (G >= 45 && G < 135)
                    return "top";
                if (G >= 135 ||
                G < -135)
                    return "left";
                if (G >= -135 && G <= -45)
                    return "bottom"
            }, y = function(P) {
                var E = P.touches;
                if (!E || E.length == 1) {
                    C = h = d(P);
                    o = Date.now()
                }
            }, F = function(P) {
                P.preventDefault();
                h = d(P)
            }, H = function(P) {
                var E;
                D = h;
                v = Date.now();
                if (t(C, D) > 30 && v - o < 500) {
                    E = p(D, C);
                    w.call(q, {oriEvt: P,target: P.target,type: "swipe",direction: E})
                }
            };
            n.on(q, m, y);
            n.on(q, r, F);
            n.on(q, k, H);
            var M = {ele: q,evtType: "swipe",handler: w};
            M.actions = {};
            M.actions[m] = y;
            M.actions[r] = F;
            M.actions[k] = H;
            B.push(M)
        },transform: function(q, w) {
            var C, h, o, v = function(y) {
                var F =
                y.touches;
                if (F)
                    if (F.length == 2) {
                        C = d(y.touches[0]);
                        h = d(y.touches[1]);
                        o = t(C, h)
                    }
            }, D = function(y) {
                y.preventDefault();
                var F = y.touches;
                if (F)
                    if (F.length == 2) {
                        F = d(y.touches[0]);
                        var H = d(y.touches[1]);
                        F = t(F, H);
                        w.call(q, {oriEvt: y,target: y.target,type: "transform",scale: F / o,rotate: rotate})
                    }
            };
            n.on(q, m, v);
            n.on(q, r, D);
            var p = {ele: q,evtType: "transform",handler: w};
            p.actions = {};
            p.actions[m] = v;
            p.actions[r] = D;
            B.push(p)
        },scrollstart: function(q, w) {
            var C, h, o = function(D) {
                if (!C) {
                    C = true;
                    w.call(q, {oriEvt: D,target: D.target,type: "scrollstart"})
                }
                clearTimeout(h);
                h = setTimeout(function() {
                    C = false
                }, 250)
            };
            n.on(q, "scroll", o);
            var v = {ele: q,evtType: "scrollstart",handler: w};
            v.actions = {};
            v.actions.scroll = o;
            B.push(v)
        },scrollend: function(q, w) {
            var C, h = function(v) {
                clearTimeout(C);
                C = setTimeout(function() {
                    w.call(q, {oriEvt: v,target: v.target,type: "scrollend"})
                }, 250)
            };
            n.on(q, "scroll", h);
            var o = {ele: q,evtType: "scrollend",handler: w};
            o.actions = {};
            o.actions.scroll = h;
            B.push(o)
        },scrolltobottom: function(q, w) {
            var C = document.body, h = function(v) {
                C.scrollHeight <= C.scrollTop + window.innerHeight &&
                w.call(q, {oriEvt: v,target: v.target,type: "scrolltobottom"})
            };
            n.on(q, "scroll", h);
            var o = {ele: q,evtType: "scrolltobottom",handler: w};
            o.actions = {};
            o.actions.scroll = h;
            B.push(o)
        },ortchange: function(q, w) {
            var C = window.innerWidth, h = function(v) {
                var D = window.innerWidth;
                if (C != D) {
                    w.call(q, {oriEvt: v,target: v.target,type: "ortchange",orientation: D > window.innerHeight ? "landscape" : "portrait"});
                    C = D
                }
            };
            n.on(window, "resize", h);
            var o = {ele: q,evtType: "ortchange",handler: w};
            o.actions = {};
            o.actions.resize = h;
            B.push(o)
        }};
    g.event =
    n
});
J.$package(function(g) {
    var a = g.dom, b = g.event, c = g.type, e = function(f) {
        f.target.type !== "range" && f.preventDefault()
    }, j = function() {
        setTimeout(function() {
            if (!location.hash) {
                var f = window.innerHeight + 60;
                document.documentElement.clientHeight < f && a.setStyle(document.body, "minHeight", f + "px");
                window.scrollTo(0, 1)
            }
        }, 200)
    };
    g.Util = {hideUrlBar: function() {
            b.on(window, "load", j)
        },preventScrolling: function() {
            b.on(document, "touchmove", e)
        },activeScrolling: function() {
            b.off(document, "touchmove", e)
        },scrollToTop: function(f, n) {
            var m =
            g.Animation, r = document.body, k = window.pageYOffset || document.body.scrollTop || document.documentElement.scrollTop;
            a.setStyle(r, a.getVendorPropertyName("transform"), "translate3d(0," + -k + "px,0)");
            r.scrollTop ? r.scrollTop = 0 : document.documentElement.scrollTop = 0;
            (new m({selector: r,duration: f,runType: n,use3d: true})).translateY(0).transit()
        },fixElement: function(f, n) {
            var m = c.isUndefined, r = window.innerHeight, k = window.innerWidth, d = f.clientHeight, t = f.clientWidth, B, z;
            g.support.fixed ? a.setStyle(f, {position: "fixed",
                top: n.top + "px",left: n.left + "px",bottom: n.bottom + "px",right: n.right + "px"}) : b.on(window, "scrollend", function() {
                B = window.pageYOffset + (m(n.top) ? m(n.bottom) ? "" : r - n.bottom - d : n.top);
                z = window.pageXOffset + (m(n.left) ? m(n.right) ? "" : k - n.right - t : n.left);
                a.setStyle(f, {position: "absolute",top: B + "px",left: z + "px"})
            })
        },hoverEffect: function(f, n) {
            var m, r, k, d;
            if (g.platform.touchDevice) {
                m = "touchstart";
                r = "touchmove";
                k = "touchend";
                d = f
            } else {
                m = "mousedown";
                r = "mousemove";
                k = "mouseup";
                d = document.body
            }
            b.on(f, m, function() {
                a.addClass(f,
                n)
            });
            b.on(f, r, function(t) {
                t.preventDefault()
            });
            b.on(d, k, function() {
                a.removeClass(f, n)
            })
        }}
});
J.$package(function(g) {
    var a = g.dom, b = g.event, c = g.type, e = a.isSupprot3d(), j = g.Class({init: function(f) {
            this.setElems(f.selector);
            this.setDuration(f.duration || 1E3);
            this.setRunType(f.runType || "ease-in-out");
            this.setDelay(f.delay || 0);
            this.setUsed3d(f.use3d);
            this.transformArr = []
        },setDuration: function(f) {
            this.duration = f;
            return this
        },setDelay: function(f) {
            this.delay = f;
            return this
        },setElems: function(f) {
            if (c.isString(f))
                this.elems = a.$(f);
            else if (c.isArray(f))
                this.elems = f;
            else if (f.tagName)
                this.elems = [f];
            return this
        },
        setRunType: function(f) {
            this.runType = f;
            return this
        },setUsed3d: function(f) {
            this.use3d = f;
            return this
        },scale: function(f) {
            this.transformArr.push("scale(" + f + ")");
            return this
        },scaleX: function(f) {
            this.transformArr.push("scalex(" + f + ")");
            return this
        },scaleY: function(f) {
            this.transformArr.push("scaley(" + f + ")");
            return this
        },rotate: function(f) {
            this.transformArr.push("rotate(" + f + "deg)");
            return this
        },rotateX: function(f) {
            this.transformArr.push("rotatex(" + f + "deg)");
            return this
        },rotateY: function() {
            this.transformArr.push("rotatey(" +
            rotateY + "deg)");
            return this
        },rotateZ: function(f) {
            this.transformArr.push("rotatez(" + f + "deg)");
            return this
        },translate: function(f, n, m) {
            e && m ? this.transformArr.push("translate3d(" + f + "," + n + "," + m + ")") : this.transformArr.push("translate(" + f + "," + n + ")");
            return this
        },translateX: function(f) {
            this.translate(f, 0);
            return this
        },translateY: function(f) {
            this.translate(0, f);
            return this
        },skew: function(f, n) {
            this.transformArr.push("skew(" + f + "deg," + n + "deg)");
            return this
        },skewX: function(f) {
            this.transformArr.push("skewx(" + f +
            "deg)");
            return this
        },skewY: function(f) {
            this.transformArr.push("skewy(" + f + "deg)");
            return this
        },setStyle: function(f, n) {
            var m = "";
            if (c.isUndefined(this.styleStr))
                this.styleStr = "";
            if (c.isObject(f))
                g.each(f, function(r, k) {
                    m += a.toCssStyle(a.getVendorPropertyName(k)) + ":" + r + ";"
                });
            else if (c.isString(f))
                m += a.toCssStyle(a.getVendorPropertyName(f)) + ":" + n + ";";
            this.styleStr += m;
            return this
        },toOrigin: function() {
            this.transformArr = [];
            return this
        },transit: function(f) {
            var n = this, m = this.elems;
            g.each(m, function(r) {
                n._transit(r)
            });
            window.setTimeout(function() {
                b.fire(n, "end");
                g.each(m, function(r) {
                    a.setStyle(r, a.getVendorPropertyName("transition"), "")
                });
                f && f.call(n)
            }, this.duration);
            return this
        },_transit: function(f) {
            var n = this.transformArr.join(" ");
            if (e && this.use3d)
                n += " translatez(0)";
            var m = "all " + this.duration / 1E3 + "s " + this.runType + " " + this.delay / 1E3 + "s";
            a.setStyle(f, a.getVendorPropertyName("transition"), m);
            f.style[a.getVendorPropertyName("transform")] = n;
            f.style.cssText += this.styleStr;
            b.fire(this, "start")
        }});
    g.Animation = j
});
J.$package(function(g) {
    var a = window.location.host;
    g.cookie = {set: function(b, c, e, j, f) {
            if (f) {
                var n = new Date;
                n.setTime((new Date).getTime() + 36E5 * f)
            }
            window.document.cookie = b + "=" + c + "; " + (f ? "expires=" + n.toGMTString() + "; " : "") + (j ? "path=" + j + "; " : "path=/; ") + (e ? "domain=" + e + ";" : "domain=" + a + ";");
            return true
        },get: function(b) {
            b = window.document.cookie.match(RegExp("(?:^|;+|\\s+)" + b + "=([^;]*)"));
            return !b ? "" : b[1]
        },remove: function(b, c, e) {
            window.document.cookie = b + "=; expires=Mon, 26 Jul 1997 05:00:00 GMT; " + (e ? "path=" +
            e + "; " : "path=/; ") + (c ? "domain=" + c + ";" : "domain=" + a + ";")
        }}
});
J.$package(function(g) {
    var a = {serializeParam: function(b) {
            if (!b)
                return "";
            var c = [], e;
            for (e in b)
                c.push(encodeURIComponent(e) + "=" + encodeURIComponent(b[e]));
            return c.join("&")
        },getUrlParam: function(b, c, e) {
            b = (b = RegExp("(?:\\?|#|&)" + b + "=([^&]*)(?:$|&|#)", "i").exec(c)) ? b[1] : "";
            return !e ? decodeURIComponent(b) : b
        },ajax: function(b) {
            var c = b.method.toLocaleUpperCase(), e = "POST" == c, j = false, f = b.timeout, n = b.withCredentials, m = "async" in b ? b.async : true, r = window.XMLHttpRequest ? new XMLHttpRequest : false;
            if (!r) {
                b.error &&
                b.error.call(null, {ret: 999,msg: "Create XHR Error!"});
                return false
            }
            var k = a.serializeParam(b.param);
            !e && (b.url += (b.url.indexOf("?") > -1 ? "&" : "?") + k);
            r.open(c, b.url, m);
            if (n)
                r.withCredentials = true;
            e && r.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            var d = 0;
            r.onreadystatechange = function() {
                if (4 == r.readyState) {
                    var B = r.status;
                    if (B >= 200 && B < 300 || B == 304 || B == 0) {
                        B = r.responseText.replace(/(\r|\n|\t)/gi, "");
                        var z = null;
                        try {
                            z = JSON.parse(B)
                        } catch (q) {
                        }
                        b.onSuccess && b.onSuccess(z, r)
                    } else
                        b.onError &&
                        b.onError(r, +new Date - t);
                    j = true;
                    d && clearTimeout(d)
                }
            };
            var t = +new Date;
            r.send(e ? k : void 0);
            if (f)
                d = setTimeout(function() {
                    if (!j) {
                        r.abort();
                        b.onTimeout && b.onTimeout(r)
                    }
                }, f);
            return r
        },offlineSend: function(b) {
            navigator.onLine ? a.ajax(b) : saveDataLocal(b)
        }};
    g.http = a
});
typeof define === "function" && define("jm", [], function() {
    return J
});
(function(g, a) {
    function b(u) {
        if (j === "")
            return u;
        u = u.charAt(0).toUpperCase() + u.substr(1);
        return j + u
    }
    var c = Math, e = a.createElement("div").style, j = function() {
        for (var u = "webkitT,MozT,msT,OT,t".split(","), s, A = 0, I = u.length; A < I; A++) {
            s = u[A] + "ransform";
            if (s in e)
                return u[A].substr(0, u[A].length - 1)
        }
        return false
    }(), f = j ? "-" + j.toLowerCase() + "-" : "", n = b("transform"), m = b("transitionProperty"), r = b("transitionDuration"), k = b("transformOrigin"), d = b("transitionTimingFunction"), t = b("transitionDelay"), B = /android/gi.test(navigator.appVersion),
    z = /iphone|ipad/gi.test(navigator.appVersion), q = /hp-tablet/gi.test(navigator.appVersion), w = b("perspective") in e, C = "ontouchstart" in g && !q, h = !!j, o = b("transition") in e, v = "onorientationchange" in g ? "orientationchange" : "resize", D = C ? "touchstart" : "mousedown", p = C ? "touchmove" : "mousemove", y = C ? "touchend" : "mouseup", F = C ? "touchcancel" : "mouseup", H = j == "Moz" ? "DOMMouseScroll" : "mousewheel", M;
    M = j === false ? false : {"": "transitionend",webkit: "webkitTransitionEnd",Moz: "transitionend",O: "oTransitionEnd",ms: "MSTransitionEnd"}[j];
    var P = function() {
        return g.requestAnimationFrame || g.webkitRequestAnimationFrame || g.mozRequestAnimationFrame || g.oRequestAnimationFrame || g.msRequestAnimationFrame || function(u) {
            return setTimeout(u, 1)
        }
    }(), E = g.cancelRequestAnimationFrame || g.webkitCancelAnimationFrame || g.webkitCancelRequestAnimationFrame || g.mozCancelRequestAnimationFrame || g.oCancelRequestAnimationFrame || g.msCancelRequestAnimationFrame || clearTimeout, G = w ? " translateZ(0)" : "", O = function(u, s) {
        var A = this, I;
        A.wrapper = typeof u == "object" ? u : a.getElementById(u);
        A.wrapper.style.overflow = "hidden";
        A.scroller = A.wrapper.children[0];
        A.options = {hScroll: true,vScroll: true,x: 0,y: 0,bounce: true,bounceLock: false,momentum: true,lockDirection: true,useTransform: true,useTransition: false,topOffset: 0,checkDOMChanges: false,handleClick: true,hScrollbar: true,vScrollbar: true,fixedScrollbar: B,hideScrollbar: z,fadeScrollbar: z && w,scrollbarClass: "",zoom: false,zoomMin: 1,zoomMax: 4,doubleTapZoom: 2,wheelAction: "scroll",snap: false,snapThreshold: 1,onRefresh: null,onBeforeScrollStart: function(L) {
                for (var Q =
                L.target; Q.nodeType != 1; )
                    Q = Q.parentNode;
                Q.tagName != "P" && L.preventDefault()
            },onScrollStart: null,onBeforeScrollMove: null,onScrollMove: null,onBeforeScrollEnd: null,onScrollEnd: null,onTouchEnd: null,onDestroy: null,onZoomStart: null,onZoom: null,onZoomEnd: null};
        for (I in s)
            A.options[I] = s[I];
        A.x = A.options.x;
        A.y = A.options.y;
        A.options.useTransform = h && A.options.useTransform;
        A.options.hScrollbar = A.options.hScroll && A.options.hScrollbar;
        A.options.vScrollbar = A.options.vScroll && A.options.vScrollbar;
        A.options.zoom = A.options.useTransform &&
        A.options.zoom;
        A.options.useTransition = o && A.options.useTransition;
        if (A.options.zoom && B)
            G = "";
        A.scroller.style[m] = A.options.useTransform ? f + "transform" : "top left";
        A.scroller.style[r] = "0";
        A.scroller.style[k] = "0 0";
        if (A.options.useTransition)
            A.scroller.style[d] = "cubic-bezier(0.33,0.66,0.66,1)";
        if (A.options.useTransform)
            A.scroller.style[n] = "translate(" + A.x + "px," + A.y + "px)" + G;
        else
            A.scroller.style.cssText += ";position:absolute;top:" + A.y + "px;left:" + A.x + "px";
        if (A.options.useTransition)
            A.options.fixedScrollbar =
            true;
        A.refresh();
        A._bind(v, g);
        A._bind(D);
        if (!C) {
            A._bind("mouseout", A.wrapper);
            A.options.wheelAction != "none" && A._bind(H)
        }
        if (A.options.checkDOMChanges)
            A.checkDOMTime = setInterval(function() {
                A._checkDOMChanges()
            }, 500)
    };
    O.prototype = {enabled: true,x: 0,y: 0,steps: [],scale: 1,currPageX: 0,currPageY: 0,pagesX: [],pagesY: [],aniTime: null,wheelZoomCount: 0,handleEvent: function(u) {
            switch (u.type) {
                case D:
                    if (!C && u.button !== 0)
                        break;
                    this._start(u);
                    break;
                case p:
                    this._move(u);
                    break;
                case y:
                case F:
                    this._end(u);
                    break;
                case v:
                    this._resize();
                    break;
                case H:
                    this._wheel(u);
                    break;
                case "mouseout":
                    this._mouseout(u);
                    break;
                case M:
                    this._transitionEnd(u)
            }
        },_checkDOMChanges: function() {
            this.moved || this.zoomed || this.animating || this.scrollerW == this.scroller.offsetWidth * this.scale && this.scrollerH == this.scroller.offsetHeight * this.scale || this.refresh()
        },_scrollbar: function(u) {
            var s;
            if (this[u + "Scrollbar"]) {
                if (!this[u + "ScrollbarWrapper"]) {
                    s = a.createElement("div");
                    if (this.options.scrollbarClass)
                        s.className = this.options.scrollbarClass + u.toUpperCase();
                    else
                        s.style.cssText =
                        "position:absolute;z-index:100;" + (u == "h" ? "height:7px;bottom:1px;left:2px;right:" + (this.vScrollbar ? "7" : "2") + "px" : "width:7px;bottom:" + (this.hScrollbar ? "7" : "2") + "px;top:2px;right:1px");
                    s.style.cssText += ";pointer-events:none;" + f + "transition-property:opacity;" + f + "transition-duration:" + (this.options.fadeScrollbar ? "350ms" : "0") + ";overflow:hidden;opacity:" + (this.options.hideScrollbar ? "0" : "1");
                    this.wrapper.appendChild(s);
                    this[u + "ScrollbarWrapper"] = s;
                    s = a.createElement("div");
                    if (!this.options.scrollbarClass)
                        s.style.cssText =
                        "position:absolute;z-index:100;background:rgba(0,0,0,0.5);border:1px solid rgba(255,255,255,0.9);" + f + "background-clip:padding-box;" + f + "box-sizing:border-box;" + (u == "h" ? "height:100%" : "width:100%") + ";" + f + "border-radius:3px;border-radius:3px";
                    s.style.cssText += ";pointer-events:none;" + f + "transition-property:" + f + "transform;" + f + "transition-timing-function:cubic-bezier(0.33,0.66,0.66,1);" + f + "transition-duration:0;" + f + "transform: translate(0,0)" + G;
                    if (this.options.useTransition)
                        s.style.cssText += ";" + f + "transition-timing-function:cubic-bezier(0.33,0.66,0.66,1)";
                    this[u + "ScrollbarWrapper"].appendChild(s);
                    this[u + "ScrollbarIndicator"] = s
                }
                if (u == "h") {
                    this.hScrollbarSize = this.hScrollbarWrapper.clientWidth;
                    this.hScrollbarIndicatorSize = c.max(c.round(this.hScrollbarSize * this.hScrollbarSize / this.scrollerW), 8);
                    this.hScrollbarIndicator.style.width = this.hScrollbarIndicatorSize + "px";
                    this.hScrollbarMaxScroll = this.hScrollbarSize - this.hScrollbarIndicatorSize;
                    this.hScrollbarProp = this.hScrollbarMaxScroll / this.maxScrollX
                } else {
                    this.vScrollbarSize = this.vScrollbarWrapper.clientHeight;
                    this.vScrollbarIndicatorSize = c.max(c.round(this.vScrollbarSize * this.vScrollbarSize / this.scrollerH), 8);
                    this.vScrollbarIndicator.style.height = this.vScrollbarIndicatorSize + "px";
                    this.vScrollbarMaxScroll = this.vScrollbarSize - this.vScrollbarIndicatorSize;
                    this.vScrollbarProp = this.vScrollbarMaxScroll / this.maxScrollY
                }
                this._scrollbarPos(u, true)
            } else if (this[u + "ScrollbarWrapper"]) {
                if (h)
                    this[u + "ScrollbarIndicator"].style[n] = "";
                this[u + "ScrollbarWrapper"].parentNode.removeChild(this[u + "ScrollbarWrapper"]);
                this[u +
                "ScrollbarWrapper"] = null;
                this[u + "ScrollbarIndicator"] = null
            }
        },_resize: function() {
            var u = this;
            setTimeout(function() {
                u.refresh()
            }, B ? 200 : 0)
        },_pos: function(u, s) {
            if (!this.zoomed) {
                u = this.hScroll ? u : 0;
                s = this.vScroll ? s : 0;
                if (this.options.useTransform)
                    this.scroller.style[n] = "translate(" + u + "px," + s + "px) scale(" + this.scale + ")" + G;
                else {
                    u = c.round(u);
                    s = c.round(s);
                    this.scroller.style.left = u + "px";
                    this.scroller.style.top = s + "px"
                }
                this.x = u;
                this.y = s;
                this._scrollbarPos("h");
                this._scrollbarPos("v")
            }
        },_scrollbarPos: function(u,
        s) {
            var A = u == "h" ? this.x : this.y;
            if (this[u + "Scrollbar"]) {
                A = this[u + "ScrollbarProp"] * A;
                if (A < 0) {
                    if (!this.options.fixedScrollbar) {
                        A = this[u + "ScrollbarIndicatorSize"] + c.round(A * 3);
                        if (A < 8)
                            A = 8;
                        this[u + "ScrollbarIndicator"].style[u == "h" ? "width" : "height"] = A + "px"
                    }
                    A = 0
                } else if (A > this[u + "ScrollbarMaxScroll"])
                    if (this.options.fixedScrollbar)
                        A = this[u + "ScrollbarMaxScroll"];
                    else {
                        A = this[u + "ScrollbarIndicatorSize"] - c.round((A - this[u + "ScrollbarMaxScroll"]) * 3);
                        if (A < 8)
                            A = 8;
                        this[u + "ScrollbarIndicator"].style[u == "h" ? "width" : "height"] =
                        A + "px";
                        A = this[u + "ScrollbarMaxScroll"] + (this[u + "ScrollbarIndicatorSize"] - A)
                    }
                this[u + "ScrollbarWrapper"].style[t] = "0";
                this[u + "ScrollbarWrapper"].style.opacity = s && this.options.hideScrollbar ? "0" : "1";
                this[u + "ScrollbarIndicator"].style[n] = "translate(" + (u == "h" ? A + "px,0)" : "0," + A + "px)") + G
            }
        },_start: function(u) {
            var s = C ? u.touches[0] : u, A, I;
            if (this.enabled) {
                this.options.onBeforeScrollStart && this.options.onBeforeScrollStart.call(this, u);
                if (this.options.useTransition || this.options.zoom)
                    this._transitionTime(0);
                this.zoomed =
                this.animating = this.moved = false;
                this.dirY = this.dirX = this.absDistY = this.absDistX = this.distY = this.distX = 0;
                if (this.options.zoom && C && u.touches.length > 1) {
                    I = c.abs(u.touches[0].pageX - u.touches[1].pageX);
                    A = c.abs(u.touches[0].pageY - u.touches[1].pageY);
                    this.touchesDistStart = c.sqrt(I * I + A * A);
                    this.originX = c.abs(u.touches[0].pageX + u.touches[1].pageX - this.wrapperOffsetLeft * 2) / 2 - this.x;
                    this.originY = c.abs(u.touches[0].pageY + u.touches[1].pageY - this.wrapperOffsetTop * 2) / 2 - this.y;
                    this.options.onZoomStart && this.options.onZoomStart.call(this,
                    u)
                }
                if (this.options.momentum) {
                    if (this.options.useTransform) {
                        A = getComputedStyle(this.scroller, null)[n].replace(/[^0-9\-.,]/g, "").split(",");
                        I = A[4] * 1;
                        A = A[5] * 1
                    } else {
                        I = getComputedStyle(this.scroller, null).left.replace(/[^0-9-]/g, "") * 1;
                        A = getComputedStyle(this.scroller, null).top.replace(/[^0-9-]/g, "") * 1
                    }
                    if (I != this.x || A != this.y) {
                        this.options.useTransition ? this._unbind(M) : E(this.aniTime);
                        this.steps = [];
                        this._pos(I, A)
                    }
                }
                this.absStartX = this.x;
                this.absStartY = this.y;
                this.startX = this.x;
                this.startY = this.y;
                this.pointX =
                s.pageX;
                this.pointY = s.pageY;
                this.startTime = u.timeStamp || Date.now();
                this.options.onScrollStart && this.options.onScrollStart.call(this, u);
                this._bind(p);
                this._bind(y);
                this._bind(F)
            }
        },_move: function(u) {
            var s = C ? u.touches[0] : u, A = s.pageX - this.pointX, I = s.pageY - this.pointY, L = this.x + A, Q = this.y + I, R = u.timeStamp || Date.now();
            this.options.onBeforeScrollMove && this.options.onBeforeScrollMove.call(this, u);
            if (this.options.zoom && C && u.touches.length > 1) {
                L = c.abs(u.touches[0].pageX - u.touches[1].pageX);
                Q = c.abs(u.touches[0].pageY -
                u.touches[1].pageY);
                this.touchesDist = c.sqrt(L * L + Q * Q);
                this.zoomed = true;
                s = 1 / this.touchesDistStart * this.touchesDist * this.scale;
                if (s < this.options.zoomMin)
                    s = 0.5 * this.options.zoomMin * Math.pow(2, s / this.options.zoomMin);
                else if (s > this.options.zoomMax)
                    s = 2 * this.options.zoomMax * Math.pow(0.5, this.options.zoomMax / s);
                this.lastScale = s / this.scale;
                L = this.originX - this.originX * this.lastScale + this.x;
                Q = this.originY - this.originY * this.lastScale + this.y;
                this.scroller.style[n] = "translate(" + L + "px," + Q + "px) scale(" + s + ")" + G;
                this.options.onZoom &&
                this.options.onZoom.call(this, u)
            } else {
                this.pointX = s.pageX;
                this.pointY = s.pageY;
                if (L > 0 || L < this.maxScrollX)
                    L = this.options.bounce ? this.x + A / 2 : L >= 0 || this.maxScrollX >= 0 ? 0 : this.maxScrollX;
                if (Q > this.minScrollY || Q < this.maxScrollY)
                    Q = this.options.bounce ? this.y + I / 2 : Q >= this.minScrollY || this.maxScrollY >= 0 ? this.minScrollY : this.maxScrollY;
                this.distX += A;
                this.distY += I;
                this.absDistX = c.abs(this.distX);
                this.absDistY = c.abs(this.distY);
                if (!(this.absDistX < 6 && this.absDistY < 6)) {
                    if (this.options.lockDirection)
                        if (this.absDistX >
                        this.absDistY + 5) {
                            Q = this.y;
                            I = 0
                        } else if (this.absDistY > this.absDistX + 5) {
                            L = this.x;
                            A = 0
                        }
                    this.moved = true;
                    this._pos(L, Q);
                    this.dirX = A > 0 ? -1 : A < 0 ? 1 : 0;
                    this.dirY = I > 0 ? -1 : I < 0 ? 1 : 0;
                    if (R - this.startTime > 300) {
                        this.startTime = R;
                        this.startX = this.x;
                        this.startY = this.y
                    }
                    this.options.onScrollMove && this.options.onScrollMove.call(this, u)
                }
            }
        },_end: function(u) {
            if (!(C && u.touches.length !== 0)) {
                var s = this, A = C ? u.changedTouches[0] : u, I, L, Q = {dist: 0,time: 0}, R = {dist: 0,time: 0}, X = (u.timeStamp || Date.now()) - s.startTime, x = s.x, K = s.y;
                s._unbind(p);
                s._unbind(y);
                s._unbind(F);
                s.options.onBeforeScrollEnd && s.options.onBeforeScrollEnd.call(s, u);
                if (s.zoomed) {
                    x = s.scale * s.lastScale;
                    x = Math.max(s.options.zoomMin, x);
                    x = Math.min(s.options.zoomMax, x);
                    s.lastScale = x / s.scale;
                    s.scale = x;
                    s.x = s.originX - s.originX * s.lastScale + s.x;
                    s.y = s.originY - s.originY * s.lastScale + s.y;
                    s.scroller.style[r] = "200ms";
                    s.scroller.style[n] = "translate(" + s.x + "px," + s.y + "px) scale(" + s.scale + ")" + G;
                    s.zoomed = false;
                    s.refresh();
                    s.options.onZoomEnd && s.options.onZoomEnd.call(s, u)
                } else {
                    if (s.moved) {
                        if (X <
                        300 && s.options.momentum) {
                            Q = x ? s._momentum(x - s.startX, X, -s.x, s.scrollerW - s.wrapperW + s.x, s.options.bounce ? s.wrapperW : 0) : Q;
                            R = K ? s._momentum(K - s.startY, X, -s.y, s.maxScrollY < 0 ? s.scrollerH - s.wrapperH + s.y - s.minScrollY : 0, s.options.bounce ? s.wrapperH : 0) : R;
                            x = s.x + Q.dist;
                            K = s.y + R.dist;
                            if (s.x > 0 && x > 0 || s.x < s.maxScrollX && x < s.maxScrollX)
                                Q = {dist: 0,time: 0};
                            if (s.y > s.minScrollY && K > s.minScrollY || s.y < s.maxScrollY && K < s.maxScrollY)
                                R = {dist: 0,time: 0};
                            var N = JM.event.getActionTarget(u, 2);
                            if (N && N.getAttribute("cmd") == "clickMemberItem") {
                                var T =
                                function(U) {
                                    U.stopPropagation();
                                    U.preventDefault();
                                    JM.event.off(N, "click", T)
                                };
                                JM.event.on(N, "click", T)
                            }
                        }
                        if (Q.dist || R.dist) {
                            Q = c.max(c.max(Q.time, R.time), 10);
                            if (s.options.snap) {
                                R = x - s.absStartX;
                                X = K - s.absStartY;
                                if (c.abs(R) < s.options.snapThreshold && c.abs(X) < s.options.snapThreshold)
                                    s.scrollTo(s.absStartX, s.absStartY, 200);
                                else {
                                    R = s._snap(x, K);
                                    x = R.x;
                                    K = R.y;
                                    Q = c.max(R.time, Q)
                                }
                            }
                            s.scrollTo(c.round(x), c.round(K), Q)
                        } else if (s.options.snap) {
                            R = x - s.absStartX;
                            X = K - s.absStartY;
                            if (c.abs(R) < s.options.snapThreshold && c.abs(X) <
                            s.options.snapThreshold)
                                s.scrollTo(s.absStartX, s.absStartY, 200);
                            else {
                                R = s._snap(s.x, s.y);
                                if (R.x != s.x || R.y != s.y)
                                    s.scrollTo(R.x, R.y, R.time)
                            }
                        } else
                            s._resetPos(200)
                    } else {
                        if (C)
                            if (s.doubleTapTimer && s.options.zoom) {
                                clearTimeout(s.doubleTapTimer);
                                s.doubleTapTimer = null;
                                s.options.onZoomStart && s.options.onZoomStart.call(s, u);
                                s.zoom(s.pointX, s.pointY, s.scale == 1 ? s.options.doubleTapZoom : 1);
                                s.options.onZoomEnd && setTimeout(function() {
                                    s.options.onZoomEnd.call(s, u)
                                }, 200)
                            } else if (this.options.handleClick)
                                s.doubleTapTimer =
                                setTimeout(function() {
                                    s.doubleTapTimer = null;
                                    for (I = A.target; I.nodeType != 1; )
                                        I = I.parentNode;
                                    if (I.tagName != "SELECT" && I.tagName != "INPUT" && I.tagName != "TEXTAREA") {
                                        L = a.createEvent("MouseEvents");
                                        L.initMouseEvent("click", true, true, u.view, 1, A.screenX, A.screenY, A.clientX, A.clientY, u.ctrlKey, u.altKey, u.shiftKey, u.metaKey, 0, null);
                                        L._fake = true;
                                        I.dispatchEvent(L)
                                    }
                                }, s.options.zoom ? 250 : 0);
                        s._resetPos(200)
                    }
                    s.options.onTouchEnd && s.options.onTouchEnd.call(s, u)
                }
            }
        },_resetPos: function(u) {
            var s = this.x >= 0 ? 0 : this.x < this.maxScrollX ?
            this.maxScrollX : this.x, A = this.y >= this.minScrollY || this.maxScrollY > 0 ? this.minScrollY : this.y < this.maxScrollY ? this.maxScrollY : this.y;
            if (s == this.x && A == this.y) {
                if (this.moved) {
                    this.moved = false;
                    this.options.onScrollEnd && this.options.onScrollEnd.call(this)
                }
                if (this.hScrollbar && this.options.hideScrollbar) {
                    if (j == "webkit")
                        this.hScrollbarWrapper.style[t] = "300ms";
                    this.hScrollbarWrapper.style.opacity = "0"
                }
                if (this.vScrollbar && this.options.hideScrollbar) {
                    if (j == "webkit")
                        this.vScrollbarWrapper.style[t] = "300ms";
                    this.vScrollbarWrapper.style.opacity =
                    "0"
                }
            } else
                this.scrollTo(s, A, u || 0)
        },_wheel: function(u) {
            var s = this, A, I;
            if ("wheelDeltaX" in u) {
                A = u.wheelDeltaX / 2;
                I = u.wheelDeltaY / 2
            } else if ("wheelDelta" in u)
                A = I = u.wheelDelta / 2;
            else if ("detail" in u)
                A = I = -u.detail * 9;
            else
                return;
            if (s.options.wheelAction == "zoom") {
                I = s.scale * Math.pow(2, 1 / 3 * (I ? I / Math.abs(I) : 0));
                if (I < s.options.zoomMin)
                    I = s.options.zoomMin;
                if (I > s.options.zoomMax)
                    I = s.options.zoomMax;
                if (I != s.scale) {
                    !s.wheelZoomCount && s.options.onZoomStart && s.options.onZoomStart.call(s, u);
                    s.wheelZoomCount++;
                    s.zoom(u.pageX,
                    u.pageY, I, 400);
                    setTimeout(function() {
                        s.wheelZoomCount--;
                        !s.wheelZoomCount && s.options.onZoomEnd && s.options.onZoomEnd.call(s, u)
                    }, 400)
                }
            } else {
                A = s.x + A;
                I = s.y + I;
                if (A > 0)
                    A = 0;
                else if (A < s.maxScrollX)
                    A = s.maxScrollX;
                if (I > s.minScrollY)
                    I = s.minScrollY;
                else if (I < s.maxScrollY)
                    I = s.maxScrollY;
                s.maxScrollY < 0 && s.scrollTo(A, I, 0)
            }
        },_mouseout: function(u) {
            var s = u.relatedTarget;
            if (s)
                for (; s = s.parentNode; )
                    if (s == this.wrapper)
                        return;
            this._end(u)
        },_transitionEnd: function(u) {
            if (u.target == this.scroller) {
                this._unbind(M);
                this._startAni()
            }
        },
        _startAni: function() {
            var u = this, s = u.x, A = u.y, I = Date.now(), L, Q, R;
            if (!u.animating)
                if (u.steps.length) {
                    L = u.steps.shift();
                    if (L.x == s && L.y == A)
                        L.time = 0;
                    u.animating = true;
                    u.moved = true;
                    if (u.options.useTransition) {
                        u._transitionTime(L.time);
                        u._pos(L.x, L.y);
                        u.animating = false;
                        L.time ? u._bind(M) : u._resetPos(0)
                    } else {
                        R = function() {
                            var X = Date.now();
                            if (X >= I + L.time) {
                                u._pos(L.x, L.y);
                                u.animating = false;
                                u.options.onAnimationEnd && u.options.onAnimationEnd.call(u);
                                u._startAni()
                            } else {
                                X = (X - I) / L.time - 1;
                                Q = c.sqrt(1 - X * X);
                                X = (L.x - s) * Q +
                                s;
                                u._pos(X, (L.y - A) * Q + A);
                                if (u.animating)
                                    u.aniTime = P(R)
                            }
                        };
                        R()
                    }
                } else
                    u._resetPos(400)
        },_transitionTime: function(u) {
            u += "ms";
            this.scroller.style[r] = u;
            if (this.hScrollbar)
                this.hScrollbarIndicator.style[r] = u;
            if (this.vScrollbar)
                this.vScrollbarIndicator.style[r] = u
        },_momentum: function(u, s, A, I, L) {
            s = c.abs(u) / s;
            var Q = s * s / 0.0012, R = 0;
            R = 0;
            if (u > 0 && Q > A) {
                R = L / (6 / (Q / s * 6.0E-4));
                A += R;
                s = s * A / Q;
                Q = A
            } else if (u < 0 && Q > I) {
                R = L / (6 / (Q / s * 6.0E-4));
                I += R;
                s = s * I / Q;
                Q = I
            }
            Q *= u < 0 ? -1 : 1;
            R = s / 6.0E-4;
            return {dist: Q,time: c.round(R)}
        },_offset: function(u) {
            for (var s =
            -u.offsetLeft, A = -u.offsetTop; u = u.offsetParent; ) {
                s -= u.offsetLeft;
                A -= u.offsetTop
            }
            if (u != this.wrapper) {
                s *= this.scale;
                A *= this.scale
            }
            return {left: s,top: A}
        },_snap: function(u, s) {
            var A, I, L;
            L = this.pagesX.length - 1;
            A = 0;
            for (I = this.pagesX.length; A < I; A++)
                if (u >= this.pagesX[A]) {
                    L = A;
                    break
                }
            L == this.currPageX && L > 0 && this.dirX < 0 && L--;
            u = this.pagesX[L];
            I = (I = c.abs(u - this.pagesX[this.currPageX])) ? c.abs(this.x - u) / I * 500 : 0;
            this.currPageX = L;
            L = this.pagesY.length - 1;
            for (A = 0; A < L; A++)
                if (s >= this.pagesY[A]) {
                    L = A;
                    break
                }
            L == this.currPageY &&
            L > 0 && this.dirY < 0 && L--;
            s = this.pagesY[L];
            A = (A = c.abs(s - this.pagesY[this.currPageY])) ? c.abs(this.y - s) / A * 500 : 0;
            this.currPageY = L;
            L = c.round(c.max(I, A)) || 200;
            return {x: u,y: s,time: L}
        },_bind: function(u, s, A) {
            (s || this.scroller).addEventListener(u, this, !!A)
        },_unbind: function(u, s, A) {
            (s || this.scroller).removeEventListener(u, this, !!A)
        },destroy: function() {
            this.scroller.style[n] = "";
            this.vScrollbar = this.hScrollbar = false;
            this._scrollbar("h");
            this._scrollbar("v");
            this._unbind(v, g);
            this._unbind(D);
            this._unbind(p);
            this._unbind(y);
            this._unbind(F);
            if (!this.options.hasTouch) {
                this._unbind("mouseout", this.wrapper);
                this._unbind(H)
            }
            this.options.useTransition && this._unbind(M);
            this.options.checkDOMChanges && clearInterval(this.checkDOMTime);
            this.options.onDestroy && this.options.onDestroy.call(this)
        },refresh: function() {
            var u, s, A, I = 0;
            s = 0;
            if (this.scale < this.options.zoomMin)
                this.scale = this.options.zoomMin;
            this.wrapperW = this.wrapper.clientWidth || 1;
            this.wrapperH = this.wrapper.clientHeight || 1;
            this.minScrollY = -this.options.topOffset || 0;
            this.scrollerW =
            c.round(this.scroller.offsetWidth * this.scale);
            this.scrollerH = c.round((this.scroller.offsetHeight + this.minScrollY) * this.scale);
            this.maxScrollX = this.wrapperW - this.scrollerW;
            this.maxScrollY = this.wrapperH - this.scrollerH + this.minScrollY;
            this.dirY = this.dirX = 0;
            this.options.onRefresh && this.options.onRefresh.call(this);
            this.hScroll = this.options.hScroll && this.maxScrollX < 0;
            this.vScroll = this.options.vScroll && (!this.options.bounceLock && !this.hScroll || this.scrollerH > this.wrapperH);
            this.hScrollbar = this.hScroll &&
            this.options.hScrollbar;
            this.vScrollbar = this.vScroll && this.options.vScrollbar && this.scrollerH > this.wrapperH;
            u = this._offset(this.wrapper);
            this.wrapperOffsetLeft = -u.left;
            this.wrapperOffsetTop = -u.top;
            if (typeof this.options.snap == "string") {
                this.pagesX = [];
                this.pagesY = [];
                A = this.scroller.querySelectorAll(this.options.snap);
                u = 0;
                for (s = A.length; u < s; u++) {
                    I = this._offset(A[u]);
                    I.left += this.wrapperOffsetLeft;
                    I.top += this.wrapperOffsetTop;
                    this.pagesX[u] = I.left < this.maxScrollX ? this.maxScrollX : I.left * this.scale;
                    this.pagesY[u] =
                    I.top < this.maxScrollY ? this.maxScrollY : I.top * this.scale
                }
            } else if (this.options.snap) {
                for (this.pagesX = []; I >= this.maxScrollX; ) {
                    this.pagesX[s] = I;
                    I -= this.wrapperW;
                    s++
                }
                if (this.maxScrollX % this.wrapperW)
                    this.pagesX[this.pagesX.length] = this.maxScrollX - this.pagesX[this.pagesX.length - 1] + this.pagesX[this.pagesX.length - 1];
                s = I = 0;
                for (this.pagesY = []; I >= this.maxScrollY; ) {
                    this.pagesY[s] = I;
                    I -= this.wrapperH;
                    s++
                }
                if (this.maxScrollY % this.wrapperH)
                    this.pagesY[this.pagesY.length] = this.maxScrollY - this.pagesY[this.pagesY.length -
                    1] + this.pagesY[this.pagesY.length - 1]
            }
            this._scrollbar("h");
            this._scrollbar("v");
            if (!this.zoomed) {
                this.scroller.style[r] = "0";
                this._resetPos(200)
            }
        },scrollTo: function(u, s, A, I) {
            var L = u;
            this.stop();
            L.length || (L = [{x: u,y: s,time: A,relative: I}]);
            u = 0;
            for (s = L.length; u < s; u++) {
                if (L[u].relative) {
                    L[u].x = this.x - L[u].x;
                    L[u].y = this.y - L[u].y
                }
                this.steps.push({x: L[u].x,y: L[u].y,time: L[u].time || 0})
            }
            this._startAni()
        },scrollToElement: function(u, s) {
            var A;
            if (u = u.nodeType ? u : this.scroller.querySelector(u)) {
                A = this._offset(u);
                A.left += this.wrapperOffsetLeft;
                A.top += this.wrapperOffsetTop;
                A.left = A.left > 0 ? 0 : A.left < this.maxScrollX ? this.maxScrollX : A.left;
                A.top = A.top > this.minScrollY ? this.minScrollY : A.top < this.maxScrollY ? this.maxScrollY : A.top;
                s = s === undefined ? c.max(c.abs(A.left) * 2, c.abs(A.top) * 2) : s;
                this.scrollTo(A.left, A.top, s)
            }
        },scrollToPage: function(u, s, A) {
            A = A === undefined ? 400 : A;
            this.options.onScrollStart && this.options.onScrollStart.call(this);
            if (this.options.snap) {
                u = u == "next" ? this.currPageX + 1 : u == "prev" ? this.currPageX - 1 : u;
                s = s ==
                "next" ? this.currPageY + 1 : s == "prev" ? this.currPageY - 1 : s;
                u = u < 0 ? 0 : u > this.pagesX.length - 1 ? this.pagesX.length - 1 : u;
                s = s < 0 ? 0 : s > this.pagesY.length - 1 ? this.pagesY.length - 1 : s;
                this.currPageX = u;
                this.currPageY = s;
                u = this.pagesX[u];
                s = this.pagesY[s]
            } else {
                u = -this.wrapperW * u;
                s = -this.wrapperH * s;
                if (u < this.maxScrollX)
                    u = this.maxScrollX;
                if (s < this.maxScrollY)
                    s = this.maxScrollY
            }
            this.scrollTo(u, s, A)
        },disable: function() {
            this.stop();
            this._resetPos(0);
            this.enabled = false;
            this._unbind(p);
            this._unbind(y);
            this._unbind(F)
        },enable: function() {
            this.enabled =
            true
        },stop: function() {
            this.options.useTransition ? this._unbind(M) : E(this.aniTime);
            this.steps = [];
            this.animating = this.moved = false
        },zoom: function(u, s, A, I) {
            var L = A / this.scale;
            if (this.options.useTransform) {
                this.zoomed = true;
                I = I === undefined ? 200 : I;
                u = u - this.wrapperOffsetLeft - this.x;
                s = s - this.wrapperOffsetTop - this.y;
                this.x = u - u * L + this.x;
                this.y = s - s * L + this.y;
                this.scale = A;
                this.refresh();
                this.x = this.x > 0 ? 0 : this.x < this.maxScrollX ? this.maxScrollX : this.x;
                this.y = this.y > this.minScrollY ? this.minScrollY : this.y < this.maxScrollY ?
                this.maxScrollY : this.y;
                this.scroller.style[r] = I + "ms";
                this.scroller.style[n] = "translate(" + this.x + "px," + this.y + "px) scale(" + A + ")" + G;
                this.zoomed = false
            }
        },isReady: function() {
            return !this.moved && !this.zoomed && !this.animating
        }};
    e = null;
    g.iScroll = O;
    typeof define === "function" && define("iscroll", [], function() {
        return O
    })
})(this, document);
function pgvGetCookieByName(g) {
    g = Tcss.d.cookie.match(RegExp("(^|\\s)" + g + "([^;]*)(;|$)"));
    return g == null ? pvNone : unescape(g[2])
}
function pgvRealSetCookie(g) {
    Tcss.d.cookie = g + ";path=/;domain=" + Tcss.domainToSet + ";expires=Sun, 18 Jan 2038 00:00:00 GMT;"
}
function pgvGetDomainInfo() {
    typeof pvCurDomain != "undefined" && pvCurDomain != "" && (Tcss.dm = pvCurDomain);
    typeof pvCurUrl != "undefined" && pvCurUrl != "" && (Tcss.url = escape(pvCurUrl));
    Tcss.arg == pvNone && (Tcss.arg = "")
}
function pgvIsPgvDomain() {
    var g = Tcss.dm.split("."), a = Tcss.dm;
    return g.length >= 3 && g[g.length - 2] == "qq" && (a = g[g.length - 3]), !/(^qzone$)|(^cache$)|(^ossweb-img$)|(^ring$)|(^im$)|(^fo$)|(^shuqian$)|(^photo$)|(^pet$)|(^r2$)|(^bar$)|(^client$)|(^music$)|(^pay$)|(^sg$)|(^vip$)|(^show$)|(^qqtang$)|(^safe$)|(^service$)|(^love$)|(^mail$)|(^qqgamecdnimg$)|(^netbar$)|(^dnf$)|(^qqgame$)|(^mgp$)|(^magic$)|(^city$)|(^1314$)|(^wb$)|(^qun$)|(^aq$)|(^17roco$)|(^minigame$)|(^cf$)|(^zg$)|(^pc$)|(^shurufa$)|(^live$)|(\.3366\.com$)/.test(a)
}
function pgvGetRefInfo() {
    typeof pvRefDomain != "undefined" && pvRefDomain != "" && (Tcss.rdm = pvRefDomain);
    Tcss.rdm = Tcss.rdm == pvNone ? "" : Tcss.rdm;
    typeof pvRefUrl != "undefined" && pvRefUrl != "" && (Tcss.rurl = pvRefUrl);
    Tcss.rurl == pvNone && (Tcss.rurl = "");
    Tcss.rarg == pvNone && (Tcss.rarg = "");
    if (pgvIsPgvDomain()) {
        if (Tcss.rdm == "") {
            var g = Tcss.l.href.match(/[?&#](((pgv_ref)|(ref)|(ptlang))=[^&#]+)(#|&|$)/);
            g && (Tcss.rdm = g[1] == null ? "" : escape(g[1]))
        }
        (g = Tcss.l.href.match(/[?&#](pref=[^&#]+)(&|#|$)/)) && (Tcss.rdm = g[1] == null ? "" : escape(g[1]))
    }
}
function pgvGetColumn() {
    Tcss.column = "";
    typeof vsPgvCol != "undefined" && vsPgvCol != "" && (Tcss.column += vsPgvCol)
}
function pgvGetTopic() {
    Tcss.subject = "";
    typeof pvCSTM != "undefined" && pvCSTM != "" && (Tcss.subject = pvCSTM)
}
function trimUin(g) {
    var a = pvNone;
    return g != pvNone && (g = g.replace(RegExp("[^0-9]", "gm"), ""), a = g.replace(RegExp("^0+", "gm"), ""), a == "" && (a = pvNone)), a
}
function pgvGetNewRand() {
    var g = trimUin(pgvGetCookieByName("uin_cookie=")), a = trimUin(pgvGetCookieByName("adid=")), b = trimUin(pgvGetCookieByName("uin=")), c = trimUin(pgvGetCookieByName("luin=")), e = trimUin(pgvGetCookieByName("clientuin=")), j = trimUin(pgvGetCookieByName("pt2gguin=")), f = trimUin(pgvGetCookieByName("zzpaneluin=")), n = trimUin(pgvGetCookieByName("o_cookie=")), m = pgvGetCookieByName("pgv_pvid=");
    return n.length > 13 && pgvRealSetCookie("o_cookie="), b != pvNone ? (pgvRealSetCookie("o_cookie=" + b), "&nrnd=" +
    b) : c != pvNone ? (pgvRealSetCookie("o_cookie=" + c), "&nrnd=" + c) : j != pvNone ? (pgvRealSetCookie("o_cookie=" + j), "&nrnd=" + j) : g != pvNone ? (pgvRealSetCookie("o_cookie=" + g), "&nrnd=" + g) : n != pvNone ? "&nrnd=" + n : a != pvNone ? (pgvRealSetCookie("o_cookie=" + a), "&nrnd=" + a) : e != pvNone ? (pgvRealSetCookie("o_cookie=" + e), "&nrnd=" + e) : f != pvNone ? (pgvRealSetCookie("o_cookie=" + f), "&nrnd=" + f) : m != pvNone ? "&nrnd=F" + m : "&nrnd=-"
}
function hotClick() {
    document.addEventListener ? document.addEventListener("click", clickEvent, false) : document.attachEvent && document.attachEvent("onclick", clickEvent);
    window.addEventListener ? window.addEventListener("onbeforeunload", staybounce, false) : window.attachEvent && window.attachEvent("onbeforeunload", staybounce)
}
function getScrollXY() {
    return document.body.scrollTop ? {x: document.body.scrollLeft,y: document.body.scrollTop} : {x: document.documentElement.scrollLeft,y: document.documentElement.scrollTop}
}
function clickEvent(g) {
    g = g || window.event;
    var a = g.clientX + getScrollXY().x - document.getElementsByTagName("body")[0].offsetLeft, b = g.clientY + getScrollXY().y - document.getElementsByTagName("body")[0].offsetTop;
    if (!(a < 0 || b < 0))
        try {
            var c = 1;
            typeof g.srcElement != "undefined" && g.srcElement == "[object]" && typeof g.srcElement.parentElement != "undefined" && g.srcElement.parentElement == "[object]" && (c = 0);
            pvClickCount += c;
            var e = new Image(1, 1);
            e.src = "http://trace.qq.com:80/collect?pj=8888&url=" + escape(location.href) + "&w=" +
            screen.width + "&x=" + a + "&y=" + b + "&v=" + c + "&u=" + trimUin(pgvGetCookieByName("o_cookie"));
            delete e
        } catch (j) {
        }
}
function tracert() {
    if (pgvIsPgvDomain()) {
        sendUrl = new Image(1, 1);
        var g = escape(window.location.href);
        g = "pj=1990&dm=" + Tcss.dm + "&url=" + Tcss.url + "&arg=" + Tcss.arg + "&rdm=" + Tcss.rdm + "&rurl=" + Tcss.rurl + "&rarg=" + Tcss.rarg + "&icache=" + Tcss.pgUserType + "&uv=&nu=&ol=&loc=" + g + "&column=" + Tcss.column + "&subject=" + Tcss.subject + pgvGetNewRand() + "&rnd=" + Math.round(Math.random() * 1E5);
        sendUrl.src = "http://trace.qq.com:80/collect?" + g;
        g = trimUin(pgvGetCookieByName("o_cookie="));
        if (pvSetupHot == 1 && g != pvNone && g % 10 == 3 && !/\/a\//.test(location.href)) {
            hotClick();
            pvStartTime = (new Date).getTime()
        }
    }
}
function staybounce() {
    dt = new Date;
    var g = dt.getTime(), a = new Image(1, 1);
    a.src = "http://trace.qq.com:80/collect?pj=8887&url=" + escape(location.href) + "&t=" + parseInt((g - pvStartTime) / 1E3) + "&v=" + pvClickCount + "&u=" + trimUin(pgvGetCookieByName("o_cookie"));
    delete a
}
var pvNone = "-", pvStartTime = 0, sendUrl, pvClickCount = 0, pvSetupHot = 1, pvCurDomain = "", pvCurUrl = "", pvRefDomain = "", pvRefUrl = "";
if (typeof pvRepeatCount == "undefined")
    var pvRepeatCount = 1;
(function() {
    function g(h) {
        this.url = [];
        this.init(h)
    }
    var a, b, c, e, j, f, n, m, r, k, d, t, B = 0, z = 0;
    _ver = "tcss.3.1.5";
    _speedTestUrl = "http://jsqmt.qq.com/cdn_djl.js";
    window.Tcss = {};
    var q = typeof tracert == "function" && typeof pgvGetColumn == "function" && typeof pgvGetTopic == "function" && typeof pgvGetDomainInfo == "function" && typeof pgvGetRefInfo == "function";
    if (typeof w == "undefined")
        var w = 1;
    g.prototype = {init: function(h) {
            h ? e = h : e = {};
            a = document;
            if (!e.statIframe && window != top)
                try {
                    a = top.document
                } catch (o) {
                }
            typeof a == "undefined" &&
            (a = document);
            b = a.location;
            c = a.body;
            q && (Tcss.d = a, Tcss.l = b);
            k = [];
            d = [];
            t = []
        },run: function() {
            var h, o, v;
            h = (new Date).getTime();
            C.init();
            this.url.push(this.getDomainInfo());
            this.coverCookie();
            C.setCookie("ssid");
            C.save();
            this.url.unshift("http://pingfore." + this.getCookieSetDomain(j) + "/pingd?");
            this.url.push(this.getRefInfo(e));
            try {
                navigator.cookieEnabled ? this.url.push("&pvid=" + C.setCookie("pgv_pvid", true)) : this.url.push("&pvid=NoCookie")
            } catch (D) {
                this.url.push("&pvid=NoCookie")
            }
            this.url.push(this.getMainEnvInfo());
            this.url.push(this.getExtendEnvInfo());
            Tcss.pgUserType = "";
            if (e.pgUserType || e.reserved2) {
                o = e.pgUserType || e.reserved2;
                o = escape(o.substring(0, 256));
                Tcss.pgUserType = o;
                t.push("pu=" + Tcss.pgUserType)
            }
            q && (pgvGetColumn(), pgvGetTopic(), this.url.push("&column=" + Tcss.column + "&subject=" + Tcss.subject), tracert());
            this.url.push("&vs=" + _ver);
            C.setCookie("ts_uid", true);
            o = (new Date).getTime();
            k.push("tm=" + (o - h));
            B && k.push("ch=" + B);
            e.extParam ? v = e.extParam + "|" : v = "";
            this.url.push("&ext=" + escape(v + k.join(";")));
            this.url.push("&hurlcn=" +
            escape(d.join(";")));
            this.url.push("&rand=" + Math.round(Math.random() * 1E5));
            typeof _speedMark == "undefined" ? this.url.push("&reserved1=-1") : this.url.push("&reserved1=" + (new Date - _speedMark));
            (h = this.getSud()) && t.push("su=" + escape(h.substring(0, 256)));
            this.url.push("&tt=" + escape(t.join(";")));
            this.sendInfo(this.url.join(""));
            if (z == 1) {
                h = this.getParameter("tcss_rp_dm", a.URL);
                h != Tcss.dm && this.sendInfo(this.url.join("").replace(/\?dm=(.*?)\&/, "?dm=" + h + "&"))
            }
            e.hot && (document.attachEvent ? document.attachEvent("onclick",
            function(p) {
                pgvWatchClick(p)
            }) : document.addEventListener("click", function(p) {
                pgvWatchClick(p)
            }, false));
            e.repeatApplay && e.repeatApplay == "true" && typeof w != "undefined" && (w = 1)
        },getSud: function() {
            if (e.sessionUserType)
                return e.sessionUserType;
            return this.getParameter(e.sudParamName || "sessionUserType", a.URL)
        },coverCookie: function() {
            if (e.crossDomain && e.crossDomain == "on") {
                var h = this.getParameter("tcss_uid", a.URL), o = this.getParameter("tcss_sid", a.URL), v = this.getParameter("tcss_refer", a.URL), D = this.getParameter("tcss_last",
                a.URL);
                o && h && (z = 1, C.setCookie("ssid", false, o), C.save(), C.setCookie("ts_refer", true, v), C.setCookie("ts_last", true, D), C.setCookie("pgv_pvid", true, h))
            }
        },getDomainInfo: function(h) {
            var o;
            return o = b.hostname.toLowerCase(), e.virtualDomain && (d.push("ad=" + o), o = e.virtualDomain), this.getCurrentUrl(), Tcss.dm = o, q && pgvGetDomainInfo(), j = Tcss.dm, f || (f = this.getCookieSetDomain(b.hostname.toLowerCase()), q && (Tcss.domainToSet = f)), h && (Tcss.dm += ".hot"), "dm=" + Tcss.dm + "&url=" + Tcss.url
        },getCurrentUrl: function() {
            var h = "", o =
            "-";
            h = escape(b.pathname);
            b.search != "" && (o = escape(b.search.substr(1)));
            if (e.senseParam) {
                var v = this.getParameter(e.senseParam, a.URL);
                v && (h += "_" + v)
            }
            e.virtualURL && (d.push("au=" + h), h = e.virtualURL);
            Tcss.url = h;
            Tcss.arg = o
        },getRefInfo: function(h) {
            var o = "-", v = "-", D = "-", p = a.referrer, y;
            h = this.getParameter(h.tagParamName || "ADTAG", a.URL);
            y = p.indexOf("://");
            if (y > -1)
                (y = p.match(/(\w+):\/\/([^\:|\/]+)(\:\d*)?(.*\/)([^#|\?|\n]+)?(#.*)?(\?.*)?/i)) && (o = y[2], v = y[4] + (y[5] ? y[5] : ""));
            if (p.indexOf("?") != -1) {
                y = p.indexOf("?") +
                1;
                D = p.substr(y)
            }
            p = o;
            e.virtualRefDomain && (o != "-" && d.push("ard=" + o), o = e.virtualRefDomain);
            e.virtualRefURL && (v != "-" && d.push("aru=" + escape(v)), v = e.virtualRefURL);
            var F;
            h && (F = o + v, o = "ADTAG", v = h);
            n = o;
            m = escape(v);
            if (n == "-" || n == "ADTAG" && p == "-") {
                o = C.get("ts_last=", true);
                o != "-" && k.push("ls=" + o)
            }
            C.setCookie("ts_last", true, escape((b.hostname + b.pathname).substring(0, 128)));
            o = C.get("ts_refer=", true);
            o != "-" && k.push("rf=" + o);
            p = b.hostname;
            e.inner && (p = "," + p + "," + e.inner + ",");
            if (!(n == "-" || ("," + p + ",").indexOf(n) > -1 || z ==
            1)) {
                v = escape((n + v).substring(0, 128));
                v != o && (B = 2);
                C.setCookie("ts_refer", true, v)
            }
            return Tcss.rdm = n, Tcss.rurl = m, Tcss.rarg = escape(D), q && pgvGetRefInfo(), F ? "&rdm=" + Tcss.rdm + "&rurl=" + Tcss.rurl + "&rarg=" + Tcss.rarg + "&or=" + F : "&rdm=" + Tcss.rdm + "&rurl=" + Tcss.rurl + "&rarg=" + Tcss.rarg
        },getMainEnvInfo: function() {
            var h = "";
            try {
                var o = "-", v = "-", D = "-", p = "-", y = "-", F = 0, H = navigator;
                self.screen && (o = screen.width + "x" + screen.height, v = screen.colorDepth + "-bit");
                H.language ? D = H.language.toLowerCase() : H.browserLanguage && (D = H.browserLanguage.toLowerCase());
                F = H.javaEnabled() ? 1 : 0;
                p = H.platform;
                y = (new Date).getTimezoneOffset() / 60;
                h = "&scr=" + o + "&scl=" + v + "&lang=" + D + "&java=" + F + "&pf=" + p + "&tz=" + y
            } catch (M) {
            }finally {
                return h
            }
        },getExtendEnvInfo: function() {
            var h = "";
            try {
                var o = b.href, v = "-";
                h += "&flash=" + this.getFlashInfo();
                c.addBehavior && (c.addBehavior("#default#homePage"), c.isHomePage(o) && (h += "&hp=Y"));
                c.addBehavior && (c.addBehavior("#default#clientCaps"), v = c.connectionType);
                h += "&ct=" + v
            } catch (D) {
            }finally {
                return h
            }
        },getFlashInfo: function() {
            var h = "-", o = navigator;
            try {
                if (o.plugins &&
                o.plugins.length)
                    for (var v = 0; v < o.plugins.length; v++) {
                        if (o.plugins[v].name.indexOf("Shockwave Flash") > -1) {
                            h = o.plugins[v].description.split("Shockwave Flash ")[1];
                            break
                        }
                    }
                else if (window.ActiveXObject)
                    for (v = 12; v >= 5; v--)
                        try {
                            if (eval("new ActiveXObject('ShockwaveFlash.ShockwaveFlash." + v + "');")) {
                                h = v + ".0";
                                break
                            }
                        } catch (D) {
                        }
            } catch (p) {
            }
            return h
        },getParameter: function(h, o) {
            if (h && o) {
                var v = o.match(RegExp("(\\?|#|&)" + h + "=([^&^#]*)(#|&|$)"));
                return v ? v[2] : ""
            }
            return ""
        },getCookieSetDomain: function(h) {
            for (var o, v, D,
            p = [], y = 0, F = 0; F < h.length; F++)
                h.charAt(F) == "." && (p[y] = F, y++);
            return o = p.length, v = h.indexOf(".cn"), v > -1 && o--, o == 1 || o > 1 && (D = h.substring(p[o - 2] + 1)), D
        },watchClick: function(h) {
            try {
                var o = true, v = "", D;
                D = window.event ? window.event.srcElement : h.target;
                switch (D.tagName) {
                    case "A":
                        v = "<A href=" + D.href + ">" + D.innerHTML + "</a>";
                        break;
                    case "IMG":
                        v = "<IMG src=" + D.src + ">";
                        break;
                    case "INPUT":
                        v = "<INPUT type=" + D.type + " value=" + D.value + ">";
                        break;
                    case "BUTTON":
                        v = "<BUTTON>" + D.innerText + "</BUTTON>";
                        break;
                    case "SELECT":
                        v = "SELECT";
                        break;
                    default:
                        o = false
                }
                if (o) {
                    var p = new g(e), y = p.getElementPos(D);
                    if (e.coordinateId) {
                        var F = p.getElementPos(document.getElementById(e.coordinateId));
                        y.x -= F.x
                    }
                    p.url.push(p.getDomainInfo(true));
                    p.url.push("&hottag=" + escape(v));
                    p.url.push("&hotx=" + y.x);
                    p.url.push("&hoty=" + y.y);
                    p.url.push("&rand=" + Math.round(Math.random() * 1E5));
                    p.url.unshift("http://pinghot." + this.getCookieSetDomain(j) + "/pingd?");
                    p.sendInfo(p.url.join(""))
                }
            } catch (H) {
            }
        },getElementPos: function(h) {
            if (h.parentNode === null || h.style.display == "none")
                return false;
            var o = navigator.userAgent.toLowerCase(), v = null, D = [], p;
            if (h.getBoundingClientRect) {
                var y, F, H, M;
                return p = h.getBoundingClientRect(), y = Math.max(document.documentElement.scrollTop, document.body.scrollTop), F = Math.max(document.documentElement.scrollLeft, document.body.scrollLeft), H = document.body.clientTop, M = document.body.clientLeft, {x: p.left + F - M,y: p.top + y - H}
            }
            if (document.getBoxObjectFor) {
                p = document.getBoxObjectFor(h);
                D = [p.x - (h.style.borderLeftWidth ? Math.floor(h.style.borderLeftWidth) : 0), p.y - (h.style.borderTopWidth ?
                    Math.floor(h.style.borderTopWidth) : 0)]
            } else {
                D = [h.offsetLeft, h.offsetTop];
                v = h.offsetParent;
                if (v != h)
                    for (; v; ) {
                        D[0] += v.offsetLeft;
                        D[1] += v.offsetTop;
                        v = v.offsetParent
                    }
                if (o.indexOf("opera") > -1 || o.indexOf("safari") > -1 && h.style.position == "absolute") {
                    D[0] -= document.body.offsetLeft;
                    D[1] -= document.body.offsetTop
                }
            }
            for (h.parentNode ? v = h.parentNode : v = null; v && v.tagName != "BODY" && v.tagName != "HTML"; ) {
                D[0] -= v.scrollLeft;
                D[1] -= v.scrollTop;
                v.parentNode ? v = v.parentNode : v = null
            }
            return {x: D[0],y: D[1]}
        },sendClick: function() {
            e.hottag &&
            (this.url.push(this.getDomainInfo(true)), this.url.push("&hottag=" + escape(e.hottag)), this.url.push("&hotx=9999&hoty=9999"), this.url.push("&rand=" + Math.round(Math.random() * 1E5)), this.url.unshift("http://pinghot." + this.getCookieSetDomain(j) + "/pingd?"), this.sendInfo(this.url.join("")))
        },pgvGetArgs: function() {
            this.getDomainInfo();
            var h = [];
            return h.push("tcss_rp_dm=" + Tcss.dm), h.push("tcss_uid=" + C.get("pgv_pvid=", true)), h.push("tcss_sid=" + C.get("ssid=", true)), h.push("tcss_refer=" + C.get("ts_refer=", true)),
            h.push("tcss_last=" + C.get("ts_last=", true)), h.join("&")
        },sendInfo: function(h) {
            r = new Image(1, 1);
            Tcss.img = r;
            r.onload = r.onerror = r.onabort = function() {
                r.onload = r.onerror = r.onabort = null;
                Tcss.img = null
            };
            r.src = h
        }};
    var C = {sck: [],sco: {},init: function() {
            var h = this.get("pgv_info=", true);
            if (h != "-") {
                h = h.split("&");
                for (var o = 0; o < h.length; o++) {
                    var v = h[o].split("=");
                    this.set(v[0], unescape(v[1]))
                }
            }
        },get: function(h, o) {
            var v = o ? a.cookie : this.get("pgv_info=", true), D = "-", p;
            p = v.indexOf(h);
            if (p > -1) {
                p += h.length;
                D = v.indexOf(";",
                p);
                D == -1 && (D = v.length);
                if (!o) {
                    var y = v.indexOf("&", p);
                    y > -1 && (D = Math.min(D, y))
                }
                D = v.substring(p, D)
            }
            return D
        },set: function(h, o) {
            this.sco[h] = o;
            for (var v = false, D = this.sck.length, p = 0; p < D; p++)
                if (h == this.sck[p]) {
                    v = true;
                    break
                }
            v || this.sck.push(h)
        },setCookie: function(h, o, v) {
            var D = b.hostname, p = C.get(h + "=", o);
            if (p == "-" && !v) {
                switch (h) {
                    case "ts_uid":
                        k.push("nw=1");
                        break;
                    case "ssid":
                        B = 1
                }
                o ? p = "" : p = "s";
                v = (new Date).getUTCMilliseconds();
                p += Math.round(Math.abs(Math.random() - 1) * 2147483647) * v % 1E10
            } else
                p = v ? v : p;
            if (o)
                switch (h) {
                    case "ts_uid":
                        this.saveCookie(h +
                        "=" + p, D, this.getExpires(1051200));
                        break;
                    case "ts_refer":
                        this.saveCookie(h + "=" + p, D, this.getExpires(259200));
                        break;
                    case "ts_last":
                        this.saveCookie(h + "=" + p, D, this.getExpires(30));
                        break;
                    default:
                        this.saveCookie(h + "=" + p, f, "expires=Sun, 18 Jan 2038 00:00:00 GMT;")
                }
            else
                this.set(h, p);
            return p
        },getExpires: function(h) {
            var o = new Date;
            return o.setTime(o.getTime() + h * 60 * 1E3), "expires=" + o.toGMTString()
        },save: function() {
            if (e.sessionSpan) {
                var h = new Date;
                h.setTime(h.getTime() + e.sessionSpan * 60 * 1E3)
            }
            for (var o = "", v = this.sck.length,
            D = 0; D < v; D++)
                o += this.sck[D] + "=" + this.sco[this.sck[D]] + "&";
            o = "pgv_info=" + o.substr(0, o.length - 1);
            v = "";
            h && (v = "expires=" + h.toGMTString());
            this.saveCookie(o, f, v)
        },saveCookie: function(h, o, v) {
            a.cookie = h + ";path=/;domain=" + o + ";" + v
        }};
    window.pgvMain = function(h, o) {
        var v = "";
        o ? (v = o, _ver = "tcsso.3.1.5") : (v = h, _ver = "tcss.3.1.5");
        try {
            q && (typeof pvRepeatCount != "undefined" && pvRepeatCount == 1 ? (w = 1, pvRepeatCount = 2) : w = 2);
            if (w == 1) {
                w = 2;
                (new g(v)).run()
            }
        } catch (D) {
        }
    };
    window.pgvSendClick = function(h) {
        (new g(h)).sendClick()
    };
    window.pgvWatchClick =
    function(h) {
        (new g(h)).watchClick(h)
    };
    window.pgvGetArgs = function(h) {
        return (new g(h)).pgvGetArgs()
    };
    (function(h) {
        var o = document.createElement("script"), v = document.getElementsByTagName("script")[0];
        o.src = h;
        o.type = "text/javascript";
        o.async = true;
        v.parentNode.insertBefore(o, v)
    })(_speedTestUrl)
})();
define("ping", function() {
});
(function(g) {
    var a = null;
    window.onerror = function(b, c, e) {
        b = "http://badjs.qq.com/cgi-bin/js_report?" + ["bid=130&", "msg=" + encodeURIComponent([b, c, e, navigator.userAgent].join("|_|"))].join("&");
        a = new Image;
        a.src = b;
        new Image;
        a.src = "http://cgi.connect.qq.com/report/report_vm?monitors=[" + g + "]"
    }
})(340059);
define("error", function() {
});
define("mq.portal", ["./ping", "./error", "jm"], function() {
    J.$package("mq", function() {
        this.MAIN_DOMAIN = window.location.host;
        this.MAIN_URL = "http://" + this.MAIN_DOMAIN + "/";
        this.WEBQQ_MAIN_URL = "http://web2.qq.com/";
        this.STATIC_CGI_URL = "http://s.web2.qq.com/";
        this.DYNAMIC_CGI_URL = "http://d.web2.qq.com/";
        this.FILE_SERVER = "http://file1.web.qq.com/";
        this.setting = {};
        this.getVersion = function() {
            return "0.0.1"
        };
        this.log = function() {
            window.console && console.log && console.log.apply && console.log.apply(console, arguments)
        };
        this.debug = function() {
            if (window.console) {
                var a = console.error || console.debug || console.dir || console.log;
                a.apply && a.apply(console, arguments)
            }
        };
        this.error = function() {
            window.console && console.error && console.log.apply && console.error.apply(console, arguments)
        };
        typeof pgvMain == "function" && pgvMain();
        this.pgvSendClick = function(a) {
            if (typeof pgvSendClick == "function") {
                pgvSendClick(a);
                this.pgvSendClick = pgvSendClick
            } else
                this.pgvSendClick = function() {
                }
        };
        if (typeof localStorage == "undefined")
            localStorage = this.setting;
        var g = function(a, b) {
            return a in localStorage ? localStorage[a] == "true" : b
        };
        this.loadSetting = function() {
            this.setting = {enableHttps: g("enableHttps", false),enableCtrlEnter: g("enableCtrlEnter", false),enableVoice: g("enableVoice", true),enableNotification: g("enableNotification", true)}
        };
        this.saveSetting = function(a) {
            for (var b = ["enableVoice", "enableNotification", "enableHttps", "enableCtrlEnter"], c = 0, e; e = b[c]; c++)
                if (e in a)
                    this.setting[e] = localStorage[e] = a[e]
        }
    })
});
define("tmpl", {load: function(g) {
        throw Error("Dynamic load not allowed: " + g);
    }});
define("tmpl!../tmpl/tmpl_main_top.html", [], function() {
    return function(g) {
        var a, b = "";
        with (g || {})
            b += '<div class="accountHeader">\r\n    <div class="avatar_wrap">\r\n        <img src="' + ((a = user.avatar) == null ? "" : a) + '" width="40" height="40"/>\r\n        <span id="user_online_state"></span>\r\n    </div>\r\n    <span class="text_ellipsis user_nick">' + ((a = encode(user.nick)) == null ? "" : a) + '</span>\r\n    <span class="text_ellipsis user_shuoshuo">' + ((a = encode(user.lnick)) == null ? "" : a) + '</span>\r\n    <div class="icons_list">\r\n    \t<a href="http://qzone.qq.com" class="i_qzone" target="_blank" title="QQ\u7a7a\u95f4">QQ\u7a7a\u95f4</a>\r\n    \t<a href="http://mail.qq.com" class="i_mail" target="_blank" title="QQ\u90ae\u7bb1">QQ\u90ae\u7bb1</a>\r\n    \t<a href="http://t.qq.com" class="i_weibo" target="_blank" title="\u817e\u8baf\u5fae\u535a">\u817e\u8baf\u5fae\u535a</a>\r\n    \t<a href="http://v.qq.com" class="i_video" target="_blank" title="\u817e\u8baf\u89c6\u9891">\u817e\u8baf\u89c6\u9891</a>\r\n    \t<a href="http://www.qq.com" class="i_qqwebsite" target="_blank" title="\u817e\u8baf\u7f51">\u817e\u8baf\u7f51</a>\r\n    \t<a href="http://y.qq.com" class="i_music" target="_blank" title="QQ\u97f3\u4e50">QQ\u97f3\u4e50</a>\r\n    \t<a href="http://wallet.tenpay.com/web/" class="i_wallet" target="_blank" title="QQ\u94b1\u5305">QQ\u94b1\u5305</a>\r\n    \t<a href="http://www.pengyou.com" class="i_pengyou" target="_blank" title="\u670b\u53cb\u7f51">\u670b\u53cb\u7f51</a>\r\n    \t<a href="http://www.weiyun.com" class="i_weiyun" target="_blank" title="\u5fae\u4e91">\u5fae\u4e91</a>\r\n    </div>\r\n</div>\r\n<div class="wallpaper-ctrl">\r\n    <a href="###" class="wallpaperImg pre" id="wp-ctrl-pre" title="\u70b9\u51fb\u5207\u6362\u80cc\u666f\u56fe\u7247" cmd="clickWPPre"> </a>\r\n    <a href="###" class="wallpaperImg next" id="wp-ctrl-next" title="\u70b9\u51fb\u5207\u6362\u80cc\u666f\u56fe\u7247" cmd="clickWPNext"> </a>\r\n</div>\r\n';
        return b
    }
});
define("../lib/mui/js/mui.tab", ["jm"], function() {
    JM.$package("MUI", function(g) {
        var a = g.dom, b = g.event, c = g.type;
        this.Tab = new g.Class({init: function(e) {
                this._arr = [];
                this._map = {};
                this._selectedIndex = -1;
                e = e || {};
                e.items && this.addRange(e.items);
                this._selectedClass = e.selectedClass || "selected";
                this._selectOnCurrent = e.selectOnCurrent || false;
                "defaultSelected" in e && this.select(e.defaultSelected, true)
            },select: function(e, j, f) {
                e = this.get(e);
                if (!e)
                    return false;
                if (this._selectedIndex === e.index && !this._selectOnCurrent && !f)
                    return false;
                f = e.item;
                var n = null, m = this._selectedIndex;
                if (this._selectedIndex !== -1 && (n = this._arr[this._selectedIndex])) {
                    n.trigger && a.removeClass(n.trigger, this._selectedClass);
                    n.sheet && a.removeClass(n.sheet, this._selectedClass)
                }
                if (this._selectedIndex === e.index)
                    this._selectedIndex = -1;
                else {
                    this._selectedIndex = e.index;
                    f.trigger && a.addClass(f.trigger, this._selectedClass);
                    f.sheet && a.addClass(f.sheet, this._selectedClass)
                }
                j || b.fire(this, "selected", {current: f,currentIndex: e.index,last: n,lastIndex: m});
                return true
            },add: function(e,
            j) {
                if (this._map[e.id])
                    return false;
                this._map[e.id] = e;
                if (typeof j == "undefined")
                    this._arr.push(e);
                else {
                    this._arr.splice(j, 0, e);
                    this._selectedIndex >= j && this._selectedIndex++
                }
            },addRange: function(e) {
                for (var j = 0, f; f = e[j]; j++)
                    this.add(f)
            },remove: function(e) {
                e = this.get(e);
                if (!e)
                    return false;
                this._arr.splice(e.index, 1);
                delete this._map[e.item.id];
                this._selectedIndex === e.index && this.select(this._arr.length - 1);
                return e
            },clear: function() {
                this._selectedIndex = -1;
                this._arr = [];
                this._map = {}
            },get: function(e) {
                var j;
                if (c.isNumber(e)) {
                    j = this._arr[e];
                    if (!j)
                        return null;
                    return {item: j,index: e}
                } else {
                    j = this._map[e];
                    if (!j)
                        return null;
                    for (var f = 0, n; n = this._arr[f]; f++)
                        if (n.id === e)
                            return {item: j,index: f};
                    return null
                }
            },getSelected: function() {
                if (this._selectedIndex !== -1)
                    return {item: this._arr[this._selectedIndex],index: this._selectedIndex};
                return null
            },getSelectedIndex: function() {
                return this._selectedIndex
            },length: function() {
                return this._arr.length
            },unselect: function(e) {
                this.select(this._selectedIndex, e, true)
            }})
    })
});
define("../lib/mui/js/mui.textarea", ["jm"], function() {
    JM.$package("MUI", function(g) {
        var a = g.dom, b = g.event;
        this.AutoGrowTextarea = g.Class({init: function(c) {
                this.id = c.id;
                this.elem = a.id(this.id);
                this.maxHeight = c.maxHeight;
                this.initHeight = c.initHeight;
                this.hiddenTextarea = this.elem.cloneNode();
                this.hiddenTextarea.id = "";
                a.addClass(this.hiddenTextarea, "hidden_textarea");
                this.elem.parentNode.appendChild(this.hiddenTextarea);
                this.bindHandler()
            },_handleEvent: function(c) {
                c.type == "input" && this._onInput(c)
            },bindHandler: function() {
                var c =
                this._handleEvent = g.bind(this._handleEvent, this);
                b.on(this.elem, "input", c)
            },_onInput: function() {
                this.adjust()
            },adjust: function() {
                this.hiddenTextarea.value = this.elem.value;
                this.hiddenTextarea.style.width = this.elem.clientWidth + "px";
                var c = this.hiddenTextarea.scrollHeight;
                if (c > this.maxHeight)
                    c = this.maxHeight;
                else if (c < this.initHeight)
                    c = this.initHeight;
                if ((parseInt(a.getStyle(this.elem, "height")) || 0) !== c) {
                    a.setStyle(this.elem, "height", c + "px");
                    b.fire(this, "heightChange", c)
                }
            },reset: function() {
                a.setStyle(this.hiddenTextarea,
                "height", this.initHeight + "px");
                a.setStyle(this.hiddenTextarea, "width", parseInt(a.getStyle(this.elem, "width")) + "px")
            },getContent: function() {
                return this.elem.value
            },setContent: function(c) {
                this.elem.value = c;
                this.reset();
                this.adjust()
            },destory: function() {
                b.off(this.elem, "input", this._handleEvent);
                a.remove(this.elem)
            }})
    })
});
define("../lib/mui/js/mui.lazyload", ["jm"], function() {
    JM.$package("MUI", function(g) {
        var a = g.dom, b = g.event;
        this.I_LazyLoadImgs = g.Class({init: function(c) {
                this.scrollObj = c.scrollObj;
                this.elem = this.scrollObj.wrapper;
                this.souceProperty = c.souceProperty || "_ori_src";
                this.isFade = c.isFade;
                this.bindHandlers()
            },_onScrollEnd: function() {
                var c = this, e = this._loadFunc, j = this.souceProperty, f = a.$("img[" + j + "]", this.elem), n;
                if (f.length != 0) {
                    g.each(f, function(m) {
                        if (c.inVisibleArea(m) && (n = m.getAttribute(j)))
                            e(m, n);
                        else
                            return false
                    });
                    b.fire(this, "loadstart")
                }
            },_loadFunc: function(c, e) {
                var j = this, f = c.cloneNode();
                this.isFade && a.addClass(f, "lazyLoadImg");
                b.once(f, "load", function() {
                    if (c.parentNode) {
                        c.parentNode.replaceChild(f, c);
                        j.isFade && setTimeout(function() {
                            a.addClass(f, "loaded")
                        }, 0);
                        b.fire(j, "loadImgOver")
                    }
                });
                b.once(f, "error", function() {
                    c.setAttribute(j.souceProperty);
                    f.setAttribute(j.souceProperty, e)
                });
                c.removeAttribute(j.souceProperty);
                f.removeAttribute(j.souceProperty);
                f.src = e
            },inVisibleArea: function(c) {
                var e = this.elem.getBoundingClientRect().top,
                j = document.documentElement.clientHeight;
                e = c.getBoundingClientRect().top - e;
                c = c.clientHeight;
                if (e > -c / 2)
                    if (e < j - c / 2)
                        return true;
                return false
            },refresh: function() {
                this._onScrollEnd()
            },bindHandlers: function() {
                var c = this, e, j;
                this._onScrollEnd = g.bind(this._onScrollEnd, this);
                this._loadFunc = g.bind(this._loadFunc, this);
                e = this.scrollObj.options;
                j = e.onScrollEnd;
                e.onScrollEnd = j ? function() {
                    j.apply(this, arguments);
                    c._onScrollEnd.apply(this, arguments)
                } : this._onScrollEnd;
                b.on(window, "load resize", this._onScrollEnd)
            },
            destory: function() {
                this.scrollObj.options.onScrollEnd = null;
                b.off(window, "load resize", this._onScrollEnd)
            }})
    })
});
define("../lib/mui/js/mui.imagechange", ["jm"], function() {
    JM.$package("MUI", function(g) {
        var a = g.dom, b = g.event;
        this.ImageChange = g.Class({init: function(c) {
                this.elem = a.id(c.id);
                this.imgsWrapClassName = c.imgsWrapClassName || "wrap";
                this.btnsWrapClassName = c.btnsWrapClassName || "btnsWrap";
                this.imgsContainer = a.className(this.imgsWrapClassName, this.elem)[0];
                this.btnsContainer = a.className(this.btnsWrapClassName, this.elem)[0];
                this.currentIndex = c.currentIndex || 0;
                this.contentsSwipe = MUI.SwipeChange({id: c.id,wrapClassName: this.imgsWrapClassName,
                    fastChange: false});
                this.preIndex = this.currentIndex;
                this.count = this.contentsSwipe.count;
                this.isAutoChange = c.isAutoChange;
                this.autoChangeTime = c.autoChangeTime || 3E3;
                this._initBtns();
                this.bindHandlers();
                this.isAutoChange && this.autoChange()
            },_handleEvent: function(c) {
                c = c || window.event;
                var e = c.type;
                e == "changed" && this._onSwipeChanged(c);
                if (e == "click") {
                    c = c.target || c.srcElement;
                    if (c.tagName == "LI") {
                        c = Number(c.getAttribute("_index"));
                        this.slideTo(c);
                        this._onSwipeChanged({currentIndex: c})
                    }
                }
            },_onSwipeChanged: function(c) {
                c =
                c.currentIndex;
                a.removeClass(this.btns[this.preIndex], "selected");
                a.addClass(this.btns[c], "selected");
                this.currentIndex = this.preIndex = c;
                this.isAutoChange && this.autoChange()
            },autoChange: function() {
                var c = this, e = this.count;
                clearTimeout(this.runTimeId);
                this.runTimeId = setTimeout(function() {
                    var j = c.currentIndex;
                    if (j >= e - 1)
                        j = 0;
                    else
                        j++;
                    c.slideTo(j)
                }, c.autoChangeTime)
            },slideTo: function(c) {
                this.contentsSwipe.slideTo(c)
            },_initBtns: function() {
                for (var c = this.count, e = this.currentIndex, j = "", f = 0; f < c; f++)
                    j += f === e ?
                    "<li class='selected' _index='" + f + "'></li>" : "<li _index='" + f + "'></li>";
                this.btnsContainer.innerHTML = j;
                this.btns = a.tagName("li", this.btnsContainer)
            },bindHandlers: function() {
                var c = this._handleEvent = g.bind(this._handleEvent, this);
                b.on(this.contentsSwipe, "changed", c);
                b.on(this.btnsContainer, "click", c)
            },destory: function() {
                b.off(this.contentsSwipe, "changed", this._handleEvent);
                this.contentsSwipe.destory();
                a.remove(this.elem)
            },refresh: function() {
                this.contentsSwipe.refresh()
            }})
    })
});
define("../lib/mui/js/mui.slide", ["jm"], function() {
    JM.$package("MUI", function(g) {
        var a = g.dom, b = g.event, c = "getBoundingClientRect" in document.body, e = "-webkit-transform" in document.body.style;
        this.Slide = g.Class({init: function(j) {
                this.elem = a.id(j.id) || j.id;
                this.wrapClassName = j.wrapClassName || "wrap";
                this.contentWrap = a.$("." + this.wrapClassName, this.elem)[0];
                this.contents = a.$("." + this.wrapClassName + ">li", this.elem);
                this.count = this.contents.length;
                this.currentIndex = j.currentIndex || 0;
                this.moveDist = 0;
                this.runType =
                j.runType || "ease-out";
                this.slideTime = j.slideTime || 200;
                this.fastChange = j.fastChange;
                this._sizeAdjust();
                this._moveTo(this.currentIndex * -this.contentWidth);
                this.bindHandlers()
            },bindHandlers: function() {
                var j = this;
                b.on(this.contentWrap, ["webkitTransitionEnd", "mozTransitionEnd"], function() {
                    alert("p");
                    b.fire(j, "changed", {type: "changed",currentIndex: j.currentIndex})
                });
                b.on(j, "changed", function(f) {
                    if (j.fastChange && j.hideArr) {
                        for (; j.hideArr[0]; ) {
                            a.setStyle(j.hideArr[0], "display", "");
                            j.hideArr.shift()
                        }
                        j._removeAnimation();
                        j._moveTo(f.currentIndex * -j.contentWidth)
                    }
                });
                b.on(window, "resize", function() {
                    j.refresh()
                })
            },_removeAnimation: function() {
                if (e)
                    this.contentWrap.style["-webkit-transition"] = ""
            },_sizeAdjust: function() {
                var j = this.elem, f = this.count, n = c ? j.getBoundingClientRect().width : j.offsetWidth;
                a.setStyle(this.contentWrap, "width", n * f + "px");
                g.each(this.contents, function(m) {
                    a.setStyle(m, "width", n + "px")
                });
                this._removeAnimation();
                this._moveTo(-n * this.currentIndex);
                this.contentWidth = n
            },_moveTo: function(j) {
                if (e)
                    this.contentWrap.style["-webkit-transform"] =
                    "translate3d(" + j + "px, 0,0 )";
                else {
                    this.contentWrap.style.position = "relative";
                    this.contentWrap.style.left = j + "px"
                }
            },slideTo: function(j) {
                var f = this, n = this.currentIndex, m = j - n;
                this.currentIndex = j;
                if (this.fastChange && m && Math.abs(m) != 1)
                    if (m != 0) {
                        var r, k = this.contents;
                        if (!this.hideArr)
                            this.hideArr = [];
                        if (m > 0) {
                            m = m - 1;
                            r = 1;
                            j = n + 1
                        } else {
                            m = -(m + 1);
                            r = -1;
                            this._removeAnimation();
                            this._moveTo((this.currentIndex + 1) * -this.contentWidth)
                        }
                        for (var d = 1; d <= m; d++) {
                            var t = k[n + d * r];
                            a.setStyle(t, "display", "none");
                            this.hideArr.push(t)
                        }
                    }
                setTimeout(function() {
                    if (e)
                        f.contentWrap.style["-webkit-transition"] =
                        "all " + f.slideTime / 1E3 + "s " + f.runType;
                    f._moveTo(j * -f.contentWidth)
                }, 0)
            },next: function() {
                var j = this.currentIndex + 1;
                j >= this.count || this.slideTo(j)
            },pre: function() {
                var j = this.currentIndex - 1;
                j < 0 || this.slideTo(j)
            },refresh: function() {
                this._sizeAdjust()
            }})
    })
});
define("../lib/mui/js/mui.swipechange", ["jm", "./mui.slide"], function() {
    JM.$package("MUI", function(g) {
        var a = g.dom, b = g.event, c = g.platform.touchDevice, e, j = (c = g.platform.touchDevice) ? "touchstart" : "mousedown", f = c ? "touchmove" : "mousemove", n = c ? "touchend" : "mouseup", m = "getBoundingClientRect" in document.body, r = g.Class({extend: MUI.Slide}, {init: function(k) {
                r.callSuper(this, "init", k);
                this.startX = 0
            },_handleEvent: function(k) {
                r.callSuper(this, "_handleEvent", k);
                switch (k.type) {
                    case j:
                        this._onStartEvt(k);
                        break;
                    case f:
                        this._onMoveEvt(k);
                        break;
                    case n:
                        this._onEndEvt(k)
                }
            },_onStartEvt: function(k) {
                var d = this.elem, t = k.target || k.srcElement;
                if (a.closest(t, "." + this.wrapClassName)) {
                    e = t;
                    k = k.touches ? k.touches[0] : k;
                    d = m ? d.getBoundingClientRect().left : d.offsetLeft;
                    this.startX = k.clientX - d
                }
            },_onMoveEvt: function(k) {
                if (e) {
                    k.preventDefault();
                    var d = this.elem;
                    k = (k.touches ? k.touches[0] : k).clientX;
                    d = m ? d.getBoundingClientRect().left : d.offsetLeft;
                    var t = d + this.contentWidth;
                    if (!(k < d || k > t)) {
                        k -= d;
                        this.moveDist = k - this.startX;
                        this._removeAnimation();
                        this._moveTo(this.currentIndex *
                        -this.contentWidth + this.moveDist)
                    }
                }
            },_onEndEvt: function() {
                if (e) {
                    var k = this.moveDist, d = this.elem, t = this.currentIndex;
                    d = (m ? d.getBoundingClientRect().left : d.offsetLeft) + this.contentWidth / 3;
                    if (k > d)
                        t = Math.max(0, t - 1);
                    else if (k < -d)
                        t = Math.min(this.contents.length - 1, t + 1);
                    this.slideTo(t);
                    e = null;
                    this.moveDist = 0
                }
            },bindHandlers: function() {
                var k = this._handleEvent = g.bind(this._handleEvent, this);
                r.callSuper(this, "bindHandlers");
                c && b.on(this.elem, [j, f, n].join(" "), k)
            },destory: function() {
                c && b.off(this.elem, [j, f, n].join(" "),
                this._handleEvent);
                r.callSuper(this, "destory")
            }});
        this.SwipeChange = r
    })
});
define("mq.i18n", ["jm"], function() {
    J.$package("mq.i18n", function(g) {
        var a = (window.navigator.language || window.navigator.browserLanguage).toLowerCase(), b = 0;
        if (a)
            b = a.indexOf("zh") === 0 ? 0 : 1;
        var c = {con_friends: ["\u597d\u53cb", "Friends"],con_groups: ["\u7fa4", "Groups"],con_discus: ["\u8ba8\u8bba\u7ec4", "Discussion"],"return": ["\u8fd4\u56de", "Back"],close: ["\u5173\u95ed", "Close"],unname: ["\u672a\u547d\u540d", "Unnamed"],session: ["\u4f1a\u8bdd", "Chats"],contact: ["\u8054\u7cfb\u4eba", "Contacts"],setting: ["\u8bbe\u7f6e",
                "Settings"],plugin: ["\u53d1\u73b0", "Discover"],send: ["\u53d1\u9001", "Send"],cancel: ["\u53d6\u6d88", "Cancel"],search: ["\u641c\u7d22", "Search"],members: ["\u6210\u5458", "Members"],record: ["\u804a\u5929\u8bb0\u5f55", "Chat History"],noRecord: ["\u6682\u65e0\u804a\u5929\u8bb0\u5f55", "No Chat Records"],sendMsg: ["\u53d1\u6d88\u606f", "Send Message"],beforeclose: ["\u60a8\u786e\u5b9a\u8981\u79bb\u5f00\u5417\uff1f", "Are you sure you want to leave this page? "],profile: ["\u8be6\u7ec6\u8d44\u6599", "Profile"],signature: ["\u4e2a\u6027\u7b7e\u540d: ",
                "What's Up: "],publish: ["\u516c\u544a", "Notice"],gender: ["\u6027\u522b", "Gender"],male: ["\u7537", "Male"],female: ["\u5973", "Female"],unknown: ["\u672a\u77e5", "Unknown"],birthday: ["\u751f\u65e5", "Birthday"],country: ["\u56fd\u5bb6", "Country"],province: ["\u7701\u4efd", "Province"],city: ["\u57ce\u5e02", "City"],phone: ["\u7535\u8bdd", "Phone"],mobile: ["\u624b\u673a", "Mobile"],email: ["\u7535\u5b50\u90ae\u7bb1", "Email"],group_member: ["\u7fa4\u6210\u5458", "Group Members"],group_profile: ["\u7fa4\u8d44\u6599", "Group Profile"],
            group_profile: ["\u7fa4\u8d44\u6599", "Group Profile"],discuss_member: ["\u8ba8\u8bba\u7ec4\u6210\u5458", "Discussion Members"],discuss_profile: ["\u8ba8\u8bba\u7ec4\u8d44\u6599", "Discussion Profile"],buddy_unit: ["\u4eba", "people"],account: ["\u5e10\u53f7", "Account"],about_qq: ["\u5173\u4e8eQQ", "About"],loginout: ["\u9000\u51fa\u5f53\u524d\u5e10\u53f7", "Log Out"],place: ["\u6240\u5728\u5730", "Location"],version: ["\u5f53\u524d\u7248\u672c", "Version"],current_version: "V1.0",service: ["\u670d\u52a1\u6761\u6b3e",
                "Terms"],help: ["\u5e2e\u52a9\u4e0e\u53cd\u9988", "Feedback"],notify_setting: ["\u6d88\u606f\u76f8\u5173\u8bbe\u7f6e", "Notify Setting"],voice: ["\u58f0\u97f3", "Voice"],notification: ["\u6d88\u606f\u6d6e\u7a97", "Notifications"],https_setting: ["HTTPS", "HTTPS"],https_msg: ["\u4f7f\u7528 HTTPS \u52a0\u5bc6\u804a\u5929\u5185\u5bb9", "Encrypt records via HTTPS"],send_msg_way: ["\u6309Ctrl+Enter\u952e\u53d1\u9001\u6d88\u606f", 'Send Message by pressing "Ctrl" + "Enter"'],qzone: ["QQ\u7a7a\u95f4", "Qzone"],qmail: ["QQ\u90ae\u7bb1",
                "QQ Mail"],qq_portal: ["\u817e\u8baf\u7f51", "QQ.com"],soso_map: ["soso\u5730\u56fe", "soso Maps"],online: ["\u5728\u7ebf", "Online"],offline: ["\u79bb\u7ebf", "Offline"],away: ["\u79bb\u5f00", "Away"],hidden: ["\u9690\u8eab", "Invisible"],busy: ["\u5fd9\u788c", "Busy"],callme: ["Q\u6211", "Q Me"],silent: ["\u9759\u97f3", "Silence"],cface: ["\u81ea\u5b9a\u4e49\u8868\u60c5", "Custom Avatars"]}, e = [["\u5fae\u7b11", "\u6487\u5634", "\u8272", "\u53d1\u5446", "\u5f97\u610f", "\u6d41\u6cea", "\u5bb3\u7f9e", "\u95ed\u5634", "\u7761",
                "\u5927\u54ed", "\u5c34\u5c2c", "\u53d1\u6012", "\u8c03\u76ae", "\u5472\u7259", "\u60ca\u8bb6", "\u96be\u8fc7", "\u9177", "\u51b7\u6c57", "\u6293\u72c2", "\u5410", "\u5077\u7b11", "\u53ef\u7231", "\u767d\u773c", "\u50b2\u6162", "\u9965\u997f", "\u56f0", "\u60ca\u6050", "\u6d41\u6c57", "\u61a8\u7b11", "\u5927\u5175", "\u594b\u6597", "\u5492\u9a82", "\u7591\u95ee", "\u5618", "\u6655", "\u6298\u78e8", "\u8870", "\u9ab7\u9ac5", "\u6572\u6253", "\u518d\u89c1", "\u64e6\u6c57", "\u62a0\u9f3b", "\u9f13\u638c", "\u7cd7\u5927\u4e86", "\u574f\u7b11",
                "\u5de6\u54fc\u54fc", "\u53f3\u54fc\u54fc", "\u54c8\u6b20", "\u9119\u89c6", "\u59d4\u5c48", "\u5feb\u54ed\u4e86", "\u9634\u9669", "\u4eb2\u4eb2", "\u5413", "\u53ef\u601c", "\u83dc\u5200", "\u897f\u74dc", "\u5564\u9152", "\u7bee\u7403", "\u4e52\u4e53", "\u5496\u5561", "\u996d", "\u732a\u5934", "\u73ab\u7470", "\u51cb\u8c22", "\u793a\u7231", "\u7231\u5fc3", "\u5fc3\u788e", "\u86cb\u7cd5", "\u95ea\u7535", "\u70b8\u5f39", "\u5200", "\u8db3\u7403", "\u74e2\u866b", "\u4fbf\u4fbf", "\u6708\u4eae", "\u592a\u9633", "\u793c\u7269", "\u62e5\u62b1",
                "\u5f3a", "\u5f31", "\u63e1\u624b", "\u80dc\u5229", "\u62b1\u62f3", "\u52fe\u5f15", "\u62f3\u5934", "\u5dee\u52b2", "\u7231\u4f60", "NO", "OK", "\u7231\u60c5", "\u98de\u543b", "\u8df3\u8df3", "\u53d1\u6296", "\u6004\u706b", "\u8f6c\u5708", "\u78d5\u5934", "\u56de\u5934", "\u8df3\u7ef3", "\u6325\u624b", "\u6fc0\u52a8", "\u8857\u821e", "\u732e\u543b", "\u5de6\u592a\u6781", "\u53f3\u592a\u6781", "\u53cc\u559c", "\u97ad\u70ae", "\u706f\u7b3c", "\u53d1\u8d22", "K\u6b4c", "\u8d2d\u7269", "\u90ae\u4ef6", "\u5e05", "\u559d\u5f69", "\u7948\u7977",
                "\u7206\u7b4b", "\u68d2\u68d2\u7cd6", "\u559d\u5976", "\u4e0b\u9762", "\u9999\u8549", "\u98de\u673a", "\u5f00\u8f66", "\u5de6\u8f66\u5934", "\u8f66\u53a2", "\u53f3\u8f66\u5934", "\u591a\u4e91", "\u4e0b\u96e8", "\u949e\u7968", "\u718a\u732b", "\u706f\u6ce1", "\u98ce\u8f66", "\u95f9\u949f", "\u6253\u4f1e", "\u5f69\u7403", "\u94bb\u6212", "\u6c99\u53d1", "\u7eb8\u5dfe", "\u836f", "\u624b\u67aa", "\u9752\u86d9"], ["Smile", "Grimace", "Drool", "Scowl", "CoolGuy", "Sob", "Shy", "Silent", "Sleep", "Cry", "Awkward", "Angry", "Tongue", "Grin",
                "Surprise", "Frown", "Ruthless", "Blush", "Scream", "Puke", "Chuckle", "Joyful", "Slight", "Smug", "Hungry", "Drowsy", "Panic", "Sweat", "Laugh", "Commando", "Determined", "Scold", "Shocked", "Shhh", "Dizzy", "Tormented", "Toasted", "Skull", "Hammer", "Wave", "Speechless", "NosePick", "Clap", "Shame", "Trick", "Bah! L", "Bah! R", "Yawn", "Pooh-pooh", "Shrunken", "TearingUp", "Sly", "Kiss", "Wrath", "Whimper", "Cleaver", "Watermelon", "Beer", "Basketball", "PingPong", "Coffee", "Rice", "Pig", "Rose", "Wilt", "Lips", "Heart", "BrokenHeart", "Cake", "Lightning",
                "Bomb", "Dagger", "Soccer", "Ladybug", "Poop", "Moon", "Sun", "Gift", "Hug", "Strong", "Weak", "Shake", "Peace", "Fight", "Beckon", "Fist", "Pinky", "RockOn", "NO", "OK", "InLove", "Blowkiss", "Waddle", "Tremble", "Aaagh", "Twirl", "Kotow", "Dramatic", "JumpRope", "Surrender", "Exciting", "HipHot", "ShowLove", "Tai Chi L", "Tai Chi R", "Congratulations", "Firecracker", "Lantern", "Richer", "Karaoke", "Shopping", "Email", "Handsome", "Cheers", "Pray", "BlowUp", "Lolly", "Milk", "Noodles", "Banana", "Plane", "Car", "Locomotive", "Train", "Train Tail",
                "Cloudy", "Rain", "Dollor", "Panda", "Bulb", "Windmill", "Clock", "Umbrella", "Balloon", "Ring", "Sofa", "toiletPaper", "Pill", "Pistol", "Frog"]];
        this.message = function(j) {
            return c[j] ? g.type.isArray(c[j]) ? c[j][b] : c[j] : j
        };
        this.faceText = function(j) {
            return e[b][j]
        };
        this.getFaceIndex = function(j) {
            return e[b].indexOf(j)
        }
    })
});
define("mq.view.transitionmanager", ["jm"], function() {
    J.$package("mq.view.transitionManager", function(g) {
        var a = this, b = g.support, c = {}, e = g.prefix && g.prefix.lowercase, j = g.prefix && g.prefix.css;
        e || (e = "");
        j || (j = "");
        var f = function(m, r) {
            for (var k = 0, d = m.length; k < d; k++)
                if (m[k].id === r)
                    return {item: m[k],index: k};
            return null
        };
        this.push = function(m) {
            var r = m.id, k = m.cate || "default", d = m.element, t = g.$default(m.transition, true), B = m.callback;
            c[k] || (c[k] = []);
            m = c[k];
            var z = f(m, r);
            if (z !== null) {
                if (t !== true)
                    t = z.index === m.length -
                    1;
                m.splice(z.index, 1);
                k = z.item
            } else
                k = {element: d,id: r,cate: k};
            d = m.length > 0 ? m[m.length - 1] : null;
            var q = null;
            if (d) {
                q = d.id;
                d = d.element
            }
            z = k.element;
            m.push(k);
            t && this.transition(d, z, false, function() {
                g.event.fire(a, "transitionEnd", {from: q,to: r});
                B && B()
            })
        };
        this.pop = function(m, r, k) {
            if (arguments.length === 2) {
                k = r;
                r = null
            }
            r || (r = "default");
            if (c[r]) {
                var d = c[r], t = f(d, m);
                if (t !== null) {
                    d.splice(t.index);
                    t = t.item.element;
                    d = d.length > 0 ? d[d.length - 1] : null;
                    var B = null;
                    if (d) {
                        B = d.id;
                        d = d.element
                    }
                    this.transition(t, d, true, function() {
                        g.event.fire(a,
                        "transitionEnd", {from: m,to: B});
                        k && k()
                    })
                }
            }
        };
        this.transition = function(m, r, k, d) {
            n(m, r, k, function() {
                if (k) {
                    if (m) {
                        m.style.transition = "transform 0.4s cubic-bezier(0,1,0,1)";
                        m.style.transform = "translate3d(100%, 0, 0)";
                        if (j) {
                            m.style[j + "transform"] = "translate3d(100%, 0, 0)";
                            m.style[j + "transition"] = j + "transform 0.4s cubic-bezier(0,1,0,1)".slice(0, 1).toUpperCase() + "transform 0.4s cubic-bezier(0,1,0,1)".slice(1)
                        }
                    }
                    if (r) {
                        r.style.transition = "transform 0.4s cubic-bezier(0,1,0,1)";
                        r.style.transform = "translate3d(0, 0, 0)";
                        if (j) {
                            r.style[j + "transform"] = "translate3d(0, 0, 0)";
                            r.style[j + "transition"] = j + "transform 0.4s cubic-bezier(0,1,0,1)".slice(0, 1).toUpperCase() + "transform 0.4s cubic-bezier(0,1,0,1)".slice(1)
                        }
                    }
                } else {
                    if (m) {
                        m.style.transition = "transform 0.4s cubic-bezier(0,1,0,1)";
                        m.style.transform = "translate3d(-100%, 0, 0)";
                        if (j) {
                            m.style[j + "transition"] = j + "transform 0.4s cubic-bezier(0,1,0,1)".slice(0, 1).toUpperCase() + "transform 0.4s cubic-bezier(0,1,0,1)".slice(1);
                            m.style[j + "transform"] = "translate3d(-100%, 0, 0)"
                        }
                    }
                    if (r) {
                        r.style.transition =
                        "transform 0.4s cubic-bezier(0,1,0,1)";
                        r.style.transform = "translate3d(0, 0, 0)";
                        if (j) {
                            r.style[j + "transition"] = j + "transform 0.4s cubic-bezier(0,1,0,1)".slice(0, 1).toUpperCase() + "transform 0.4s cubic-bezier(0,1,0,1)".slice(1);
                            r.style[j + "transform"] = "translate3d(0, 0, 0)"
                        }
                    }
                }
                var t = r || m, B = function() {
                    if (m)
                        m.style.display = "none";
                    d && d()
                };
                if (window.matchMedia)
                    if (window.matchMedia("(min-width:1000px)").matches) {
                        B();
                        return
                    }
                b.transitionend ? g.event.once(t, "transitionend", B) : B()
            })
        };
        var n = function(m, r, k, d) {
            if (r) {
                r.style.transition =
                "none";
                r.style.transform = "translate3d(" + (k ? "-" : "") + "100%, 0, 0)";
                if (j) {
                    r.style[j + "transition"] = "none";
                    r.style[j + "transform"] = "translate3d(" + (k ? "-" : "") + "100%, 0, 0)"
                }
                r.style.display = "block";
                setTimeout(d, 20)
            }
        }
    })
});
define("mq.util", ["jm"], function() {
    J.$package("mq.util", function(g) {
        var a = {NORMAL: 0,ID_EXIST: 1,ID_NOT_EXIST: 2}, b = {};
        this.delay = function(j, f, n) {
            var m = arguments, r = a.NORMAL;
            if (m.length === 1) {
                n = j;
                f = 0;
                j = null
            } else if (m.length === 2) {
                n = f;
                f = j;
                j = null
            }
            f = f || 0;
            if (j && f) {
                if (j in b) {
                    window.clearTimeout(b[j]);
                    r = a.ID_EXIST
                }
                m = window.setTimeout(function() {
                    b[j] = 0;
                    delete b[j];
                    n.apply(window, [j])
                }, f);
                b[j] = m
            } else
                window.setTimeout(n, f);
            return r
        };
        this.clearDelay = function(j) {
            if (j in b) {
                window.clearTimeout(b[j]);
                b[j] = 0;
                delete b[j];
                return a.NORMAL
            }
            return a.ID_NOT_EXIST
        };
        this.report2BNL = function(j) {
            if (!j)
                return false;
            if (!j.opername)
                j.opername = "mediacenter";
            if (!j.obj)
                j.obj = 0;
            j = "http://cgi.connect.qq.com/report/report?strValue=" + JSON.stringify(j) + "&tag=0&qver=" + mq.getVersion();
            qtracker.tracker.Img.send(j)
        };
        this.report2BNL2 = function(j, f) {
            f = f || 0;
            var n = "http://cgi.connect.qq.com/report/report?strValue=" + f + "&nValue=" + j + "&tag=0&qver=" + mq.getVersion();
            qtracker.tracker.Img.send(n)
        };
        var c = {10: "online",20: "offline",30: "away",40: "hidden",
            50: "busy",60: "callme",70: "silent"};
        this.code2state = function(j) {
            return c[j] || "online"
        };
        var e = {online: 10,offline: 20,away: 30,hidden: 40,busy: 50,callme: 60,silent: 70};
        this.state2code = function(j) {
            return e[j] || 0
        };
        this.download = function(j) {
            var f = g.dom.id("fileDownloader");
            if (!f) {
                f = document.createElement("iframe");
                f.id = "fileDownloader";
                f.name = "fileDownloader";
                f.src = mq.WEBQQ_MAIN_URL + "domain.html";
                f.style.display = "none";
                document.body.appendChild(f)
            }
            f.src = j
        }
    });
    J.$package("mq.util", function() {
        function g(r, k) {
            function d() {
                t =
                t.onload = t.onerror = t.onreadystatechange = null;
                k()
            }
            var t = e.createElement("script");
            if ("onload" in t) {
                t.onload = d;
                t.onerror = function() {
                    d()
                }
            } else
                t.onreadystatechange = function() {
                    /loaded|complete/.test(t.readyState) && d()
                };
            t.async = true;
            t.src = r;
            b(t)
        }
        function a(r, k) {
            function d() {
                t = t.onload = t.onerror = t.onreadystatechange = null;
                k()
            }
            var t = e.createElement("link"), B = "onload" in t;
            if (!B || j)
                setTimeout(function() {
                    c(t, k)
                }, 1);
            else if (B) {
                t.onload = d;
                t.onerror = function() {
                    d()
                }
            }
            t.rel = "stylesheet";
            t.type = "text/css";
            t.href = r;
            b(t)
        }
        function b(r) {
            n ? f.insertBefore(r, n) : f.appendChild(r)
        }
        function c(r, k) {
            var d = r.sheet, t;
            if (j) {
                if (d)
                    t = true
            } else if (d)
                try {
                    if (d.cssRules)
                        t = true
                } catch (B) {
                    if (B.name === "NS_ERROR_DOM_SECURITY_ERR")
                        t = true
                }
            setTimeout(function() {
                t ? k() : c(r, k)
            }, 20)
        }
        var e = window.document, j = +navigator.userAgent.replace(/.*AppleWebKit\/(\d+)\..*/, "$1") < 536, f = e.getElementsByTagName("head")[0] || e.documentElement, n = f.getElementsByTagName("base")[0], m = /\.css(?:\?|$)/i;
        this.loadJs = g;
        this.loadCss = a;
        this.loadFile = function(r, k) {
            m.test(r) ?
            a(r, k) : g(r, k)
        }
    });
    MM = function() {
        var g = new Image, a = {};
        return {init: function(b, c, e) {
                a = {appid: b,touin: c,releaseversion: e,frequency: 1}
            },report: function(b, c, e, j) {
                var f = [];
                a.commandid = b;
                a.resultcode = c;
                a.tmcost = e;
                if (j)
                    for (var n in j)
                        if (j.hasOwnProperty(n))
                            a[n] = j[n];
                if (c == 0)
                    a.frequency = 1;
                for (var m in a)
                    a.hasOwnProperty(m) && f.push(m + "=" + encodeURIComponent(a[m]));
                b = "http://wspeed.qq.com/w.cgi?" + f.join("&");
                g.src = b
            }}
    }();
    MM.init(1000143, null, "SMARTQQ")
});
define("tmpl!../tmpl/tmpl_title_panel.html", [], function() {
    return function(g) {
        var a, b = "";
        with (g || {}) {
            b += "";
            if (hasHeader) {
                b += '\r\n<header id="panelHeader-' + ((a = id) == null ? "" : a) + '" class="panel_header">\r\n    ';
                if (leftButton)
                    b += '\r\n    <div id="panelLeftButton-' + ((a = id) == null ? "" : a) + '" class="btn btn_small btn_left btn_black ' + ((a = leftButton.className) == null ? "" : a) + '" cmd="clickLeftButton">\r\n        <span id="panelLeftButtonText-' + ((a = id) == null ? "" : a) + '" class="' + ((a = leftButton.text ? "btn_text" : "btn_img") ==
                    null ? "" : a) + '">' + ((a = encode(leftButton.text)) == null ? "" : a) + "</span>\r\n    </div>\r\n    ";
                b += '\r\n        <h1 id="panelTitle-' + ((a = id) == null ? "" : a) + '" class="text_ellipsis padding_20">' + ((a = encode(title)) == null ? "" : a) + "</h1>\r\n    ";
                if (rightButton)
                    b += '\r\n    <button id="panelRightButton-' + ((a = id) == null ? "" : a) + '" class="btn btn_small btn_right btn_black ' + ((a = rightButton.className) == null ? "" : a) + '" cmd="clickRightButton">\r\n        <span id="panelRightButtonText-' + ((a = id) == null ? "" : a) + '" class="' + ((a =
                    rightButton.text ? "btn_text" : "btn_img") == null ? "" : a) + '">' + ((a = encode(rightButton.text)) == null ? "" : a) + "</span>\r\n    </button>\r\n    ";
                b += "\r\n</header>\r\n"
            }
            b += '\r\n<div id="panelBodyWrapper-' + ((a = id) == null ? "" : a) + '" class="panel_body_container" style="' + ((a = hasHeader ? "top: 45px;" : "") == null ? "" : a) + " " + ((a = hasFooter ? "bottom: 50px;" : "") == null ? "" : a) + '">\r\n    <div id="panelBody-' + ((a = id) == null ? "" : a) + '" class="panel_body ' + ((a = body.className) == null ? "" : a) + '">' + ((a = body.html) == null ? "" : a) + '</div>\r\n    <ul id="pannelMenuList-' +
            ((a = id) == null ? "" : a) + '" class="pannel_menu_list">\r\n    </ul>\r\n</div>\r\n';
            if (hasFooter)
                b += '\r\n<footer id="panelFooter-' + ((a = id) == null ? "" : a) + '" class="' + ((a = footer.className || "") == null ? "" : a) + '" >\r\n    ' + ((a = footer.html) == null ? "" : a) + "\r\n</footer>\r\n";
            b += "\r\n"
        }
        return b
    }
});
define("tmpl!../tmpl/tmpl_main_menu.html", [], function() {
    return function(g) {
        var a, b = "";
        with (g || {}) {
            b += "";
            g = 0;
            for (var c; c = menuItems[g]; g++)
                b += '\r\n<li cmd="' + ((a = c.cmd) == null ? "" : a) + '" class="' + ((a = c.cmd) == null ? "" : a) + '">\r\n    <div class="menu_list_icon"></div>\r\n    ' + ((a = c.text) == null ? "" : a) + "\r\n</li>\r\n";
            b += ""
        }
        return b
    }
});
define("mq.view.TitlePanel", ["tmpl!../tmpl/tmpl_title_panel.html", "tmpl!../tmpl/tmpl_main_menu.html", "./mq.i18n", "./mq.view.transitionmanager"], function(g, a) {
    J.$package("mq.view", function(b) {
        var c = JM.event, e = JM.dom, j = JM.string, f = mq.i18n.message, n = 0;
        this.TitlePanel = b.Class({init: function(m) {
                m = m || {};
                this.parent = m.parent || document.body;
                this.containerNode = m.containerNode || "div";
                this.id = m.id || n++;
                this.option = m;
                var r = this.renderData = {id: this.id,title: m.title || f("unname"),className: m.className || "",hasHeader: typeof m.hasHeader ===
                    "undefined" ? true : m.hasHeader,leftButton: m.leftButton || false,rightButton: m.rightButton || false,hasFooter: !!m.footer || m.hasFooter || false,footer: m.footer,body: b.extend({html: "",className: ""}, m.body || {}),encode: j.encodeHtml};
                if (m.leftButton)
                    r.leftButton = b.extend({text: f("return"),className: ""}, m.leftButton);
                if (m.hasBackButton)
                    r.leftButton = {className: "btn_arrow_left",text: f("return")};
                if (m.rightButton)
                    r.rightButton = b.extend({text: "",className: ""}, m.rightButton);
                this.create(g)
            },create: function(m) {
                if (!m)
                    throw Error("no panel template!");
                this.container = document.createElement(this.containerNode);
                this.container.setAttribute("class", "panel " + this.renderData.className);
                this.container.id = "panel-" + this.id;
                this.container.innerHTML = m(this.renderData);
                this.parent.appendChild(this.container);
                this.bodyWrapper = e.id("panelBodyWrapper-" + this.id);
                this.body = e.id("panelBody-" + this.id);
                this.title = e.id("panelTitle-" + this.id);
                this.header = e.id("panelHeader-" + this.id);
                this.footer = e.id("panelFooter-" + this.id);
                this.menuList = e.id("pannelMenuList-" + this.id);
                this.leftButton = e.id("panelLeftButton-" + this.id);
                this.rightButton = e.id("panelRightButton-" + this.id);
                if (this.option.hasScroller)
                    this.scroller = new iScroll(this.bodyWrapper);
                c.fire(this, "create", this)
            },destory: function() {
                c.fire(this, "beforeDestory", this);
                this.parent.removeChild(this.container);
                for (var m in this)
                    if (this.hasOwnProperty(m)) {
                        this[m] = null;
                        delete this[m]
                    }
            },setTitle: function(m) {
                this.title.innerHTML = j.encodeHtml(m)
            },setBody: function(m) {
                this.body.innerHTML = m
            },show: function() {
                e.setStyle(this.container,
                "display", "block")
            },hide: function() {
                e.setStyle(this.container, "display", "none")
            },setLeftText: function(m) {
                if (!this.leftButtonText)
                    this.leftButtonText = e.id("panelLeftButtonText-" + this.id);
                this.leftButtonText.innerHTML = j.encodeHtml(m)
            },setMenuItems: function(m) {
                this.menuList.innerHTML = a({menuItems: m});
                this.hideMenuList();
                e.setStyle(this.menuList, "display", "block")
            },hideMenuList: function() {
                e.removeClass(this.menuList, "show")
            },showMenuList: function() {
                e.addClass(this.menuList, "show")
            },toggleMenuList: function() {
                var m =
                this.menuList;
                if (m)
                    e.hasClass(m, "show") ? this.hideMenuList() : this.showMenuList()
            }})
    })
});
define("mq.report", ["jm"], function() {
    J.$package("mq.report", function(g) {
        var a = JM.type, b = null, c = {}, e = function(m) {
            if (!m)
                return "";
            var r = [], k;
            for (k in m)
                m.hasOwnProperty(k) && r.push(encodeURIComponent(k) + "=" + encodeURIComponent(m[k]));
            return r.join("&")
        }, j = function(m, r) {
            var k = new Image;
            k.onload = function() {
                k = null
            };
            if (r) {
                m += m.indexOf("?") == -1 ? "?" : "&";
                m += e(r)
            }
            k.src = m
        }, f = function(m) {
            for (var r in c) {
                for (var k = c[r], d = {}, t = r.split("-"), B = false, z = 0; z < t.length; z++)
                    d["flag" + (z + 1)] = t[z];
                for (var q in k)
                    if (a.isArray(k[q])) {
                        d[q] =
                        k[q][0];
                        B = true;
                        delete k[q]
                    }
                B && j("http://isdspeed.qq.com/cgi-bin/r.cgi", d);
                m && n(r, m)
            }
        }, n = function(m, r) {
            if (m) {
                var k = c[m];
                if (k)
                    if (r)
                        if (a.isArray(r))
                            for (var d in k)
                                d in r && delete k[d]
            }
        };
        (function() {
            window.onerror = function(m, r, k) {
                m = "http://badjs.qq.com/cgi-bin/js_report?" + ["bid=254&", "msg=" + encodeURIComponent([m, r, k, navigator.userAgent].join("|_|"))].join("&");
                b = new Image;
                b.src = m
            }
        })();
        g.extend(this, {speedReport: function(m, r, k, d) {
                if (m) {
                    var t = c[m];
                    t || (t = c[m] = {});
                    if (k) {
                        if (!a.isArray(t[r]))
                            if (t[r]) {
                                t[r] = [Date.now() -
                                    t[r]];
                                d && f()
                            }
                    } else
                        t[r] || (t[r] = Date.now())
                }
            },flushSpeedCache: f,clearSpeedCache: n});
        (function() {
            var m = window.speedTempCache;
            m && a.isObject(m) && g.extend(c, m)
        })()
    });
    MM = function() {
        var g = new Image, a = {};
        return {init: function(b, c, e) {
                a = {appid: b,touin: c,releaseversion: e,frequency: 1}
            },report: function(b, c, e, j) {
                var f = [];
                a.commandid = b;
                a.resultcode = c;
                a.tmcost = e;
                if (j)
                    for (var n in j)
                        if (j.hasOwnProperty(n))
                            a[n] = j[n];
                if (c == 0)
                    a.frequency = 1;
                for (var m in a)
                    a.hasOwnProperty(m) && f.push(m + "=" + encodeURIComponent(a[m]));
                b = "http://wspeed.qq.com/w.cgi?" +
                f.join("&");
                g.src = b
            }}
    }();
    MM.init(1000164, null, "SMARTQQ")
});
define("mq.rpcservice", ["./mq.portal", "./mq.report"], function() {
    J.$package("alloy", function() {
        this.ajaxProxyCallback = function(g, a) {
            switch (g) {
                case 1:
                    mq.rpcService.onAjaxFrameLoad(a)
            }
        }
    });
    J.$package("mq.rpcService", function(g) {
        var a = this, b = JM.event, c = JM.dom, e = mq.DYNAMIC_CGI_URL + "channel/login2", j = mq.DYNAMIC_CGI_URL + "channel/poll2", f = mq.STATIC_CGI_URL + "api/getvfwebqq", n = mq.DYNAMIC_CGI_URL + "channel/refuse_file2", m = mq.DYNAMIC_CGI_URL + "channel/notify_offfile2", r = {"s.web2.qq.com": "http://s.web2.qq.com/proxy.html?v=20130916001",
            "d.web2.qq.com": "http://d.web2.qq.com/proxy.html?v=20130916001"}, k = 0, d, t = new g.Class({init: function(E) {
                this._ajaxRequestInstant = E
            },send: function(E, G) {
                G = G || {};
                G.cacheTime = G.cacheTime || 0;
                G.onSuccess = G.onSuccess;
                G.onError = G.onError;
                G.onTimeout = G.onTimeout;
                G.onComplete = G.onComplete;
                var O = {iframeName: G.iframeName,method: G.method || "GET",contentType: G.contentType || "",enctype: G.enctype || "",data: G.data || {},arguments: G.arguments || {},context: G.context || null,timeout: G.timeout || 3E4,onSuccess: G.onSuccess && function(s) {
                        s =
                        s.responseText || "-";
                        var A = {};
                        try {
                            A = JSON.parse(s)
                        } catch (I) {
                            mq.error("alloy.rpcservice: JSON \u683c\u5f0f\u51fa\u9519", "HttpRequest")
                        }
                        A.arguments = G.arguments || {};
                        G.onSuccess.call(G.context, A)
                    },onError: G.onError && function(s) {
                        G.onError.call(G.context, s)
                    },onTimeout: G.onTimeout && function() {
                        var s = {};
                        s.arguments = G.arguments || {};
                        G.onTimeout.call(G.context, s)
                    },onComplete: G.onComplete && function() {
                        var s = {};
                        s.arguments = G.arguments || {};
                        G.onComplete.call(G.context, s)
                    }};
                O.data = g.http.serializeParam(O.data);
                if (O.method ==
                "GET") {
                    var u = O.data;
                    if (G.cacheTime === 0)
                        u += u ? "&t=" + (new Date).getTime() : "t=" + (new Date).getTime();
                    if (u)
                        E = E + "?" + u;
                    O.data = null
                } else if (!O.contentType)
                    O.contentType = "application/x-www-form-urlencoded";
                this._ajaxRequestInstant(E, O)
            }}), B = new g.Class({init: function(E, G) {
                var O = "qqweb_proxySendIframe_" + E, u = this, s;
                this.iframeName = O;
                this._ajaxCallbacks = [];
                this._proxyAjaxSend = this._proxySend = null;
                G += (/\?/.test(G) ? "&" : "?") + "id=" + E;
                s = document.body;
                var A = c.node("div");
                A.setAttribute("class", "hiddenIframe");
                A.innerHTML =
                '<iframe id="' + O + '" class="hiddenIframe" name="' + O + '" src="' + G + '" width="1" height="1"></iframe>';
                s.appendChild(A);
                s = document.getElementById(O);
                this.id = E;
                this.onAjaxFrameLoad = function() {
                    var I = window.frames[O];
                    try {
                        if (I.ajax) {
                            u._proxyAjaxSend = I.ajax;
                            var L = u._ajaxCallbacks;
                            I = 0;
                            for (var Q = L.length; I < Q; I++)
                                u.proxySend(L[I].url, L[I].option);
                            u._ajaxCallbacks = []
                        }
                    } catch (R) {
                        mq.error("ProxyRequest >>>>> ajaxProxy error: " + R.message + " !!!!", "ProxyRequest")
                    }
                };
                g.browser.firefox && s.setAttribute("src", G)
            },send: function(E,
            G) {
                if (this._proxyAjaxSend) {
                    this.proxySend(E, G);
                    this.send = this.proxySend
                } else
                    this._ajaxCallbacks.push({url: E,option: G})
            },proxySend: function(E, G) {
                if (!this._proxySend)
                    this._proxySend = new t(this._proxyAjaxSend);
                G.iframeName = this.iframeName;
                this._proxySend.send(E, G)
            }}), z = new g.Class({init: function(E, G) {
                var O = "qqweb_proxySendIframe" + E;
                this.iframeName = O;
                var u = this;
                this._ajaxCallbacks = [];
                this._proxyAjaxSend = this._proxySend = null;
                var s = document.body, A = c.node("div");
                A.setAttribute("class", "hiddenIframe");
                A.innerHTML =
                '<iframe id="' + O + '" class="hiddenIframe" name="' + O + '" src="' + G + '" width="1" height="1"></iframe>';
                s.appendChild(A);
                O = c.id(O);
                b.on(O, "load", function() {
                    u._proxyAjaxSend = u.cfProxySend;
                    for (var I = u._ajaxCallbacks, L = 0, Q = I.length; L < Q; L++)
                        u.proxySend(I[L].url, I[L].option);
                    u._ajaxCallbacks = []
                });
                O.setAttribute("src", G)
            },send: function(E, G) {
                if (this._proxyAjaxSend) {
                    this.proxySend(E, G);
                    this.send = this.proxySend
                } else
                    this._ajaxCallbacks.push({url: E,option: G})
            },proxySend: function(E, G) {
                if (!this._proxySend)
                    this._proxySend =
                    new t(this._proxyAjaxSend);
                G.iframeName = this.iframeName;
                this._proxySend.send(E, G)
            },cfProxySend: function(E, G) {
                var O = w.setOption(G);
                E = E.replace("http://", "https://");
                O = JSON.stringify({id: O,option: {method: G.method || "GET",data: G.data || null,isAsync: G.isAsync || true,timeout: G.timeout,contentType: G.contentType || "",type: G.type,uri: E},uri: E,iframeName: G.iframeName,host: mq.MAIN_URL,timestamp: +new Date});
                RegExp(/(^http(s)?:\/\/[\w\.]+)\//).test(E);
                var u = RegExp.$1;
                if ("postMessage" in window && !g.browser.ie)
                    window.frames[G.iframeName].postMessage(O,
                    u);
                else {
                    var s = c.node("div");
                    u = u + "/app.rpc.proxy.html";
                    s.innerHTML = '<iframe class="hiddenCFProxy" name="' + encodeURIComponent(O) + '" src="' + u + '" onload="mq.rpcService.removeCF(this)"></iframe>';
                    document.body.appendChild(s)
                }
            }}), q = new g.Class({init: function() {
                this._proxyArr = {};
                this._cFproxyArr = {};
                this._proxyId = 1
            },getProxyId: function() {
                return this._proxyId++
            },getProxy: function(E, G) {
                if (G)
                    E = E.replace("proxy.html", "cfproxy.html").replace("http://", "https://");
                var O = this._proxyArr[E];
                if (!O) {
                    O = G ? new z(this.getProxyId(),
                    E) : new B(this.getProxyId(), E);
                    this._proxyArr[E] = O
                }
                return O
            },getProxyById: function(E) {
                for (var G in this._proxyArr)
                    if (this._proxyArr[G].id == E)
                        return this._proxyArr[G];
                return null
            }});
        this.onAjaxFrameLoad = function(E) {
            (E = d.getProxyById(E)) && E.onAjaxFrameLoad()
        };
        var w = {id: 0,map: {},getOptionId: function() {
                return this.id++
            },setOption: function(E) {
                var G = this.getOptionId();
                this.map[G] = E;
                return G
            },getOption: function(E, G) {
                var O = this.map[E];
                G || delete this.map[E];
                return O
            }};
        this.rpcProxyCallback = function(E) {
            E = g.type.isObject(E) ?
            E : JSON.parse(E);
            var G = E.type, O = w.getOption(E.id);
            O && O[G](E.option)
        };
        var C = function(E) {
            var G = E.data;
            E.origin.indexOf("web2.qq.com") > -1 && G && a.rpcProxyCallback(G)
        };
        if ("postMessage" in window)
            if (window.addEventListener)
                window.addEventListener("message", C, false);
            else if (window.attachEvent)
                window.attachEvent("onmessage", C);
            else
                window.onmessage = C;
        this.removeCF = function(E) {
            E && window.setTimeout(function() {
                var G = E.parentNode;
                G.parentNode.removeChild(G)
            }, 1E3)
        };
        this.require = function(E) {
            var G = E.data || E.param ||
            {}, O = E.url, u = E.action, s = E.https;
            E.method = E.method || "GET";
            E.data = E.method == "POST" ? {r: JSON.stringify(G)} : G;
            E.onSuccess = E.onSuccess || function(I) {
                var L = "retcode" in I ? I.retcode : "ret" in I ? I.ret : -1;
                window.MM && MM.report(O.split("?")[0], L || 0, +new Date - A);
                L === 0 ? b.fire(a, u + "Success", I) : b.fire(a, u + "Failure", I)
            };
            E.onError = E.onError || function(I) {
                b.fire(a, u + "Failure", I)
            };
            E.onTimeout = E.onTimeout || function(I) {
                b.fire(a, u + "Timeout", I)
            };
            d || (d = new q);
            G = g.string.parseURL(O);
            if (G = r[G.host]) {
                G += (/\?/.test(G) ? "&" : "?") + "callback=1";
                s = d.getProxy(G, s);
                var A = +new Date;
                s.send(O, E)
            } else
                mq.error("wrong url or no proxy!")
        };
        this.login = function() {
            var E = {ptwebqq: mq.ptwebqq,clientid: mq.clientid,psessionid: mq.psessionid}, G = mq.util.code2state(mq.main.loginType);
            E.status = G;
            this.require({url: e,action: "login",method: "POST",data: E,onSuccess: h,onError: o,onTimeout: v})
        };
        var h = function(E) {
            switch (E.retcode) {
                case 0:
                    b.fire(a, "LoginSuccess", E);
                    break;
                default:
                    b.fire(a, "LoginFailure", {text: "\u767b\u9646\u5931\u8d25"})
            }
        }, o = function() {
            b.fire(a, "LoginFailure",
            {text: "\u767b\u9646\u5931\u8d25"})
        }, v = function() {
            b.fire(a, "LoginFailure", {text: "\u767b\u9646\u5931\u8d25"})
        };
        this.getVfWebQQ = function() {
            this.require({url: f,action: "getVfWebQQ",method: "GET",data: {ptwebqq: mq.ptwebqq,clientid: mq.clientid,psessionid: mq.psessionid}})
        };
        this.sendPoll = function() {
            this.require({url: j,https: mq.setting.enableHttps,action: "poll",method: "POST",data: {ptwebqq: mq.ptwebqq,clientid: mq.clientid,psessionid: mq.psessionid,key: ""},timeout: 12E4,onSuccess: D,onError: p,onTimeout: y})
        };
        var D =
        function(E) {
            var G = E ? E.retcode : -1;
            if (G === 0 || G === 102) {
                k = 0;
                try {
                    b.fire(a, "PollSuccess", E.result)
                }finally {
                    b.fire(a, "PollComplete")
                }
            } else if (G === 100)
                b.fire(a, "NotReLogin");
            else if (G === 120)
                b.fire(a, "ReLinkFailure", E);
            else if (G === 121)
                b.fire(a, "ReLinkFailure", E);
            else if (G === 116) {
                mq.main.setValidate({ptwebqq: E.p});
                try {
                    b.fire(a, "PollComplete")
                } catch (O) {
                    mq.debug("pollComplete notify error: " + O.message, O)
                }
                mq.pgvSendClick({hottag: "smartqq.im.switchpw"})
            } else {
                G != 109 && G != 110 && F();
                try {
                    b.fire(a, "PollComplete")
                } catch (u) {
                    mq.debug("pollComplete notify error: " +
                    u.message, u)
                }
            }
        }, p = function(E) {
            mq.debug("onPollError");
            y(E)
        }, y = function() {
            F();
            try {
                b.fire(a, "PollComplete")
            } catch (E) {
                mq.debug("pollComplete notify error: " + E.message, E)
            }
            mq.pgvSendClick({hottag: "smartqq.im.polltimeout"})
        }, F = function() {
            mq.debug("pool failure " + k);
            if (++k > 4) {
                k = 0;
                b.fire(a, "FailCountOverMax")
            }
        };
        this.sendReLink = function() {
            var E = {ptwebqq: mq.ptwebqq,clientid: mq.clientid,psessionid: mq.psessionid,key: "",state: mq.util.code2state(mq.main.loginType)};
            this.require({url: e,action: "relink",method: "POST",
                data: E,onSuccess: H,onError: M,onTimeout: P})
        };
        var H = function(E) {
            switch (E.retcode) {
                case 0:
                    pollMax = 1;
                    b.fire(a, "ReLinkSuccess", E.result);
                    break;
                case 103:
                    b.fire(a, "NotReLogin", E.result);
                    break;
                case 113:
                case 115:
                case 112:
                    b.fire(a, "ReLinkFailure", E);
                    break;
                default:
                    b.fire(a, "ReLinkStop")
            }
        }, M = function() {
            b.fire(a, "ReLinkFailure")
        }, P = function() {
            b.fire(a, "ReLinkFailure")
        };
        this.sendRefuseFile = function(E) {
            E.psessionid = mq.psessionid;
            E.clientid = mq.clientid;
            this.require({url: n,method: "GET",data: E})
        };
        this.sendRefuseOfflineFile =
        function(E) {
            E.psessionid = mq.psessionid;
            E.clientid = mq.clientid;
            this.require({url: m,method: "GET",data: E})
        }
    })
});
define("mq.view.MemberList", ["./mq.i18n", "./mq.view.transitionmanager"], function() {
    J.$package("mq.view", function(g) {
        var a = g.dom, b = g.string, c = mq.i18n.message, e = document;
        this.MemberList = g.Class({init: function(j) {
                j = j || {};
                this.id = j.id;
                this.scrollArea = j.scrollArea;
                this.listContainer = j.listContainer;
                this.listTmpl = j.listTmpl;
                this.create()
            },create: function() {
                this.scroll = new iScroll(this.scrollArea);
                this.lazyload = MUI.I_LazyLoadImgs({scrollObj: this.scroll,isFade: true})
            },render: function(j, f) {
                this._preprocessData(j);
                j.dataType = j.prefix;
                this.listContainer.innerHTML = this.listTmpl(j);
                !f && this.refresh()
            },renderAllCategory: function(j) {
                var f, n;
                f = 0;
                for (n = j.length; f < n; ++f)
                    this.renderOneCategory(j[f])
            },renderOneCategory: function(j) {
                var f = [], n = j.list;
                j = j.index;
                g.each(["callme", "online", "away", "busy", "silent", "offline"], function(m) {
                    f = f.concat(n[m])
                });
                this._renderOneCategory(f, j)
            },_renderOneCategory: function(j, f) {
                if (container = a.id("groupBodyUl-" + f))
                    container.innerHTML = this.listTmpl({type: "list",list: j,prefix: this.id,html: b.encodeHtml})
            },
            renderOneSignature: function(j, f) {
                var n = this.listContainer.querySelector("#friend-item-friend-" + j), m, r;
                if (n) {
                    m = n.querySelector(".member_signature");
                    r = b.encodeHtml;
                    if (m)
                        m.innerHTML = r(f);
                    else {
                        m = e.createElement("span");
                        m.setAttribute("class", "member_signature");
                        m.innerHTML = r(f);
                        msgEle = n.querySelector(".member_msg");
                        msgEle.appendChild(m)
                    }
                }
            },renderOneState: function(j, f) {
                var n = this.listContainer.querySelector("#friend-item-friend-" + j);
                if (n)
                    if (n = n.querySelector(".member_state"))
                        n.innerHTML = "[" + c(f) + "]"
            },
            renderAllOnlineStateCount: function(j) {
                var f = a.className("onlinePercent"), n;
                g.each(j, function(m, r) {
                    if (n = f[r])
                        n.innerHTML = m.count - m.list.offline.length + "/" + m.count
                })
            },append: function(j, f) {
                this._preprocessData(j);
                j.dataType = j.prefix;
                var n = this.listTmpl(j), m = document.createElement("div");
                m.innerHTML = n;
                n = m.childNodes;
                for (m = document.createDocumentFragment(); n[0]; )
                    m.appendChild(n[0]);
                this.listContainer.appendChild(m);
                !f && this.refresh()
            },destory: function() {
                for (var j in this)
                    if (this.hasOwnProperty(j)) {
                        this[j] =
                        null;
                        delete this[j]
                    }
            },refresh: function() {
                this.scroll.refresh();
                this.lazyload.refresh()
            },renderCateItems: function(j) {
                var f = {}, n = [], m, r;
                for (m = 0; r = j[m]; m++) {
                    r = g.extend({}, r);
                    r.stateName = "[" + c(r.state) + "]";
                    if (!f[r.category]) {
                        f[r.category] = [];
                        n.push(r.category)
                    }
                    f[r.category].push(r)
                }
                j = n.length;
                for (m = 0; m <= j; m++) {
                    var k = n[m];
                    if (f.hasOwnProperty(k)) {
                        r = f[k];
                        this._renderOneCategory(r, k)
                    }
                }
                this.refresh()
            },_preprocessData: function(j) {
                j.html = b.encodeHtml;
                j.prefix = this.id;
                return j
            }})
    })
});
define("mq.model.memberlist", ["./mq.i18n", "./mq.portal", "./mq.report"], function() {
    J.$package("mq.model.buddylist", function(g) {
        var a = JM.event, b = mq.i18n.message, c = this, e = [], j = [], f = [], n = [], m = [], r = [], k = {}, d = {}, t = {}, B = {}, z = {}, q = [], w = {}, C, h, o = mq.STATIC_CGI_URL + "api/get_user_friends2", v = mq.STATIC_CGI_URL + "api/get_group_name_list_mask2", D = mq.STATIC_CGI_URL + "api/get_discus_list", p = mq.DYNAMIC_CGI_URL + "channel/get_recent_list2", y = mq.STATIC_CGI_URL + "api/get_single_long_nick2", F = mq.STATIC_CGI_URL + "api/get_self_info2",
        H = mq.STATIC_CGI_URL + "api/get_group_info_ext2", M = mq.DYNAMIC_CGI_URL + "channel/get_discu_info", P = mq.STATIC_CGI_URL + "api/get_friend_info2", E = mq.STATIC_CGI_URL + "api/get_friend_uin2", G = mq.DYNAMIC_CGI_URL + "channel/get_online_buddies2", O = mq.DYNAMIC_CGI_URL + "channel/change_status2", u = function(x, K) {
            x += "";
            for (var N = [], T = 0; T < K.length; T++)
                N[T % 4] ^= K.charCodeAt(T);
            var U = ["EC", "OK"], V = [];
            V[0] = x >> 24 & 255 ^ U[0].charCodeAt(0);
            V[1] = x >> 16 & 255 ^ U[0].charCodeAt(1);
            V[2] = x >> 8 & 255 ^ U[1].charCodeAt(0);
            V[3] = x & 255 ^ U[1].charCodeAt(1);
            U = [];
            for (T = 0; T < 8; T++)
                U[T] = T % 2 == 0 ? N[T >> 1] : V[T >> 1];
            N = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"];
            V = "";
            for (T = 0; T < U.length; T++) {
                V += N[U[T] >> 4 & 15];
                V += N[U[T] & 15]
            }
            return V
        }, s = function(x) {
            var K = {};
            g.each(x.gmasklist, function(N) {
                K[N.gid] = N.mask
            });
            g.each(x.gnamelist, function(N) {
                N.mask = K[N.gid] || 0;
                c.addGroup(new R(N))
            });
            a.fire(c, "groupListChange", j)
        }, A = function(x) {
            g.each(x.dnamelist, function(K) {
                c.addDiscuss(new X(K))
            });
            a.fire(c, "discussListChange", m)
        }, I = function(x, K, N, T, U) {
            N = 0;
            for (var V =
            x.length; N < V; N++) {
                var Y = x[N];
                Y.count = 0;
                Y.onlineCount = 0;
                Y.list = {callme: [],online: [],away: [],busy: [],silent: [],offline: []};
                c.addCatagory(Y)
            }
            g.each(K, function(S, ba) {
                if (S.uin != C) {
                    var W = T[ba];
                    W = {uin: W.uin,allow: W.allow,nick: W.nick,face: W.face,age: W.age,gender: W.gender,vip: W.vip,ruin: W.ruin,category: S.categories || 0};
                    W.mark = U[W.uin] ? U[W.uin].markname : false;
                    c.addFriend(new Q(W));
                    (W = c.getCatagoryById(S.categories)) && W.count++
                }
            });
            a.fire(c, "friendsListChange", e, n)
        }, L = {onGetFriendsListSuccess: function(x) {
                var K =
                x.categories || [], N = x.friends || [], T = x.vipinfo || [], U = x.info || [];
                x = x.marknames || [];
                for (var V = {}, Y = false, S = 0; S < K.length; S++)
                    if (K[S].index == 0)
                        Y = true;
                for (S = 0; S < x.length; S++)
                    V[x[S].uin] = x[S];
                Y || K.unshift({index: 0,name: "\u6211\u7684\u597d\u53cb"});
                I(K, N, T, U, V)
            },onGetFriendUinSuccess: function(x) {
                var K = c.getFriendByUin(x.uin);
                if (K) {
                    K.ruin = x.account;
                    a.fire(c, "friendInfoUpdate", K)
                }
            },onGetGroupListSuccess: function(x) {
                s(x)
            },onGetDiscussListSuccess: function(x) {
                A(x)
            },onGetRecentListSuccess: function(x) {
                f = x;
                a.fire(c,
                "recentListChange", f)
            },onGetSignatureSuccess: function(x, K) {
                c.addSignature(x, K);
                var N = c.getFriendByUin(x);
                N && N.setSignature(K);
                a.fire(c, "signatureGot", x, K)
            },onGetSelfInfoSuccess: function(x) {
                c.setSelfInfo(x);
                a.fire(c, "selfInfoChange", x)
            },onGetGroupInfoListSuccess: function(x) {
                var K = x.ginfo, N = K.members, T = x.minfo, U = x.vipinfo, V = x.cards || [], Y = V.length || 0, S = c.getGroupByGid(K.gid);
                g.extend(S, K);
                S.hasDetailInfo = true;
                S.members = [];
                g.each(N, function(ba, W) {
                    for (var Z = "", ca = ba.muin, $ = T[W], da = U[W], aa = 0; aa < Y; aa++)
                        if (V[aa].muin ==
                        ca) {
                            Z = V[aa].card;
                            break
                        }
                    Z = new Q({uin: ca,allow: $.allow,nick: $.nick,face: $.face,age: $.age,gender: $.gender,vip: da.is_vip,country: $.country,city: $.city,province: $.province,group: K,cardName: Z});
                    if (!c.getFriendByUin(Z.uin)) {
                        Z.isStrange = 1;
                        Z.groupUin = K.gid
                    }
                    c.addFriend(Z);
                    S.members.push(Z)
                });
                a.fire(c, "groupInfoUpdate", S)
            },onGetDiscussInfoListSuccess: function(x) {
                var K = x.info, N = K.mem_list, T = x.mem_info, U = c.getDiscussById(K.did);
                U.hasDetailInfo = true;
                U.members = [];
                g.each(N, function(V, Y) {
                    var S = T[Y];
                    S = new Q({uin: V.mem_uin,
                        nick: S.nick,allow: S.allow,face: S.face,age: S.age,gender: S.gender,country: S.country,city: S.city,province: S.province,discuss: K});
                    if (!c.getFriendByUin(S.uin)) {
                        S.isStrange = 1;
                        S.discussUin = K.did
                    }
                    c.addFriend(S);
                    U.members.push(S)
                });
                a.fire(c, "discussInfoUpdate", U)
            },onGetFriendInfo: function(x) {
                var K = c.getFriendByUin(x.uin);
                g.extend(K, x);
                K.hasDetailInfo = true;
                a.fire(c, "friendInfoUpdate", K)
            },onGetBuddyOnlineStateSuccess: function(x) {
                c.setAllBuddyState(x)
            }}, Q = g.Class({init: function(x) {
                this.uin = this.account = x.uin;
                this.ruin = x.ruin;
                this.uiuin = x.uiuin;
                this.allow = x.allow;
                this.face = x.face;
                this.age = x.age;
                this.gender = x.gender;
                this.name = this.nick = x.nick;
                this.country = x.country;
                this.city = x.city;
                this.province = x.province;
                this.avatar = this.getAvatar();
                this.category = x.category;
                this.group = x.group;
                this.discuss = x.discuss;
                this.vip = x.vip || false;
                this.clientType = x.clientType || "10000";
                this.mark = x.mark || false;
                this.state = x.state || "offline";
                this.stateName = "[" + b(this.state) + "]";
                this.isStrange = x.isStrange;
                this.cardName = x.cardName || ""
            },
            getAvatar: function() {
                return c.getAvatar(this.uin, 1)
            },setSignature: function(x) {
                if (x) {
                    this.signature = x;
                    a.fire(c, "userSignatureChange", this)
                }
            },setState: function(x) {
                this.state = x;
                this.stateName = "[" + b(x) + "]"
            }}), R = g.Class({init: function(x) {
                this.gid = this.account = x.gid;
                this.code = x.code;
                this.preMask = this.mask = parseInt(x.mask);
                this.name = x.name;
                this.markName = x.markName;
                this.type = x.type;
                this.hasManageAuthority = this.isLoadInfo = false;
                this.uin2members = {};
                this.level = 0;
                this.avatar = this.getAvatar()
            },getAvatar: function() {
                return c.getAvatar(this.gid,
                4)
            }}), X = g.Class({init: function(x) {
                this.did = this.account = x.did;
                this.mask = parseInt(x.mask || 0);
                this.preMask = parseInt(this.mask);
                this.name = x.name;
                this.isLoadInfo = false;
                this.members = [];
                this.owner = "";
                this.notSetName = false;
                this.hadModified = true;
                this.avatar = this.getAvatar()
            },getAvatar: function() {
                return "http://0.web.qstatic.com/webqqpic/style/images/discu_avatar.png"
            }});
        this.init = function(x) {
            C = x.selfUin
        };
        this.bindHandlers = function() {
        };
        this.getAvatar = function(x, K) {
            K = K || 1;
            return "http://face" + x % 10 + ".web.qq.com/cgi/svr/face/getface?cache=1&type=" +
            K + "&f=40&uin=" + x + "&t=" + Math.floor(new Date / 1E3) + "&vfwebqq=" + mq.vfwebqq
        };
        mq.report.clearSpeedCache("7832-22-1", 4);
        mq.report.speedReport("7832-22-1", 4);
        this.getUserFriends = function() {
            var x = {};
            x.vfwebqq = mq.vfwebqq;
            x.hash = u(C, mq.ptwebqq);
            return function(K) {
                mq.rpcService.require({url: o,method: "POST",withCredentials: true,param: x,onSuccess: function(N) {
                        mq.report.speedReport("7832-22-1", 4, true, true);
                        if (N.retcode == 0) {
                            K();
                            L.onGetFriendsListSuccess(N.result)
                        }
                    }})
            }
        };
        mq.report.clearSpeedCache("7832-22-1", 5);
        mq.report.speedReport("7832-22-1",
        5);
        this.getGroupList = function() {
            var x = {};
            x.vfwebqq = mq.vfwebqq;
            x.hash = u(C, mq.ptwebqq);
            return function(K) {
                mq.rpcService.require({url: v,method: "POST",withCredentials: true,param: x,onSuccess: function(N) {
                        mq.report.speedReport("7832-22-1", 5, true, true);
                        if (N.retcode == 0) {
                            K();
                            L.onGetGroupListSuccess(N.result)
                        }
                    }})
            }
        };
        mq.report.clearSpeedCache("7832-22-1", 6);
        mq.report.speedReport("7832-22-1", 6);
        this.getDiscussList = function() {
            var x = {};
            x.clientid = mq.clientid;
            x.psessionid = mq.psessionid;
            x.vfwebqq = mq.vfwebqq;
            return function(K) {
                mq.rpcService.require({url: D,
                    method: "GET",withCredentials: true,param: x,onSuccess: function(N) {
                        mq.report.speedReport("7832-22-1", 6, true, true);
                        if (N.retcode == 0) {
                            K();
                            L.onGetDiscussListSuccess(N.result)
                        }
                    }})
            }
        };
        this.getRecentList = function(x) {
            var K = {};
            K.vfwebqq = mq.vfwebqq;
            K.clientid = mq.clientid;
            K.psessionid = mq.psessionid;
            mq.rpcService.require({url: p,method: "POST",withCredentials: true,param: K,onSuccess: function(N) {
                    if (N.retcode == 0) {
                        L.onGetRecentListSuccess(N.result);
                        mq.report.speedReport("7832-22-1", 3, true, true);
                        x && x()
                    }
                }})
        };
        this.sendGetSignature =
        function(x) {
            mq.rpcService.require({url: y,method: "GET",param: {tuin: x,vfwebqq: mq.vfwebqq},withCredentials: true,onSuccess: function(K) {
                    K.retcode === 0 && L.onGetSignatureSuccess(x, K.result[0].lnick)
                }})
        };
        this.getGroupInfoList = function(x) {
            var K = {};
            K.gcode = x;
            K.vfwebqq = mq.vfwebqq;
            mq.rpcService.require({url: H,method: "GET",param: K,withCredentials: true,onSuccess: function(N) {
                    N.retcode === 0 && L.onGetGroupInfoListSuccess(N.result)
                }})
        };
        this.getDiscussInfoList = function(x) {
            var K = {};
            K.did = x;
            K.vfwebqq = mq.vfwebqq;
            K.clientid =
            mq.clientid;
            K.psessionid = mq.psessionid;
            mq.rpcService.require({url: M,method: "GET",param: K,withCredentials: true,onSuccess: function(N) {
                    N.retcode === 0 && L.onGetDiscussInfoListSuccess(N.result)
                }})
        };
        this.sendGetFriendUin = function(x) {
            var K = {};
            K.tuin = x;
            K.type = 1;
            K.vfwebqq = mq.vfwebqq;
            mq.rpcService.require({url: E,method: "GET",param: K,withCredentials: true,onSuccess: function(N) {
                    N.retcode === 0 && L.onGetFriendUinSuccess(N.result)
                }})
        };
        this.sendGetFriendInfo = function(x) {
            var K = {};
            K.tuin = x;
            K.vfwebqq = mq.vfwebqq;
            K.clientid =
            mq.clientid;
            K.psessionid = mq.psessionid;
            mq.rpcService.require({url: P,method: "GET",param: K,withCredentials: true,onSuccess: function(N) {
                    N.retcode === 0 && L.onGetFriendInfo(N.result)
                }})
        };
        this.sendGetBuddyOnlineState = function() {
            var x = {};
            x.vfwebqq = mq.vfwebqq;
            x.clientid = mq.clientid;
            x.psessionid = mq.psessionid;
            mq.rpcService.require({url: G,method: "GET",param: x,withCredentials: true,onSuccess: function(K) {
                    K.retcode === 0 && L.onGetBuddyOnlineStateSuccess(K.result)
                }})
        };
        this.getBuddyInfo = function(x, K) {
            K = K || "friend";
            var N;
            if (K == "friend") {
                N = this.getFriendByUin(x);
                "signature" in N || this.sendGetSignature(x);
                N.hasDetailInfo || this.sendGetFriendInfo(x)
            } else if (K == "group") {
                N = this.getGroupByGid(x);
                N.hasDetailInfo || this.getGroupInfoList(N.code)
            } else if (K == "discuss") {
                N = this.getDiscussById(x);
                N.hasDetailInfo || this.getDiscussInfoList(N.did)
            }
            return N
        };
        this.getStrangeByUin = function(x) {
            return w[x]
        };
        this.getFriendByUin = function(x) {
            return d[x]
        };
        this.getFriends = function() {
            return n
        };
        this.getGroupByGid = function(x) {
            return t[x]
        };
        this.getDiscussById =
        function(x) {
            return B[x]
        };
        this.getSignatureByUin = function(x) {
            return z[x] || 1
        };
        this.getSelfInfo = function() {
            return h
        };
        this.addStrange = function(x) {
            if (!w[x.uin]) {
                w[x.uin] = x;
                q.push(x)
            }
            return x
        };
        this.addFriend = function(x) {
            if (!d[x.uin]) {
                if (!x.type)
                    x.type = "friend";
                d[x.uin] = x;
                n.push(x)
            }
            return x
        };
        this.addGroup = function(x) {
            if (!t[x.gid]) {
                x.type = "group";
                t[x.gid] = x;
                j.push(x)
            }
            return x
        };
        this.addDiscuss = function(x) {
            if (!B[x.did]) {
                x.type = "discuss";
                B[x.did] = x;
                m.push(x)
            }
            return x
        };
        this.addSignature = function(x, K) {
            if (!z[x]) {
                z[x] =
                K;
                r.push(K)
            }
            return K
        };
        this.addCatagory = function(x) {
            if (!k[x.index]) {
                k[x.index] = x;
                e.push(x)
            }
            return x
        };
        this.getCatagories = function() {
            return e
        };
        this.getCatagoryById = function(x) {
            return k[x]
        };
        this.getSelfUin = function() {
            return C
        };
        this.sendGetSelfInfo = function() {
            mq.rpcService.require({url: F,method: "GET",withCredentials: true,onSuccess: function(x) {
                    x.retcode == 0 && L.onGetSelfInfoSuccess(x.result)
                }})
        };
        this.setSelfInfo = function(x) {
            x.name = x.nick;
            x.avatar = this.getAvatar(C);
            x.isSelf = true;
            h = x;
            a.fire(c, "getFirstSelfInfo",
            h)
        };
        this.searchFriends = function(x) {
            var K = [], N = n.concat(j).concat(m);
            x.length > 0 && g.each(N, function(T) {
                if (T.name.toUpperCase().indexOf(x.toUpperCase()) > -1 || T.mark && T.mark.toUpperCase().indexOf(x.toUpperCase()) > -1)
                    K.push(T)
            });
            return K
        };
        this.setAllBuddyState = function(x) {
            for (var K = 0; K < x.length; K++) {
                var N = x[K];
                N.uin != C && this.setState(N.uin, N.status, N.client_type)
            }
            a.fire(this, "allBuddyStateChange")
        };
        this.setState = function(x, K) {
            var N = this.getFriendByUin(x);
            if (N && N.state !== K) {
                N.setState(K);
                a.fire(this, "buddyStateChange",
                {uin: x})
            }
        };
        this.sendChangeStatus = function(x) {
            x = x || {newstatus: "hidden"};
            x.clientid = mq.clientid;
            x.psessionid = mq.psessionid;
            mq.rpcService.require({url: O,method: "GET",param: x,withCredentials: true,onSuccess: function() {
                    mq.rpcService.require({url: G,method: "GET",param: x,withCredentials: true,onSuccess: function() {
                        }})
                }})
        }
    })
});
define("mq.presenter.memberlist", ["jm"], function() {
    J.$package("mq.presenter.buddylist", function() {
        var g = JM.event, a = JM.dom, b = this, c = {onRecentListChange: function(e) {
                for (var j = b.model, f = j.getSelfUin(), n = [], m, r = 0, k; k = e[r]; r++)
                    if (k.uin != f) {
                        if (k.type == 0)
                            m = j.getFriendByUin(k.uin);
                        else if (k.type == 1)
                            m = j.getGroupByGid(k.uin);
                        else if (k.type == 2)
                            m = j.getDiscussById(k.uin);
                        m && n.push(m)
                    }
                b.sessionView.render(n)
            },onFriendsListChange: function(e, j) {
                var f = b.contactView;
                f.memberListAreas.friend.render({type: "category",
                    list: e}, true);
                f.memberListAreas.friend.renderCateItems(j)
            },onGroupListChange: function(e) {
                b.contactView.memberListAreas.group.render({type: "list",list: e})
            },onDiscussListChange: function(e) {
                b.contactView.memberListAreas.discuss.render({type: "list",list: e})
            },onUserSignatureChange: function(e) {
                b.contactView.memberListAreas.friend.renderOneSignature(e.uin, e.signature)
            },onReceiveMessage: function(e) {
                var j = e.send_to || e.from_group || e.from_discuss || e.from_user;
                j = e.notNotify || mq.presenter.chat.isChating(j);
                b.sessionView.onReceiveMessage(e,
                j)
            },onMemberInVisibleArea: function(e, j) {
                var f = b.model;
                if (j === "friend") {
                    friend = f.getFriendByUin(e);
                    friend.signature || f.sendGetSignature(e)
                }
            },onFriendUinUpdate: function(e) {
                e = a.id("friend-uin-" + e.account);
                console.log(e)
            },onBuddyStateChange: function(e) {
                e = e.uin;
                var j = b.model.getFriendByUin(e);
                b.contactView.memberListAreas.friend.renderOneState(e, j.state)
            },onAllBuddyStateChange: function() {
                for (var e = b.model.getFriends(), j = b.model.getCatagories(), f = b.contactView.memberListAreas.friend, n = 0, m = e.length; n < m; n++) {
                    var r =
                    e[n];
                    b.model.getCatagoryById(r.category).list[r.state].push(r)
                }
                f.renderAllOnlineStateCount(j);
                f.renderAllCategory(j)
            }};
        this.init = function() {
            this.contactView = mq.view.contact;
            this.sessionView = mq.view.session;
            this.model = mq.model.buddylist;
            this.view = mq.view.buddylist;
            this.bindHandlers()
        };
        this.bindHandlers = function() {
            var e = this.model, j = mq.model.chat, f = this.contactView;
            g.on(e, "recentListChange", c.onRecentListChange);
            g.on(e, "groupListChange", c.onGroupListChange);
            g.on(e, "discussListChange", c.onDiscussListChange);
            g.on(e, "userSignatureChange", c.onUserSignatureChange);
            g.on(e, "getFriendUinUpdate", c.onFriendUinUpdate);
            g.on(e, "friendsListChange", c.onFriendsListChange);
            g.on(e, "buddyStateChange", c.onBuddyStateChange);
            g.on(e, "allBuddyStateChange", c.onAllBuddyStateChange);
            g.on(j, "messageReceived", c.onReceiveMessage);
            g.on(j, "groupMessageReceived", c.onReceiveMessage);
            g.on(j, "discussMessageReceived", c.onReceiveMessage);
            g.on(f, "memberInVisibleArea", c.onMemberInVisibleArea)
        }
    })
});
define("mq.model.chat", ["./mq.portal"], function() {
    J.$package("mq.model.chat", function(g) {
        var a = JM.event, b = mq.DYNAMIC_CGI_URL + "channel/send_buddy_msg2", c = mq.DYNAMIC_CGI_URL + "channel/send_sess_msg2", e = mq.DYNAMIC_CGI_URL + "channel/send_qun_msg2", j = mq.DYNAMIC_CGI_URL + "channel/send_discu_msg2", f = mq.DYNAMIC_CGI_URL + "channel/get_c2cmsg_sig2", n = this, m = {}, r = {}, k = {}, d = {}, t = {}, B, z = 0, q = (new Date).getTime();
        q = (q - q % 1E3) / 1E3;
        q = q % 1E4 * 1E4;
        var w = function() {
            z++;
            return q + z
        };
        this.addMessage = function(h, o) {
            m[h] || (m[h] = []);
            m[h].push(o);
            a.fire(n, "messageReceived", o);
            return o
        };
        this.addGroupMessage = function(h, o) {
            r[h] || (r[h] = []);
            r[h].push(o);
            a.fire(n, "groupMessageReceived", o);
            return o
        };
        this.addDiscussMessage = function(h, o) {
            k[h] || (k[h] = []);
            k[h].push(o);
            a.fire(n, "discussMessageReceived", o);
            return o
        };
        var C = {onPollMessageSuccess: function(h) {
                var o = h.value, v = o.from_uin, D = null;
                switch (h.poll_type) {
                    case "sess_message":
                    case "message":
                        h = n.m_model.getFriendByUin(v);
                        if (v === 0) {
                            v = n.m_model.getSelfUin();
                            h = n.m_model.getSelfInfo()
                        }
                        if (h) {
                            D =
                            {content: o.content,from_uin: v,from_user: h,sender: h,sender_uin: v,time: o.time ? o.time * 1E3 : +new Date};
                            n.addMessage(v, D)
                        }
                        break;
                    case "group_message":
                        var p = n.m_model.getGroupByGid(v);
                        h = n.m_model.getFriendByUin(o.send_uin);
                        for (var y = p.members || [], F = y.length || 0, H = 0; H < F; H++)
                            if (y[H].uin == h.uin) {
                                h.cardName = y[H].cardName;
                                break
                            }
                        if (p && p.mask != 2) {
                            D = {notNotify: !!p.mask,content: o.content,from_uin: v,from_group: p,sender_uin: o.send_uin,sender: h,time: o.time * 1E3};
                            n.addGroupMessage(v, D)
                        }
                        break;
                    case "discu_message":
                        v = o.did;
                        p = n.m_model.getDiscussById(v);
                        h = n.m_model.getFriendByUin(o.send_uin);
                        if (p) {
                            D = {content: o.content,from_uin: v,from_discuss: p,sender_uin: o.send_uin,sender: h,time: o.time * 1E3};
                            n.addDiscussMessage(v, D)
                        }
                        break;
                    case "filesrv_transfer":
                        n.receiveTransferMsg(h.value);
                        break;
                    case "file_message":
                        n.receiveFile(h.value);
                        break;
                    case "push_offfile":
                        n.receiveOffFile(h.value);
                        break;
                    case "notify_offfile":
                        n.receiveNotifyOffFile(h.value)
                }
                D && a.fire(n, "allMessageReceived", D)
            }};
        this.init = function() {
            this.m_model = mq.model.buddylist;
            a.on(mq.main, "receiveMessage", C.onPollMessageSuccess);
            a.on(mq.main, "receiveFileMessage", C.onPollMessageSuccess)
        };
        this.sendMsg = function(h) {
            h.clientid = mq.clientid;
            h.msg_id = w();
            h.psessionid = mq.psessionid;
            mq.rpcService.require({url: b,https: mq.setting.enableHttps,param: h,withCredentials: true,method: "POST",onSuccess: function() {
                }})
        };
        this.sendGetSessionSignature = function(h) {
            var o = {id: h.group_uin || h.discuss_uin,to_uin: h.to_uin,clientid: mq.clientid,psessionid: mq.psessionid};
            if (h.group_uin)
                o.service_type = 0;
            else if (h.discuss_uin)
                o.service_type = 1;
            currentServiceType = o.service_type;
            mq.rpcService.require({url: f,param: o,withCredentials: true,method: "GET",onSuccess: function(v) {
                    if (v.retcode == 0)
                        B = v.result.value
                }})
        };
        this.sendSessMsg = function(h) {
            h.clientid = mq.clientid;
            h.msg_id = w();
            h.psessionid = mq.psessionid;
            h.group_sig = B;
            h.service_type = currentServiceType;
            mq.rpcService.require({url: c,param: h,withCredentials: true,method: "POST",onSuccess: function() {
                }})
        };
        this.sendGroupMsg = function(h) {
            h.clientid = mq.clientid;
            h.msg_id =
            w();
            h.psessionid = mq.psessionid;
            mq.rpcService.require({url: e,https: mq.setting.enableHttps,param: h,withCredentials: true,method: "POST",onSuccess: function() {
                }})
        };
        this.sendDiscussMsg = function(h) {
            h.clientid = mq.clientid;
            h.msg_id = w();
            h.psessionid = mq.psessionid;
            mq.rpcService.require({url: j,https: mq.setting.enableHttps,param: h,withCredentials: true,method: "POST",onSuccess: function() {
                }})
        };
        this.getMsgByUin = function(h) {
            return m[h]
        };
        this.getGroupMsgByGid = function(h) {
            return r[h]
        };
        this.getDiscussMsgByDid = function(h) {
            return k[h]
        };
        this.getMessages = function(h, o) {
            o = o || "friend";
            var v = [];
            if (o == "friend")
                v = this.getMsgByUin(h);
            else if (o == "group")
                v = this.getGroupMsgByGid(h);
            else if (o == "discuss")
                v = this.getDiscussMsgByDid(h);
            return v
        };
        this.sendFile = function(h) {
            var o = [["sendfile", h.filename]], v = {type: "sendfile",name: h.filename,from_uin: h.to_uin,time: (new Date).getTime(),isread: true,session_id: h.lcid};
            d[h.to_uin + "_" + h.lcid] = v;
            h = {notNotify: true,type: "send_file",system: true,content: o,attach: v,from_uin: n.m_model.getSelfUin(),to_uin: h.to_uin};
            n.receiveMessage(h)
        };
        this.receiveTransferMsg = function(h) {
            var o = h.file_infos[0];
            if (o.file_name != "") {
                var v = "", D = "";
                if (o.file_status == 51) {
                    v = [["transtimeout", o.file_name, h.lc_id]];
                    D = {type: "transtimeout",name: o.file_name,isread: true}
                } else if (o.file_status == 50) {
                    v = [["transerror", o.file_name, h.lc_id]];
                    D = {type: "transerror",name: o.file_name,isread: true}
                } else if (o.file_status == 53) {
                    v = [["refusedbyclient", o.file_name, h.lc_id]];
                    D = {type: "refusedbyclient",name: o.file_name,isread: true}
                } else if (o.file_status == 0) {
                    v =
                    [["transok", o.file_name, h.lc_id]];
                    D = {type: "transok",name: o.file_name,isread: true}
                } else
                    return false;
                o = d[h.from_uin + "_" + h.lc_id] || {};
                if (o.isFinished || typeof t[h.session_id] != "undefined" && t[h.session_id] === true)
                    return false;
                else
                    o.isFinished = true;
                this.receiveMessage({type: "file_message",system: true,to_uin: h.to_uin,from_uin: h.from_uin,content: v,attach: D})
            }
        };
        this.receiveMessage = function(h) {
            var o = h.from_uin, v, D = h.to_uin, p;
            p = this.m_model.getSelfUin();
            v = !o || o == p ? this.m_model.getSelfInfo() : this.m_model.getFriendByUin(o);
            p = D == p ? this.m_model.getSelfInfo() : this.m_model.getFriendByUin(D);
            if (v) {
                D = {from_uin: o,from_user: v,sender_uin: o,sender: v,to_uin: D,to_user: p,time: h.time ? h.time * 1E3 : +new Date};
                if (v.isSelf)
                    D.send_to = p;
                D = g.extend(h, D);
                this.addMessage(o, D)
            }
        };
        this.receiveFile = function(h) {
            if (h.mode === "recv") {
                var o = [["rfile", h.name, h.session_id]];
                h.content = o;
                h.attach = {type: "rfile",name: h.name,from_uin: h.from_uin,time: h.time,isread: false,session_id: h.session_id,msg_type: h.msg_type};
                o = h.from_uin + "_" + h.session_id;
                if (d[o])
                    d[o] =
                    h.attach;
                else {
                    d[o] = h.attach;
                    h.type = "receive_file";
                    h.system = true;
                    this.receiveMessage(h)
                }
            } else if (h.mode === "refuse") {
                if (h.type !== 161) {
                    if (h.cancel_type == 2) {
                        t[h.session_id] = true;
                        var v = parseInt(h.session_id, 10).toString(2);
                        if (v.length >= 12) {
                            v = v.substr(v.length - 12, 12);
                            h.session_id = parseInt(v, 2).toString(10)
                        }
                    }
                    o = h.from_uin + "_" + h.session_id;
                    v = d[o];
                    if (typeof v == "undefined")
                        return false;
                    if (v.isFinished)
                        return false;
                    else
                        d[o].isFinished = true;
                    o = [["rffile", v.name]];
                    v.type = "rffile";
                    if (h.cancel_type == 2) {
                        o = [["wrffile",
                                v.name]];
                        v.type = "wrffile"
                    } else if (h.cancel_type == 3) {
                        o = [["rtfile", v.name]];
                        v.type = "rtfile"
                    }
                    h.content = o;
                    h.attach = v;
                    h.type = "refuse_file";
                    h.system = true;
                    this.receiveMessage(h)
                }
            } else if (h.mode === "send_ack") {
                v = parseInt(h.session_id, 10).toString(2);
                if (v.length < 12)
                    return false;
                v = v.substr(v.length - 12, 12);
                h.session_id = parseInt(v, 2).toString(10);
                o = h.from_uin + "_" + h.session_id;
                v = d[o];
                o = [["wrfile", v.name, v.session_id]];
                h.content = o;
                h.attach = {type: "wrfile",name: v.name,from_uin: v.from_uin,time: h.time,session_id: h.session_id};
                h.type = "accept_file";
                h.system = true;
                this.receiveMessage(h)
            }
        };
        this.getFilesList = function() {
            return d
        };
        this.receiveOffFile = function(h) {
            var o = h.from_uin + "_" + h.msg_id;
            h.msg_type = 9;
            h.content = [["offfile", "\u5bf9\u65b9\u7ed9\u4f60\u53d1\u9001\u79bb\u7ebf\u6587\u4ef6\u3002"]];
            h.attach = h;
            h.attach.type = "offfile";
            h.attach.fileid = o;
            d[o] = h.attach;
            h.type = "offfile";
            h.system = true;
            this.receiveMessage(h)
        };
        this.receiveNotifyOffFile = function(h) {
            var o = "", v = "";
            if (h.action == 1) {
                o = '\u5bf9\u65b9\u5df2\u6210\u529f\u63a5\u6536\u4e86\u60a8\u53d1\u9001\u7684\u79bb\u7ebf\u6587\u4ef6"' +
                h.filename + '"\u3002';
                v = "notifyagreeofffile"
            } else {
                o = '\u5bf9\u65b9\u62d2\u7edd\u63a5\u6536\u60a8\u53d1\u9001\u7684\u79bb\u7ebf\u6587\u4ef6"' + h.filename + '"\u3002';
                v = "notifyrefuseofffile"
            }
            o = [[v, o]];
            var D = {type: v,name: h.filename,from_uin: h.from_uin,time: (new Date).getTime()};
            h = {type: v,from_uin: 0,to: h.from_uin,content: o,attach: D};
            h.system = true;
            this.receiveMessage(h)
        };
        this.agreeReceiveFile = function(h) {
            var o = [["agfile", h.name, h.session_id]];
            h.type = "agfile";
            h = {from_uin: 0,to_uin: h.from_uin,content: o,attach: h};
            h.system = true;
            this.receiveMessage(h)
        };
        this.refuseReceiveFile = function(h) {
            var o = [["rffile", h.name, h.session_id]];
            h.type = "rffile";
            o = {from_uin: 0,to_uin: h.from_uin,content: o,attach: h};
            o.system = true;
            this.receiveMessage(o);
            d[h.from_uin + "_" + h.session_id].isFinished = true;
            mq.rpcService.sendRefuseFile({to: h.from_uin,lcid: h.session_id})
        };
        this.refuseOfflineFile = function(h) {
            mq.rpcService.sendRefuseOfflineFile({to: h.from_uin,file_name: h.name,file_size: h.size,action: 2});
            h = {type: "single",from_uin: 0,to: h.from_uin,
                content: [["refuseofffile", "\u60a8\u62d2\u7edd\u63a5\u6536\u201c" + h.name + "\u201d\uff0c\u6587\u4ef6\u4f20\u8f93\u5931\u8d25\u3002"]],attach: {type: "refuseofffile",name: h.name,from_uin: h.from_uin,time: +new Date}};
            h.system = true;
            this.receiveMessage(h)
        };
        this.nextOfflineFile = function(h) {
            var o = [["nextofffile", '\u60a8\u53d6\u6d88\u4e86\u79bb\u7ebf\u6587\u4ef6"' + h.name + '"\u7684\u63a5\u6536\uff0c\u6211\u4eec\u5c06\u5728\u60a8\u4e0b\u6b21\u767b\u5f55\u540e\u8fdb\u884c\u63d0\u9192\u3002']], v = {type: "nextofffile",
                name: h.name,from_uin: h.from_uin,time: (new Date).getTime()};
            h = {type: "single",from_uin: 0,to: h.from_uin,content: o,attach: v};
            h.system = true;
            this.receiveMessage(h)
        }
    })
});
define("tmpl!../tmpl/tmpl_chat_footer.html", [], function() {
    return function(g) {
        var a, b = "";
        with (g || {}) {
            b += '<div class="chat_toolbar">\r\n<!--     <div id="add_app_btn" class="btn btn_add_grey">\r\n        <span class="btn_img"></span>\r\n    </div> --\>\r\n    <div id="add_face_btn" class="btn btn_face" >\r\n        <span class="btn_img"></span>\r\n    </div>\r\n    <textarea id="chat_textarea" class="input input_white chat_textarea"></textarea>\r\n    <button id="send_chat_btn" class="btn btn_small btn_blue" cmd="sendMsg">\r\n        <span class="btn_text">' + ((a =
            $M("send")) == null ? "" : a) + '</span>\r\n    </button>\r\n</div>\r\n<div id="face_images" class="qq_face_area" style="display:none;">\r\n    <ul class="wrap">\r\n        ';
            for (g = 1; g < 7; g++) {
                b += '\r\n        <li class="faceIteam faceIteam' + ((a = g) == null ? "" : a) + '" cmd="chooseFace">\r\n            ';
                for (var c = 20 * (g - 1); c < 20 * g; c++)
                    b += '\r\n        <i title="' + ((a = $F(c)) == null ? "" : a) + '" href="javascript:;"></i>\r\n            ';
                b += '\r\n            <i title="delKey" href="javascript:;"></i>\r\n        </li>\r\n        '
            }
            b +=
            '\r\n    </ul>\r\n    <ul class="btnsWrap"></ul>\r\n</div>\r\n<!-- <div id="qq_app_area" class="qq_app_area" style="display: none;">\r\n    <ul></ul>\r\n</div> --\>\r\n<iframe id="panel_uploadFilIframe" name="panel_uploadFilIframe" style="display:none"></iframe>\r\n'
        }
        return b
    }
});
define("tmpl!../tmpl/tmpl_chat_list.html", [], function() {
    return function(g) {
        var a, b = "";
        with (g || {}) {
            b += "";
            g = 0;
            for (var c; c = list[g]; g++) {
                var e = c.sender;
                if (c.htmlContent) {
                    b += "\r\n    ";
                    if (lastMessage && isNearTime(lastMessage.time, c.time))
                        b += "\r\n    ";
                    else {
                        lastMessage = c;
                        b += '\r\n<div class="chat_time"><span>' + ((a = formatChatTime(c.time)) == null ? "" : a) + "</span></div>\r\n    "
                    }
                    b += '\r\n\r\n<div class="chat_content_group ' + ((a = c.sender_uin == selfUin ? "self" : "buddy") == null ? "" : a) + " " + ((a = e ? "" : "need_update") == null ?
                    "" : a) + " " + ((a = c.system ? "system" : "") == null ? "" : a) + '" _sender_uin="' + ((a = c.sender_uin) == null ? "" : a) + '">\r\n    ';
                    if (!c.system) {
                        b += '\r\n    <img class="chat_content_avatar" src="' + ((a = e ? e.avatar : "") == null ? "" : a) + '" width="40px" height="40px">\r\n    ';
                        b += c.from_group && e && e.cardName ? '\r\n        <p class="chat_nick">' + ((a = html(e.cardName + "")) == null ? "" : a) + "</p>\r\n    " : '\r\n        <p class="chat_nick">' + ((a = html((e ? e.name : c.sender_uin) + "")) == null ? "" : a) + "</p>\r\n    ";
                        b += "\r\n    "
                    }
                    b += '\r\n    <p class="chat_content ">' +
                    ((a = translate(c.htmlContent)) == null ? "" : a) + "</p>\r\n</div>\r\n\r\n"
                }
            }
            b += "\r\n"
        }
        return b
    }
});
define("tmpl!../tmpl/tmpl_chat_tools.html", [], function() {
    return function(g) {
        var a, b = "";
        with (g || {})
            b += '\r\n<iframe id="panel_uploadFilIframe_' + ((a = friendUin) == null ? "" : a) + '" name="panel_uploadFilIframe_' + ((a = friendUin) == null ? "" : a) + '" style="display:none" src="http://web2.qq.com/domain.html"></iframe>\r\n<form id="panel_uploadFile_' + ((a = friendUin) == null ? "" : a) + '" name="panel_uploadFile_' + ((a = friendUin) == null ? "" : a) + '"  title="\u53d1\u9001\u6587\u4ef6..." class="panelSendForm" target="panel_uploadFilIframe_' +
            ((a = friendUin) == null ? "" : a) + '" action="" method="POST" enctype="multipart/form-data">\r\n   <a href="javascript:void(0)" id="panel_fileButton_' + ((a = friendUin) == null ? "" : a) + '" hidefocus="true" class="simpleMenuItem panel_sendFileButton" title="\u53d1\u9001\u6587\u4ef6...">\r\n        <input id="upload_file_' + ((a = friendUin) == null ? "" : a) + '" class="f" name="file" type="file" >\r\n   </a>\r\n</form>';
        return b
    }
});
define("tmpl!../tmpl/tmpl_chat_sendfile.html", [], function() {
    return function(g) {
        var a, b = "";
        with (g || {})
            b += '<form id="panel_uploadFile_' + ((a = id) == null ? "" : a) + '" name="panel_uploadFile" title="' + ((a = title) == null ? "" : a) + '" class="panelSendForm" target="panel_uploadFilIframe" action="" method="POST" enctype="multipart/form-data">\r\n    <a href="#" hidefocus="true" class="panel_sendFileButton" title="' + ((a = title) == null ? "" : a) + '">\r\n        <input id="upload_file_' + ((a = id) == null ? "" : a) + '" class="file_input" name="file" type="file">\r\n    </a>\r\n</form>';
        return b
    }
});
define("mq.view.chat", ["tmpl!../tmpl/tmpl_chat_footer.html", "tmpl!../tmpl/tmpl_chat_list.html", "tmpl!../tmpl/tmpl_chat_tools.html", "tmpl!../tmpl/tmpl_chat_sendfile.html", "./mq.i18n", "./mq.view.transitionmanager"], function(g, a) {
    J.$package("mq.view.chat", function(b) {
        var c = this, e = JM.event, j = JM.dom, f = JM.string, n = mq.i18n.message;
        $F = mq.i18n.faceText;
        var m = null, r = null, k = false, d, t, B, z, q, w = {group: [{text: n("group_member"),cmd: "viewMembers"}, {text: n("group_profile"),cmd: "viewInfo"}, {text: n("record"),cmd: "viewRecord"}],
            discuss: [{text: n("discuss_member"),cmd: "viewMembers"}, {text: n("discuss_profile"),cmd: "viewInfo"}, {text: n("record"),cmd: "viewRecord"}],friend: [{text: n("qzone"),cmd: "viewQzone"}, {text: n("profile"),cmd: "viewInfo"}, {text: n("record"),cmd: "viewRecord"}]};
        this.createPanel = function() {
            if (!this.panel) {
                var p = {parent: mq.view.main.container,className: "chat-panel",leftButton: {className: "btn_setting",text: ""},rightButton: {className: "btn_setting",text: n("close")},body: {className: "chat_container"},footer: {className: "chat_toolbar_footer",
                        html: g({$F: $F,$M: n})}};
                this.panel = new mq.view.TitlePanel(p);
                this.scroll = new iScroll(this.panel.bodyWrapper);
                this.lazyload = MUI.I_LazyLoadImgs({scrollObj: this.scroll,isFade: true});
                d = this.chatTextarea = MUI.AutoGrowTextarea({id: "chat_textarea",maxHeight: 80,initHeight: 32});
                e.bindCommands(c.panel.container, C);
                e.on(d, "heightChange", h.onTextAreaHeightChange);
                e.on(d, "keydown", h.onTextKeydown);
                e.on(j.id("add_face_btn"), b.platform.touchDevice ? "tap" : "click", h.onClickFace);
                e.on(c.lazyload, "loadImgOver", h.onLoadImgOver)
            }
            return this.panel
        };
        this.setPannelMenu = function() {
            var p = w[m.type];
            p && this.panel.setMenuItems(p);
            B = j.id("upload_file_sendFile");
            t = j.id("panel_uploadFile_sendFile");
            B && e.on(B, "change", this.uploadSendFile)
        };
        this.init = function() {
            this.main_view = mq.main;
            this.model = mq.model.chat;
            this.m_model = mq.model.buddylist;
            this.presenter = mq.presenter.chat
        };
        var C = {sendMsg: function() {
                var p = d.getContent();
                if (p != "") {
                    d.setContent("");
                    d.reset();
                    e.fire(c, "sendMessage", {textContent: p})
                }
            },clickLeftButton: function() {
                c.panel.toggleMenuList()
            },clickRightButton: function() {
                m =
                null;
                mq.view.transitionManager.pop("chat");
                e.fire(c, "close")
            },chooseFace: function(p, y, F) {
                e.fire(c, "chooseFace", F)
            },viewQzone: function() {
                if (m.ruin) {
                    window.open("http://user.qzone.qq.com/" + m.ruin, "_blank");
                    c.panel.toggleMenuList()
                }
            },viewInfo: function() {
                e.fire(mq.view, "viewProfile", {from: m.name,account: m.account,type: m.type});
                c.panel.toggleMenuList()
            },viewRecord: function() {
                e.fire(mq.view, "viewRecord", {user: m});
                c.panel.toggleMenuList()
            },viewMembers: function() {
                var p = m.type == "group" ? "viewGroupMember" : "viewDiscussMember",
                y = {};
                y[m.type] = m;
                e.fire(mq.view, p, y);
                c.panel.toggleMenuList()
            },sendPicture: function() {
                c.panel.hideMenuList()
            },sendFile: function() {
                c.panel.hideMenuList()
            },agreeFile: function(p, y) {
                var F = y.getAttribute("_fileid");
                e.fire(c, "agreeReceiveFile", F)
            },refuseFile: function(p, y) {
                var F = y.getAttribute("_fileid");
                e.fire(c, "refuseReceiveFile", F)
            },agreeOfflineFile: function(p, y) {
                var F = y.getAttribute("_fileid");
                e.fire(c, "agreeOfflineFile", F)
            },nextOfflineFile: function(p, y) {
                var F = y.getAttribute("_fileid");
                e.fire(c, "nextOfflineFile",
                F)
            },refuseOfflineFile: function(p, y) {
                var F = y.getAttribute("_fileid");
                e.fire(c, "refuseOfflineFile", F)
            }}, h = {onTextAreaHeightChange: function() {
                var p = j.getStyle(c.panel.footer, "height");
                j.setStyle(c.panel.bodyWrapper, "bottom", p);
                c.scroll.refresh()
            },onClickFace: function() {
                z = j.id("face_images");
                if (z.style.display == "none") {
                    z.style.display = "block";
                    j.addClass(c.panel.bodyWrapper, "panelShowFace");
                    c.scroll.refresh();
                    c.scroll.scrollTo(0, c.scroll.maxScrollY, 0);
                    if (k)
                        q && q.refresh();
                    else {
                        k = true;
                        q = MUI.ImageChange({id: "face_images",
                            canSwipe: true})
                    }
                } else {
                    z.style.display = "none";
                    var p = j.getStyle(c.panel.footer, "height");
                    j.setStyle(c.panel.bodyWrapper, "bottom", p);
                    j.removeClass(c.panel.bodyWrapper, "panelShowFace");
                    c.scroll.refresh()
                }
            },onTextKeydown: function(p) {
                var y = d.getContent(), F = function() {
                    if (p.ctrlKey && p.keyCode == 13) {
                        p.preventDefault();
                        d.setContent(y + "\n");
                        return false
                    }
                    if (p.keyCode == 13) {
                        p.preventDefault();
                        if (y != "") {
                            C.sendMsg();
                            return false
                        }
                    }
                };
                if (b.platform.touchDevice)
                    F();
                else if (mq.setting.enableCtrlEnter) {
                    if (p.ctrlKey && p.keyCode ==
                    13) {
                        p.preventDefault();
                        y != "" && C.sendMsg();
                        return false
                    }
                    if (p.keyCode == 13) {
                        p.preventDefault();
                        d.setContent(y + "\n");
                        return false
                    }
                } else
                    F()
            },onLoadImgOver: function() {
                c.scroll.refresh()
            }}, o = function(p) {
            return p.replace(/\n\r|\r\n|\r|\n/g, "<br/>")
        }, v = function(p, y) {
            return Math.abs(p - y) < 12E4
        }, D = function(p) {
            p = new Date(p);
            var y = new Date;
            return p.getFullYear() === y.getFullYear() && p.getMonth() === y.getMonth() && p.getDate() === y.getDate() ? b.format.date(p, "hh:mm") : b.format.date(p, "YYYY-MM-DD hh:mm")
        };
        this.startChat =
        function(p) {
            if (p) {
                this.createPanel();
                if (z && z.style.display == "block") {
                    z.style.display = "none";
                    d.setContent("");
                    j.removeClass(c.panel.bodyWrapper, "panelShowFace");
                    c.scroll.refresh()
                }
                if (!(m && m.type === p.type && m.account === p.account)) {
                    m = p;
                    r = null;
                    c.panel.setTitle(p.name);
                    c.panel.body.innerHTML = "";
                    d.setContent("");
                    c.scroll.refresh();
                    c.presenter.initChatMessage(p)
                }
                this.setPannelMenu();
                mq.view.transitionManager.push({id: "chat",element: this.panel.container,callback: function() {
                        c.scroll.refresh();
                        d.reset();
                        c.scroll.scrollTo(0,
                        c.scroll.maxScrollY, 0)
                    }});
                b.platform.touchDevice || setTimeout(function() {
                    d.elem.focus()
                }, 200);
                e.fire(c, "startChat", p)
            }
        };
        this.appendMessage = function(p) {
            var y = a({selfUin: this.m_model.getSelfUin(),list: p,html: f.encodeHtml,translate: o,lastMessage: r,isNearTime: v,formatChatTime: D});
            r = p[p.length - 1];
            this.panel.body.innerHTML += y;
            this.scroll.refresh();
            this.scroll.scrollTo(0, this.scroll.maxScrollY, 0);
            !b.platform.touchDevice && d.elem && d.elem.focus()
        };
        this.updateBuddyInfo = function(p) {
            var y, F = this.panel.body.querySelectorAll('div[_sender_uin="' +
            p.account + '"]');
            if (F.length)
                for (var H = 0, M; M = F[H]; H++) {
                    (y = M.querySelector(".chat_content_avatar")) && (y.src = p.avatar);
                    (y = M.querySelector(".chat_nick")) && (y.innerHTML = f.encodeHtml(p.name));
                    M.removeAttribute("_sender_uin")
                }
        };
        this.getFileSize = function(p) {
            var y = new Image, F = p.value, H = 0;
            try {
                y.dynsrc = F
            } catch (M) {
                return 0
            }
            try {
                H = y.fileSize || 0
            } catch (P) {
            }
            if (H == 0)
                try {
                    H = p.files[0].fileSize
                } catch (E) {
                }
            return H
        };
        this.uploadSendFile = function() {
            var p = "";
            p = B.value;
            if (p == "")
                alert("\u8bf7\u9009\u62e9\u6587\u4ef6!");
            else if (c.getFileSize(B) >
            10485760) {
                alert("\u6587\u4ef6\u5927\u5c0f\u8d85\u51fa10M\u9650\u5236!");
                t.reset()
            } else {
                var y = (new Date).getTime() % 4096;
                t.action = mq.FILE_SERVER + "v2/" + mq.model.buddylist.getSelfUin() + "/" + m.account + "/" + y + "/" + mq.index + "/" + mq.port + "/1/f/1/0/0?psessionid=" + mq.psessionid;
                t.submit();
                t.reset();
                e.fire(c, "sendFile", {filename: p,to_uin: m.account,lcid: y})
            }
        };
        this.removeReceiveFileLink = function(p) {
            var y = [], F = j.id("agree_" + p);
            F && y.push(F);
            (F = j.id("refuse_" + p)) && y.push(F);
            (F = j.id("next_" + p)) && y.push(F);
            for (p = 0; F = y[p]; p++) {
                F.style.color =
                "gray";
                F.style.cursor = "default";
                F.removeAttribute("cmd")
            }
        };
        this.receiveFile = function(p) {
            mq.util.download(mq.DYNAMIC_CGI_URL + "channel/get_file2?lcid=" + p.session_id + "&guid=" + p.name + "&to=" + p.from_uin + "&psessionid=" + mq.psessionid + "&count=1&time=" + +new Date + "&clientid=" + mq.clientid)
        };
        this.receiveOfflineFile = function(p) {
            mq.util.download("http://" + p.ip + ":" + p.port + "/" + p.name + "?ver=2173&rkey=" + p.rkey + "&range=0")
        }
    })
});
define("mq.presenter.chat", ["./mq.i18n"], function() {
    J.$package("mq.presenter.chat", function(g) {
        var a = JM.event, b = g.string, c = mq.i18n.message, e = mq.i18n.faceText, j = mq.i18n.getFaceIndex, f = this, n, m, r, k, d = [], t = [], B = [14, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 15, 16, 96, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 89, 113, 114, 115, 60, 61, 46, 63, 64, 116, 66, 67, 53, 54, 55, 56, 57, 117, 59, 75, 74, 69, 49, 76, 77, 78, 79, 118, 119, 120, 121, 122, 123, 124, 42, 85, 43,
            41, 86, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170], z = [14, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 50, 51, 96, 53, 54, 73, 74, 75, 76, 77, 78, 55, 56, 57, 58, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 32, 113, 114, 115, 63, 64, 59, 33, 34, 116, 36, 37, 38, 91, 92, 93, 29, 117, 72, 45, 42, 39, 62, 46, 47, 71, 95, 118, 119, 120, 121, 122, 123, 124, 27, 21, 23, 25, 26, 125, 126, 127,
            128, 129, 130, 131, 132, 133, 134, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170], q = /\[([A-Z\u4e00-\u9fa5]{1,20}?)\]/gi, w = ["font", {name: "\u5b8b\u4f53",size: 10,style: [0, 0, 0],color: "000000"}], C = {onMessageReceived: function(p) {
                var y = p.send_to || p.from_user;
                if (y.isSelf)
                    y = p.to_user;
                if (y && m === "friend" && (y.uin == n || y.uin == r))
                    f.appendMessage([p])
            },onGroupMessageReceived: function(p) {
                var y = p.from_group, F = p.from_user;
                if (y && y.gid ==
                n && m === "group" || F && F.uin == r)
                    f.appendMessage([p])
            },onDiscussMessageReceived: function(p) {
                var y = p.from_discuss, F = p.from_user;
                if (y && y.did == n && m === "discuss" || F && F.uin == r)
                    f.appendMessage([p])
            },onLoginSuccess: function(p) {
                r = p.selfUin
            },onStartChat: function(p) {
                var y;
                y = p.type;
                p = p.uin;
                var F = mq.model.buddylist;
                if (y == "friend") {
                    F.sendGetFriendUin(p);
                    var H = F.getFriendByUin(p);
                    H.isStrange && f.model.sendGetSessionSignature({to_uin: p,group_uin: H.groupUin,discuss_uin: H.discussUin})
                }
                y = F.getBuddyInfo(p, y);
                n = y.uin || y.did ||
                y.gid;
                m = y.type;
                f.view.startChat(y)
            },onSendMessage: function(p) {
                if (mq.main.isOnline()) {
                    var y = f.model, F = mq.model.buddylist, H = F.getSelfUin(), M = F.getSelfInfo(), P = f.getCurrentChatUin(), E = f.getCurrentChatType(), G = p.textContent;
                    G = G.replace(q, "@#[$1]@# ");
                    d = G.split("@#");
                    p = d.length;
                    if (p > 1) {
                        for (G = 0; G < p; G++) {
                            d[G] == "" && d.splice(G, G + 1);
                            if (q.test(d[G])) {
                                var O = d[G].replace("[", "").replace("]", "");
                                if ((k = z[j(O)]) || k === 0)
                                    d[G] = ["face", k]
                            }
                        }
                        d.push(w)
                    } else
                        d = [G, w];
                    p = JSON.stringify(d);
                    H = {notNotify: true,content: d,from_uin: H,
                        sender_uin: H,from_user: M,sender: M,to_uin: P,to_type: E,time: Date.now()};
                    if (E == "friend") {
                        F.getFriendByUin(P).isStrange ? y.sendSessMsg({to: P,content: p,face: M.face}) : y.sendMsg({to: P,content: p,face: M.face});
                        H.send_to = F.getFriendByUin(P);
                        y.addMessage(P, H)
                    } else if (E == "group") {
                        y.sendGroupMsg({group_uin: P,content: p,face: M.face});
                        H.send_to = F.getGroupByGid(P);
                        y.addGroupMessage(P, H)
                    } else if (E == "discuss") {
                        y.sendDiscussMsg({did: P,content: p,face: M.face});
                        H.send_to = F.getDiscussById(P);
                        y.addDiscussMessage(P, H)
                    }
                } else
                    mq.bubble('\u60a8\u5df2\u7ecf\u79bb\u7ebf\uff0c\u8bf7\u91cd\u65b0<a href="javascript:void(0);" cmd="gotoLogin" title="\u767b\u5f55">\u767b\u5f55</a>')
            },
            onSendFile: function(p) {
                f.model.sendFile(p)
            },onChooseFace: function(p) {
                if (p.target && p.target.title) {
                    var y = mq.view.chat.chatTextarea.getContent();
                    if (p.target.title === "delKey") {
                        var F = y.length;
                        if (y.charAt(F - 1) === "]" && F >= 3) {
                            var H = y.substring(F - 20, F);
                            p = y.substring(0, F - 20);
                            H = H.replace(q, "@#[$1]@#");
                            t = H.split("@#");
                            H = t.length;
                            if (H > 1 && t[H - 1] == "") {
                                var M = H - 2;
                                if (q.test(t[M])) {
                                    var P = t[M].replace("[", "").replace("]", "");
                                    k = z[j(P)];
                                    if (k >= 0) {
                                        t.splice(M, M + 1);
                                        y = "";
                                        for (F = 0; F < H - 1; F++)
                                            if (t[F])
                                                y += t[F];
                                        mq.view.chat.chatTextarea.setContent(p +
                                        y);
                                        return
                                    }
                                }
                            }
                        }
                        p = y.substring(0, F - 1);
                        mq.view.chat.chatTextarea.setContent(p)
                    } else
                        mq.view.chat.chatTextarea.setContent(y + "[" + p.target.title + "]")
                }
            },onBuddyInfoUpdate: function(p) {
                p.account === n && p.type === m && p.members && p.members.forEach(function(y) {
                    f.view.updateBuddyInfo(y)
                })
            },onClose: function() {
                m = n = null
            },onAgreeReceiveFile: function(p) {
                var y = f.model.getFilesList()[p];
                y.isread = true;
                f.view.removeReceiveFileLink(p);
                f.view.receiveFile(y);
                f.model.agreeReceiveFile(y)
            },onRefuseReceiveFile: function(p) {
                var y = f.model.getFilesList();
                y[p].isread = true;
                f.view.removeReceiveFileLink(p);
                f.model.refuseReceiveFile(y[p])
            },onAgreeOfflineFile: function(p) {
                var y = f.model.getFilesList()[p];
                y.isread = true;
                f.view.removeReceiveFileLink(p);
                f.view.receiveOfflineFile(y);
                f.model.agreeReceiveFile(y)
            },onNextOfflineFile: function(p) {
                f.model.getFilesList()[p].isread = true;
                f.view.removeReceiveFileLink(p)
            },onRefuseOfflineFile: function(p) {
                var y = f.model.getFilesList()[p];
                y.isread = true;
                f.view.removeReceiveFileLink(p);
                f.model.refuseOfflineFile(y)
            }};
        this.init =
        function() {
            this.view = mq.view.chat;
            this.model = mq.model.chat;
            h()
        };
        var h = function() {
            var p = f.model;
            a.on(p, "messageReceived", C.onMessageReceived);
            a.on(p, "groupMessageReceived", C.onGroupMessageReceived);
            a.on(p, "discussMessageReceived", C.onDiscussMessageReceived);
            a.on(mq.main, "loginSuccess", C.onLoginSuccess, this);
            a.on(mq.view, "startChat", C.onStartChat);
            a.on(mq.view.chat, "sendMessage", C.onSendMessage);
            a.on(mq.view.chat, "sendFile", C.onSendFile);
            a.on(mq.view.chat, "chooseFace", C.onChooseFace);
            a.on(mq.view.chat,
            "close", C.onClose);
            a.on(mq.view.chat, "agreeReceiveFile", C.onAgreeReceiveFile);
            a.on(mq.view.chat, "refuseReceiveFile", C.onRefuseReceiveFile);
            a.on(mq.view.chat, "agreeOfflineFile", C.onAgreeOfflineFile);
            a.on(mq.view.chat, "nextOfflineFile", C.onNextOfflineFile);
            a.on(mq.view.chat, "refuseOfflineFile", C.onRefuseOfflineFile);
            a.on(mq.model.buddylist, "groupInfoUpdate", C.onBuddyInfoUpdate);
            a.on(mq.model.buddylist, "discussInfoUpdate", C.onBuddyInfoUpdate)
        };
        this.getCurrentChatUin = function() {
            return n
        };
        this.getCurrentChatType =
        function() {
            return m
        };
        this.isChating = function(p) {
            return p && p.account == n && p.type == m
        };
        this.initChatMessage = function(p) {
            (p = f.model.getMessages(p.account, p.type)) && this.appendMessage(p)
        };
        this.appendMessage = function(p) {
            p = this.translateMessages(p);
            this.view.appendMessage(p)
        };
        this.translateMessages = function(p) {
            for (var y = 0, F; F = p[y]; y++)
                if (F.content) {
                    if (!F.sender)
                        F.sender = mq.model.buddylist.getFriendByUin(F.sender_uin);
                    F.htmlContent = this.translateMessage(F)
                }
            return p
        };
        this.translateMessage = function(p) {
            for (var y =
            p.content, F = p.from_uin, H = !F || F == mq.model.buddylist.getSelfUin(), M = [], P = 0, E; E = y[P]; P++)
                if (g.type.isArray(E))
                    switch (E[0]) {
                        case "font":
                            break;
                        case "face":
                            E = z.indexOf(E[1]);
                            M.push('<img class="EQQ_faceImg" src="http://pub.idqqimg.com/lib/qqface/' + B[E] + '.gif" width="24px" height="24px">');
                            break;
                        case "cface":
                            M.push("[\u81ea\u5b9a\u4e49\u8868\u60c5]");
                            break;
                        case "offpic":
                            M.push('<img rdata="offpic" src="/css/image/img_loading.gif" _ori_src="http://w.qq.com/d/channel/get_offpic2?file_path=' + encodeURIComponent(E[1].file_path) +
                            "&f_uin=" + F + "&clientid=" + mq.clientid + "&psessionid=" + mq.psessionid + '" title="\u81ea\u5b9a\u4e49\u8868\u60c5\u56fe\u7247" style="max-width:100%" />');
                            break;
                        case "sendfile":
                            M.push('<span class="icon icon_info"></span>\u60a8\u53d1\u9001\u6587\u4ef6"' + b.encodeHtml(E[1]) + '"\u7ed9\u5bf9\u65b9\u3002');
                            break;
                        case "transtimeout":
                            M.push('<span class="icon icon_err"></span>\u63a5\u6536\u6587\u4ef6"' + b.encodeHtml(E[1]) + '"\u8d85\u65f6\uff0c\u6587\u4ef6\u4f20\u8f93\u5931\u8d25\u3002');
                            break;
                        case "refusedbyclient":
                            M.push('<span class="icon icon_err"></span>\u5bf9\u65b9\u53d6\u6d88\u4e86\u63a5\u6536\u6587\u4ef6"' +
                            b.encodeHtml(E[1]) + '"\uff0c\u6587\u4ef6\u4f20\u8f93\u5931\u8d25\u3002');
                            break;
                        case "transok":
                            M.push('<span class="icon icon_succ"></span>\u6587\u4ef6"' + b.encodeHtml(E[1]) + '"\u4f20\u8f93\u6210\u529f\u3002');
                            break;
                        case "transerror":
                            M.push('<span class="icon icon_err"></span>\u5bf9\u65b9\u53d6\u6d88\u4e86\u63a5\u6536\u6587\u4ef6"' + b.encodeHtml(E[1]) + '"\u6216\u4f20\u8f93\u9519\u8bef\uff0c\u6587\u4ef6\u4f20\u8f93\u5931\u8d25\u3002');
                            break;
                        case "rffile":
                            H ? M.push('<span class="icon icon_err"></span>\u60a8\u62d2\u7edd\u63a5\u6536"' +
                            b.encodeHtml(E[1]) + '"\uff0c\u6587\u4ef6\u4f20\u8f93\u5931\u8d25\u3002') : M.push('<span class="icon icon_err"></span>\u5bf9\u65b9\u53d6\u6d88\u4e86\u63a5\u6536\u6587\u4ef6"' + b.encodeHtml(E[1]) + '"\uff0c\u6587\u4ef6\u4f20\u8f93\u5931\u8d25\u3002');
                            break;
                        case "agfile":
                            M.push('<span class="icon icon_info"></span>\u60a8\u540c\u610f\u4e86\u63a5\u6536\u6587\u4ef6"' + b.encodeHtml(E[1]) + '"\u3002');
                            break;
                        case "rtfile":
                            M.push('<span class="icon icon_err"></span>\u63a5\u6536\u6587\u4ef6"' + b.encodeHtml(E[1]) + '"\u8d85\u65f6\uff0c\u6587\u4ef6\u4f20\u8f93\u5931\u8d25\u3002');
                            break;
                        case "wrfile":
                            M.push('<span class="icon icon_info"></span>\u5bf9\u65b9\u5df2\u540c\u610f\u63a5\u6536"' + b.encodeHtml(E[1]) + '"\uff0c\u5f00\u59cb\u4f20\u8f93\u6587\u4ef6\u3002');
                            break;
                        case "wrffile":
                            M.push('<span class="icon icon_err"></span>\u5bf9\u65b9\u62d2\u7edd\u4e86\u63a5\u6536\u6587\u4ef6"' + b.encodeHtml(E[1]) + '"\uff0c\u6587\u4ef6\u4f20\u8f93\u5931\u8d25\u3002');
                            break;
                        case "rfile":
                            M.push(v(p));
                            break;
                        case "offfile":
                            M.push(D(p));
                            break;
                        case "sendofffile":
                        case "sendofffileerror":
                        case "refuseofffile":
                        case "nextofffile":
                        case "canceloffupload":
                        case "notifyagreeofffile":
                        case "notifyrefuseofffile":
                            M.push(b.encodeHtml(E[1]));
                            break;
                        default:
                            M.push(b.encodeHtml(E[1]))
                    }
                else {
                    E = b.encodeHtml(E);
                    M.push(E)
                }
            return M.join("")
        };
        this.translateMessage2Text = function(p) {
            p = p.content;
            var y = [], F, H;
            for (F = 0; H = p[F]; ++F)
                if (g.type.isArray(H))
                    switch (H[0]) {
                        case "face":
                            y.push("[" + e(z.indexOf(H[1])) + "]");
                            break;
                        case "cface":
                        case "offpic":
                            y.push("[" + c("cface") + "]")
                    }
                else
                    g.type.isString(H) && y.push(b.encodeHtml(H));
            return y.join("")
        };
        var o = function(p) {
            if (!(typeof p == "undefined" || p == "")) {
                p = p.split(".");
                p = p[p.length - 1].toLowerCase();
                switch (p) {
                    case "excel":
                    case "xls":
                    case "xlsx":
                        p =
                        "excel";
                        break;
                    case "doc":
                    case "docx":
                        p = "word";
                        break;
                    case "ppt":
                    case "pptx":
                        p = "ppt";
                        break;
                    case "bmp":
                    case "png":
                    case "gif":
                    case "jpeg":
                    case "jpg":
                    case "ico":
                        p = "pic";
                        break;
                    case "tga":
                    case "tif":
                    case "psd":
                    case "tiff":
                        p = "pic";
                        break;
                    case "mov":
                    case "avi":
                    case "mpeg":
                    case "mpg":
                    case "ra":
                    case "rm":
                    case "rmvb":
                    case "qt":
                    case "asf":
                    case "wmv":
                    case "swf":
                    case "flv":
                    case "mp4":
                        p = "media";
                        break;
                    case "mp3":
                    case "wav":
                    case "mid":
                        p = "music";
                        break;
                    case "arj":
                    case "rar":
                    case "zip":
                    case "jar":
                    case "7z":
                    case "tar":
                    case "uc2":
                    case "gz":
                    case "lha":
                    case "ace":
                    case "tgz":
                        p =
                        "rar-zip";
                        break;
                    case "txt":
                    case "text":
                        p = "share-txt";
                        break;
                    case "pdf":
                        p = "pdf16";
                        break;
                    case "com":
                        p = "exe16";
                        break;
                    default:
                        p = "others"
                }
                return p
            }
        }, v = function(p) {
            var y = p.content[0];
            p = p.from_uin + "_" + y[2];
            var F = mq.model.chat.getFilesList();
            html = '<span class="icon icon_info" ></span>\u5bf9\u65b9\u7ed9\u60a8\u53d1\u9001\u6587\u4ef6: <br/><span class="file_icon icon_' + o(y[1]) + '">&nbsp;</span>' + b.encodeHtml(y[1]) + '<span class="fileAct">';
            if (F[p].isread)
                html += "&nbsp;[\u540c\u610f][\u62d2\u7edd]";
            else {
                html += '&nbsp;<span class="fileLink" id="agree_' +
                p + '" _fileid="' + p + '" cmd="agreeFile" >[\u540c\u610f]</span>';
                html += '&nbsp;<span class="fileLink" id="refuse_' + p + '" _fileid="' + p + '" cmd="refuseFile">[\u62d2\u7edd]</span>'
            }
            html += "</span>";
            return html
        }, D = function(p) {
            var y = p.attach.from_uin + "_" + p.attach.msg_id, F = g.format.date(new Date(p.attach.expire_time * 1E3), "YYYY-MM-DD"), H = '<span class="icon icon_info" ></span>\u5bf9\u65b9\u7ed9\u60a8\u53d1\u9001\u79bb\u7ebf\u6587\u4ef6:<br />';
            H += '<span class="file_icon icon_' + o(p.attach.name) + '">&nbsp;</span>' +
            b.encodeHtml(p.attach.name) + "(" + F + '\u5230\u671f)<span class="fileAct">';
            H += '&nbsp;<span class="fileLink" id="agree_' + y + '" _fileid="' + y + '" cmd="agreeOfflineFile">[\u63a5\u6536]</span>';
            H += '&nbsp;<span class="fileLink" id="next_' + y + '" _fileid="' + y + '" cmd="nextOfflineFile">[\u4e0b\u6b21\u63a5\u6536]</span>';
            H += '&nbsp;<span class="fileLink" id="refuse_' + y + '" _fileid="' + y + '" cmd="refuseOfflineFile" >[\u62d2\u7edd]</span>';
            H += "</span>";
            return H
        }
    })
});
define("mq.presenter.search", ["./mq.i18n", "./mq.view.transitionmanager"], function() {
    J.$package("mq.presenter.search", function() {
        var g = this, a = JM.event;
        this.init = function() {
            this.view = mq.view.search;
            this.model = mq.model.buddylist;
            a.on(mq.view, "startSearch", b.onStartSearch);
            a.on(g.view, "searchFriends", b.onSearchFriends)
        };
        var b = {onStartSearch: function(c) {
                g.view.startSearch(c)
            },onSearchFriends: function(c) {
                c = g.model.searchFriends(c.keyword);
                g.view.renderResult({type: "list",list: c})
            }}
    })
});
define("tmpl!../tmpl/tmpl_search_body.html", [], function() {
    return function(g) {
        var a, b = "";
        with (g || {})
            b += '<div id="searchBar" class="search_wrapper">\r\n    <div class="search_inner">\r\n        <input id="searchInput" type="text" class="searchInput" placeholder="' + ((a = $M("search")) == null ? "" : a) + '" autocapitalize="off" />\r\n        <button id="searchClear" class="searchClear" cmd="clearSearchWord"></button>\r\n    </div>\r\n    <button id="searchCancel" class="searchCancel" cmd="clearSearchWord">' + ((a =
            $M("cancel")) == null ? "" : a) + '</button>\r\n</div>\r\n<div id="search_container_scroll_area" class="scrollWrapper search">\r\n    <div id="search_container" class="search_container">\r\n        <ul id="search_result_list" class="list list_white catogory_List">\r\n        </ul>\r\n    </div>\r\n</div>';
        return b
    }
});
define("tmpl!../tmpl/tmpl_member_list.html", [], function() {
    return function(g) {
        var a, b = "";
        with (g || {}) {
            b += "";
            g = 0;
            var c;
            b += "\r\n";
            if (type === "category") {
                b += "\r\n";
                for (g = 0; c = list[g]; g++)
                    b += '\r\n<li class="list_group">\r\n    <div id="groupTitle-' + ((a = c.index) == null ? "" : a) + '" class="list_group_title list_group_white_title list_arrow_right" cmd="clickMemberGroup" param="' + ((a = c.index) == null ? "" : a) + '">\r\n        <span>' + ((a = html(c.name)) == null ? "" : a) + '</span>\r\n        <span class="onlinePercent"></span>\r\n    </div>\r\n    <ul id="groupBodyUl-' +
                    ((a = c.index) == null ? "" : a) + '" class="list_group_body list list_white catogory_List"></ul>\r\n</li>\r\n';
                b += "\r\n"
            } else if (type === "list") {
                b += "\r\n";
                for (g = 0; c = list[g]; g++) {
                    b += '\r\n<li id="' + ((a = prefix ? prefix + "-" : "") == null ? "" : a) + "item-" + ((a = c.type + "-" + c.account) == null ? "" : a) + '" class="list_item" _uin="' + ((a = c.account) == null ? "" : a) + '" _type="' + ((a = c.type) == null ? "" : a) + '" cmd="clickMemberItem">\r\n    <a href="javascript:void(0);" class="avatar" cmd="clickMemberAvatar" _uin="' + ((a = c.account) == null ? "" : a) + '" _type="' +
                    ((a = c.type) == null ? "" : a) + '"><img  src="/css/image/avatar_default_40_40.gif" _ori_src="' + ((a = c.avatar) == null ? "" : a) + '" >\r\n        ';
                    if (c.mask)
                        b += '\r\n        <span class="group_mask" />\r\n        ';
                    b += '\r\n    </a>\r\n    <p class="member_nick" id="userNick-' + ((a = c.account) == null ? "" : a) + '">\r\n    ';
                    b += c.mark ? "\r\n        " + ((a = html(c.mark)) == null ? "" : a) + "<span>(" + ((a = html(c.name)) == null ? "" : a) + ")</span>\r\n    " : c.cardName ? "\r\n        " + ((a = html(c.cardName)) == null ? "" : a) + " <span> (" + ((a = html(c.name)) ==
                    null ? "" : a) + ")</span>\r\n    " : "\r\n        " + ((a = html(c.name)) == null ? "" : a) + "\r\n    ";
                    b += "\r\n    </p>\r\n    ";
                    if (typeof dataType != "undefined" && dataType === "recent")
                        b += '\r\n    <p id="recent-item-' + ((a = c.type) == null ? "" : a) + "-" + ((a = c.account) == null ? "" : a) + '-msg" class="member_msg text_ellipsis">' + ((a = c.recentMessage || "") == null ? "" : a) + "</p>\t\r\n    ";
                    else if (typeof dataType == "undefined" || dataType != "search") {
                        b += '\r\n    <p class="member_msg text_ellipsis" >\r\n    ';
                        if (c.stateName)
                            b += '\r\n    <span class="member_state">' +
                            ((a = c.stateName) == null ? "" : a) + "</span>\r\n    ";
                        b += "\r\n    ";
                        if (c.signature)
                            b += '\r\n    <span class="member_signature" _signature_load="1">' + ((a = html(c.signature)) == null ? "" : a) + "</span>\r\n    ";
                        b += "\t\r\n    </p>\r\n    "
                    }
                    b += "\t\r\n\r\n    </li>\r\n    "
                }
                b += "\r\n    "
            }
            b += "\r\n\r\n"
        }
        return b
    }
});
define("mq.view.search", ["tmpl!../tmpl/tmpl_search_body.html", "tmpl!../tmpl/tmpl_member_list.html", "./mq.i18n", "./mq.view.transitionmanager"], function(g, a) {
    J.$package("mq.view.search", function() {
        var b = this, c = JM.event, e = JM.dom, j = mq.i18n.message;
        this.createPanel = function() {
            if (!this.panel) {
                var m = {parent: mq.view.main.container,className: "search-panel",title: j("search"),hasBackButton: true,body: {html: g({$M: j})}};
                this.panel = new mq.view.TitlePanel(m);
                this.searchBar = e.id("searchBar");
                this.searchInput = e.id("searchInput");
                m = this.scrollArea = e.id("search_container_scroll_area");
                this.memberList = new mq.view.MemberList({id: "search",scrollArea: m,listContainer: e.id("search_result_list"),listTmpl: a});
                c.bindCommands(b.panel.container, f);
                c.on(b.searchInput, "input", n.onSearchInput)
            }
            return this.panel
        };
        this.init = function() {
        };
        var f = {clickMemberItem: function(m, r) {
                var k = r.getAttribute("_uin"), d = r.getAttribute("_type");
                c.fire(mq.view, "startChat", {uin: k,type: d})
            },clickLeftButton: function() {
                mq.view.transitionManager.pop("search")
            },clearSearchWord: function() {
                b.searchInput.value =
                "";
                e.removeClass(b.searchBar, "hascontent")
            }}, n = {onSearchInput: function() {
                if (b.searchInput.value != "")
                    e.hasClass(b.searchBar, "hascontent") || e.addClass(b.searchBar, "hascontent");
                else
                    e.removeClass(b.searchBar, "hascontent");
                c.fire(b, "searchFriends", {keyword: b.searchInput.value})
            }};
        this.startSearch = function(m) {
            var r = this.createPanel();
            m = m.from || j("return");
            r.setLeftText(m);
            mq.view.transitionManager.push({id: "search",element: r.container,callback: null})
        };
        this.renderResult = function(m) {
            this.memberList.render(m)
        }
    })
});
define("mq.presenter.profile", ["./mq.i18n", "./mq.view.transitionmanager"], function() {
    J.$package("mq.presenter.profile", function() {
        var g = this, a = JM.event, b = null;
        this.init = function() {
            this.view = mq.view.profile;
            this.model = mq.model.buddylist;
            a.on(mq.view, "viewProfile", c.onViewProfile);
            a.on(g.view, "dismiss", c.onDismiss);
            a.on(g.model, "friendInfoUpdate", c.onBuddyInfoUpdate);
            a.on(g.model, "discussInfoUpdate", c.onBuddyInfoUpdate);
            a.on(g.model, "groupInfoUpdate", c.onBuddyInfoUpdate);
            a.on(g.model, "userSignatureChange",
            c.onUserSignatureChange)
        };
        var c = {onViewProfile: function(e) {
                var j = g.model.getBuddyInfo(e.account, e.type);
                b = e.profile = j;
                g.view.viewProfile(e)
            },onBuddyInfoUpdate: function(e) {
                if (b && b.type === e.type && b.account === e.account) {
                    b = e;
                    g.view.refreshProfile(e)
                }
            },onUserSignatureChange: function(e) {
                c.onBuddyInfoUpdate({info: e})
            },onDismiss: function() {
                b = null
            }}
    })
});
define("tmpl!../tmpl/tmpl_profile_body.html", [], function() {
    return function(g) {
        var a, b = "";
        with (g || {}) {
            b += '\r\n<div class="group">\r\n    <div class="row clearfix">\r\n        <div class="cloumn">\r\n            <img class="avatar" src="' + ((a = profile.avatar) == null ? "" : a) + '">\r\n        </div>\r\n        <div class="cloumn profile_title">\r\n            <div class="row profile_name">' + ((a = encode(profile.name)) == null ? "" : a) + '</div>\r\n            <div class="row profile_account">' + ((a = profile.ruin ? profile.ruin :
            "") == null ? "" : a) + "</div>\r\n        </div>\r\n        ";
            if (profile.type === "friend")
                b += '\r\n        <button class="sendMsg2Member" cmd="sendMsg2Member">' + ((a = $M("sendMsg")) == null ? "" : a) + "</button>\r\n        ";
            b += "\r\n    </div>\r\n</div>\r\n";
            if (profile.type === "friend") {
                b += "\r\n    ";
                if (profile.signature)
                    b += '\r\n<div class="group">\r\n    <div class="row profile_signature">\r\n        <span class="label">' + ((a = $M("signature")) == null ? "" : a) + '</span><p class="row-content">' + ((a = encode(profile.signature)) ==
                    null ? "" : a) + "</p>\r\n    </div>\r\n</div>\r\n    ";
                b += '\r\n<div class="group">\r\n    ';
                if (profile.gender) {
                    b += '\r\n    <div class="row ">\r\n        <span class="label">' + ((a = $M("gender")) == null ? "" : a) + "</span>";
                    b += profile.gender === "male" ? "" + ((a = $M("male")) == null ? "" : a) + "" : profile.gender === "female" ? "" + ((a = $M("female")) == null ? "" : a) + "" : "" + ((a = $M("unknown")) == null ? "" : a) + "";
                    b += "\r\n    </div>\r\n    "
                }
                b += "\r\n    ";
                if (profile.birthday) {
                    g = profile.birthday;
                    b += '\r\n    <div class="row ">\r\n        <span class="label">' +
                    ((a = $M("birthday")) == null ? "" : a) + "</span>" + ((a = g.year + "/" + g.month + "/" + g.day) == null ? "" : a) + "\r\n    </div>\r\n    "
                }
                b += '\r\n</div>\r\n<div class="group">\r\n    ';
                if (profile.country)
                    b += '\r\n    <div class="row ">\r\n        <span class="label">' + ((a = $M("country")) == null ? "" : a) + "</span>" + ((a = encode(profile.country)) == null ? "" : a) + "\r\n    </div>\r\n    ";
                b += "\r\n    ";
                if (profile.province)
                    b += '\r\n    <div class="row ">\r\n        <span class="label">' + ((a = $M("province")) == null ? "" : a) + "</span>" + ((a = encode(profile.province)) ==
                    null ? "" : a) + "\r\n    </div>\r\n    ";
                b += "\r\n    ";
                if (profile.city)
                    b += '\r\n    <div class="row ">\r\n        <span class="label">' + ((a = $M("city")) == null ? "" : a) + "</span>" + ((a = encode(profile.city)) == null ? "" : a) + "\r\n    </div>\r\n    ";
                b += '\r\n</div>\r\n<div class="group">\r\n    ';
                if (profile.phone)
                    b += '\r\n    <div class="row ">\r\n        <span class="label">' + ((a = $M("phone")) == null ? "" : a) + "</span>" + ((a = encode(profile.phone + "")) == null ? "" : a) + "\r\n    </div>\r\n    ";
                b += "\r\n    ";
                if (profile.mobile)
                    b += '\r\n    <div class="row ">\r\n        <span class="label">' +
                    ((a = $M("mobile")) == null ? "" : a) + "</span>" + ((a = encode(profile.mobile + "")) == null ? "" : a) + "\r\n    </div>\r\n    ";
                b += "\r\n    ";
                if (profile.email)
                    b += '\r\n    <div class="row ">\r\n        <span class="label">' + ((a = $M("email")) == null ? "" : a) + "</span>" + ((a = encode(profile.email)) == null ? "" : a) + "\r\n    </div>\r\n    ";
                b += "\r\n</div>\r\n"
            }
            b += "\r\n";
            if (profile.type === "group") {
                b += "\r\n";
                if (profile.memo)
                    b += '\r\n<div class="group">\r\n    <div class="row ">\r\n        <span class="label">' + ((a = $M("publish")) == null ?
                    "" : a) + '</span><p class="row-content">' + ((a = encode(profile.memo)) == null ? "" : a) + "</p>\r\n    </div>\r\n</div>\r\n";
                b += '\r\n<div class="group clickable">\r\n    <div class="row clearfix" cmd="viewGroupMember">\r\n        <span class="label">' + ((a = $M("group_member")) == null ? "" : a) + '</span><span class="more_icon"></span><span class="text_right">' + ((a = profile.members.length + $M("buddy_unit")) == null ? "" : a) + "</span>\r\n    </div>\r\n</div>\r\n"
            }
            b += "\r\n";
            if (profile.type === "discuss")
                b += '\r\n<div class="group clickable">\r\n    <div class="row clearfix" cmd="viewDiscussMember">\r\n        <span class="label">' +
                ((a = $M("discuss_member")) == null ? "" : a) + '</span><span class="more_icon"></span><span class="text_right">' + ((a = profile.members.length + $M("buddy_unit")) == null ? "" : a) + "</span>\r\n    </div>\r\n</div>\r\n";
            b += "\r\n"
        }
        return b
    }
});
define("mq.view.profile", ["tmpl!../tmpl/tmpl_profile_body.html", "./mq.i18n", "./mq.view.transitionmanager"], function(g) {
    J.$package("mq.view.profile", function() {
        var a = this, b = JM.event, c = JM.dom, e = JM.string, j = mq.i18n.message, f = window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || window.oRequestAnimationFrame || window.msRequestAnimationFrame || function(r) {
            window.setTimeout(r, 1E3 / 60)
        }, n = null;
        this.createPanel = function() {
            if (!this.panel) {
                var r = {id: "",parent: mq.view.main.container,
                    className: "profile-panel",title: j("profile"),hasBackButton: true,hasScroller: true,footer: {className: "profile-footer"},body: {className: "list_page"},rightButton: {text: j("record")}};
                this.panel = new mq.view.TitlePanel(r);
                c.setStyle(this.panel.bodyWrapper, "background", "rgb(237, 237, 237)");
                b.bindCommands(a.panel.container, m)
            }
            return this.panel
        };
        this.init = function() {
        };
        var m = {clickLeftButton: function() {
                n = null;
                mq.view.transitionManager.pop("profile");
                b.fire(a, "dismiss")
            },clickRightButton: function() {
                b.fire(mq.view,
                "viewRecord", {user: n})
            },viewGroupMember: function() {
                b.fire(mq.view, "viewGroupMember", {group: n})
            },viewDiscussMember: function() {
                b.fire(mq.view, "viewDiscussMember", {discuss: n})
            },sendMsg2Member: function() {
                var r = n, k = {uin: r.uin,type: r.type};
                if (r.group)
                    k.group_uin = r.group.gid;
                else if (r.discuss)
                    k.discuss_uin = r.discuss.did;
                b.fire(mq.view, "startChat", k)
            }};
        this.viewProfile = function(r) {
            this.createPanel().setLeftText(r.from || j("return"));
            this.refreshProfile(r.profile);
            mq.view.transitionManager.push({id: "profile",
                element: this.panel.container,callback: null})
        };
        this.refreshProfile = function(r) {
            n = r;
            var k = this.createPanel();
            k.body.innerHTML = g({profile: r,encode: e.encodeHtml,$M: j});
            r = c.getStyle(a.panel.footer, "height");
            c.setStyle(a.panel.bodyWrapper, "bottom", r);
            f(function() {
                k.scroller.refresh()
            })
        }
    })
});
define("tmpl!../tmpl/tmpl_members_body.html", [], function() {
    return function(g) {
        var a, b = "";
        with (g || {})
            b += '<div id="member_searchBar" class="search_wrapper">\r\n    <div class="search_inner">\r\n        <input id="member_searchInput" type="text" class="input_search" placeholder="' + ((a = $M("search")) == null ? "" : a) + '" autocapitalize="off" />\r\n        <button id="member_searchClear" class="searchClear" cmd="clearSearchWord"></button> \r\n    </div>\r\n    <button id="searchCancel" class="searchCancel" cmd="clearSearchWord" >' +
            ((a = $M("cancel")) == null ? "" : a) + '</button>\r\n</div>\r\n<div id="member_search_container_scroll_area" class="scrollWrapper search">\r\n    <div id="member_search_container" class="search_container">\r\n        <ul id="member_search_result_list" class="list list_white catogory_List">\r\n        </ul>\r\n    </div>\r\n</div>';
        return b
    }
});
define("mq.view.member", ["tmpl!../tmpl/tmpl_members_body.html", "tmpl!../tmpl/tmpl_member_list.html", "./mq.i18n", "./mq.view.transitionmanager"], function(g, a) {
    J.$package("mq.view.member", function() {
        var b = this, c = JM.event, e = JM.dom, j = mq.i18n.message;
        this.createPanel = function() {
            if (!this.panel) {
                var m = {parent: mq.view.main.container,className: "member-panel",title: j("members"),hasBackButton: true,body: {html: g({$M: j})}};
                this.panel = new mq.view.TitlePanel(m);
                this.searchBar = e.id("member_searchBar");
                this.searchInput =
                e.id("member_searchInput");
                m = this.scrollArea = e.id("member_search_container_scroll_area");
                this.memberList = new mq.view.MemberList({id: "search",scrollArea: m,listContainer: e.id("member_search_result_list"),listTmpl: a});
                c.bindCommands(b.panel.container, f);
                c.on(b.searchInput, "input", n.onSearchInput)
            }
            return this.panel
        };
        this.init = function() {
        };
        var f = {clickMemberItem: function(m, r) {
                var k = r.getAttribute("_uin"), d = r.getAttribute("_type");
                c.fire(mq.view, "viewProfile", {from: j("session"),account: k,type: d})
            },clickLeftButton: function() {
                mq.view.transitionManager.pop("members")
            },
            clearSearchWord: function() {
                b.searchInput.value = "";
                e.removeClass(b.searchBar, "hascontent");
                c.fire(b, "searchMembers", {keyword: ""})
            }}, n = {onSearchInput: function() {
                if (b.searchInput.value != "")
                    e.hasClass(b.searchBar, "hascontent") || e.addClass(b.searchBar, "hascontent");
                else
                    e.removeClass(b.searchBar, "hascontent");
                c.fire(b, "searchMembers", {keyword: b.searchInput.value})
            }};
        this.viewMembers = function(m) {
            var r = this.createPanel();
            mq.view.transitionManager.push({id: "members",element: r.container,callback: null});
            this.renderMembers(m)
        };
        this.renderMembers = function(m) {
            this.memberList.render({type: "list",list: m})
        }
    })
});
define("mq.presenter.member", ["./mq.i18n", "./mq.view.transitionmanager"], function() {
    J.$package("mq.presenter.member", function(g) {
        var a = this, b = JM.event, c;
        this.init = function() {
            this.view = mq.view.member;
            this.model = mq.model.buddylist;
            b.on(mq.view, "viewGroupMember", e.onViewGroupMember);
            b.on(mq.view, "viewDiscussMember", e.onViewDiscussMember);
            b.on(a.view, "searchMembers", e.onSearchMembers)
        };
        var e = {onViewGroupMember: function(j) {
                j = j.group;
                a.view.viewMembers(j.members);
                c = j.members
            },onViewDiscussMember: function(j) {
                j =
                j.discuss;
                a.view.viewMembers(j.members);
                c = j.members
            },onSearchMembers: function(j) {
                var f = j.keyword, n = [];
                if (f == "")
                    a.view.renderMembers(c);
                else {
                    g.each(c, function(m) {
                        m.nick.indexOf(f) > -1 && n.push(m)
                    });
                    a.view.renderMembers(n)
                }
            },onGroupInfoUpdate: function() {
            }}
    })
});
define("mq.model.record", ["jm"], function() {
    J.$package("mq.model.record", function() {
        var g = JM.event;
        this.getRecordSuccess = function(a) {
            g.fire(this, "getRecordSuccess", a)
        };
        this.sendGetRecord = function(a, b, c) {
            var e = document.createElement("script");
            document.body.appendChild(e);
            e.src = "http://web2.qq.com/cgi-bin/webqq_chat/?cmd=1&tuin=" + a.uin + "&vfwebqq=" + mq.vfwebqq + "&page=" + b + "&row=" + c + "&callback=mq.model.record.getRecordSuccess"
        }
    })
});
define("tmpl!../tmpl/tmpl_record_footer.html", [], function() {
    return function(g) {
        var a = "";
        with (g || {})
            a += '<div>\r\n    <a href="javascript:" class="record_pre_page" cmd="selectPrePage"><</a>\r\n    <input id="record_page_input" class="record_page_input" value="1">\r\n    <span>/</span>\r\n    <span id="record_total_count">3</span>\r\n    <a href="javascript:" class="record_next_page" cmd="selectNextPage">></a>\r\n</div>';
        return a
    }
});
define("mq.view.record", ["tmpl!../tmpl/tmpl_record_footer.html", "./mq.i18n", "./mq.view.transitionmanager"], function(g) {
    J.$package("mq.view.record", function(a) {
        var b = this, c = JM.event, e = JM.dom, j = JM.string, f = mq.i18n.message, n, m;
        this.createPanel = function() {
            if (!this.panel) {
                var k = {parent: mq.view.main.container,className: "record-panel",title: f("record"),hasBackButton: true,body: {className: "record_container"},footer: {className: "record_toolbar_footer",html: g({$M: f})}};
                this.panel = new mq.view.TitlePanel(k);
                this.pageInput =
                e.id("record_page_input");
                this.totalNumText = e.id("record_total_count");
                this.scrollArea = e.id("record_container_scroll_area");
                c.bindCommands(b.panel.container, r)
            }
            return this.panel
        };
        this.init = function() {
        };
        var r = {clickLeftButton: function() {
                mq.view.transitionManager.pop("record")
            },selectPrePage: function() {
                if (!(n <= 1)) {
                    n--;
                    c.fire(b, "selectPage", {pageIndex: n})
                }
            },selectNextPage: function() {
                if (!(n >= m)) {
                    n++;
                    c.fire(b, "selectPage", {pageIndex: n})
                }
            }};
        this.viewRecord = function() {
            var k = this.createPanel();
            mq.view.transitionManager.push({id: "record",
                element: k.container,callback: null})
        };
        this.renderRecord = function(k) {
            var d = k.recordData, t = k.user;
            k = k.self;
            var B = "", z, q = d.chatlogs, w = this.panel.body;
            this.pageInput.value = n = d.page || 1;
            this.totalNumText.innerHTML = m = d.total || 1;
            w.innerHTML = "";
            if (!q || q.length == 0)
                w.innerHTML += "<p class='no_record'>" + f("noRecord") + "</p>";
            else {
                d = 0;
                for (var C = q.length; d < C; d++) {
                    z = q[d];
                    var h = a.format.date(new Date(z.time * 1E3), "YYYY-MM-DD hh:mm:ss");
                    if (z.cmd == 16) {
                        z = z.msg[0];
                        B += '<dl class="me">                            <dt>' + j.encodeHtml(k.name) +
                        "<span>" + h + "</span></dt>                            <dd>" + j.encodeHtml(z) + "</dd>                        </dl>"
                    } else if (z.cmd == 17) {
                        z = z.msg[0];
                        B += '<dl class="buddy">                            <dt>' + j.encodeHtml(t.nick) + "<span>" + h + "</span></dt>                            <dd>" + j.encodeHtml(z) + "</dd>                        </dl>"
                    }
                }
                w.innerHTML = B
            }
        }
    })
});
define("mq.presenter.record", ["./mq.i18n", "./mq.view.transitionmanager"], function() {
    J.$package("mq.presenter.record", function() {
        var g = this, a = JM.event, b;
        this.init = function() {
            this.view = mq.view.record;
            this.model = mq.model.record;
            this.m_model = mq.model.buddylist;
            a.on(mq.view, "viewRecord", c.onViewRecord);
            a.on(g.view, "selectPage", c.onSelectPage);
            a.on(g.model, "getRecordSuccess", c.onGetRecordSuccess)
        };
        var c = {onViewRecord: function(e) {
                b = e.user || b;
                g.view.viewRecord(e);
                a.fire(g.view, "selectPage", {pageIndex: 0,rowCount: 10})
            },
            onSelectPage: function(e) {
                pageNum = e.pageIndex || 0;
                rowCount = e.rowCount || 10;
                g.model.sendGetRecord(b, pageNum, rowCount)
            },onGetRecordSuccess: function(e) {
                g.view.renderRecord({recordData: e,user: b,self: g.m_model.getSelfInfo()})
            }}
    })
});
define("tmpl!../tmpl/tmpl_session_body.html", [], function() {
    return function(g) {
        var a = "";
        with (g || {})
            a += '<div id="current_chat_scroll_area" class="scrollWrapper">\r\n    <ul id="current_chat_list" class="list list_white"></ul>\r\n</div>';
        return a
    }
});
define("mq.view.session", ["tmpl!../tmpl/tmpl_session_body.html", "tmpl!../tmpl/tmpl_member_list.html", "./mq.i18n", "./mq.view.transitionmanager"], function(g, a) {
    J.$package("mq.view.session", function() {
        var b = this, c = JM.event, e = JM.dom, j = mq.i18n.message, f = null, n = {}, m = 0;
        this.createPanel = function(d) {
            if (!this.panel) {
                d = {parent: d,title: j("session"),hasFooter: false,body: {html: g()}};
                this.panel = new mq.view.TitlePanel(d);
                this.scrollArea = e.id("current_chat_scroll_area");
                this.listContainer = e.id("current_chat_list");
                this.memberList = new mq.view.MemberList({id: "recent",scrollArea: this.scrollArea,listContainer: this.listContainer,listTmpl: a})
            }
            return this.panel
        };
        this.init = function() {
            c.bindCommands(b.scrollArea, r);
            c.on(mq.view.chat, "startChat", k.onStartChat);
            c.on(b, "show", k.onShow)
        };
        var r = {clickMemberItem: function(d, t) {
                var B = t.getAttribute("_uin"), z = t.getAttribute("_type");
                c.fire(mq.view, "startChat", {uin: B,type: z});
                e.removeClass(t, "notify")
            },clickMemberAvatar: function(d, t) {
                var B = t.parentNode.getAttribute("_uin"), z =
                t.parentNode.getAttribute("_type");
                c.fire(mq.view, "viewProfile", {from: j("session"),account: B,type: z})
            }}, k = {onStartChat: function(d) {
                if (d) {
                    m -= n[d.type + "-" + d.account] || 0;
                    if (m < 1) {
                        f || (f = e.id("session"));
                        e.removeClass(f, "point")
                    }
                }
            },onShow: function() {
                b.memberList.refresh()
            }};
        this.render = function(d) {
            d = d.slice(0, 10);
            this.memberList.render({type: "list",list: d,dataType: "recent"})
        };
        this.onReceiveMessage = function(d, t) {
            t || this.updateNotify(d);
            this.updateMessagePreview(d, t)
        };
        this.updateNotify = function(d) {
            d = d.send_to ||
            d.from_discuss || d.from_group || d.from_user;
            d = d.type + "-" + d.account;
            if (!n[d]) {
                n[d] = 1;
                m += 1
            }
            f || (f = e.id("session"));
            e.addClass(f, "point")
        };
        this.updateMessagePreview = function(d, t) {
            var B = d.send_to || d.from_discuss || d.from_group || d.from_user, z = "recent-item-" + (B.type + "-" + B.account), q = e.id(z);
            if (!q) {
                for (; this.listContainer.children.length >= 10; )
                    this.listContainer.removeChild(this.listContainer.children[this.listContainer.children.length - 1]);
                this.memberList.append({type: "list",list: [B]}, true);
                q = e.id(z);
                if (!q)
                    return
            }
            t ||
            e.addClass(q, "notify");
            B = e.id(z + "-msg");
            if (!B) {
                B = document.createElement("p");
                B.id = z + "-msg";
                B.setAttribute("class", "member_msg text_ellipsis");
                q.appendChild(B)
            }
            z = mq.presenter.chat.translateMessage(d);
            B.innerHTML = z;
            z = q.parentNode;
            z.children[0] && z.insertBefore(q, z.children[0]);
            this.memberList.refresh()
        }
    })
});
define("tmpl!../tmpl/tmpl_contact_body.html", [], function() {
    return function(g) {
        var a, b = "";
        with (g || {})
            b += '<div id="contactList" class="tab tab_animate member_tab">\r\n    <ul id="memberTab" class="tab_head">\r\n        <li cmd="clickMemberTab" param="friend">' + ((a = $M("con_friends")) == null ? "" : a) + '</li>\r\n        <li cmd="clickMemberTab" param="group">' + ((a = $M("con_groups")) == null ? "" : a) + '</li>\r\n        <li cmd="clickMemberTab" param="discuss">' + ((a = $M("con_discus")) == null ? "" : a) + '</li>\r\n    </ul>\r\n    <ul class="tab_body member_tab_body">\r\n        <li id="memberTabBody-friend">\r\n            <div id="f_list_scroll_area" class="member_scroll_area">\r\n                <ul id="friend_groupList" class="group_list member_group_list">\r\n                </ul> \r\n            </div>\r\n        </li>\r\n        <li id="memberTabBody-group">\r\n            <div id="group_list_scroll_area" class="member_scroll_area">\r\n                <ul id="g_list" class="list list_white catogory_List">\r\n                </ul>\r\n            </div>\r\n        </li>\r\n        <li id="memberTabBody-discuss">\r\n            <div id="discuss_list_scroll_area" class="member_scroll_area">\r\n                <ul id="d_list" class="list list_white catogory_List">\r\n                </ul>\r\n            </div>\r\n        </li>\r\n    </ul>\r\n</div>\r\n';
        return b
    }
});
define("mq.view.contact", ["tmpl!../tmpl/tmpl_contact_body.html", "tmpl!../tmpl/tmpl_member_list.html", "./mq.i18n", "./mq.view.transitionmanager"], function(g, a) {
    J.$package("mq.view.contact", function(b) {
        var c = this, e = JM.event, j = JM.dom, f = mq.i18n.message;
        this.createPanel = function(k) {
            if (!this.panel) {
                k = {parent: k,title: f("contact"),rightButton: {text: "",className: "btn_search"},leftButton: {className: "contact_null_btn"},body: {html: g({$M: f})}};
                this.panel = new mq.view.TitlePanel(k)
            }
            return this.panel
        };
        this.init = function() {
            this.contactList =
            j.id("contactList");
            this.memberListAreas = {};
            for (var k = [], d = j.id("memberTab").children, t, B = 0, z, q, w; z = d[B]; B++) {
                q = z.getAttribute("param");
                w = j.id("memberTabBody-" + q);
                k.push({id: q,trigger: z,sheet: w});
                this.memberListAreas[q] = new mq.view.MemberList({id: q,scrollArea: w.children[0],listContainer: w.children[0].children[0],listTmpl: a});
                if (q === "friend") {
                    for (t in r)
                        if (r.hasOwnProperty(t))
                            this.memberListAreas[q][t] = r[t];
                    this.memberListAreas[q].bindHandlers()
                }
            }
            this.tab = new MUI.Tab({items: k,selectedClass: "active"});
            e.bindCommands(c.panel.container, n);
            e.on(c.tab, "selected", m.onTabItemSelected);
            this.tab.select(0)
        };
        var n = {clickMemberTab: function(k) {
                c.tab.select(k)
            },clickMemberGroup: function(k, d) {
                j.toggleClass(d.parentNode, "active");
                c.memberListAreas.friend.refresh()
            },clickMemberItem: function(k, d) {
                var t = d.getAttribute("_uin"), B = d.getAttribute("_type");
                e.fire(mq.view, "startChat", {uin: t,type: B})
            },clickRightButton: function() {
                e.fire(mq.view, "startSearch", {from: f("contact")})
            },clickLeftButton: function() {
            }}, m = {onTabItemSelected: function(k) {
                k =
                k.current.id;
                c.memberListAreas[k] && c.memberListAreas[k].refresh()
            }}, r = {onScrollEnd: function() {
                var k = this.listContainer.querySelectorAll(".active"), d, t, B, z, q, w, C;
                if (k && k.length) {
                    if (!this._visibleContainer)
                        this._visibleContainer = j.id("f_list_scroll_area");
                    t = 0;
                    for (B = k.length; t < B; ++t) {
                        d = this._friendElements = k[t].querySelectorAll('[id^="friend-item"]');
                        if (this.inVisibleArea(k[t])) {
                            z = 0;
                            for (q = d.length; z < q; ++z) {
                                friendEle = d[z];
                                if (this.inVisibleArea(friendEle)) {
                                    e.fire(c, "memberInVisibleArea", friendEle.getAttribute("_uin"),
                                    "friend");
                                    w = true
                                } else if (w) {
                                    C = true;
                                    break
                                }
                            }
                            if (C)
                                break
                        }
                    }
                }
            },inVisibleArea: function(k, d) {
                d = d || this._visibleContainer;
                var t = d.getBoundingClientRect().top, B = d.clientHeight;
                t = k.getBoundingClientRect().top - t;
                return t >= 0 && t <= B
            },bindHandlers: function() {
                var k = this, d = this.scroll.options.onScrollEnd;
                this.onScrollEnd = b.bind(this.onScrollEnd, this);
                this.scroll.options.onScrollEnd = function() {
                    d.apply(this, arguments);
                    k.onScrollEnd.apply(this, arguments)
                };
                e.on(window, "load resize", this.onScrollEnd)
            },destroy: function() {
                this.scroll &&
                this.scroll.options && (this.scroll.options.onScrollEnd = null);
                e.off(window, "load resize", this._onScrollEnd);
                this.constructor.prototype.destroy.apply(this, arguments)
            },refresh: function() {
                this.onScrollEnd();
                this.constructor.prototype.refresh.apply(this, arguments)
            }}
    })
});
define("tmpl!../tmpl/tmpl_setting_body.html", [], function() {
    return function(g) {
        var a, b = "";
        with (g || {}) {
            b += '<div class="group">\r\n    <div class="row clearfix">\r\n        <div class="cloumn">\r\n            <img class="avatar" src="' + ((a = user.avatar) == null ? "" : a) + '">\r\n        </div>\r\n        <div class="cloumn profile_title_setting">\r\n            <div class="text_ellipsis profile_name row">' + ((a = encode(user.nick)) == null ? "" : a) + '</div>\r\n            <div class="row profile_account">' + ((a = user.account) ==
            null ? "" : a) + '</div>\r\n        </div>\r\n        <div id="online_state_setting" class="online_state_setting">\r\n            <i id="main_icon" class="main_icon online_icon"></i><i class="down_arrow"></i>\r\n            <ul>\r\n                <li><i class="online_icon"></i>' + ((a = $M("online")) == null ? "" : a) + '</li>\r\n                <li><i class="callme_icon"></i>' + ((a = $M("callme")) == null ? "" : a) + '</li>\r\n                <li><i class="away_icon"></i>' + ((a = $M("away")) == null ? "" : a) + '</li>\r\n                <li><i class="busy_icon"></i>' +
            ((a = $M("busy")) == null ? "" : a) + '</li>\r\n                <li><i class="silent_icon"></i>' + ((a = $M("silent")) == null ? "" : a) + '</li>\r\n                <li><i class="hidden_icon"></i>' + ((a = $M("hidden")) == null ? "" : a) + '</li>\r\n                <li><i class="offline_icon"></i>' + ((a = $M("offline")) == null ? "" : a) + "</li>\r\n            </ul>\r\n\r\n        </div>\r\n    </div> \r\n</div> \r\n\r\n";
            if (user.lnick)
                b += '\r\n<div class="group">\r\n    <div class="row profile_signature">\r\n        <span class="label">' + ((a =
                $M("signature")) == null ? "" : a) + "</span>\r\n        <span>" + ((a = encode(user.lnick)) == null ? "" : a) + "</span>\r\n    </div>\r\n    \r\n</div>\r\n";
            b += '  \r\n\r\n<div class="group clickAble" cmd="clickNotifySetting">\r\n    <div class="row ">\r\n        ' + ((a = $M("notify_setting")) == null ? "" : a) + '\r\n        <span class="more_icon"></span>\r\n    </div>\r\n</div>\r\n\r\n<div class="group clickAble" cmd="clickShowAbout">\r\n    <div class="row ">\r\n        ' + ((a = $M("about_qq")) == null ? "" : a) + '\r\n        <span class="more_icon"></span>\r\n    </div>\r\n</div>\r\n\r\n<div id="about_qq_all" class="group" style="display:none;">\r\n             <div class="row ">\r\n              <span class="label">' +
            ((a = $M("version")) == null ? "" : a) + "</span>\r\n              " + ((a = $M("current_version")) == null ? "" : a) + '\r\n            </div>\r\n            <div class="row ">\r\n            ' + ((a = $M("service")) == null ? "" : a) + '\r\n            </div>\r\n            <div class="row " cmd="clickFeedBack">\r\n                ' + ((a = $M("help")) == null ? "" : a) + '\r\n                <span class="more_icon"></span>\r\n            </div>\r\n\r\n</div>\r\n\r\n<div class="group clickAble" cmd="clickLogout">\r\n    <div class="row loginout">    \r\n            ' +
            ((a = $M("loginout")) == null ? "" : a) + "          \r\n    </div>\r\n</div>\r\n"
        }
        return b
    }
});
define("../lib/mui/js/mui.select", ["jm"], function() {
    JM.$package("MUI", function(g) {
        var a = g.dom, b = g.event;
        this.Select = g.Class({init: function(c) {
                this.elem = a.id(c.id) || c.id;
                this.select_list = a.tagName("ul", this.elem)[0];
                this.onSelected = c.onSelected;
                this.listItems = a.tagName("li", this.select_list);
                this.bindHandlers()
            },bindHandlers: function() {
                var c = this, e, j, f = this.listItems, n;
                b.on(this.elem, "click", function(m) {
                    m = m || window.event;
                    m = m.target || m.srcElement;
                    c.select_list.style.display != "block" ? a.setStyle(c.select_list,
                    "display", "block") : a.setStyle(c.select_list, "display", "none");
                    if (a.closest(m, "ul")) {
                        e = a.closest(m, "li");
                        g.each(f, function(r, k) {
                            if (r == e)
                                j = k
                        });
                        if (!g.type.isUndefined(j)) {
                            n = {selectedIndex: j,selectedItem: e};
                            b.fire(c, "selected", n);
                            c.onSelected && c.onSelected(n)
                        }
                    }
                })
            }})
    })
});
define("mq.view.setting", ["tmpl!../tmpl/tmpl_setting_body.html", "./mq.i18n", "./mq.view.transitionmanager", "../lib/mui/js/mui.select"], function(g) {
    J.$package("mq.view.setting", function() {
        var a = this, b = JM.event, c = JM.dom, e = JM.string, j = mq.i18n.message, f = ["online", "callme", "away", "busy", "silent", "hidden", "offline"];
        this.createPanel = function() {
            if (!this.panel) {
                var m = {parent: mq.view.main.body,title: j("setting"),hasScroller: true,body: {className: "list_page setting"}};
                this.panel = new mq.view.TitlePanel(m);
                b.bindCommands(a.panel.container,
                n)
            }
            return this.panel
        };
        this.init = function() {
            b.bindCommands(a.panel.container, n)
        };
        var n = {clickLogout: function() {
                b.fire(a, "logout")
            },clickShowAbout: function(m, r) {
                b.fire(a, "showAbout", r)
            },clickNotifySetting: function() {
                b.fire(a, "notifySetting")
            },clickFeedBack: function() {
                window.open("http://support.qq.com/discuss/513_1.shtml")
            }};
        this.viewSelfProfile = function(m) {
            this.createPanel();
            this.refreshSelfProfile(m);
            this.onlineStateSelect = new MUI.Select({id: "online_state_setting",onSelected: this.onSelectState});
            this.setOnlieStateIcon(mq.main.getCurrentOnlineState())
        };
        this.refreshSelfProfile = function(m) {
            var r = this.createPanel();
            r.body.innerHTML = g({user: m,encode: e.encodeHtml,$M: j});
            r.scroller.refresh()
        };
        this.setOnlieStateIcon = function(m) {
            c.id("main_icon").className = "main_icon " + m + "_icon"
        };
        this.onSelectState = function(m) {
            m = f[m.selectedIndex];
            b.fire(mq, "onlineStateChange", {state: m});
            a.setOnlieStateIcon(m)
        }
    })
});
define("mq.presenter.setting", ["./mq.i18n", "./mq.view.transitionmanager"], function() {
    J.$package("mq.presenter.setting", function() {
        var g = this, a = JM.event, b = JM.dom, c = mq.i18n.message, e;
        this.init = function() {
            this.view = mq.view.setting;
            this.model = mq.model.buddylist;
            a.on(mq, "onlineStateChange", j.onStateChanged);
            a.on(mq.view.setting, "show", j.onSettingShow);
            a.on(mq.view.setting, "notifySetting", j.onNotifySetting);
            a.on(mq.view.setting, "logout", j.onLogout);
            a.on(mq.view.setting, "showAbout", j.onShowAbout)
        };
        var j =
        {onSettingShow: function() {
                var f = g.model.getSelfInfo();
                g.view.viewSelfProfile(f)
            },onNotifySetting: function() {
                a.fire(mq.view, "viewNotifySetting", {from: c("setting")})
            },onStateChanged: function(f) {
                g.model.sendChangeStatus({newstatus: f.state})
            },onLogout: function() {
                if (confirm("\u60a8\u786e\u5b9a\u8981\u9000\u51fa\u5417\uff1f")) {
                    mq.main.logout();
                    window.location.href = window.location.href
                }
            },onShowAbout: function(f) {
                e = b.id("about_qq_all");
                var n = mq.view.setting.createPanel();
                if (e.style.display === "none") {
                    b.addClass(f,
                    "active");
                    e.style.display = "block"
                } else {
                    b.removeClass(f, "active");
                    e.style.display = "none"
                }
                n.scroller.refresh()
            }}
    })
});
define("mq.presenter.pluginDisplayer", ["jm"], function() {
    J.$package("mq.presenter.pluginDisplayer", function() {
        var g = this, a = JM.event, b = {onStartDisplayPlugin: function(c) {
                g.view.startDisplayPlugin(c)
            }};
        this.init = function() {
            this.view = mq.view.pluginDisplayer;
            a.on(mq.view, "startDisplayPlugin", b.onStartDisplayPlugin)
        }
    })
});
define("tmpl!../tmpl/tmpl_plugin_body.html", [], function() {
    return function(g) {
        var a, b = "";
        with (g || {}) {
            b += '<ul id="plugin_list" class="clearfix">\r\n    ';
            g = 0;
            for (var c; c = items[g]; ++g)
                b += '\r\n    <li id="' + ((a = c.id) == null ? "" : a) + '" cmd="clickItem">\r\n        <span class="icon"></span>\r\n        <a>' + ((a = c.text) == null ? "" : a) + "</a>\r\n    </li>\r\n    ";
            b += "\r\n</ul>"
        }
        return b
    }
});
define("mq.view.plugin", ["tmpl!../tmpl/tmpl_plugin_body.html", "jm", "./mq.i18n", "./mq.view.transitionmanager"], function(g) {
    J.$package("mq.view.plugin", function(a) {
        var b = this, c = JM.event, e = JM.dom, j = mq.i18n.message, f = a.platform.touchDevice, n = [{id: "qzone",url: f ? "http://pt.3g.qq.com/s?aid=touchLogin&t=qzone&bid_code=qzoneLogin&go_url=http://m.qzone.com/infocenter" : "http://qz.qq.com/",text: j("qzone")}, {id: "qmail",url: f ? "http://w.mail.qq.com/" : "http://ptlogin2.qq.com/pt4_web_jump?pt4_token=g3jdGooid--jhmLnMc5mIA__&daid=4&appid=522005705&succ_url=http%3A%2F%2Fmail.qq.com%2Fcgi-bin%2Flogin%3Ffun%3Dpassport%26from%3Dwebqq",
                text: j("qmail")}, {id: "qq_portal",url: f ? "http://shipei.qq.com/" : "http://www.qq.com/",text: j("qq_portal")}], m = {clickItem: function(r, k, d) {
                e.id("plugin_displayer");
                var t;
                for (r = n.length - 1; r >= 0; r--)
                    if (n[r].id === k.id) {
                        t = n[r];
                        break
                    }
                if (t)
                    f ? c.fire(mq.view, "startDisplayPlugin", t) : window.open(t.url, "_blank");
                d.preventDefault()
            }};
        this.createPanel = function(r) {
            if (!this.panel) {
                r = {parent: r,title: j("plugin"),hasScroller: true,body: {className: "plugin",html: g({items: n})}};
                this.panel = new mq.view.TitlePanel(r)
            }
            return this.panel
        };
        this.init = function() {
            if (/^[.\w-]+\.qq\.com/i.test(document.domain))
                document.domain = "qq.com";
            c.bindCommands(b.panel.container, m)
        }
    })
});
define("mq.view.pluginDisplayer", ["./mq.i18n", "./mq.view.transitionmanager"], function() {
    J.$package("mq.view.pluginDisplayer", function(g) {
        var a = this, b = g.event, c = g.dom;
        g = mq;
        var e = g.view, j = g.i18n.message;
        $TM = e.transitionManager;
        var f = null;
        tmplDisplayer = function(m, r) {
            return ['<iframe id="', m, '" ', r ? 'src="' + r + '"' : "", ">"].join("")
        };
        var n = {clickLeftButton: function() {
                $TM.pop("displayPlugin")
            }};
        this.startDisplayPlugin = function(m) {
            var r, k, d;
            if (m) {
                d = this.createPanel();
                if (f) {
                    r = false;
                    for (k in m)
                        if (m.hasOwnProperty(k) &&
                        m[k] !== f[k]) {
                            r = true;
                            break
                        }
                } else
                    r = true;
                if (r) {
                    f = m;
                    d.setTitle(m.text);
                    c.remove(d.body.querySelector("#plugin_displayer"));
                    d.body.innerHTML = tmplDisplayer("plugin_displayer", m.url)
                }
                $TM.push({id: "displayPlugin",element: this.panel.container,callback: function() {
                        a.scroll.refresh()
                    }})
            }
        };
        this.createPanel = function() {
            if (!this.panel) {
                this.panel = new e.TitlePanel({parent: e.main.container,className: "plugin-displayer-panel",leftButton: {className: "btn_arrow_left",text: j("return")},body: {className: "plugin_displayer_container",
                        html: tmplDisplayer("plugin_displayer")}});
                this.scroll = new iScroll(this.panel.bodyWrapper);
                b.bindCommands(a.panel.container, n)
            }
            return this.panel
        };
        this.init = function() {
        }
    })
});
define("jmAudio", ["jm"], function() {
    J.$package("J", function(g) {
        var a = function() {
            return 0
        }, b = {NONE: 0,NATIVE: 1,WMP: 2,FLASH: 3,MOBILE: 4};
        a = g.Class({init: function() {
                throw "BaseAudio does not implement a required interface";
            },play: a,pause: a,stop: a,getVolume: a,setVolume: a,getLoop: a,setLoop: a,setMute: a,getMute: a,getPosition: a,setPosition: a,getBuffered: a,getDuration: a,free: a,on: a,off: a});
        var c = function() {
            var d;
            return function(t) {
                if (!d) {
                    var B = document.createElement("div");
                    B.style.cssText = "position:absolute;width:1px;height:1px;overflow:hidden;margin:0;padding:0;left:0;top:0;";
                    (document.body || document.documentElement).appendChild(B);
                    if (t == b.FLASH) {
                        B.innerHTML = '<object id="jmAudioObject" name="jmAudioObject" ' + (g.browser.ie ? 'classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"' : 'type="application/x-shockwave-flash" data="../../../audio/jmAudioObject.swf"') + ' width="1" height="1" align="top"><param name="movie" value="../../../audio/jmAudioObject.swf" /><param name="allowScriptAccess" value="always" /><param name="allowFullScreen" value="false" /><param name="quality" value="high" /><param name="wmode" value="opaque" /></object>';
                        d = g.dom.id("jmAudioObject") || window.jmAudioObject || document.jmAudioObject
                    } else
                        d = B
                }
                return d
            }
        }(), e = function() {
            var d = 0;
            return function() {
                return d++
            }
        }(), j = function() {
            if (window.Audio && (new Audio).canPlayType("audio/mpeg")) {
                if (/\bmobile\b/i.test(navigator.userAgent))
                    return b.MOBILE;
                return b.NATIVE
            } else {
                var d;
                if (g.browser.plugins.flash >= 9)
                    d = b.FLASH;
                else {
                    if (d = window.ActiveXObject)
                        a: {
                            try {
                                new ActiveXObject("WMPlayer.OCX.7")
                            } catch (t) {
                                d = false;
                                break a
                            }
                            d = true
                        }
                    d = d ? b.WMP : b.NONE
                }
                return d
            }
        }();
        switch (j) {
            case b.NATIVE:
            case b.MOBILE:
                var f =
                g.Class({extend: a}, {init: function(d) {
                        d = d || {};
                        (this._el = new Audio).loop = Boolean(d.loop);
                        d.src && this.play(d.src)
                    },play: function(d) {
                        if (d)
                            this._el.src = d;
                        this._el.paused && this._el.play()
                    },pause: function() {
                        this._el.pause()
                    },stop: function() {
                        this._el.currentTime = Infinity
                    },getVolume: function() {
                        return !this._el.muted && this._el.volume || 0
                    },setVolume: function(d) {
                        if (isFinite(d)) {
                            this._el.volume = Math.max(0, Math.min(d, 1));
                            this._el.muted = false
                        }
                    },getLoop: function() {
                        return this._el.loop
                    },setLoop: function(d) {
                        this._el.loop =
                        d !== false
                    },getMute: function() {
                        return this._el.muted
                    },setMute: function(d) {
                        this._el.muted = d !== false
                    },getPosition: function() {
                        return this._el.currentTime
                    },setPosition: function(d) {
                        if (!isNaN(d))
                            this._el.currentTime = Math.max(0, d)
                    },getBuffered: function() {
                        return this._el.buffered.length && this._el.buffered.end(0) || 0
                    },getDuration: function() {
                        return this._el.duration
                    },free: function() {
                        this._el.pause();
                        this._el = null
                    },on: function(d, t) {
                        this._el.addEventListener(d, t, false)
                    },off: function(d, t) {
                        this._el.removeEventListener(d,
                        t, false)
                    }});
                if (j = b.NATIVE) {
                    g.Audio = f;
                    break
                }
                var n = [], m = function() {
                    var d = n.length;
                    n.pop().off("ended", m);
                    d >= 2 && n[d - 2]._el.play()
                };
                g.Audio = g.Class({extend: f}, {init: function(d) {
                        f.prototype.init.call(this, d)
                    },play: function(d) {
                        var t = n.length;
                        if (t && n[t - 1] !== this) {
                            t = g.indexOf(n, this);
                            -1 !== t ? n.splice(t, 1) : this.on("ended", m)
                        }
                        n.push(this);
                        if (d)
                            this._el.src = d;
                        this._el.paused && this._el.play()
                    },pause: function() {
                        for (var d = 0, t = n.length; d < t; d++)
                            n[d].off("ended", m);
                        n = [];
                        this._el.pause()
                    }});
                break;
            case b.FLASH:
                var r =
                function() {
                    var d = 0, t = [], B = false, z = function() {
                        ++d;
                        var q = c();
                        if (q.audioLoad && typeof q.audioLoad === "function") {
                            B = true;
                            q = 0;
                            for (var w = t.length; q < w; q++)
                                t[q]._sync();
                            t = null
                        } else
                            d < 3E4 && setTimeout(z, 100)
                    };
                    return function(q) {
                        if (B)
                            q._sync();
                        else {
                            -1 === g.indexOf(t, q) && t.push(q);
                            d === 0 && z()
                        }
                    }
                }(), k;
                (function() {
                    var d = [];
                    window.J.AudioEventDispatcher = function(t, B, z) {
                        t = d[t];
                        var q;
                        t && t._handler && (q = t._handler[B]);
                        B = 0;
                        for (var w = q && q.length; B < w; B++)
                            q[B].call(t, z)
                    };
                    k = function(t) {
                        d[t._seq] = t
                    }
                })();
                g.Audio = g.Class({init: function(d) {
                        this._seq =
                        e();
                        this._volume = 1;
                        this._muted = false;
                        d = d || {};
                        this._loop = Boolean(d.loop);
                        this._paused = true;
                        c(b.FLASH);
                        d.src && this.play(d.src)
                    },play: function(d) {
                        var t = c();
                        if (d) {
                            this._src = d;
                            this._paused = false;
                            t.audioLoad ? this._sync() : r(this)
                        } else {
                            this._paused = false;
                            t.audioPlay && t.audioPlay(this._seq)
                        }
                    },pause: function() {
                        var d = c();
                        this._paused = true;
                        d.audioPause && d.audioPause(this._seq)
                    },stop: function() {
                        this._paused = true;
                        var d = c();
                        d.audioStop && d.audioStop(this._seq)
                    },getVolume: function() {
                        return !this._muted && this._volume ||
                        0
                    },setVolume: function(d) {
                        if (isFinite(d)) {
                            this._volume = Math.max(0, Math.min(d, 1));
                            this._muted = false;
                            d = c();
                            d.audioSetVolume && d.audioSetVolume(this._seq, this._volume)
                        }
                    },getLoop: function() {
                        return this._loop
                    },setLoop: function(d) {
                        this._loop = d !== false;
                        d = c();
                        d.audioSetLoop && d.audioSetLoop(this._loop)
                    },getMute: function() {
                        return this._muted
                    },setMute: function(d) {
                        this._muted = d !== false;
                        d = c();
                        d.audioSetVolume && d.audioSetVolume(this._seq, this.getVolume())
                    },getPosition: function() {
                        var d = c();
                        return d.audioGetPosition &&
                        d.audioGetPosition(this._seq) / 1E3 || 0
                    },setPosition: function(d) {
                        isNaN(d) || c().audioSetPosition(this._seq, Math.max(0, d) * 1E3)
                    },getBuffered: function() {
                        var d = c();
                        return d.audioGetBuffered && d.audioGetBuffered(this._seq) / 1E3 || 0
                    },getDuration: function() {
                        var d = c();
                        return d.audioGetDuration && d.audioGetDuration(this._seq) / 1E3 || 0
                    },free: function() {
                        this._paused = true;
                        var d = c();
                        d.audioFree && d.audioFree(this._seq)
                    },on: function(d, t) {
                        if (!this._handler) {
                            this._handler = {};
                            k(this)
                        }
                        if (!this._handler[d] || !this._handler[d].length) {
                            this._handler[d] =
                            [t];
                            var B = c();
                            B.audioOn && B.audioOn(this._seq, d)
                        } else
                            -1 === g.indexOf(this._handler[d], t) && this._handler[d].push(t)
                    },off: function(d, t) {
                        var B;
                        if (this._handler && this._handler[d] && -1 !== (B = g.indexOf(this._handler[d], t))) {
                            this._handler[d].splice(B, 1);
                            if (!this._handler[d].length) {
                                B = c();
                                B.audioOff && B.audioOff(this._seq, d);
                                delete this._handler[d]
                            }
                        }
                    },_sync: function() {
                        if (this._src) {
                            var d = c(), t = this._seq;
                            d.audioLoad(t, this._src);
                            var B = this.getVolume();
                            B != 1 && d.audioSetVolume(t, B);
                            this._loop && d.audioSetLoop(t, true);
                            for (var z in this._handler)
                                d.audioOn(t, z);
                            this._paused || d.audioPlay(t)
                        }
                    }});
                break;
            case b.WMP:
                g.Audio = g.Class({extend: a}, {init: function(d) {
                        this._seq = e();
                        d = d || {};
                        var t = document.createElement("div");
                        c(b.WMP).appendChild(t);
                        t.innerHTML = '<object id="WMPObject' + this._seq + '" classid="CLSID:6BF52A52-394A-11D3-B153-00C04F79FAA6" standby="" type="application/x-oleobject" width="0" height="0">                        <param name="AutoStart" value="true"><param name="ShowControls" value="0"><param name="uiMode" value="none"></object>';
                        this._el = g.dom.id("WMPObject" + this._seq) || window["WMPObject" + this._seq];
                        d.loop && this._el.settings.setMode("loop", true);
                        d.src && this.play(d.src)
                    },play: function(d) {
                        if (d) {
                            var t = document.createElement("a");
                            t.href = d;
                            g.dom.getHref(t);
                            this._canPlayThroughFired = this._isBuffering = this._isPlaying = false;
                            this._el.URL = g.dom.getHref(t)
                        }
                        this._el.playState !== 3 && this._el.controls.play();
                        this._hasPoll() && this._startPoll()
                    },pause: function() {
                        this._el.controls.pause()
                    },stop: function() {
                        this._el.controls.stop()
                    },getVolume: function() {
                        return !this._el.settings.mute &&
                        this._el.settings.volume / 100 || 0
                    },setVolume: function(d) {
                        if (isFinite(d)) {
                            d = Math.max(0, Math.min(d, 1)) * 100;
                            if (this._el.settings.volume !== d || this._el.settings.mute) {
                                this._el.settings.volume = d;
                                this._el.settings.mute = false;
                                this._fire("volumechange")
                            }
                        }
                    },getLoop: function() {
                        return this._el.settings.getMode("loop")
                    },setLoop: function(d) {
                        this._el.settings.setMode("loop", d !== false)
                    },getMute: function() {
                        return this._el.settings.mute
                    },setMute: function(d) {
                        d = d !== false;
                        if (this._el.settings.mute !== d) {
                            this._el.settings.mute =
                            d;
                            this._fire("volumechange")
                        }
                    },getPosition: function() {
                        return this._el.controls.currentPosition
                    },setPosition: function(d) {
                        if (!isNaN(d)) {
                            this._fire("seeking");
                            this._el.controls.currentPosition = Math.max(0, d)
                        }
                    },getBuffered: function() {
                        return this._el.network.downloadProgress * 0.01 * this.getDuration()
                    },getDuration: function() {
                        return (this._el.currentMedia || 0).duration || 0
                    },free: function() {
                        this._el.controls.stop();
                        this._el = null
                    },on: function(d, t) {
                        if (!this._handler)
                            this._handler = {};
                        var B = this;
                        switch (d) {
                            case "timeupdate":
                                this._startPoll();
                            case "seeked":
                                if (!this._hasPositionChange()) {
                                    this._onPositionChange = function() {
                                        B._fire("timeupdate");
                                        B._fire("seeked")
                                    };
                                    this._el.attachEvent("PositionChange", this._onPositionChange)
                                }
                                break;
                            case "waiting":
                            case "playing":
                                if (!this._hasBuffering()) {
                                    this._onBuffering = function(z) {
                                        if ((B._el.currentMedia || 0).sourceURL)
                                            if (z) {
                                                B._isBuffering = true;
                                                B._fire("waiting")
                                            } else {
                                                B._isBuffering = false;
                                                B._fire("playing")
                                            }
                                    };
                                    this._el.attachEvent("Buffering", this._onBuffering)
                                }
                                break;
                            case "error":
                                this._el.attachEvent("Error",
                                t);
                                break;
                            case "progress":
                            case "ended":
                            case "play":
                            case "pause":
                                if (!this._hasPlayStateChange()) {
                                    this._onPlayStateChange = function(z) {
                                        if ((B._el.currentMedia || 0).sourceURL)
                                            if (z === 2) {
                                                B._isPlaying = false;
                                                B._fire("pause")
                                            } else if (z === 3) {
                                                if (!B._isPlaying) {
                                                    B._isPlaying = true;
                                                    B._fire("play")
                                                }
                                            } else if (z === 6)
                                                B._fire("progress");
                                            else if (z === 1)
                                                if (B._isPlaying) {
                                                    B._isPlaying = false;
                                                    B._fire("ended");
                                                    B._stopPoll()
                                                }
                                    };
                                    this._el.attachEvent("PlayStateChange", this._onPlayStateChange)
                                }
                                break;
                            case "loadstart":
                            case "loadeddata":
                            case "canplay":
                                if (!this._hasOpenStateChange()) {
                                    this._onOpenStateChange =
                                    function(z) {
                                        if ((B._el.currentMedia || 0).sourceURL)
                                            if (z === 21)
                                                B._fire("loadstart");
                                            else if (z === 13) {
                                                B._fire("loadeddata");
                                                B._fire("canplay")
                                            }
                                    };
                                    this._el.attachEvent("OpenStateChange", this._onOpenStateChange)
                                }
                                break;
                            case "canplaythrough":
                            case "durationchange":
                                this._startPoll()
                        }
                        (this._handler[d] || (this._handler[d] = [])).push(t)
                    },off: function(d, t) {
                        if (this._handler) {
                            var B;
                            if (this._handler && this._handler[d] && -1 !== (B = g.indexOf(this._handler[d], t)))
                                this._handler[d].splice(B, 1);
                            switch (d) {
                                case "timeupdate":
                                    this._hasPoll() ||
                                    this._stopPoll();
                                case "seeked":
                                    this._hasPositionChange() || this._el.detachEvent("PositionChange", this._onPositionChange);
                                    break;
                                case "waiting":
                                case "playing":
                                    this._hasBuffering() || this._el.detachEvent("Buffering", this._onBuffering);
                                    break;
                                case "error":
                                    this._el.detachEvent("Error", t);
                                    break;
                                case "progress":
                                case "ended":
                                case "play":
                                case "pause":
                                    this._hasPlayStateChange() || this._el.detachEvent("PlayStateChange", this._onPlayStateChange);
                                    break;
                                case "loadstart":
                                case "loadeddata":
                                case "canplay":
                                    this._hasOpenStateChange() ||
                                    this._el.detachEvent("OpenStateChange", this._onOpenStateChange);
                                    break;
                                case "canplaythrough":
                                case "durationchange":
                                    this._hasPoll() || this._stopPoll()
                            }
                        }
                    },_fire: function(d) {
                        var t;
                        if (this._handler && (t = this._handler[d])) {
                            d = 0;
                            for (var B = t.length; d < B; d++)
                                t[d].call(this)
                        }
                    },_startPoll: function() {
                        if (this._timer === undefined) {
                            this._canPlayThroughFired = this._canPlayThroughFired || this._el.network.downloadProgress === 100;
                            this._duration = this.getDuration();
                            var d = this;
                            this._timer = setInterval(function() {
                                if (d._isPlaying &&
                                !d._isBuffering && (d._handler.timeupdate || 0).length && (d._el.currentMedia || 0).sourceURL)
                                    d._fire("timeupdate");
                                var t = d.getDuration();
                                if (d._duration !== t) {
                                    d._duration = t;
                                    d._fire("durationchange")
                                }
                                if (!d._canPlayThroughFired)
                                    if (d._el.network.downloadProgress === 100) {
                                        d._canPlayThroughFired = true;
                                        d._fire("canplaythrough")
                                    }
                            }, 1E3)
                        }
                    },_stopPoll: function() {
                        clearInterval(this._timer);
                        delete this._timer
                    },_hasPositionChange: function() {
                        return this._handler.timeupdate && this._handler.timeupdate.length || this._handler.seeked &&
                        this._handler.seeked.length
                    },_hasBuffering: function() {
                        return this._handler.waiting && this._handler.waiting.length || this._handler.playing && this._handler.playing.length
                    },_hasPlayStateChange: function() {
                        return this._handler.progress && this._handler.progress.length || this._handler.ended && this._handler.ended.length || this._handler.play && this._handler.play.length || this._handler.pause && this._handler.pause.length
                    },_hasOpenStateChange: function() {
                        return this._handler.loadstart && this._handler.loadstart.length || this._handler.loadeddata &&
                        this._handler.loadeddata.length || this._handler.canplay && this._handler.canplay.length
                    },_hasPoll: function() {
                        return this._handler.timeupdate && this._handler.timeupdate.length || this._handler.canplaythrough && this._handler.canplaythrough.length || this._handler.durationchange && this._handler.durationchange.length
                    }});
                break;
            case b.NONE:
                g.Audio = g.Class({extend: a}, {init: function() {
                        console.log("Audio is not supported", "Audio")
                    }})
        }
    })
});
define("mq.view.audioNotification", ["jmAudio"], function() {
    J.$package("mq.view.audioNotification", function(g) {
        var a = g.Audio;
        this.init = function() {
            this.audio = new a
        };
        this.onAllMessageReceived = function(b) {
            b || this.audio.play("../audio/classic.mp3")
        }
    })
});
define("mq.view.desktopNotificationManager", ["jm"], function() {
    J.$package("mq.view.desktopNotificationManager", function(g) {
        function a(q, w) {
            var C;
            if (f.Notification)
                C = new f.Notification(q, {icon: j.isString(w.icon) ? w.icon : d,body: w.body || d,tag: w.tag || undefined});
            else if (f.webkitNotifications) {
                C = f.webkitNotifications.createNotification(w.icon, q, w.body);
                C.show()
            } else if (n.mozNotification) {
                C = n.mozNotification.createNotification(q, w.body, w.icon);
                C.show()
            }
            return C
        }
        function b() {
            var q;
            if (t)
                if ((q = f.Notification) &&
                q.permission)
                    return q.permission;
                else if ((q = f.webkitNotifications) && q.checkPermission)
                    return k[f.webkitNotifications.checkPermission()];
                else if (n.mozNotification)
                    return r;
                else if ((q = f.Notification) && q.permission)
                    permission = q.permissionLevel()
        }
        function c(q) {
            if (q)
                return {primal: q,close: function() {
                        var w;
                        if (j.isFunction(q.close))
                            w = q.close();
                        else if (j.isFunction(q.cancel))
                            w = q.cancel();
                        j.isNumber(this.timer) && f.clearTimeout(this.timer);
                        return w
                    },on: function(w, C) {
                        if (w === "show" && "ondisplay" in q)
                            w = "display";
                        if (q.addEventListener)
                            q.addEventListener(w, C, false);
                        else
                            q["on" + w] = C
                    },once: function(w, C) {
                        function h() {
                            C.apply(f, arguments);
                            o.off(w, h)
                        }
                        var o = this;
                        this.on(w, h)
                    },off: function(w) {
                        if (w === "show" && "ondisplay" in q)
                            w = "display";
                        if (q.removeEventListener)
                            q.removeEventListener(w);
                        else
                            q["on" + w] = null
                    }}
        }
        function e(q) {
            q.timer = f.setTimeout(function() {
                q.close()
            }, z.autoClose)
        }
        var j = g.type, f = window, n = navigator, m = document, r = "granted", k = [r, "default", "denied"], d = "", t = function() {
            var q = false;
            try {
                q = !!(f.Notification || f.webkitNotifications ||
                n.mozNotification)
            } catch (w) {
            }
            return q
        }(), B = function() {
        }, z = {autoClose: 0,detectPageVisibilify: true};
        this.PERMISSION_DEFAULT = "default";
        this.PERMISSION_GRANTED = r;
        this.PERMISSION_DENIED = "denied";
        this.isSupported = t;
        this.config = function(q) {
            q && j.isObject(q) && g.extend(z, q);
            return z
        };
        this.createNotificationWrapper = function(q, w) {
            var C, h;
            if (!(!t || b() !== r))
                if (!(z.detectPageVisibilify && !(m.hidden || m.mozHidden || m.webkitHidden))) {
                    if (j.isString(q) && w && j.isString(w.icon)) {
                        C = a(q, w);
                        h = c(C);
                        if (z.autoClose)
                            n.mozNotification ?
                            e(h) : h.on("show", function() {
                                e(h)
                            })
                    }
                    return h
                }
        };
        this.permissionLevel = b;
        this.requestPermission = function(q) {
            if (t) {
                q = j.isFunction(q) ? q : B;
                if (f.webkitNotifications && f.webkitNotifications.requestPermission)
                    return f.webkitNotifications.requestPermission();
                else if (f.Notification && f.Notification.requestPermission)
                    return f.Notification.requestPermission(q)
            }
        }
    })
});
define("mq.view.desktopNotification", ["./mq.view.desktopNotificationManager", "./mq.presenter.chat"], function() {
    J.$package("mq.view.desktopNotification", function(g) {
        var a = this, b = g.event, c = mq.view.desktopNotificationManager, e = window, j = e.document, f = mq.presenter.chat.translateMessage2Text, n = [], m = {onClose: function(r) {
                r = a.getNotificationIndex(r.target);
                r < 0 || n.splice(r, 1)
            },onBeforeUnload: function() {
                g.each(n, function(r) {
                    r.close()
                })
            }};
        this.init = function() {
            c.config({detectPageVisibilify: true,autoClose: 3E3});
            if (c.permissionLevel() === c.PERMISSION_DEFAULT)
                b.once(j.querySelector("body"), g.platform.touchDevice ? "tap" : "click", function() {
                    c.requestPermission()
                });
            b.on(e, "beforeunload", m.onBeforeUnload)
        };
        this.onAllMessageReceived = function(r, k) {
            k || !c.isSupported || c.permissionLevel() !== c.PERMISSION_GRANTED || this.appendNotification(r)
        };
        this.appendNotification = function(r) {
            n.length === 3 && n[0].close();
            if (r = c.createNotificationWrapper(r.name, {icon: r.avatar,body: f(r)})) {
                r.once("close", m.onClose);
                n.push(r)
            }
        };
        this.getNotificationIndex =
        function(r) {
            var k;
            for (k = 0; k < n.length; ++k)
                if (r === n[k].primal)
                    return k;
            return -1
        }
    })
});
define("mq.presenter.notification", ["./mq.model.chat", "./mq.model.memberlist", "./mq.view.desktopNotification", "./mq.view.audioNotification"], function() {
    J.$package("mq.presenter.notification", function(g) {
        var a = this, b = g.event, c = {onAllMessageReceived: function(e) {
                var j = e.from_group || e.from_user || e.from_discuss;
                j = a.buddylistModel.getBuddyInfo(j.account, j.type);
                var f = e.notNotify;
                a.desktopView.onAllMessageReceived({content: e.content,avatar: j.avatar,name: j.name}, !mq.setting.enableNotification || f);
                a.audioView.onAllMessageReceived(!mq.setting.enableVoice ||
                f)
            }};
        this.init = function() {
            this.chatModel = mq.model.chat;
            this.buddylistModel = mq.model.buddylist;
            this.desktopView = mq.view.desktopNotification;
            this.audioView = mq.view.audioNotification;
            this.bindHandlers()
        };
        this.bindHandlers = function() {
            b.on(this.chatModel, "allMessageReceived", c.onAllMessageReceived)
        }
    })
});
define("tmpl!../tmpl/tmpl_notify_setting.html", [], function() {
    return function(g) {
        var a, b = "";
        with (g || {}) {
            b += '\r\n<div class="group">\r\n    <div class="row clearfix">\r\n        <span class="label">' + ((a = $M("voice")) == null ? "" : a) + '</span>\r\n        <label class="switch switch-white" cmd="clickVoiceSetting">\r\n            <input id="enableVoiceBtn" type="checkbox" ' + ((a = data.enableVoice ? "checked" : "") == null ? "" : a) + '>\r\n            <span/>\r\n        </label>\r\n    </div>\r\n    <div class="row clearfix">\r\n        <span class="label">' +
            ((a = $M("notification")) == null ? "" : a) + '</span>\r\n        <label class="switch switch-white" cmd="clickNotificationSetting">\r\n            <input id="enableNotificationBtn" type="checkbox" ' + ((a = data.enableNotification ? "checked" : "") == null ? "" : a) + '>\r\n            <span/>\r\n        </label>\r\n    </div>\r\n</div>\r\n\r\n<div class="group">\r\n    <div class="row">\r\n        <div class="clearfix">\r\n            <span class="label">' + ((a = $M("https_setting")) == null ? "" : a) + '</span>\r\n            <label class="switch switch-white" cmd="clickHttpsSetting">\r\n                <input id="enableHttpsBtn" type="checkbox" ' +
            ((a = data.enableHttps ? "checked" : "") == null ? "" : a) + '>\r\n                <span/>\r\n            </label>\r\n        </div>\r\n        <div class="tips">' + ((a = $M("https_msg")) == null ? "" : a) + "</div>\r\n    </div>\r\n</div>\r\n";
            J.platform.touchDevice || (b += '\r\n<div class="group">\r\n    <div class="row">\r\n        <div class="clearfix">\r\n            <span class="long_label">' + ((a = $M("send_msg_way")) == null ? "" : a) + '</span>\r\n            <label class="switch switch-white" cmd="clickCtrlEnterSetting">\r\n                <input id="enableCtrlEnterBtn" type="checkbox" ' +
            ((a = data.enableCtrlEnter ? "checked" : "") == null ? "" : a) + ">\r\n                <span/>\r\n            </label>\r\n        </div>\r\n    </div>\r\n</div>\r\n");
            b += "\r\n"
        }
        return b
    }
});
define("mq.view.notifySetting", ["tmpl!../tmpl/tmpl_notify_setting.html", "./mq.i18n", "./mq.view.transitionmanager"], function(g) {
    J.$package("mq.view.notifySetting", function() {
        var a = this, b = JM.event, c = JM.dom, e = JM.string, j = mq.i18n.message, f, n, m;
        this.createPanel = function() {
            if (!this.panel) {
                var k = {id: "notifySetting",parent: mq.view.main.container,className: "profile-panel",title: j("notify_setting"),body: {className: "list_page notify_setting"},hasBackButton: true,hasScroller: true};
                this.panel = new mq.view.TitlePanel(k);
                b.bindCommands(a.panel.container, r)
            }
            return this.panel
        };
        this.init = function() {
        };
        var r = {clickLeftButton: function() {
                currentProfile = null;
                mq.view.transitionManager.pop("notifySetting");
                b.fire(a, "dismiss")
            },clickVoiceSetting: function() {
                b.fire(a, "settingChange", {enableVoice: f.checked || false})
            },clickNotificationSetting: function() {
                b.fire(a, "settingChange", {enableNotification: n.checked || false})
            },clickHttpsSetting: function() {
                b.fire(a, "settingChange", {enableHttps: m.checked || false})
            },clickCtrlEnterSetting: function() {
                b.fire(a,
                "settingChange", {enableCtrlEnter: enableCtrlEnterBtn.checked || false})
            }};
        this.show = function(k) {
            var d = this.createPanel();
            d.setLeftText(k.from || j("return"));
            d.body.innerHTML = g({encode: e.encodeHtml,$M: j,data: k.setting});
            f = c.id("enableVoiceBtn");
            n = c.id("enableNotificationBtn");
            m = c.id("enableHttpsBtn");
            mq.view.transitionManager.push({id: "notifySetting",element: this.panel.container,callback: function() {
                    d.scroller.refresh()
                }})
        }
    })
});
define("mq.presenter.notifySetting", ["./mq.i18n", "./mq.view.transitionmanager"], function() {
    J.$package("mq.presenter.notifySetting", function() {
        var g = this, a = JM.event;
        this.init = function() {
            this.view = mq.view.notifySetting;
            a.on(mq.view, "viewNotifySetting", b.onViewNotifySetting);
            a.on(g.view, "settingChange", b.onSettingChange)
        };
        var b = {onViewNotifySetting: function(c) {
                c || (c = {});
                c.setting = mq.setting;
                g.view.show(c)
            },onSettingChange: function(c) {
                mq.saveSetting(c)
            }}
    })
});
define("tmpl!../tmpl/tmpl_main_footer.html", [], function() {
    return function(g) {
        var a, b = "";
        with (g || {}) {
            b += '<nav id="nav_tab">\r\n    <ul class="nav_tab_head">\r\n        ';
            g = 0;
            for (var c; c = items[g]; g++)
                b += '\r\n        <li id="' + ((a = c.id) == null ? "" : a) + '" class="' + ((a = c.className) == null ? "" : a) + '" cmd="clickNav" param="' + ((a = c.id) == null ? "" : a) + '">\r\n            <a>\r\n                <div class="icon"></div>\r\n                <span>' + ((a = c.text) == null ? "" : a) + "</span>\r\n            </a>\r\n        </li>\r\n        ";
            b += '\r\n    </ul>\r\n    <div class="wallpaper-ctrl">\r\n        <a href="###" class="wallpaperImg pre" id="wp-ctrl-pre" title="\u70b9\u51fb\u5207\u6362\u80cc\u666f\u56fe\u7247" cmd="clickWPPre"> </a>\r\n        <a href="###" class="wallpaperImg next" id="wp-ctrl-next" title="\u70b9\u51fb\u5207\u6362\u80cc\u666f\u56fe\u7247" cmd="clickWPNext"> </a>\r\n    </div>\r\n    <div class="suggestion"><a href = "http://support.qq.com/discuss/513_1.shtml" target="_blank">\u610f\u89c1\u53cd\u9988</a></div>\r\n</nav>\r\n\r\n'
        }
        return b
    }
});
define("mq.view.main", ["tmpl!../tmpl/tmpl_main_footer.html", "./mq.i18n", "./mq.view.transitionmanager"], function(g) {
    J.$package("mq.view.main", function(a) {
        var b = this, c, e, j, f = window.localStorage.localBgImage, n = JM.event, m = JM.dom, r = mq.i18n.message;
        this.init = function() {
            var z;
            this.container = m.id("container");
            if (a.platform.touchDevice)
                z = m.id("container");
            else {
                z = window.innerWidth > 1E3 ? m.id("main_container") : m.id("container");
                n.on(window, "resize", function() {
                    var y = m.className("main-panel", document.body)[0];
                    z =
                    window.innerWidth < 1E3 ? m.id("container") : m.id("main_container");
                    z.appendChild(y)
                })
            }
            var q = {parent: z,hasHeader: false,className: "main-panel"}, w = [{id: "session",className: "contact",text: r("session")}, {id: "contact",className: "conversation",text: r("contact")}, {id: "plugin",className: "plugin",text: r("plugin")}, {id: "setting",className: "setup",text: r("setting")}], C = g({items: w});
            q.footer = {html: C};
            q = new mq.view.TitlePanel(q);
            this.body = q.body;
            this.body.innerHTML = "<div id='mainTopAll'></div>";
            C = m.id("nav_tab");
            for (var h =
            C.children[0].children, o = [], v, D = 0, p; p = h[D]; D++) {
                v = mq.view[w[D].id].createPanel(q.body);
                o.push({id: w[D].id,trigger: p,sheet: v.container})
            }
            w = this.nav = new MUI.Tab({items: o});
            n.bindCommands(C, d);
            n.on(b.nav, "selected", t.onNavItemSelected);
            n.on(mq.view.transitionManager, "transitionEnd", t.onTransitionEnd);
            n.on(window, "beforeunload", t.closeHook);
            q.show();
            mq.view.transitionManager.push({id: "main",element: q.container,transition: false});
            w.select(0);
            if (m.id("bgAllImage") && !a.platform.IOS && !a.platform.android &&
            !a.platform.winPhone) {
                w = f ? f : "1";
                c = parseInt(Math.random() * 28);
                w = "img/bg/" + w + ".jpg";
                q = document.createElement("img");
                q.setAttribute("class", "bgAllImage");
                q.src = w;
                m.id("bgAllImage").appendChild(q)
            }
        };
        var k = function() {
            setTimeout(function() {
                if (e == c)
                    window.localStorage && window.localStorage.setItem("localBgImage", e);
                else {
                    e = c;
                    k()
                }
            }, 8E3)
        }, d = {clickNav: function(z) {
                b.nav.select(z)
            },clickWPPre: function() {
                if (c === 0)
                    c = 28;
                else
                    c--;
                m.id("bgAllImage").innerHTML = "<img class='bgAllImage' src='img/bg/" + c + ".jpg'/>";
                if (!j) {
                    e =
                    c;
                    j = true
                }
                k()
            },clickWPNext: function() {
                if (c === 28)
                    c = 0;
                else
                    c++;
                m.id("bgAllImage").innerHTML = "<img class='bgAllImage' src='img/bg/" + c + ".jpg'/>";
                if (!j) {
                    e = c;
                    j = true
                }
                k()
            }}, t = {onNavItemSelected: function(z) {
                z = z.current.id;
                mq.view[z] && n.fire(mq.view[z], "show")
            },onTransitionEnd: function(z) {
                if (z.to === "main") {
                    z = b.nav.getSelected().item.id;
                    mq.view[z] && n.fire(mq.view[z], "show")
                }
            },closeHook: function() {
                if (mq.main.isOnline())
                    return r("beforeclose")
            }};
        this.showGuide = function() {
            var z = m.id("guide"), q = m.id("container"),
            w = m.id("main_container"), C = navigator.platform;
            (window.orientation != undefined ? "iPod" : (C.match(/mac|win|linux/i) || ["unknown"])[0]).match(/mac|win|linux/i) || m.setStyle(m.id("qrcode"), "display", "none");
            m.setStyle(z, "display", "block");
            m.setStyle(q, "display", "none");
            m.setStyle(w, "display", "none")
        };
        this.removeGuide = function() {
            var z = m.id("guide"), q = m.id("container"), w = m.id("main_container");
            z && z.parentNode.removeChild(z);
            m.setStyle(q, "display", "block");
            m.setStyle(w, "display", "block")
        };
        this.setOnlineState =
        function(z) {
            if (!this.onlineState)
                this.onlineState = m.id("user_online_state");
            this.onlineState.className = "state_" + z
        };
        var B = {init: function() {
                this._init = true;
                var z = this._el = document.createElement("div");
                z.setAttribute("class", "message_bubble");
                z.innerHTML = '<div class="message_body"><div cmd="closeBubble" class="close" title="\u5173\u95ed">X</div><div class="message_content"></div></div>';
                this._msgEl = z.firstChild.lastChild;
                var q = this;
                n.bindCommands(z.firstChild, {closeBubble: function() {
                        q.hide()
                    },gotoLogin: function() {
                        mq.main.gotoLogin()
                    }});
                document.body.appendChild(z)
            },show: function(z, q) {
                this._init || this.init();
                this._timeout && clearTimeout(this._timeout);
                this._msgEl.innerHTML = z;
                var w = this;
                if (q)
                    this._timeout = setTimeout(function() {
                        w.hide();
                        w._timeout = 0
                    }, q);
                m.addClass(this._el, "show")
            },hide: function() {
                this._init && m.removeClass(this._el, "show")
            }};
        mq.bubble = function(z, q) {
            B.show(z, q)
        };
        mq.hideBubble = function() {
            B.hide()
        }
    })
});
define("mq.view.loginPanel", ["./mq.i18n", "./mq.view.transitionmanager"], function() {
    J.$package("mq.view.loginPanel", function() {
        var g = this, a = JM.event, b = JM.dom, c = JM.http, e, j;
        this.init = function() {
        };
        this.show = function() {
            if (!j) {
                j = document.createElement("div");
                j.setAttribute("class", "masker");
                document.body.appendChild(j);
                e = document.createElement("div");
                e.setAttribute("class", "login-panel");
                e.innerHTML = '<iframe noscroll frameborder="0" style="position:absolute;width:100%;height:100%;border:0;"></iframe>';
                a.on(e.lastChild, "click", f);
                document.body.appendChild(e)
            }
            e.firstChild.src = "https://ui.ptlogin2.qq.com/cgi-bin/login?" + c.serializeParam({daid: 164,target: "self",style: 16,mibao_css: "m_webqq",appid: 501004106,enable_qlogin: 0,no_verifyimg: 1,s_url: "http://w.qq.com/proxy.html",f_url: "loginerroralert",strong_login: 1,login_state: 10,t: 20131024001});
            b.setStyle(j, "display", "block");
            b.setStyle(e, "display", "block");
            setTimeout(function() {
                b.addClass(e, "show")
            }, 0)
        };
        this.hide = function() {
            j && b.setStyle(j, "display", "none");
            e && b.setStyle(e, "display", "none");
            b.removeClass(e, "show")
        };
        var f = function() {
            g.hide()
        }
    })
});
define("qtracker", [], function() {
    (function(g, a) {
        var b;
        window[g] || (b = window[g] = {});
        var c = {utils: {halt: function() {
                }}}, e = function() {
        }, j = {}, f = function(k, d) {
            var t = function() {
                if (this instanceof arguments.callee)
                    this.__init__ && this.__init__.apply(this, arguments);
                else
                    throw Error("You must new an instance");
            };
            if (d) {
                t.prototype = new d;
                for (var B in k)
                    if (k.hasOwnProperty(B)) {
                        if (B == "__init__") {
                            var z = t.prototype.__init__, q = k[B];
                            if (z) {
                                t.prototype.__init__ = function() {
                                    z.apply(this, arguments);
                                    q.apply(this, arguments)
                                };
                                continue
                            }
                        }
                        t.prototype[B] = k[B]
                    }
            } else
                t.prototype = k;
            return t
        }, n = f({send: function() {
                throw Error("This method should be rewrite!");
            }}), m = f({__init__: function(k) {
                k = k || {};
                this._initOption(k);
                k = this.size;
                this.len = k - 1;
                this.array = [];
                this.array[k - 1] = a;
                this.errors = this.pointer = 0
            },_initOption: function(k) {
                this.size = k.size || 20;
                this.timeout = k.timeout || 3;
                this.errorMax = k.errormax || 10
            },send: function(k) {
                for (var d = this.pointer, t = 0, B = this.len, z = this.array; t <= B; t++) {
                    d = d + 1 > B ? d - B : d + 1;
                    c.utils.halt("check if " + d + " is free.");
                    if (this._isFree(z[d], d)) {
                        this.pointer = d;
                        this._send(k, d);
                        c.utils.halt(d + " is free!");
                        break
                    }
                }
            },_onError: function() {
                this.errors++;
                if (this.errors >= this.errorMax) {
                    this.send = e;
                    c.utils.halt("stop report")
                }
            },_isFree: function(k, d) {
                if (k && "ts" in k && +new Date - k.ts < this.timeout * 1E3)
                    return false;
                else if (k && "ts" in k) {
                    if (!k.finish) {
                        this._onError();
                        this._setFree(d);
                        c.utils.halt("report time out!");
                        return false
                    }
                    return true
                }
                return true
            },_setFree: function(k) {
                this.array[k].finish = true
            },release: function() {
                return window.CollectGarbage ?
                window.CollectGarbage : function() {
                }
            }(),_send: function(k) {
                var d = this.array[this.pointer];
                if (!(d && "ts" in d)) {
                    d = this.array[this.pointer] = {};
                    d.dom = new Image;
                    d.dom.onload = function() {
                        d.finish = true
                    };
                    d.dom.onerror = function() {
                        d.finish = true
                    }
                }
                d.ts = +new Date;
                d.dom.src = k + "&t=" + d.ts;
                d.finish = false
            }}, n);
        n = f({__init__: function(k) {
                k = k || {};
                this.interval = k.interval || 10;
                this.urlLimit = k.urlLimit || 1024;
                this.errorTimeout = k.errorTimeout || 4;
                this.transport = new m;
                this.urlHead = "http://isdspeed.qq.com/cgi-bin/r.cgi?";
                this.pages =
                {}
            },registerPage: function(k, d) {
                return this.pages[k] = new r({transport: this.transport,urlHead: this.urlHead,flags: d})
            },add: function(k) {
                k = this.pages[k];
                console.info(k, this.pages[k], this.pages);
                if (k)
                    k.add.apply(k, Array.prototype.slice.call(arguments, 1));
                else
                    throw Error("No such Page!Check the page name.");
            },send: function(k) {
                if (k = this.pages[k])
                    k.send();
                else
                    throw Error("No such Page!Check the page name.");
            }});
        var r = f({__init__: function(k) {
                this.transport = k.transport;
                for (var d = [], t = 0; t < k.flags.length; t++)
                    d.push("flag" +
                    (1 + t) + "=" + k.flags[t]);
                this.urlHead = k.urlHead + d.join("&") + "&";
                this.itemsHash = {}
            },add: function(k, d, t, B) {
                var z = this.itemsHash[k] = this.itemsHash[k] || [];
                z[0] = z[0] || j[k];
                z[2] = d || z[2];
                z[3] = t || z[3];
                z[1] = z[3] - z[2];
                B && this.send()
            },send: function(k) {
                var d = this.urlHead, t = [], B;
                for (B in this.itemsHash)
                    if (this.itemsHash.hasOwnProperty(B))
                        if (k = this.itemsHash[B])
                            if (!isNaN(k[1])) {
                                t.push(k.slice(0, 2).join("="));
                                delete this.itemsHash[B]
                            }
                t.length && this.transport.send(d + t.join("&"))
            },disable: function() {
                if (!this.isDisable) {
                    this.add =
                    this.send = e;
                    this.isDisable = true
                }
            }});
        b.setPageItemsHash = function(k) {
            j = k
        };
        b.tracker = {Isd: new n({}),Img: new m}
    })("qtracker")
});
define("mq.main", ["tmpl!../tmpl/tmpl_main_top.html", "../lib/mui/js/mui.tab", "../lib/mui/js/mui.textarea", "../lib/mui/js/mui.lazyload", "../lib/mui/js/mui.imagechange", "../lib/mui/js/mui.slide", "../lib/mui/js/mui.swipechange", "./mq.i18n", "./mq.view.transitionmanager", "./mq.util", "./mq.view.TitlePanel", "./mq.rpcservice", "./mq.view.MemberList", "./mq.model.memberlist", "./mq.presenter.memberlist", "./mq.model.chat", "./mq.view.chat", "./mq.presenter.chat", "./mq.presenter.search", "./mq.view.search", "./mq.presenter.profile",
    "./mq.view.profile", "./mq.view.member", "./mq.presenter.member", "./mq.model.record", "./mq.view.record", "./mq.presenter.record", "./mq.view.session", "./mq.view.contact", "./mq.view.setting", "./mq.presenter.setting", "./mq.presenter.pluginDisplayer", "./mq.view.plugin", "./mq.view.pluginDisplayer", "./mq.view.audioNotification", "./mq.view.desktopNotificationManager", "./mq.view.desktopNotification", "./mq.presenter.notification", "./mq.view.notifySetting", "./mq.presenter.notifySetting", "./mq.view.main", "./mq.view.loginPanel",
    "./mq.main", "./qtracker"], function(g) {
    J.$package("mq.main", function(a) {
        var b = JM.event, c = JM.dom, e = JM.http, j = JM.string, f = this, n = "poll", m, r = 3, k = 0, d = function(q, w) {
            var C = q.length, h = function() {
                C--;
                C == 0 && w()
            };
            a.each(q, function(o) {
                o(h)
            })
        }, t = function(q, w) {
            return (q.value && q.value.time || 0) < (w.value && w.value.time || 0) ? 1 : -1
        }, B = {}, z = {onLoginSuccess: function(q) {
                q = q.result;
                speedTempCache["7832-22-1"]["3"] = Date.now();
                f.setValidate({psessionid: q.psessionid});
                mq.port = q.port;
                mq.index = q.index;
                mq.view.main.init();
                mq.view.contact.init();
                mq.view.session.init();
                mq.presenter.buddylist.init();
                mq.model.buddylist.init({selfUin: q.uin});
                mq.model.chat.init();
                mq.view.chat.init();
                mq.presenter.chat.init();
                mq.view.search.init();
                mq.presenter.search.init();
                mq.view.profile.init();
                mq.presenter.profile.init();
                mq.view.setting.init();
                mq.presenter.setting.init();
                mq.presenter.member.init();
                mq.presenter.record.init();
                mq.view.plugin.init();
                mq.view.pluginDisplayer.init();
                mq.presenter.pluginDisplayer.init();
                mq.view.audioNotification.init();
                mq.view.desktopNotification.init();
                mq.presenter.notification.init();
                mq.presenter.notifySetting.init();
                var w = mq.model.buddylist;
                d([w.getUserFriends(), w.getGroupList(), w.getDiscussList()], function() {
                    w.sendGetBuddyOnlineState();
                    w.getRecentList(function() {
                        f.startPoll()
                    })
                });
                w.sendGetSelfInfo();
                b.fire(f, "loginSuccess", {selfUin: q.uin});
                if (c.id("mainTopAll") && !a.platform.IOS && !a.platform.android && !a.platform.winPhone) {
                    var C = c.id("mainTopAll");
                    b.bindCommands(C, B)
                }
                m = q.status
            },onGetVfWebQQSuccess: function(q) {
                f.setValidate({vfwebqq: q.result.vfwebqq});
                mq.rpcService.login()
            },onGetVfWebQQFailure: function() {
                f.gotoLogin()
            },onLoginFailure: function() {
                f.gotoLogin()
            },onPollSuccess: function(q) {
                if (q) {
                    q.sort(t);
                    for (var w = 0, C; C = q[w]; w++)
                        switch (C.poll_type) {
                            case "sess_message":
                            case "message":
                            case "group_message":
                            case "discu_message":
                                b.fire(f, "receiveMessage", C);
                                break;
                            case "kick_message":
                                f.stopPoll();
                                f.logout();
                                mq.log("kick message");
                                b.fire(f, "SelfOffline", {message: C.value.reason,action: "relogin"});
                                break;
                            case "filesrv_transfer":
                            case "file_message":
                            case "push_offfile":
                            case "notify_offfile":
                                b.fire(f,
                                "receiveFileMessage", C)
                        }
                }
            },onPollComplete: function() {
                f.keepPoll()
            },onGetFirstSelfInfo: function(q) {
                if (c.id("mainTopAll") && !a.platform.IOS && !a.platform.android && !a.platform.winPhone) {
                    c.id("mainTopAll").innerHTML = g({user: q,encode: j.encodeHtml});
                    mq.view.main.setOnlineState(m)
                }
            },onOnlineStateChange: function(q) {
                m = q.state;
                mq.view.main.setOnlineState(m)
            },onReLinkSuccess: function(q) {
                r = 3;
                k = 0;
                mq.debug("\u91cd\u8fde\u6210\u529f.");
                mq.hideBubble();
                f.setValidate(q);
                f.startPoll();
                mq.pgvSendClick({hottag: "smartqq.im.relinksuccess"})
            },
            onReLinkStop: function() {
                mq.debug("\u5f88\u52aa\u529b\u5730\u91cd\u8fde\u4e86, \u8fd8\u662f\u5931\u8d25\u4e86.");
                f.stopPoll();
                mq.hideBubble();
                b.fire(f, "SelfOffline", {message: "\u8eab\u4efd\u9a8c\u8bc1\u5931\u6548\uff0c\u8bf7\u91cd\u65b0\u767b\u5f55",action: "relogin"});
                mq.pgvSendClick({hottag: "smartqq.im.relinkstop"})
            },onFailCountOverMax: function() {
                f.stopPoll();
                if (k < r) {
                    setTimeout(function() {
                        f.reLink()
                    }, 1E3);
                    b.fire(f, "SelfOffline", {message: "\u56e0\u7f51\u7edc\u6216\u5176\u4ed6\u539f\u56e0\u4e0e\u670d\u52a1\u5668\u5931\u53bb\u8054\u7cfb\uff0c\u6b63\u5728\u5c1d\u8bd5\u91cd\u65b0\u767b\u5f55...",
                        action: "relink"})
                } else
                    z.onReLinkStop();
                k++
            },onNotLogin: function() {
                b.fire(f, "SelfOffline", {message: "\u4f60\u7684\u767b\u5f55\u5df2\u5931\u6548\uff0c\u8bf7\u91cd\u65b0\u767b\u5f55\u3002",action: "login"})
            },onNotReLogin: function() {
                b.fire(f, "SelfOffline", {message: "\u56e0\u7f51\u7edc\u6216\u5176\u4ed6\u539f\u56e0\u4e0e\u670d\u52a1\u5668\u5931\u53bb\u8054\u7cfb\uff0c\u8bf7\u91cd\u65b0\u767b\u5f55\u3002",action: "login"})
            },onSelfOffline: function(q) {
                mq.bubble(q.message, q.action == "relogin" ? 0 : 5E3)
            }};
        this.bindHandlers =
        function() {
            b.on(mq.rpcService, "LoginSuccess", z.onLoginSuccess);
            b.on(mq.rpcService, "LoginFailure", z.onLoginFailure);
            b.on(mq.rpcService, "getVfWebQQSuccess", z.onGetVfWebQQSuccess);
            b.on(mq.rpcService, "getVfWebQQFailure", z.onGetVfWebQQFailure);
            b.on(mq.rpcService, "PollComplete", z.onPollComplete);
            b.on(mq.rpcService, "PollSuccess", z.onPollSuccess);
            b.on(mq, "onlineStateChange", z.onOnlineStateChange);
            b.on(mq.model.buddylist, "getFirstSelfInfo", z.onGetFirstSelfInfo);
            b.on(mq.rpcService, "NotLogin", z.onNotLogin);
            b.on(mq.rpcService, "NotReLogin", z.onNotReLogin);
            b.on(mq.rpcService, "ReLinkStop", z.onReLinkStop);
            b.on(mq.rpcService, "FailCountOverMax", z.onFailCountOverMax);
            b.on(mq.rpcService, "ReLinkSuccess", z.onReLinkSuccess);
            b.on(mq.rpcService, "ReLinkFailure", z.onFailCountOverMax);
            b.on(f, "SelfOffline", z.onSelfOffline)
        };
        this.start = function() {
            mq.loadSetting();
            this.setValidate({clientid: 53999199,ptwebqq: a.cookie.get("ptwebqq"),skey: a.cookie.get("skey")});
            if (e.getUrlParam("guide", location.href) == 1)
                mq.view.main.showGuide();
            else
                !mq.ptwebqq || !mq.skey ? this.gotoLogin() : this.onPTLoginSuccess();
            mq.util.report2BNL2("11201")
        };
        this.setValidate = function(q) {
            mq.psessionid = q.psessionid || mq.psessionid || "";
            mq.vfwebqq = q.vfwebqq || mq.vfwebqq || "";
            mq.ptwebqq = q.ptwebqq || mq.ptwebqq || "";
            q.ptwebqq && a.cookie.set("ptwebqq", q.ptwebqq, "qq.com");
            mq.clientid = q.clientid || mq.clientid || "";
            mq.skey = q.skey || mq.skey || ""
        };
        this.onPTLoginSuccess = function(q) {
            this.loginType = q || 10;
            mq.view.loginPanel.hide();
            this.setValidate({ptwebqq: a.cookie.get("ptwebqq"),skey: a.cookie.get("skey")});
            mq.view.main.removeGuide();
            this.bindHandlers();
            mq.rpcService.getVfWebQQ();
            mq.util.report2BNL2("11202")
        };
        this.gotoLogin = function() {
            mq.util.report2BNL2("11203");
            mq.pgvSendClick({hottag: "smartqq.portal.jumptologin"});
            mq.view.loginPanel.show()
        };
        this.logout = function() {
            a.cookie.remove("ptwebqq", "qq.com");
            a.cookie.remove("skey", "qq.com")
        };
        this.isOnline = function() {
            return n == "poll"
        };
        this.startPoll = function() {
            n = "poll";
            this.keepPoll()
        };
        this.stopPoll = function() {
            n = "stop"
        };
        this.keepPoll = function() {
            n === "poll" &&
            mq.rpcService.sendPoll()
        };
        this.reLink = function() {
            mq.debug("reLink ");
            this.stopPoll();
            mq.rpcService.sendReLink();
            mq.pgvSendClick({hottag: "smartqq.im.relink"})
        };
        this.getCurrentOnlineState = function() {
            return m
        }
    })
});
require.config({paths: {jm: "../lib/jm/jm",jmAudio: "../lib/jm/jm.audio",iscroll: "../lib/iscroll/iscroll",tmpl: "../lib/require/tmpl"}});
require(["jm", "iscroll", "./mq.portal", "./mq.main", "./mq.report"], function() {
    var g = window.navigator.userAgent.toLowerCase(), a, b, c;
    if (J.platform.touchDevice || g.indexOf("webkit") >= 1 || g.indexOf("gecko") >= 1)
        mq.main.start();
    else if (J.platform.ieVersion > 8 && document.documentMode > 8) {
        g = document.getElementsByTagName("html")[0];
        a = "ie ie" + J.platform.ieVersion;
        if (g.className)
            a = " " + a;
        g.className = a;
        g = document.getElementsByTagName("head")[0] || document.documentElement;
        if (J.platform.ieVersion <= 8) {
            a = document.createElement("script");
            a.src = "lib/html5shiv/html5shiv.js";
            g.appendChild(a)
        }
        a = document.createElement("link");
        a.type = "text/css";
        a.rel = "stylesheet";
        a.href = "css/ie.css";
        g.appendChild(a);
        b = ["js/ie.js"];
        g = function() {
            ++c;
            c === b.length && mq.main.start()
        };
        a = mq.util.loadFile;
        for (c = b.length; c--; )
            a(b[c], g);
        c = 0
    } else {
        g = document.createElement("div");
        g.className = "newMaskAll";
        g.innerHTML = "<div class='newMaskText'>\u8bf7\u4f7f\u7528\u4ee5\u4e0b\u6d4f\u89c8\u5668\u8fdb\u884c\u8bbf\u95ee\uff1a</div><div class='newMaskLogo'><a class='newMaskChrome'href='https://www.google.com/intl/en/chrome/browser/' target='_blank' title='\u70b9\u51fb\u8df3\u8f6c\u5230chrome\u6d4f\u89c8\u5668\u4e0b\u8f7d\u9875'></a><a class='newMaskFirefox' href='http://firefox.com.cn/' target='_blank' title='\u70b9\u51fb\u8df3\u8f6c\u5230Firefox\u6d4f\u89c8\u5668\u4e0b\u8f7d\u9875'></a></div>";
        a = document.getElementById("container");
        a.parentNode.insertBefore(g, a)
    }
    mq.report.speedReport("7832-22-1", 2, true, true);
    mq.report.speedReport("7832-22-1", 1, true, true)
});
define("main.js", function() {
});
