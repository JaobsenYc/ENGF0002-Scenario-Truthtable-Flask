(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-af030c44","chunk-d0e51818","chunk-a1e052ac","chunk-25787ef0","chunk-525aa973","chunk-2d21d841"],{"0aca":function(e,t,n){"use strict";n.r(t);var r=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"nav-title"},e._l(e.titleArr,function(t,r){return n("a",{key:r,staticClass:"item",staticStyle:{cursor:"default"}},[n("p",[e._v(e._s(t))])])}),0)},a=[],i={data:function(){return{}},computed:{stageInfo:function(){return this.$store.getters.getStageInfo(this.$route.name)},titleArr:function(){return this.stageInfo.map(function(e){return e.title}).filter(function(e){return!!e})}}},s=i,o=(n("adc7"),n("2877")),l=Object(o["a"])(s,r,a,!1,null,null,null);t["default"]=l.exports},"337b":function(e,t,n){"use strict";var r=n("ad7d"),a=n.n(r);a.a},3557:function(e,t,n){},"5d06":function(e,t,n){},"77c2":function(e,t,n){"use strict";n.r(t);var r=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"tab",attrs:{title:"关闭全部历史记录"},on:{click:e.closeReuseTab}},[n("i",{staticClass:"iconfont icon-moshubang"})])},a=[],i={name:"CloseTab",inject:["eventBus"],methods:{closeReuseTab:function(){this.eventBus.$emit("clearTap")}}},s=i,o=(n("8a1d"),n("2877")),l=Object(o["a"])(s,r,a,!1,null,"4c104e75",null);t["default"]=l.exports},"77e0":function(e,t,n){},"8a1d":function(e,t,n){"use strict";var r=n("5d06"),a=n.n(r);a.a},"93bf":function(e,t,n){
/*!
* screenfull
* v4.2.0 - 2019-04-01
* (c) Sindre Sorhus; MIT License
*/
(function(){"use strict";var t="undefined"!==typeof window&&"undefined"!==typeof window.document?window.document:{},n=e.exports,r="undefined"!==typeof Element&&"ALLOW_KEYBOARD_INPUT"in Element,a=function(){for(var e,n=[["requestFullscreen","exitFullscreen","fullscreenElement","fullscreenEnabled","fullscreenchange","fullscreenerror"],["webkitRequestFullscreen","webkitExitFullscreen","webkitFullscreenElement","webkitFullscreenEnabled","webkitfullscreenchange","webkitfullscreenerror"],["webkitRequestFullScreen","webkitCancelFullScreen","webkitCurrentFullScreenElement","webkitCancelFullScreen","webkitfullscreenchange","webkitfullscreenerror"],["mozRequestFullScreen","mozCancelFullScreen","mozFullScreenElement","mozFullScreenEnabled","mozfullscreenchange","mozfullscreenerror"],["msRequestFullscreen","msExitFullscreen","msFullscreenElement","msFullscreenEnabled","MSFullscreenChange","MSFullscreenError"]],r=0,a=n.length,i={};r<a;r++)if(e=n[r],e&&e[1]in t){for(r=0;r<e.length;r++)i[n[0][r]]=e[r];return i}return!1}(),i={change:a.fullscreenchange,error:a.fullscreenerror},s={request:function(e){return new Promise(function(n){var i=a.requestFullscreen,s=function(){this.off("change",s),n()}.bind(this);e=e||t.documentElement,/ Version\/5\.1(?:\.\d+)? Safari\//.test(navigator.userAgent)?e[i]():e[i](r?Element.ALLOW_KEYBOARD_INPUT:{}),this.on("change",s)}.bind(this))},exit:function(){return new Promise(function(e){if(this.isFullscreen){var n=function(){this.off("change",n),e()}.bind(this);t[a.exitFullscreen](),this.on("change",n)}else e()}.bind(this))},toggle:function(e){return this.isFullscreen?this.exit():this.request(e)},onchange:function(e){this.on("change",e)},onerror:function(e){this.on("error",e)},on:function(e,n){var r=i[e];r&&t.addEventListener(r,n,!1)},off:function(e,n){var r=i[e];r&&t.removeEventListener(r,n,!1)},raw:a};a?(Object.defineProperties(s,{isFullscreen:{get:function(){return Boolean(t[a.fullscreenElement])}},element:{enumerable:!0,get:function(){return t[a.fullscreenElement]}},enabled:{enumerable:!0,get:function(){return Boolean(t[a.fullscreenEnabled])}}}),n?(e.exports=s,e.exports.default=s):window.screenfull=s):n?e.exports=!1:window.screenfull=!1})()},"942b":function(e,t,n){"use strict";n.r(t);var r=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"app-nav-bar"},[n("div",{staticClass:"nav-content"},[n("breadcrumb"),n("div",{staticClass:"right-info"},[n("lin-notify",{staticClass:"lin-notify",attrs:{height:"370",trigger:"click",messages:e.messages,value:e.value,hidden:e.hidden},on:{readMessages:e.readMessages,readAll:e.readAll,viewAll:e.viewAll}}),n("clear-tab"),n("screenfull"),n("user")],1)],1)])},a=[],i=n("0aca"),s=n("c80e"),o=n("bccf"),l=n("77c2"),c={name:"NavBar",created:function(){},watch:{messages:{handler:function(){this.value=this.messages.filter(function(e){return!1===e.is_read}).length,0===this.value?this.hidden=!0:this.hidden=!1},immediate:!0}},data:function(){return{value:0,hidden:!0,messages:[]}},methods:{readAll:function(){console.log("点击了readAll")},viewAll:function(){console.log("点击了viewAll")},readMessages:function(e,t){this.messages[t].is_read=!0}},components:{Breadcrumb:i["default"],User:o["default"],Screenfull:s["default"],ClearTab:l["default"]}},u=c,f=(n("d085"),n("2877")),d=Object(f["a"])(u,r,a,!1,null,"59a7e98e",null);t["default"]=d.exports},ad7d:function(e,t,n){},adc7:function(e,t,n){"use strict";var r=n("bbaf"),a=n.n(r);a.a},bb65:function(e,t,n){"use strict";var r=n("77e0"),a=n.n(r);a.a},bbaf:function(e,t,n){},bccf:function(e,t,n){"use strict";n.r(t);var r=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"user"},[r("el-dropdown",[r("span",{staticClass:"el-dropdown-link"},[r("div",{staticClass:"nav-avatar"},[r("img",{attrs:{src:e.user.avatar||e.defaultAvatar,alt:"头像"}})])]),r("el-dropdown-menu",{staticClass:"user-box",attrs:{slot:"dropdown"},slot:"dropdown"},[r("div",{staticClass:"user-info"},[r("div",{staticClass:"avatar",attrs:{title:"点击修改头像"}},[r("img",{attrs:{src:e.user.avatar||e.defaultAvatar,alt:"头像"}}),r("label",{staticClass:"mask"},[r("i",{staticClass:"iconfont icon-icon-test",staticStyle:{"font-size":"20px"}}),r("input",{ref:"avatarInput",attrs:{type:"file",accept:"image/*"},on:{change:e.fileChange}})])]),r("div",{staticClass:"text"},[e.nicknameChanged?r("el-input",{ref:"input",attrs:{placeholder:"请输入内容",size:"small"},on:{blur:e.blur},model:{value:e.nickname,callback:function(t){e.nickname=t},expression:"nickname"}}):r("div",{staticClass:"username",on:{click:e.changeNickname}},[e._v(e._s(e.nickname))])],1),r("img",{staticClass:"corner",attrs:{src:n("d241")}})]),r("ul",{staticClass:"dropdown-box"},[r("li",{staticClass:"password",on:{click:e.goToCenter}},[r("i",{staticClass:"iconfont icon-weibaoxitongshangchuanlogo-"}),r("span",[e._v("个人中心")])]),r("li",{staticClass:"account",on:{click:e.outLogin}},[r("i",{staticClass:"iconfont icon-tuichu"}),r("span",[e._v("退出账户")])])])])],1),r("el-dialog",{attrs:{title:"裁剪",visible:e.cropVisible,width:"300px","append-to-body":!0,"close-on-click-modal":!1,"custom-class":"croppa-dialog",center:""},on:{"update:visible":function(t){e.cropVisible=t}}},[r("div",{staticStyle:{"text-align":"center"}},[r("div",{staticClass:"avatar-croppa-container"},[r("croppa",{ref:"croppa",attrs:{width:e.cropRule.width,height:e.cropRule.height,placeholder:"loading","zoom-speed":30,"disable-drag-and-drop":!1,"show-remove-button":!1,"prevent-white-space":!0,"disable-click-to-choose":!1,"disable-scroll-to-zoom":!1,"show-loading":!0,quality:e.quality,"initial-image":e.cropImg}})],1),r("div",{staticStyle:{"margin-top":"1em"}},[e._v("通过鼠标滚轮调节头像大小")])]),r("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[r("el-button",{attrs:{size:"small"},on:{click:function(t){e.cropVisible=!1}}},[e._v("取 消")]),r("el-button",{attrs:{type:"primary",size:"small"},on:{click:e.handleCrop}},[e._v("确 定")])],1)]),r("el-dialog",{staticClass:"user-dialog",attrs:{title:"修改密码","append-to-body":!0,"before-close":e.handleClose,visible:e.dialogFormVisible},on:{"update:visible":function(t){e.dialogFormVisible=t}}},[r("el-form",{ref:"form",attrs:{model:e.form,"status-icon":"",rules:e.rules,"label-position":"left","label-width":"90px"},nativeOn:{submit:function(e){e.preventDefault()}}},[r("el-form-item",{attrs:{label:"原始密码",prop:"old_password"}},[r("el-input",{attrs:{type:"password",autocomplete:"off"},model:{value:e.form.old_password,callback:function(t){e.$set(e.form,"old_password",t)},expression:"form.old_password"}})],1),r("el-form-item",{attrs:{label:"新密码",prop:"new_password"}},[r("el-input",{attrs:{type:"password",autocomplete:"off"},model:{value:e.form.new_password,callback:function(t){e.$set(e.form,"new_password",t)},expression:"form.new_password"}})],1),r("el-form-item",{attrs:{label:"确认密码",prop:"confirm_password","label-position":"top"}},[r("el-input",{attrs:{type:"password",autocomplete:"off"},model:{value:e.form.confirm_password,callback:function(t){e.$set(e.form,"confirm_password",t)},expression:"form.confirm_password"}})],1),r("el-form-item",[r("el-button",{attrs:{type:"primary"},on:{click:function(t){return e.submitForm("form")}}},[e._v("保存")]),r("el-button",{on:{click:function(t){return e.resetForm("form")}}},[e._v("重置")])],1)],1)],1)],1)},a=[],i=n("a34a"),s=n.n(i),o=n("2f62"),l=n("2b0e"),c=n("2896"),u=n.n(c),f=n("0b69"),d=(n("40d9"),n("0ca5")),p=n.n(d);function m(e,t,n,r,a,i,s){try{var o=e[i](s),l=o.value}catch(c){return void n(c)}o.done?t(l):Promise.resolve(l).then(r,a)}function h(e){return function(){var t=this,n=arguments;return new Promise(function(r,a){var i=e.apply(t,n);function s(e){m(i,r,a,s,o,"next",e)}function o(e){m(i,r,a,s,o,"throw",e)}s(void 0)})}}function g(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter(function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable})),n.push.apply(n,r)}return n}function b(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?g(n,!0).forEach(function(t){w(e,t,n[t])}):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):g(n).forEach(function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))})}return e}function w(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}l["default"].use(u.a);var v=150,A=150,k={name:"user",components:{},data:function(){var e=this,t=function(e,t,n){if(!t)return n(new Error("原始密码不能为空"));n()},n=function(t,n,r){""===n?r(new Error("请输入密码")):n.length<6?r(new Error("密码长度不能少于6位数")):(""!==e.form.checkPassword&&e.$refs.form.validateField("confirm_password"),r())},r=function(t,n,r){""===n?r(new Error("请再次输入密码")):n!==e.form.new_password?r(new Error("两次输入密码不一致!")):r()};return{username:null,dialogFormVisible:!1,nicknameChanged:!1,nickname:null,groupName:null,form:{old_password:"",new_password:"",confirm_password:""},rules:{old_password:[{validator:t,trigger:"blur",required:!0}],new_password:[{validator:n,trigger:"blur",required:!0}],confirm_password:[{validator:r,trigger:"blur",required:!0}]},cropRule:{width:v,height:A},imgRule:{minWidth:v,minHeight:A},cropVisible:!1,cropImg:"",croppa:{},imgInfo:null,quality:1,defaultAvatar:p.a}},computed:b({},Object(o["c"])(["user"])),watch:{cropVisible:function(e){e||(this.$refs.croppa.remove(),this.cropImg="",this.imgInfo=null)}},created:function(){this.init()},methods:b({},Object(o["b"])(["loginOut","setUserAndState"]),{fileChange:function(e){var t=this;if(1===e.target.files.length){var n=e.target.files[0];if(n.size>5242880)return this.$message.error("文件过大超过5M"),void this.clearFileInput(this.$refs.avatarInput);var r=window.URL.createObjectURL(n),a=new Image;a.src=r,a.onload=function(){var e=a.width,n=a.height;return e<50?(t.$message.error("图像宽度过小, 请选择大于50px的图像"),void t.clearFileInput(t.$refs.avatarInput)):n<50?(t.$message.error("图像高度过小, 请选择大于50px的图像"),void t.clearFileInput(t.$refs.avatarInput)):(t.cropImg=r,t.cropVisible=!0,void(t.$refs.croppa&&t.$refs.croppa.refresh()))},a.onerror=function(){t.$message.error("获取本地图片出现错误, 请重试"),t.clearFileInput(t.$refs.avatarInput)}}},handleCrop:function(){var e=h(s.a.mark(function e(){var t,n,r=this;return s.a.wrap(function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,this.$refs.croppa.promisedBlob("image/jpeg",.8);case 2:return t=e.sent,n=new File([t],"avatar.jpg",{type:"image/jpeg"}),e.abrupt("return",this.$axios({method:"post",url:"/cms/file",data:{file:n}}).then(function(e){return r.clearFileInput(r.$refs.avatarInput),Array.isArray(e)&&1===e.length?r.$axios({method:"put",url:"/cms/user",data:{avatar:e[0].path}}).then(function(e){return e.code<window.MAX_SUCCESS_CODE?(r.$message({type:"success",message:"更新头像成功"}),r.cropVisible=!1,f["default"].getInformation()):Promise.reject(new Error("更新头像失败"))}).then(function(e){var t=e;r.setUserAndState(t)}):(r.$message.error("头像上传失败, 请重试"),!1)}));case 5:case"end":return e.stop()}},e,this)}));function t(){return e.apply(this,arguments)}return t}(),changeNickname:function(){var e=this;this.nicknameChanged=!0,setTimeout(function(){e.$refs.input.focus()},200)},blur:function(){var e=h(s.a.mark(function e(){var t,n=this;return s.a.wrap(function(e){while(1)switch(e.prev=e.next){case 0:this.nickname&&(t=this.$store.state.user,this.nickname!==t.nickname&&"佚名"!==this.nickname&&this.$axios({method:"put",url:"/cms/user",data:{nickname:this.nickname},showBackend:!0}).then(function(e){if(e.code<window.MAX_SUCCESS_CODE)return n.$message({type:"success",message:"更新昵称成功"}),f["default"].getInformation()}).then(function(e){n.setUserAndState(e),n.nickname=e.nickname})),this.nicknameChanged=!1;case 2:case"end":return e.stop()}},e,this)}));function t(){return e.apply(this,arguments)}return t}(),init:function(){var e=this.$store.state.user;this.username=e?e.username:"未登录",this.groupName=e.groupName?e.groupName:"超级管理员",this.nickname=e&&e.nickname?e.nickname:"佚名"},goToCenter:function(){this.$router.push("/center")},handleClose:function(e){this.dialogFormVisible=!1,e()},outLogin:function(){window.location.reload(!0),this.loginOut()},submitForm:function(e){var t=this;""!==this.form.old_password||""!==this.form.new_password||""!==this.form.confirm_password?this.form.old_password!==this.form.new_password?this.$refs[e].validate(function(){var n=h(s.a.mark(function n(r){var a;return s.a.wrap(function(n){while(1)switch(n.prev=n.next){case 0:if(!r){n.next=7;break}return n.next=3,f["default"].updatePassword(t.form);case 3:a=n.sent,a.code<window.MAX_SUCCESS_CODE&&(t.$message.success("".concat(a.message)),t.resetForm(e),t.dialogFormVisible=!1,setTimeout(function(){t.loginOut();var e=window.location.origin;window.location.href=e},1e3)),n.next=10;break;case 7:return console.log("error submit!!"),t.$message.error("请填写正确的信息"),n.abrupt("return",!1);case 10:case"end":return n.stop()}},n)}));return function(e){return n.apply(this,arguments)}}()):this.$message.error("新密码不能与原始密码一样"):this.dialogFormVisible=!1},resetForm:function(e){this.$refs[e].resetFields()},clearFileInput:function(e){e.value=""}})},C=k,y=(n("337b"),n("2877")),F=Object(y["a"])(C,r,a,!1,null,"46312a10",null);t["default"]=F.exports},c80e:function(e,t,n){"use strict";n.r(t);var r=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"container",attrs:{title:"全屏/正常"}},[n("i",{staticClass:"iconfont",class:e.isFullscreen?"icon-quxiaoquanping":"icon-quanping",on:{click:e.handleFullScreen}})])},a=[],i=n("93bf"),s=n.n(i),o={data:function(){return{isFullscreen:!1}},mounted:function(){this.init()},beforeDestroy:function(){this.destroy()},methods:{handleFullScreen:function(){if(!s.a.enabled)return this.$message({message:"you browser can not work",type:"warning"}),!1;s.a.toggle()},change:function(){this.isFullscreen=s.a.isFullscreen},init:function(){s.a.enabled&&s.a.on("change",this.change)},destroy:function(){s.a.enabled&&s.a.off("change",this.change)}}},l=o,c=(n("bb65"),n("2877")),u=Object(c["a"])(l,r,a,!1,null,"5e701d13",null);t["default"]=u.exports},d085:function(e,t,n){"use strict";var r=n("3557"),a=n.n(r);a.a},d241:function(e,t){e.exports="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADcAAAAVCAMAAADVYYZJAAABS2lUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxNDAgNzkuMTYwNDUxLCAyMDE3LzA1LzA2LTAxOjA4OjIxICAgICAgICAiPgogPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIi8+CiA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgo8P3hwYWNrZXQgZW5kPSJyIj8+LUNEtwAAAARnQU1BAACxjwv8YQUAAAABc1JHQgCuzhzpAAAAVFBMVEUAAABbb6BYaZhebqBic59bbZ9WappZbJxdbZ1gcp5Za5xdbqFebqBXapdVaJlabJ1YaplWa5pbbqFcbaFabJ1Xaplfb6NdbqNecKNhcaNbb6NjcqPkGGQ/AAAAE3RSTlMAurONXdN/6T8do3ivzo3NrXCWt2J7PgAAARhJREFUOMuVkuuWgyAMhLXVIm33mhBg9/3fc5NwEW1d7Rz948lHZga7bkPDybi3i+1e0zC6pPdXKHtyVWY6jE3GtbocxL7cSp+HsOuCQUSAcb8e+yHDBQLvQbQb0hqUHXkVUSDlgIadRhCxWiRWXgg/t/9uDVVpIYaWA/jexM5YpNlCYKpg3E6/gd0rVblmHaNPa7UjNpJ04tNTAjdrnQwf2ILCKTlzfJXrWm+p75ZknzNXdV147HP2BSe3x4+vNvXgxutgeBuRgjNMRYtu+M3/ub2zH6BI7UrQbJQqrWYx9yorz796KJSAoFSMkfgoMepVTUQe6KdOBniMuVg4CAmLpJ0ytMJYzCkpWNSMnCx9oRhCMurhgfwDhnY01GZ3WbcAAAAASUVORK5CYII="}}]);