(this.webpackJsonpvzxk_ui=this.webpackJsonpvzxk_ui||[]).push([[0],{25:function(e,t,n){},45:function(e,t,n){"use strict";n.r(t);var c=n(2),a=n.n(c),r=n(14),s=n.n(r),i=(n(25),n(15)),u=n(16),o=n(20),l=n(19),j=n(0),m=function(e){Object(o.a)(n,e);var t=Object(l.a)(n);function n(e){var c;return Object(i.a)(this,n),(c=t.call(this,e)).state={currentTime:(new Date).toLocaleString()},c}return Object(u.a)(n,[{key:"componentDidMount",value:function(){var e=this;this.timerId=setInterval((function(){e.setState({currentTime:(new Date).toLocaleString()})}),1e3)}},{key:"componentWillUnmount",value:function(){clearInterval(this.timerId)}},{key:"render",value:function(){return Object(j.jsx)("div",{children:this.state.currentTime})}}]),n}(a.a.Component),d=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,46)).then((function(t){var n=t.getCLS,c=t.getFID,a=t.getFCP,r=t.getLCP,s=t.getTTFB;n(e),c(e),a(e),r(e),s(e)}))},h=n(18),b=n(17),v=n.n(b);var f=function(){var e=Object(c.useState)([]),t=Object(h.a)(e,2),n=t[0],a=t[1];return Object(c.useEffect)((function(){v()({method:"GET",url:"http://127.0.0.1:8000/customers"}).then((function(e){a(e.data)}))}),[]),Object(j.jsx)("div",{className:"peopleGet",children:n.map((function(e){return Object(j.jsxs)("div",{children:[Object(j.jsxs)("p",{className:"username_last_name",children:[" ",e.last_name]},e.id),Object(j.jsx)("p",{className:"username",children:e.first_name},e.id),Object(j.jsx)("p",{className:"username_last_name",children:e.three_name},e.id),Object(j.jsx)("img",{className:"avatar",src:e.avatar})]})}))})};s.a.render(Object(j.jsxs)(a.a.StrictMode,{children:[Object(j.jsx)("div",{className:"clock",children:Object(j.jsx)(m,{})}),Object(j.jsx)(f,{})]}),document.getElementById("root")),d()}},[[45,1,2]]]);
//# sourceMappingURL=main.35cf99aa.chunk.js.map