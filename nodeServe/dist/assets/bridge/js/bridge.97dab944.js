!function (e) {
  var t = {};
  
  function r(n) {
    if (t[n]) return t[n].exports;
    var s = t[n] = {i: n, l: !1, exports: {}};
    return e[n].call(s.exports, s, s.exports, r), s.l = !0, s.exports
  }
  
  r.m = e, r.c = t, r.d = function (e, t, n) {
    r.o(e, t) || Object.defineProperty(e, t, {enumerable: !0, get: n})
  }, r.r = function (e) {
    "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {value: "Module"}), Object.defineProperty(e, "__esModule", {value: !0})
  }, r.t = function (e, t) {
    if (1 & t && (e = r(e)), 8 & t) return e;
    if (4 & t && "object" == typeof e && e && e.__esModule) return e;
    var n = Object.create(null);
    if (r.r(n), Object.defineProperty(n, "default", {
      enumerable: !0,
      value: e
    }), 2 & t && "string" != typeof e) for (var s in e) r.d(n, s, function (t) {
      return e[t]
    }.bind(null, s));
    return n
  }, r.n = function (e) {
    var t = e && e.__esModule ? function () {
      return e.default
    } : function () {
      return e
    };
    return r.d(t, "a", t), t
  }, r.o = function (e, t) {
    return Object.prototype.hasOwnProperty.call(e, t)
  }, r.p = "", r(r.s = 0)
}([function (e, t, r) {
  "use strict";
  r.r(t);
  let n = {};
  const s = sessionStorage, i = localStorage;
  const o = "__MY_WEB_MESSAGER__";
  const a = new class {
    constructor(e) {
      const t = this.options = {target: window, bridge: null, origin: null, ready: null, ...e};
      this.target = t.target, this.handlers = {}, this.proxyBridgeHandler = this.bridgeHandler.bind(this), window.addEventListener("storage", this.proxyBridgeHandler), t.bridge ? this.buildBridge().then(e => {
        this.target = e.contentWindow, this.el = e, t.ready && t.ready(this)
      }) : t.ready && t.ready(this)
    }
    
    on(e, t) {
      const r = function (r) {
        let n = r.data || {};
        n && n.type === o && n.data.type === e && t(n.data.data, n.data.bridge)
      };
      this.handlers[e] || (this.handlers[e] = []), this.handlers[e].push(r), window.addEventListener("message", r)
    }
    
    off(e, t) {
      if (e && t) {
        const r = this.handlers[e] || [];
        r.forEach((e, n) => {
          t === e && (r.splice(n, 1), window.removeEventListener("message", e))
        })
      } else if (e) {
        (this.handlers[e] || []).forEach(e => {
          window.removeEventListener("message", e)
        }), delete this.handlers[e]
      } else Object.keys(this.handlers).forEach(e => {
        this.off(e)
      })
    }
    
    fire(e, t) {
      if (!this.target) return;
      const r = {type: o, data: {type: e, data: t, bridge: this.options.origin}};
      if (this.options.bridge) {
        const e = {type: o, data: r};
        this.target.postMessage(e, "*")
      } else this.target.postMessage(r, "*")
    }
    
    once(e, t) {
      this.on(e, () => {
        t.apply(this, arguments), this.off(e, t)
      })
    }
    
    buildBridge() {
      return new Promise((e, t) => {
        const r = document.createElement("iframe");
        r.style.display = "none", r.setAttribute("src", this.options.bridge + "?t=" + (new Date).getTime()), r.onload = () => {
          e(r)
        }, r.onerror = e => {
          t(e)
        }, document.body.appendChild(r)
      })
    }
    
    pass(e) {
      !function (e, t, r = s) {
        n[e] = t;
        const i = "object" == typeof t ? JSON.stringify(t) : t;
        r.setItem(e, i)
      }(o, {message: e, __t__: (new Date).getTime()}, i)
    }
    
    bridgeHandler(e) {
      if (e.key !== o) return;
      const t = JSON.parse(e.newValue);
      if (t && t.message) {
        const e = t.message;
        (this.handlers[e.type] || []).forEach(t => {
          t({data: {type: o, data: e}})
        })
      }
    }
    
    destroy() {
      this.off(), this.proxyBridgeHandler && window.removeEventListener("storage", this.proxyBridgeHandler), this.el && this.el.parentNode.removeChild(this.el)
    }
  }({target: parent.window});
  a.on(o, (function (e) {
    a.pass(e)
  }))
}]);
