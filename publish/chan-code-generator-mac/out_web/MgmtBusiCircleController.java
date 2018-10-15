package com.ai.channel.mgmt.web.controller.chlbusicircle;

import java.util.ArrayList;
import java.util.List;

import javax.servlet.http.HttpServletRequest;

import org.apache.commons.lang3.StringUtils;
import org.apache.shiro.authz.annotation.RequiresPermissions;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import com.ai.channel.base.BusinessConstants;
import com.ai.channel.base.vo.BaseResponse;
import com.ai.channel.base.vo.PageArg;
import com.ai.channel.base.vo.PageResult;
import com.ai.channel.common.dubbo.util.DubboConsumerFactory;
import com.ai.channel.common.util.CollectionUtil;
import com.ai.channel.mgmt.api.chlbusicircle.interfaces.IMgmtBusiCircleSV;
import com.ai.channel.mgmt.api.chlbusicircle.param.QueryMgmtBusiCircleRequest;
import com.ai.channel.mgmt.api.chlbusicircle.param.SaveMgmtBusiCircleRequest;
import com.ai.channel.mgmt.api.chlbusicircle.vo.MgmtBusiCircleDetailVo;
import com.ai.channel.mgmt.api.chlbusicircle.vo.MgmtBusiCircleItemVo;
import com.ai.channel.mgmt.web.utils.SessionUserUtil;
import com.ai.channel.sso.module.SessionUser;
import com.alibaba.fastjson.JSON;

/**
 * MgmtBusiCircleController.java
 * 
 * 
 * @date 2018-10-15 21:05 
 * @author wygdove
 */
@Controller
@RequestMapping("/mgmtbusicircle")
public class MgmtBusiCircleController {
	private static final Logger log=LoggerFactory.getLogger(MgmtBusiCircleController.class);
	
	@RequestMapping("/index")
    public String toIndex(HttpServletRequest request,Model model) {
    	log.info("controller:/mgmtbusicircle/index");
    	return "mgmtbusicircle/index";
    }
	
	@RequestMapping("/toSave")
    public String toSave(HttpServletRequest request,Model model) {
    	log.info("controller:/mgmtbusicircle/toSave");
    	String itemId=request.getParameter("itemId");
    	itemId=StringUtils.isBlank(itemId)?"":itemId;
    	log.info("/mgmtbusicircle/toSave itemId:"+JSON.toJSONString(itemId));
    	model.addAttribute("itemId",itemId);
    	return "mgmtbusicircle/save";
    }
	
	@RequestMapping("/toDetail")
	public String toDetail(HttpServletRequest request,Model model) {
		log.info("controller:/mgmtbusicircle/toDetail");
		String itemId=request.getParameter("itemId");
		itemId=StringUtils.isBlank(itemId)?"":itemId;
		log.info("/mgmtbusicircle/toDetail itemId:"+JSON.toJSONString(itemId));
		model.addAttribute("itemId",itemId);
		return "mgmtbusicircle/detail";
	}
	
	
	
	@RequiresPermissions("mgmt:mgmtbusicircle:save")
	@RequestMapping("save")
    @ResponseBody
    public BaseResponse<String> save(HttpServletRequest request,SaveMgmtBusiCircleRequest saveRequest) {
    	log.info("controller:/mgmtbusicircle/save");
    	BaseResponse<String> response=new BaseResponse<>();
    	IMgmtBusiCircleSV mgmtBusiCircleSV=DubboConsumerFactory.getService(IMgmtBusiCircleSV.class);
    	SessionUser sessionUser=SessionUserUtil.getSessionUser();
    	saveRequest.setUserId(sessionUser.getUserName());
		log.info("/mgmtbusicircle/save saveRequest:"+JSON.toJSONString(saveRequest));
		String recordFlag="";
		if(StringUtils.isBlank(saveRequest.getGridId())) {
			response=mgmtBusiCircleSV.addMgmtBusiCircle(saveRequest);
		}else {
			response=mgmtBusiCircleSV.updateMgmtBusiCircle(saveRequest);
		}
		log.info("/mgmtbusicircle/save response:"+JSON.toJSONString(response));
    	return response;
    }
	
	
	@RequiresPermissions("mgmt:mgmtbusicircle:save")
	@RequestMapping("delete")
    @ResponseBody
    public BaseResponse<String> delete(HttpServletRequest request,SaveMgmtBusiCircleRequest saveRequest) {
    	log.info("controller:/mgmtbusicircle/delete");
    	IMgmtBusiCircleSV mgmtBusiCircleSV=DubboConsumerFactory.getService(IMgmtBusiCircleSV.class);
    	SessionUser sessionUser=SessionUserUtil.getSessionUser();
    	saveRequest.setUserId(sessionUser.getUserName());
    	saveRequest.setDelflag(""+GisConstants.GridDelFlag.DEL_YES);
		log.info("/mgmtbusicircle/delete saveRequest:"+JSON.toJSONString(saveRequest));
		BaseResponse<String> response=mgmtBusiCircleSV.deleteMgmtBusiCircle(saveRequest);
		log.info("/mgmtbusicircle/delete response:"+JSON.toJSONString(response));
    	return response;
    }
	
	
	@RequestMapping("queryDetail")
    @ResponseBody
    public BaseResponse<MgmtBusiCircleDetailVo> queryDetail(HttpServletRequest request,String mgmtbusicircleId) {
    	log.info("controller:/mgmtbusicircle/queryDetail");
    	IMgmtBusiCircleSV mgmtBusiCircleSV=DubboConsumerFactory.getService(IMgmtBusiCircleSV.class);
    	QueryMgmtBusiCircleRequest queryRequest=new QueryMgmtBusiCircleRequest();
//    	queryRequest.setId("id");
		log.info("/mgmtbusicircle/queryDetail queryRequest:"+JSON.toJSONString(queryRequest));
		BaseResponse<MgmtBusiCircleDetailVo> response=mgmtBusiCircleSV.queryDetailMgmtBusiCircle(queryRequest);
		log.info("/mgmtbusicircle/queryDetail response:"+JSON.toJSONString(response));
    	return response;
    }
	
	
	@RequestMapping("queryPageList")
    @ResponseBody
    public BaseResponse<PageResult<MgmtBusiCircleItemVo>> queryPageList(HttpServletRequest request,QueryMgmtBusiCircleRequest queryRequest) {
    	log.info("controller:/mgmtbusicircle/queryPageList");
    	SessionUser sessionUser=SessionUserUtil.getSessionUser();
		queryRequest=this.setQueryUser(sessionUser,queryRequest);
		if(queryRequest==null) {
			return new BaseResponse<>(false,BusinessConstants.BUSI_FAILURE_CODE,"错误：用户没有权限！");
		}
    	IMgmtBusiCircleSV mgmtBusiCircleSV=DubboConsumerFactory.getService(IMgmtBusiCircleSV.class);
    	int pageNo=1,pageSize=5;
        try{ pageNo=Integer.parseInt(request.getParameter("pageNo"));
        	pageSize=Integer.parseInt(request.getParameter("pageSize"));
        }catch(Exception e) {pageNo=1;pageSize=5;}
		queryRequest.setPage(new PageArg(pageNo,pageSize));
		log.info("/mgmtbusicircle/queryPageList queryRequest:"+JSON.toJSONString(queryRequest));
		BaseResponse<PageResult<MgmtBusiCircleItemVo>> response=mgmtBusiCircleSV.queryPageMgmtBusiCircle(queryRequest);
		log.info("/mgmtbusicircle/queryPageList response:"+JSON.toJSONString(response));
    	return response;
    }
	@RequestMapping("queryList")
    @ResponseBody
    public BaseResponse<List<MgmtBusiCircleItemVo>> queryList(HttpServletRequest request,QueryMgmtBusiCircleRequest queryRequest) {
    	log.info("controller:/mgmtbusicircle/queryList");
    	IMgmtBusiCircleSV mgmtBusiCircleSV=DubboConsumerFactory.getService(IMgmtBusiCircleSV.class);
    	SessionUser sessionUser=SessionUserUtil.getSessionUser();
		queryRequest=this.setQueryUser(sessionUser,queryRequest);
		log.info("/mgmtbusicircle/queryPageList queryList:"+JSON.toJSONString(queryRequest));
		BaseResponse<List<MgmtBusiCircleItemVo>> response=mgmtBusiCircleSV.queryListMgmtBusiCircle(queryRequest);
		log.info("/mgmtbusicircle/queryPageList response:"+JSON.toJSONString(response));
    	return response;
    }
	private QueryMgmtBusiCircleRequest setQueryUser(SessionUser sessionUser,QueryMgmtBusiCircleRequest request) {
		List<UserBusiAreaVO> userBusiRegList=sessionUser.getUserBusiRegList();
		log.info("/mgmtbusicircle/setQueryUser userBusiRegList:"+JSON.toJSONString(userBusiRegList));
		List<String> rolenames=sessionUser.getRolenames();
		log.info("/mgmtbusicircle/setQueryUser rolenames:"+JSON.toJSONString(rolenames));
		if(!CollectionUtil.isEmpty(userBusiRegList)&&!CollectionUtil.isEmpty(rolenames)) {
			
		}else {
			request=null;
		}
		return request;
	}


}
