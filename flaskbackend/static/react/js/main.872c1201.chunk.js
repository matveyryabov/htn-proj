(this.webpackJsonpreactfrontend=this.webpackJsonpreactfrontend||[]).push([[0],{23:function(e,t,n){},24:function(e,t,n){},43:function(e,t,n){"use strict";n.r(t);var i=n(0),c=n(2),l=n.n(c),s=n(12),a=n.n(s),o=(n(23),n.p,n(24),n(13)),r=n(14),d=n(17),j=n(16),h=n(15),p=n.n(h),b=function(e){Object(d.a)(n,e);var t=Object(j.a)(n);function n(){var e;Object(o.a)(this,n);for(var c=arguments.length,l=new Array(c),s=0;s<c;s++)l[s]=arguments[s];return(e=t.call.apply(t,[this].concat(l))).state={selectedFile:null},e.onFileChange=function(t){e.setState({selectedFile:t.target.files[0]})},e.onFileUpload=function(){var t=new FormData;t.append("myFile",e.state.selectedFile,e.state.selectedFile.name),console.log(e.state.selectedFile),p.a.post("http://localhost:5000/api/upload",t)},e.fileData=function(){return e.state.selectedFile?Object(i.jsxs)("div",{children:[Object(i.jsx)("h2",{children:"File Details:"}),Object(i.jsxs)("p",{children:["File Name: ",e.state.selectedFile.name]}),Object(i.jsxs)("p",{children:["File Type: ",e.state.selectedFile.type]}),Object(i.jsxs)("p",{children:["Last Modified:"," ",e.state.selectedFile.lastModifiedDate.toDateString()]})]}):Object(i.jsxs)("div",{children:[Object(i.jsx)("br",{}),Object(i.jsx)("h4",{children:"Choose before Pressing the Upload button"})]})},e}return Object(r.a)(n,[{key:"render",value:function(){return Object(i.jsxs)("div",{children:[Object(i.jsx)("h1",{children:"Upload Img"}),Object(i.jsxs)("div",{children:[Object(i.jsx)("input",{type:"file",onChange:this.onFileChange}),Object(i.jsx)("button",{onClick:this.onFileUpload,children:"Upload!"})]}),this.fileData()]})}}]),n}(c.Component);var u=function(){return Object(i.jsx)("div",{className:"App",children:Object(i.jsx)(b,{})})},f=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,44)).then((function(t){var n=t.getCLS,i=t.getFID,c=t.getFCP,l=t.getLCP,s=t.getTTFB;n(e),i(e),c(e),l(e),s(e)}))};a.a.render(Object(i.jsx)(l.a.StrictMode,{children:Object(i.jsx)(u,{})}),document.getElementById("root")),f()}},[[43,1,2]]]);
//# sourceMappingURL=main.872c1201.chunk.js.map