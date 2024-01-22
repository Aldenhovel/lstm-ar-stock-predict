(function(){"use strict";var t={7583:function(t,e,o){var a=o(144),n=o(998),i=o(2928),r=o(1713),s=function(){var t=this,e=t._self._c;return e(n.Z,[e(r.Z,{staticStyle:{overflow:"hidden",height:"80px","margin-bottom":"5px"}},[e("top-nav-bar")],1),e(i.Z,[e("router-view")],1),e(r.Z,[e("bottom-nav-bar")],1)],1)},c=[],l=o(3107),u=o(8762),d=o(4324),h=function(){var t=this,e=t._self._c;return e("div",{staticClass:"bottomNavBar"},[e(n.Z,[e(l.Z,{staticStyle:{position:"fixed"},attrs:{value:t.value,color:"primary",width:"100%"}},t._l(t.labels,(function(o){return e(u.Z,{key:o.id,staticStyle:{"background-color":"white"},attrs:{height:"100%"},on:{click:function(e){return t.goto(o.to)}}},[e("span",[t._v(t._s(o.name))]),e(d.Z,[t._v(t._s(o.icon))])],1)})),1)],1)],1)},m=[],v={name:"BottomNavBar",data(){return{labels:[{name:"Dashboard",icon:"mdi-chart-areaspline",to:"/chart1"},{name:"information",icon:"mdi-information",to:"/chart2"}]}},methods:{goto(t){this.$router.replace(t)}}},f=v,p=o(1001),b=(0,p.Z)(f,h,m,!1,null,"4ae01236",null),g=b.exports,Z=o(5550),_=o(6312),w=o(2118),y=o(3687),x=o(6313),k=function(){var t=this,e=t._self._c;return e(w.Z,[e(n.Z,[e(x.Z,{attrs:{dark:"",prominent:"",src:"https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg",height:"80px",width:"100%"}},[e(Z.Z),e(_.Z),e(y.Z)],1)],1)],1)},C=[],B={name:"TopNavBar"},S=B,j=(0,p.Z)(S,k,C,!1,null,"60bac776",null),O=j.exports,P={name:"App",components:{TopNavBar:O,BottomNavBar:g},data:()=>({})},T=P,D=(0,p.Z)(T,s,c,!1,null,null,null),A=D.exports,I=o(8345),N=o(4145),E=o(266),M=o(2138),V=o(5495),F=o(7148),L=function(){var t=this,e=t._self._c;return e(w.Z,[e(r.Z,[e(E.Z,{attrs:{cols:"9"}},[e(N.Z,{staticClass:"mx-auto ma-1",attrs:{outlined:"",elevation:"3",width:"100%"}},[e(V.Z,{attrs:{src:t.gs_img}})],1),e(N.Z,{staticClass:"mx-auto ma-1",attrs:{outlined:"",elevation:"3",width:"100%"}},[e(V.Z,{attrs:{src:t.bs_img}})],1)],1),e(E.Z,{attrs:{cols:"3"}},[e(F.Z,{attrs:{clearable:"",label:"Stock Code",variant:"solo-filled",placeholder:"300001"},on:{focus:t.codeFocus,blur:t.codeBlur},model:{value:t.code,callback:function(e){t.code=e},expression:"code"}}),t._v(" Select a date to predict: "),e(M.Z,{attrs:{width:"100%"},model:{value:t.endDate,callback:function(e){t.endDate=e},expression:"endDate"}}),e(u.Z,{attrs:{variant:"tonal",width:"100%"},on:{click:function(e){return t.predict()}}},[t._v("Predict")])],1)],1)],1)},q=[],H=o(8830),$={name:"ChartView1",data:()=>({endDate:"",code:"",bs_img:"https://cdn.vuetifyjs.com/images/parallax/material.jpg",gs_img:"https://cdn.vuetifyjs.com/images/parallax/material.jpg"}),methods:{codeFocus(){var t=this.code.substr(0,2);"30"!==t&&"60"!==t&&"00"!==t&&"68"!==t||(this.code=this.code.substr(0,this.code.length-3))},codeBlur(){var t=this.code.substr(0,2);this.code="30"===t||"00"===t?this.code+".SZ":"60"===t||"68"===t?this.code+".SH":""},predict(){H.Z.post("/predict",{code:this.code,endDate:this.endDate}).then((t=>{let e=t.data;console.log(e.gs_img),console.log(e.bs_img),this.bs_img=e.bs_img,this.gs_img=e.gs_img}))}},mounted(){},watch:{endDate(t,e){console.log(t,e)},code(t,e){console.log(t,e)}}},G=$,J=(0,p.Z)(G,L,q,!1,null,"163d5e0a",null),R=J.exports,U=o(4886),z=o(9202),K=function(){var t=this,e=t._self._c;return e(w.Z,[e(r.Z,[e(E.Z,{attrs:{cols:"12"}},[e(N.Z,{staticClass:"mx-auto",attrs:{outlined:"",elevation:"3",height:"600"}},[[e("div",{staticClass:"text-center"},[e(u.Z,{staticClass:"ma-2",attrs:{color:"primary",width:"50%"},on:{click:function(e){t.dialog=!0}}},[t._v(" VERSION: BETA 0.0.1 ")]),e(z.Z,{attrs:{width:"auto"},model:{value:t.dialog,callback:function(e){t.dialog=e},expression:"dialog"}},[e(N.Z,[e(U.ZB,{staticStyle:{width:"50vw"}},[e("br"),t._v(" Version: BETA 0.0.1 "),e("br"),t._v(" Update: 2024-1-22 "),e("br")])],1)],1)],1),e("div",{staticClass:"text-center"},[e(u.Z,{staticClass:"ma-2",attrs:{color:"primary",width:"50%"},on:{click:function(e){t.mit=!0}}},[t._v(" License ")]),e(z.Z,{attrs:{width:"auto"},model:{value:t.mit,callback:function(e){t.mit=e},expression:"mit"}},[e(N.Z,[e(U.ZB,{staticStyle:{width:"50vw"}},[e("br"),t._v(" MIT License "),e("br")])],1)],1)],1),e("div",{staticClass:"text-center"},[e(u.Z,{staticClass:"ma-2",attrs:{color:"primary",width:"50%"},on:{click:function(e){t.declaration=!0}}},[t._v(" Declaration ")]),e(z.Z,{attrs:{width:"auto"},model:{value:t.declaration,callback:function(e){t.declaration=e},expression:"declaration"}},[e(N.Z,[e(U.ZB,{staticStyle:{width:"50vw"}},[e("br"),t._v(" 这个项目并非为了研究金融交易投资工具，实际上这是我研究 Image Caption 任务时突发奇想做的小玩具。因为没有经过经济学或者投资策略上的专业设计，效果不好很正常，你可以自己改进。 "),e("br"),t._v(" This project is not to study financial trading investment tools. In fact, it is a small toy that I made on a whim when I was studying the Image Caption task. Because it has not been professionally designed in terms of economics or investment strategies, it is normal for the results to be poor, and you can improve it yourself. "),e("br")])],1)],1)],1),e("div",{staticClass:"text-center"},[e(u.Z,{staticClass:"ma-2",attrs:{color:"primary",width:"50%"},on:{click:function(e){t.thx=!0}}},[t._v(" About ")]),e(z.Z,{attrs:{width:"auto"},model:{value:t.thx,callback:function(e){t.thx=e},expression:"thx"}},[e(N.Z,[e(U.ZB,{staticStyle:{width:"50vw"}},[e("br"),t._v(" Author: Aldenhovel (J.B.Liang) "),e("br"),t._v(" Email: 1736724492@qq.com "),e("br"),t._v(" GitHub: https://github.com/Aldenhovel/lstm-ar-stock-predict "),e("br")])],1)],1)],1)]],2)],1)],1)],1)},Q=[],W={name:"ChartView2",data:()=>({dialog:!1,mit:!1,declaration:!1,thx:!1}),mounted(){}},X=W,Y=(0,p.Z)(X,K,Q,!1,null,"64355a1c",null),tt=Y.exports;a.ZP.use(I.ZP);const et=[{path:"/",name:"home",component:R},{path:"/chart1",name:"about",component:R},{path:"/chart2",name:"about",component:tt}],ot=new I.ZP({routes:et});var at=ot,nt=o(6560);a.ZP.use(nt.Z);var it=new nt.Z({});a.ZP.config.productionTip=!1,new a.ZP({router:at,vuetify:it,axios:H.Z,render:t=>t(A)}).$mount("#app")}},e={};function o(a){var n=e[a];if(void 0!==n)return n.exports;var i=e[a]={exports:{}};return t[a].call(i.exports,i,i.exports,o),i.exports}o.m=t,function(){var t=[];o.O=function(e,a,n,i){if(!a){var r=1/0;for(u=0;u<t.length;u++){a=t[u][0],n=t[u][1],i=t[u][2];for(var s=!0,c=0;c<a.length;c++)(!1&i||r>=i)&&Object.keys(o.O).every((function(t){return o.O[t](a[c])}))?a.splice(c--,1):(s=!1,i<r&&(r=i));if(s){t.splice(u--,1);var l=n();void 0!==l&&(e=l)}}return e}i=i||0;for(var u=t.length;u>0&&t[u-1][2]>i;u--)t[u]=t[u-1];t[u]=[a,n,i]}}(),function(){o.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return o.d(e,{a:e}),e}}(),function(){o.d=function(t,e){for(var a in e)o.o(e,a)&&!o.o(t,a)&&Object.defineProperty(t,a,{enumerable:!0,get:e[a]})}}(),function(){o.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(t){if("object"===typeof window)return window}}()}(),function(){o.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)}}(),function(){o.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})}}(),function(){var t={143:0};o.O.j=function(e){return 0===t[e]};var e=function(e,a){var n,i,r=a[0],s=a[1],c=a[2],l=0;if(r.some((function(e){return 0!==t[e]}))){for(n in s)o.o(s,n)&&(o.m[n]=s[n]);if(c)var u=c(o)}for(e&&e(a);l<r.length;l++)i=r[l],o.o(t,i)&&t[i]&&t[i][0](),t[i]=0;return o.O(u)},a=self["webpackChunkds"]=self["webpackChunkds"]||[];a.forEach(e.bind(null,0)),a.push=e.bind(null,a.push.bind(a))}();var a=o.O(void 0,[998],(function(){return o(7583)}));a=o.O(a)})();
//# sourceMappingURL=app.c804a4c3.js.map