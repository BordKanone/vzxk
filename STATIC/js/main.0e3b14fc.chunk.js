(this.webpackJsonpvzxk_ui=this.webpackJsonpvzxk_ui||[]).push([[0],{25:function(t,e,n){},45:function(t,e,n){"use strict";n.r(e);var c=n(2),i=n.n(c),r=n(14),a=n.n(r),u=(n(25),n(15)),o=n(16),s=n(20),l=n(19),j=n(1),d=function(t){Object(s.a)(n,t);var e=Object(l.a)(n);function n(t){var c;return Object(u.a)(this,n),(c=e.call(this,t)).state={currentTime:(new Date).toLocaleString()},c}return Object(o.a)(n,[{key:"componentDidMount",value:function(){var t=this;this.timerId=setInterval((function(){t.setState({currentTime:(new Date).toLocaleString()})}),1e3)}},{key:"componentWillUnmount",value:function(){clearInterval(this.timerId)}},{key:"render",value:function(){return Object(j.jsx)("div",{children:this.state.currentTime})}}]),n}(i.a.Component),h=function(t){t&&t instanceof Function&&n.e(3).then(n.bind(null,46)).then((function(e){var n=e.getCLS,c=e.getFID,i=e.getFCP,r=e.getLCP,a=e.getTTFB;n(t),c(t),i(t),r(t),a(t)}))},b=n(18),f=n(17),m=n.n(f);var v=function(){var t=Object(c.useState)([]),e=Object(b.a)(t,2),n=e[0],i=e[1];return Object(c.useEffect)((function(){m()({method:"GET",url:"http://127.0.0.1/customers/"}).then((function(t){i(t.data)}))}),[]),Object(j.jsx)("div",{className:"peopleGet",children:Object(j.jsx)("ul",{children:n.map((function(t){return Object(j.jsx)("li",{children:t.first_name},t.id)}))})})};a.a.render(Object(j.jsx)(i.a.StrictMode,{children:Object(j.jsxs)("div",{className:"clock",children:[Object(j.jsx)(d,{}),Object(j.jsx)(v,{})]})}),document.getElementById("root")),h()}},[[45,1,2]]]);
//# sourceMappingURL=main.0e3b14fc.chunk.js.map