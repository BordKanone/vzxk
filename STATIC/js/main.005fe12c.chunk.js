(this.webpackJsonpvzxk_ui=this.webpackJsonpvzxk_ui||[]).push([[0],{25:function(t,e,n){},45:function(t,e,n){"use strict";n.r(e);var c=n(2),i=n.n(c),r=n(14),a=n.n(r),s=(n(25),n(15)),o=n(16),u=n(20),l=n(19),j=n(0),d=function(t){Object(u.a)(n,t);var e=Object(l.a)(n);function n(t){var c;return Object(s.a)(this,n),(c=e.call(this,t)).state={currentTime:(new Date).toLocaleString()},c}return Object(o.a)(n,[{key:"componentDidMount",value:function(){var t=this;this.timerId=setInterval((function(){t.setState({currentTime:(new Date).toLocaleString()})}),1e3)}},{key:"componentWillUnmount",value:function(){clearInterval(this.timerId)}},{key:"render",value:function(){return Object(j.jsx)("div",{children:this.state.currentTime})}}]),n}(i.a.Component),h=function(t){t&&t instanceof Function&&n.e(3).then(n.bind(null,46)).then((function(e){var n=e.getCLS,c=e.getFID,i=e.getFCP,r=e.getLCP,a=e.getTTFB;n(t),c(t),i(t),r(t),a(t)}))},v=n(18),b=n(17),m=n.n(b);var f=function(){var t=Object(c.useState)([]),e=Object(v.a)(t,2),n=e[0],i=e[1];return Object(c.useEffect)((function(){m()({method:"GET",url:"http://127.0.0.1:8000/customers"}).then((function(t){i(t.data)}))}),[]),Object(j.jsx)("div",{className:"peopleGet",children:n.map((function(t){return Object(j.jsxs)("div",{children:[Object(j.jsx)("p",{children:t.first_name},t.id),Object(j.jsx)("img",{className:"avatar",src:t.avatar})]})}))})};a.a.render(Object(j.jsxs)(i.a.StrictMode,{children:[Object(j.jsx)("div",{className:"clock",children:Object(j.jsx)(d,{})}),Object(j.jsx)(f,{})]}),document.getElementById("root")),h()}},[[45,1,2]]]);
//# sourceMappingURL=main.005fe12c.chunk.js.map