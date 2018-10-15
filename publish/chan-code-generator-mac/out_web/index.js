define('app/jsp/mgmtbusicircle/index',function(require,exports,module) {
	'use strict';
	var $=require('jquery'),
		Widget=require('arale-widget/1.2.0/widget'),
		Dialog=require("app/common/ai-dialog/src/dialog"),
		AjaxController=require('app/common/ai-ajax/1.0.0/index');
	require("jsviews/jsrender.min");
	require("jsviews/jsviews.min");
	require("app/util/jsviews-ext");
	require("jquery-validation/1.15.1/jquery.validate");
	require("app/util/jquery-validate-ext");
	require("app/common/ai-paging/ai.pagination");
	require("app/util/jquery.dotdotdot");
	var IEPlaceHolder=require("app/jsp/layout/ieplaceholder");
	var iePlaceHolder=new IEPlaceHolder();
	var ajaxController=new AjaxController();
	var HEIGHT=25;
	
	var svIndexPager=Widget.extend({
		attrs:{clickId:""},
		Statics:{DEFAULT_PAGE_SIZE:10},
		params:{},
		events:{
			"click #tab-query":"_seeTabQuery",
			"click #highquery":"_highQuery",
			"click #fuzzyquery":"_fuzzyQuery"
		},
		setup:function() {
			var _this=this;
			_this._initPage();
			_this._initEvent();
			_this._queryList({});
			iePlaceHolder._placeholder();
		},
		_initPage:function() {
			var _this=this;
			_this._initBusiCountys();
			_this._initSysParams({typeCode:"",paramCode:""},"#htmlDivId","#scripTmplId");
		},
		_initBusiCountys:function() {
			$("#busiRegCounty").html('<option value="">请选择</option>');
			ajaxController.ajax({
				type:"post",data:{},processing:false,
				url:_base+"/sysservice/getBusiCountys",
				success:function(data) {
					if(data&&data.result) {
						$("#busiRegCounty").append($.templates("#busiCountyTmpl").render(data.result));
					}
				}
			});
		},
		
		_initEvent:function() {
			var _this=this;
			$("#item-list").delegate(".itemdelete","click",function() {
				var itemId=$(this).parent().attr("data-id");
				var itemCode=$(this).parent().attr("data-code");
				_this._delItem(itemId,itemCode);
			});
		},
		

		_seeTabQuery:function() {
			var _this=this;
			_this._queryList({});
		},
		_fuzzyQuery:function() {
			var _this=this;
			var queryData={
				itemName:$("#fuzzyinput").val()
			};
			_this._queryList(queryData);
		},
		_highQuery:function() {
			var _this=this;
			var queryData={
				itemName:$("#itemName").val(),
				busiRegCountyCode:$("#busiRegCounty").val()
			};
			_this._queryList(queryData);
		},
		_queryList:function(queryData) {
			var _this=this;
			// console.log(queryData);
			$("#item-pagination").runnerPagination({
				method:"POST",dataType:"json",data:queryData,
				url:_base+"/mgmtbusicircle/queryPageList",
				renderId:"item-list",messageId:"item-showMessage",
				pageSize:5,visiblePages:5,processing:true,
				message:"正在为您查询数据...",
				render:function(data) {
					// console.log(data);
					if(data&&data.result) {
						$("#item-list").html($.templates("#itemTmpl").render(data.result));
						// _this._clearQueryInput();
					}
				}
			});
		},
		_clearQueryInput:function() {
			$(":text").val('');
			$("select").val('');
		},
		
		
		_delItem:function(itemId,itemCode) {
			new Dialog({
				title:"提示",icon:'prompt',okValue:"确定",cancelValue:"取消",
				content:"确认要删除？<br/>删除前请确认......。",
				ok:function(){
					ajaxController.ajax({
						type:"post",processing: true,message:"已提交，请稍后...",
						url:_base+"/mgmtbusicircle/delete",
						data:{itemId:itemId,itemCode:itemCode},
						success:function(data) {
							if(data.resultCode=="000000") {
								// window.location.href=_base+"/mgmtbusicircle/index";
								_this._queryList({});
							}else {
								_this._showWarn(data.resultMessage);
							}
						}
					});
				},
				cancel:function(){this.close();}
			}).showModal();
		},
		
		_initSysParams:function(queryData,htmlId,TmplId) {
			var _this=this;
			$(htmlId).html('<option value="">请选择</option>');
			ajaxController.ajax({
				type:"post",data:queryData,
				url:_base+"/sysparam/getParams",
				success:function(data) {
					if(data.success&&data.result) {
						$(htmlId).append($.templates(TmplId).render(data.result));
					}
				}
			});
		},
		_serializeObject:function(formId) {
			var o={};
			var a=$("#"+formId).serializeArray();
			$.each(a,function() {
				if(o[this.name]!==undefined) {
					if(!o[this.name].push) {o[this.name]=[o[this.name]];}
					o[this.name].push(this.value||'');
				} 
				else {o[this.name]=this.value||'';}
			});
			return o;
		},
    	_showWarn:function(msg){
			new Dialog({
				content:msg,title:"提示",icon:'warning',
				okValue:"确定",ok:function(){this.close();}
			}).showModal();
		}
	
	});
	module.exports=svIndexPager;
});