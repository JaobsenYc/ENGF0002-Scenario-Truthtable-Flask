(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-5708c90e"],{a569:function(e,t,n){"use strict";var i=n("b5a2"),a=n.n(i);a.a},b3b8:function(e,t,n){"use strict";var i=n("f378"),a=n.n(i);a.a},b5a2:function(e,t,n){},de53:function(e,t,n){"use strict";n.r(t);var i=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"lin-table"},[n("el-table",{directives:[{name:"loading",rawName:"v-loading",value:e.loading,expression:"loading"}],ref:"linTable",attrs:{stripe:"","row-key":"id",border:e.border,data:e.currentData,"highlight-current-row":!!e.highlightCurrentRow,"element-loading-text":e.loadingText,"element-loading-spinner":e.loadingIcon,"element-loading-background":e.loadingBG,"row-class-name":e.rowClassName},on:{"current-change":e.handleCurrentChange,"selection-change":e.handleSelectionChange,"select-all":e.selectAll,"row-click":e.rowClick}},[e.type?n("el-table-column",{attrs:{type:e.type,width:"55"}}):e._e(),e.index?n("el-table-column",{attrs:{type:e.index,index:e.currentIndex,width:"55"}}):e._e(),e._l(e.filterTableColumn,function(e){return n("el-table-column",{key:e.id,attrs:{prop:e.prop,label:e.label,"show-overflow-tooltip":!0,filters:e.filters?e.filters:null,"filter-method":e.filterMethod?e.filterMethod:null,"column-key":e.filterMethod?e.prop:null,formatter:e.formatter?e.formatter:null,sortable:!!e.sortable&&e.sortable,fixed:!!e.fixed&&e.fixed,width:e.width?e.width:""}})}),e.operate.length>0?n("el-table-column",{attrs:{label:"Operation",fixed:"right",width:"275"},scopedSlots:e._u([{key:"default",fn:function(t){return e._l(e.operate,function(i,a){return n("el-button",{directives:[{name:"permission",rawName:"v-permission",value:{permission:i.permission?i.permission:"",type:"disabled"},expression:"{ permission: item.permission ? item.permission : '', type: 'disabled' }"}],key:a,attrs:{type:i.type,plain:"",size:"mini"},nativeOn:{click:function(n){return n.preventDefault(),n.stopPropagation(),e.buttonMethods(i.func,t.$index,t.row)}}},[e._v(e._s(i.name))])})}}],null,!1,2525776182)}):e._e()],2),e.pagination?n("el-pagination",{staticClass:"pagination",attrs:{background:"",layout:"prev, pager, next","page-size":e.pagination.pageSize?e.pagination.pageSize:10,total:e.pagination.pageTotal?e.pagination.pageTotal:null,"current-page":e.pagination.currentPage?e.pagination.currentPage:1},on:{"current-change":e.currentChange}}):e._e()],1)},a=[];function l(e){return s(e)||o(e)||r()}function r(){throw new TypeError("Invalid attempt to spread non-iterable instance")}function o(e){if(Symbol.iterator in Object(e)||"[object Arguments]"===Object.prototype.toString.call(e))return Array.from(e)}function s(e){if(Array.isArray(e)){for(var t=0,n=new Array(e.length);t<e.length;t++)n[t]=e[t];return n}}var u={props:{tableColumn:{type:Array,default:function(){return[]}},tableData:{type:Array,default:function(){return[]}},operate:{type:Array,default:function(){return[]}},customColumn:{type:Array,default:function(){return[]}},fixedLeftList:{type:Array,default:function(){return[]}},fixedRightList:{type:Array,default:function(){return[]}},type:{type:String,default:null},index:{index:String,default:""},highlightCurrentRow:{type:Boolean,default:!1},loading:{type:Boolean,default:!1},loadingText:{type:String,default:""},loadingIcon:{type:String,default:"el-icon-loading"},loadingBG:{type:String,default:"rgba(255,255,255,0.5)"},pagination:{type:[Object,Boolean],default:!1},border:{type:Boolean,default:!1}},data:function(){return{filterTableColumn:[],currentPage:1,currentData:[],selectedTableData:[],currentRow:null,oldVal:[],oldKey:[],currentIndex:1,rowClassName:""}},created:function(){},beforeMount:function(){sessionStorage.setItem("selectedTableData",JSON.stringify([]))},methods:{buttonMethods:function(e,t,n){var i=this,a=this.$options.methods;a[e](i,t,n)},openQuiz:function(e,t,n){e.$emit("openQuiz",{index:t,row:n})},handleEdit:function(e,t,n){e.$emit("handleEdit",{index:t,row:n})},handleDelete:function(e,t,n){e.$emit("handleDelete",{index:t,row:n})},goToGroupEditPage:function(e,t,n){e.$emit("goToGroupEditPage",{index:t,row:n})},toggleSelection:function(e,t){var n=this;e?e.forEach(function(e){n.$refs.linTable.toggleRowSelection(e,t)}):this.$refs.linTable.clearSelection()},selectAll:function(e){this.oldKey=e.map(function(e){return e.key})},handleCurrentChange:function(e,t){this.currentRow=e,this.$emit("handleCurrentChange",{val:e,oldVal:t})},rowClick:function(e){if(this.oldKey.includes(e.key)){this.oldKey=this.oldKey.filter(function(t){return t!==e.key});var t=this.oldVal.filter(function(t){return t.key!==e.key});this.handleSelectionChange(t),this.toggleSelection(this.currentData.filter(function(t){return t.key===e.key}),!1)}else{this.oldKey.push(e.key);var n=this.oldVal.concat(e);this.handleSelectionChange(n),this.toggleSelection(this.currentData.filter(function(t){return t.key===e.key}))}if(this.currentOldRow&&this.currentOldRow.key===e.key)return this.$refs.linTable.setCurrentRow(),void(this.currentOldRow=null);this.currentOldRow=e},currentChange:function(e){var t=this,n=[];this.oldVal=[],this.currentPage=e,this.selectedTableData=JSON.parse(sessionStorage.getItem("selectedTableData")),this.currentData=this.tableData.filter(function(e,n){return n>=(t.currentPage-1)*t.pagination.pageSize&&n<t.currentPage*t.pagination.pageSize}),this.$emit("currentChange",e),this.selectedTableData.forEach(function(e){for(var i=0;i<t.currentData.length;i++)t.currentData[i].key===e.key&&(t.oldVal.push(t.currentData[i]),n.push(t.currentData[i]))}),this.$nextTick(function(){t.toggleSelection(n)}),this.currentIndex=(this.currentPage-1)*this.pagination.pageSize+1},handleSelectionChange:function(e){var t=e.map(function(e){return e.key}),n=this.oldVal.map(function(e){return e.key});if(this.selectedTableData=JSON.parse(sessionStorage.getItem("selectedTableData")),0===this.selectedTableData.length)return this.selectedTableData=this.selectedTableData.concat(e),this.$emit("selection-change",this.selectedTableData),this.oldVal=l(e),void sessionStorage.setItem("selectedTableData",JSON.stringify(this.selectedTableData));if(t.length<n.length){var i=n.filter(function(e){return!t.includes(e)});this.selectedTableData=this.selectedTableData.filter(function(e){return!i.includes(e.key)}),this.$emit("selection-change",this.selectedTableData)}else{var a=t.filter(function(e){return!n.includes(e)}),r=e.filter(function(e){return a.includes(e.key)});this.selectedTableData=this.selectedTableData.concat(r),this.$emit("selection-change",this.selectedTableData)}sessionStorage.setItem("selectedTableData",JSON.stringify(this.selectedTableData)),this.oldVal=l(e)}},watch:{fixedLeftList:{handler:function(){var e=this;this.filterTableColumn.map(function(t,n){return e.fixedLeftList.indexOf(t.label)>-1?e.$set(e.filterTableColumn[n],"fixed","left"):-1===e.fixedRightList.indexOf(t.label)&&e.$set(e.filterTableColumn[n],"fixed",!1),""})},deep:!0,immediate:!0},fixedRightList:{handler:function(){var e=this;this.filterTableColumn.map(function(t,n){return e.fixedRightList.indexOf(t.label)>-1?e.$set(e.filterTableColumn[n],"fixed","right"):-1===e.fixedLeftList.indexOf(t.label)&&e.$set(e.filterTableColumn[n],"fixed",!1),""})},deep:!0,immediate:!0},customColumn:{handler:function(e){e.length>1&&(this.filterTableColumn=this.tableColumn.filter(function(t){return e.indexOf(t.label)>-1}))},deep:!0},tableData:{handler:function(){var e=this;this.pagination&&this.pagination.pageSize?this.currentData=this.tableData.filter(function(t,n){return n<e.pagination.pageSize}):this.currentData=this.tableData},deep:!0,immediate:!0},tableColumn:{handler:function(){var e=this;this.customColumn.length>1?this.filterTableColumn=this.tableColumn.filter(function(t){return e.customColumn.indexOf(t.label)>-1}):this.filterTableColumn=this.tableColumn},deep:!0,immediate:!0}}},c=u,d=(n("a569"),n("b3b8"),n("2877")),f=Object(d["a"])(c,i,a,!1,null,"c5055eac",null);t["default"]=f.exports},f378:function(e,t,n){}}]);