<!-- 
@filename: 
@author: wygdove
@date 2018-10-15 20:59: 
@update: 
-->
<%@ page contentType="text/html;charset=UTF-8" language="java"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
<title></title>
<%@ include file="/inc/inc.jsp"%>
<style>
</style>
</head>
<body>
	<div class="l-crm">
		<p><a href="${_base}/goHome">门户</a>></p>
		<p><a href="${_base}/"></a>></p>
		<p><a href="${_base}/mgmtbusicircle/index"></a></p>
	</div>
	<div class="l-bd">
		<div id="funtabs" class="trading-tab seven-tab">
			<ul class="z-crt">
				<a id="tab-query" href="#">
					<li class="bj"><i class="icon iconfont">&#xe6ee;</i></li>
					<li class="rt"><p>信息</p><p class="line"></p></li>
				</a>
			</ul>
			<shiro:hasPermission name="mgmt:mgmtbusicircle:save">
				<ul class="ml-10">
					<a href="${_base}/mgmtbusicircle/toSave">
						<li class="bj"><i class="icon iconfont">&#xe641;</i></li>
						<li class="rt"><p>新增</p><p class="line"></p></li>
					</a>
				</ul>
			</shiro:hasPermission>
		</div>
		<div class="m-trk-sch">
			<div class="m-trk-tt">
				<p class="line"></p>
				<p class="title">列表</p>
				<p class="rt">
					<span class="sh">
						<input id="fuzzyinput" type="text" class="int-text int-200" placeholder="名称">
						<a id="fuzzyquery" href="#" title="搜索"><i class="icon iconfont">&#xe65e;</i></a>
					</span>
					<span class="gj">高级搜索<i class="icon-double-angle-down"></i></span>
				</p>
			</div>
			<div class="m-xd-warp">
				<div class="m-xd-sh" style="display:none;">
					<ul>
						<li>
							<p class="bt">名称：</p>
							<p><input id="searchName" name="searchName" type="text" class="int-text int180" /></p>
						</li>
						<li>
							<p class="bt">网格所属区县：</p>
							<p><select id="searchBusiRegCounty" name="searchBusiRegCounty" class="select select-180"></select></p>
						</li>
						<li><a id="highquery" href="#" class="btn btn-green btn40"><i class="icon iconfont">&#xe669;</i></a></li>
					</ul>
				</div>
				<div class="sh-ct-nb">
					<div class="m-trk-lst pd-0" id="item-list"></div>
					<div class="m-pag">
						<div class="paging paging-large">
							<ul id="item-pagination"></ul>
						</div>
					</div>
					<div id="item-showMessage"></div>
				</div>
			</div>
		</div>
	</div>


<script id="searchBusiCountyTmpl" type="text/x-jsrender">
{{for}}
	<option value="{{:code }}">{{:name }}</option>
{{/for}}
</script>
<script id="itemTmpl" type="text/x-jsrender">
{{for}}
	<div class="m-trk-lst-ct backnone bb-none">
		<div class="m-starsh-lst mb-u">
			<ul>
				<li class="x-wh pl-10"><p class="">编码：</p><p>{{:Code}}</p></li>
				<li class="x-wh"><p class="">归属区县：</p><p>{{:busiRegCountyName}}</p></li>
			</ul>
		</div>
	</div>
{{/for}}
</script>
<script id="sysParamTmpl" type="text/x-jsrender">
{{for}}
	<option value="{{:columnValue }}">{{:columnDesc }}</option>
{{/for}}
</script>
<script type="text/javascript">
$(document).ready(function(){
	var pager;
	seajs.use(['app/jsp/mgmtbusicircle/index'],function(svIndexPager) {
		pager=new svIndexPager({element:document.body});
		pager.render();
	});
});
</script>
</body>
</html>
