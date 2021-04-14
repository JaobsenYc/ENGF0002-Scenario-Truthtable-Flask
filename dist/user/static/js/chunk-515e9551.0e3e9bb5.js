(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-515e9551"],{"61eb":function(t,e,i){"use strict";i.r(e);var n=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",{staticClass:"lin-container"},[i("div",{staticClass:"lin-title"},[t._v("Timeline 时间线")]),i("div",{staticClass:"lin-wrap-ui"},[i("el-card",{staticStyle:{"margin-bottom":"50px"}},[i("div",{attrs:{slot:"header"},slot:"header"},[i("span",[t._v("基础用法")])]),i("el-row",[i("span",{staticClass:"demonstration"},[t._v("Timeline 可拆分成多个按照时间戳正序或倒序排列的 activity，时间戳是其区分于其他控件的重要特征，使⽤时注意与\n          Steps 步骤条等区分。")]),i("div",{staticClass:"block"},[t._v("\n          排序:\n          "),i("div",{staticClass:"radio"},[i("el-radio-group",{model:{value:t.reverse,callback:function(e){t.reverse=e},expression:"reverse"}},[i("el-radio",{attrs:{label:!0}},[t._v("倒序")]),i("el-radio",{attrs:{label:!1}},[t._v("正序")])],1)],1),i("el-timeline",{attrs:{reverse:t.reverse}},t._l(t.activities,function(e,n){return i("el-timeline-item",{key:n,attrs:{timestamp:e.timestamp}},[t._v("\n              "+t._s(e.content)+"\n            ")])}),1)],1)]),i("el-collapse",[i("el-collapse-item",{attrs:{title:"查看代码",name:"2"}},[i("div",{staticStyle:{"white-space":"pre-wrap"}},[t._v(t._s(t.base))])])],1)],1),i("el-card",{staticStyle:{"margin-bottom":"50px"}},[i("div",{attrs:{slot:"header"},slot:"header"},[i("span",[t._v("⾃定义节点样式")])]),i("el-row",[i("div",{staticClass:"block"},[i("el-timeline",t._l(t.activities1,function(e,n){return i("el-timeline-item",{key:n,attrs:{icon:e.icon,type:e.type,color:e.color,size:e.size,timestamp:e.timestamp}},[t._v("\n              "+t._s(e.content)+"\n            ")])}),1)],1)]),i("el-collapse",{staticClass:"test",staticStyle:{color:"red"}},[i("el-collapse-item",{attrs:{title:"查看代码",name:"2"}},[i("div",{staticStyle:{"white-space":"pre-wrap"}},[t._v(t._s(t.diy))])])],1)],1),i("el-card",{staticStyle:{"margin-bottom":"50px"}},[i("div",{attrs:{slot:"header"},slot:"header"},[i("span",[t._v("⾃定义时间戳")])]),i("el-row",[i("div",{staticClass:"block"},[i("el-timeline",[i("el-timeline-item",{attrs:{timestamp:"2018/4/12",placement:"top"}},[i("el-card",{staticClass:"timeLineCard"},[i("h4",[t._v("更新 Github 模板")]),i("p",[t._v("王小虎 提交于 2018/4/12 20:46")])])],1),i("el-timeline-item",{attrs:{timestamp:"2018/4/3",placement:"top"}},[i("el-card",{staticClass:"timeLineCard"},[i("h4",[t._v("更新 Github 模板")]),i("p",[t._v("王小虎 提交于 2018/4/3 20:46")])])],1),i("el-timeline-item",{attrs:{timestamp:"2018/4/2",placement:"top"}},[i("el-card",{staticClass:"timeLineCard"},[i("h4",[t._v("更新 Github 模板")]),i("p",[t._v("王小虎 提交于 2018/4/2 20:46")])])],1)],1)],1)]),i("el-collapse",{staticClass:"test",staticStyle:{color:"red"}},[i("el-collapse-item",{attrs:{title:"查看代码",name:"2"}},[i("div",{staticStyle:{"white-space":"pre-wrap"}},[t._v(t._s(t.placement))])])],1)],1)],1)])},a=[],l={name:"",components:{},data:function(){return{base:'<div class="block">\n  <div class="radio">\n    排序：\n    <el-radio-group v-model="reverse">\n      <el-radio :label="true">倒序</el-radio>\n      <el-radio :label="false">正序</el-radio>\n    </el-radio-group>\n  </div>\n\n  <el-timeline :reverse="reverse">\n    <el-timeline-item\n      v-for="(activity, index) in activities"\n      :key="index"\n      :timestamp="activity.timestamp">\n      {{activity.content}}\n    </el-timeline-item>\n  </el-timeline>\n</div>\n\n<script>\n  export default {\n    data() {\n      return {\n        reverse: true,\n        activities: [{\n          content: \'活动按期开始\',\n          timestamp: \'2018-04-15\'\n        }, {\n          content: \'通过审核\',\n          timestamp: \'2018-04-13\'\n        }, {\n          content: \'创建成功\',\n          timestamp: \'2018-04-11\'\n        }]\n      };\n    }\n  };\n<\/script>\n        ',diy:"\n        <div class=\"block\">\n  <el-timeline>\n    <el-timeline-item\n      v-for=\"(activity, index) in activities\"\n      :key=\"index\"\n      :icon=\"activity.icon\"\n      :type=\"activity.type\"\n      :color=\"activity.color\"\n      :size=\"activity.size\"\n      :timestamp=\"activity.timestamp\">\n      {{activity.content}}\n    </el-timeline-item>\n  </el-timeline>\n</div>\n\n<script>\n  export default {\n    data() {\n      return {\n        activities: [{\n          content: '支持使用图标',\n          timestamp: '2018-04-12 20:46',\n          size: 'large',\n          type: 'primary',\n          icon: 'el-icon-more'\n        }, {\n          content: '支持自定义颜色',\n          timestamp: '2018-04-03 20:46',\n          color: '#3963bc'\n        }, {\n          content: '支持自定义尺寸',\n          timestamp: '2018-04-03 20:46',\n          size: 'large'\n        }, {\n          content: '默认样式的节点',\n          timestamp: '2018-04-03 20:46'\n        }]\n      };\n    }\n  };\n<\/script>",placement:'<div class="block">\n  <el-timeline>\n    <el-timeline-item timestamp="2018/4/12" placement="top">\n      <el-card>\n        <h4>更新 Github 模板</h4>\n        <p>王小虎 提交于 2018/4/12 20:46</p>\n      </el-card>\n    </el-timeline-item>\n    <el-timeline-item timestamp="2018/4/3" placement="top">\n      <el-card>\n        <h4>更新 Github 模板</h4>\n        <p>王小虎 提交于 2018/4/3 20:46</p>\n      </el-card>\n    </el-timeline-item>\n    <el-timeline-item timestamp="2018/4/2" placement="top">\n      <el-card>\n        <h4>更新 Github 模板</h4>\n        <p>王小虎 提交于 2018/4/2 20:46</p>\n      </el-card>\n    </el-timeline-item>\n  </el-timeline>\n</div>',reverse:!0,activities:[{content:"活动按期开始",timestamp:"2018-04-15"},{content:"通过审核",timestamp:"2018-04-13"},{content:"创建成功",timestamp:"2018-04-11"}],activities1:[{content:"支持使用图标",timestamp:"2018-04-12 20:46",size:"large",type:"primary",icon:"el-icon-more"},{content:"支持自定义颜色",timestamp:"2018-04-03 20:46",color:"#3963bc"},{content:"支持自定义尺寸",timestamp:"2018-04-03 20:46",size:"large"},{content:"默认样式的节点",timestamp:"2018-04-03 20:46"}]}},computed:{},watch:{},mounted:function(){this.init()},methods:{init:function(){}}},s=l,c=(i("85dd"),i("2877")),r=Object(c["a"])(s,n,a,!1,null,"2046bfac",null);e["default"]=r.exports},"85dd":function(t,e,i){"use strict";var n=i("9ba5"),a=i.n(n);a.a},"9ba5":function(t,e,i){}}]);