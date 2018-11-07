package com.cmi.res.business.impl;

import com.ai.appframe2.common.AIException;
import com.ai.appframe2.service.ServiceFactory;
import com.alibaba.fastjson.JSON;
import com.cmi.common.domain.Page;
import com.cmi.common.domain.PageResult;
import com.cmi.common.domain.Response;
import com.cmi.common.util.DateUtil;
import com.cmi.res.atom.bo.ResStorageStaffBean;
import com.cmi.res.atom.interfaces.IResStorageStaffAtomSV;
import com.cmi.res.business.interfaces.IResStorageStaffBizSV;
import com.cmi.res.constants.ExceptCodeConstants;
import com.cmi.res.domain.resstoragestaff.params.QueryResStorageStaffRequest;
import com.cmi.res.domain.resstoragestaff.params.SaveResStorageStaffRequest;
import com.cmi.res.domain.resstoragestaff.vo.ResStorageStaffDetailVo;
import com.cmi.res.domain.resstoragestaff.vo.ResStorageStaffItemVo;
import com.cmi.res.util.PageUtil;
import com.cmi.res.util.VoConvertUtil;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @Title:
 * @Description:
 * @Date: 2018-11-07 09:42
 * @Author: wygdove
 */
public class ResStorageStaffBizSVImpl implements IResStorageStaffBizSV {

	@Override
	public Response<String> addResStorageStaff(SaveResStorageStaffRequest request) throws Exception {
		Response<String> response=new Response<>(true,ExceptCodeConstants.Special.SUCCESS,"success");
//		long id=SeqUtil.createId();
		IResStorageStaffAtomSV resStorageStaffAtomSV=(IResStorageStaffAtomSV)ServiceFactory.getService(IResStorageStaffAtomSV.class);
		ResStorageStaffBean beanRequest=this.setAtomSave(request);
//		beanRequest.setId(id);

		resStorageStaffAtomSV.add(beanRequest);

//		response.setResult(""+id);
		response.setSuccess(true);
		response.setResultCode(ExceptCodeConstants.Special.SUCCESS);
		response.setResultMessage("success");
		return response;
	}

	@Override
	public Response<String> addBatchResStorageStaff(SaveResStorageStaffRequest request) {
		return null;
	}

	@Override
	public Response<String> updateResStorageStaff(SaveResStorageStaffRequest request) throws Exception {
		Response<String> response=new Response<>(true,ExceptCodeConstants.Special.SUCCESS,"success");

		IResStorageStaffAtomSV resStorageStaffAtomSV=(IResStorageStaffAtomSV)ServiceFactory.getService(IResStorageStaffAtomSV.class);
		ResStorageStaffBean beanRequest=this.setAtomSave(request);
		resStorageStaffAtomSV.update(beanRequest);

//		response.setResult(request.getId());
		response.setSuccess(true);
		response.setResultCode(ExceptCodeConstants.Special.SUCCESS);
		response.setResultMessage("success");
		return response;
	}

	@Override
	public Response<String> deleteResStorageStaff(SaveResStorageStaffRequest request) throws Exception {
		Response<String> response=new Response<>(true,ExceptCodeConstants.Special.SUCCESS,"success");

		IResStorageStaffAtomSV resStorageStaffAtomSV=(IResStorageStaffAtomSV)ServiceFactory.getService(IResStorageStaffAtomSV.class);
		ResStorageStaffBean beanRequest=this.setAtomSave(request);
		resStorageStaffAtomSV.update(beanRequest);

		response.setResult(request.getOrderId());
		response.setSuccess(true);
		response.setResultCode(ExceptCodeConstants.Special.SUCCESS);
		response.setResultMessage("success");
		return response;
	}

	@Override
	public Response<ResStorageStaffDetailVo> queryDetailResStorageStaff(QueryResStorageStaffRequest request) throws Exception {
		Response<ResStorageStaffDetailVo> response=new Response<>(true,ExceptCodeConstants.Special.SUCCESS,"success");
		ResStorageStaffDetailVo result=new ResStorageStaffDetailVo();

		if(request==null||request.getLocale()==null) {
			response.setResult(result);
			response.setSuccess(false);
			response.setResultCode(ExceptCodeConstants.Special.PARAM_IS_NULL);
			response.setResultMessage("request and param can't be null");
			return response;
		}

		IResStorageStaffAtomSV resStorageStaffAtomSV=(IResStorageStaffAtomSV)ServiceFactory.getService(IResStorageStaffAtomSV.class);
		ResStorageStaffBean beanRequest=new ResStorageStaffBean();
		try {
			beanRequest.setId(Long.parseLong(request.getId()));
		}catch(Exception e) {
			response.setResult(result);
			response.setSuccess(false);
			response.setResultCode(ExceptCodeConstants.Special.PARAM_TYPE_NOT_RIGHT);
			response.setResultMessage("param type is not right");
			return response;
		}
		ResStorageStaffBean ResStorageStaffBean=resStorageStaffAtomSV.queryById(beanRequest);
		result=this.setVoDetail(ResStorageStaffBean);

		response.setResult(result);
		response.setSuccess(true);
		response.setResultCode(ExceptCodeConstants.Special.SUCCESS);
		response.setResultMessage("success");
		return response;
	}

	@Override
	public Response<List<ResStorageStaffItemVo>> queryListResStorageStaff(QueryResStorageStaffRequest request) throws Exception {
		Response<List<ResStorageStaffItemVo>> response=new Response<>(true,ExceptCodeConstants.Special.SUCCESS,"success");
		List<ResStorageStaffItemVo> result=new ArrayList<>();

		if(request==null||request.getLocale()==null) {
			response.setResult(result);
			response.setSuccess(false);
			response.setResultCode(ExceptCodeConstants.Special.PARAM_IS_NULL);
			response.setResultMessage("request and param can't be null");
			return response;
		}

		IResStorageStaffAtomSV resStorageStaffAtomSV=(IResStorageStaffAtomSV)ServiceFactory.getService(IResStorageStaffAtomSV.class);
		ResStorageStaffBean beanRequest=this.setAtomQuery(request);
		Map<String,Object> orderReqmap=this.setAtomQueryMap(request);
		ResStorageStaffBean[] ResStorageStaffBeans=resStorageStaffAtomSV.query(beanRequest,orderReqmap);
		ResStorageStaffItemVo temp=null;
		for(ResStorageStaffBean ResStorageStaffBean:ResStorageStaffBeans) {
			temp=this.setVoItem(ResStorageStaffBean);
			result.add(temp);
		}

		response.setResult(result);
		response.setSuccess(true);
		response.setResultCode(ExceptCodeConstants.Special.SUCCESS);
		response.setResultMessage("success");
		return response;
	}

	@Override
	public Response<PageResult<ResStorageStaffItemVo>> queryPageResStorageStaff(QueryResStorageStaffRequest request) throws Exception {
		Response<PageResult<ResStorageStaffItemVo>> response=new Response<>(true,ExceptCodeConstants.Special.SUCCESS,"success");
		PageResult<ResStorageStaffItemVo> pageResult=new PageResult<>();
		List<ResStorageStaffItemVo> result=new ArrayList<>();

		if(request==null||request.getPage()==null||request.getLocale()==null) {
			response.setResult(pageResult);
			response.setSuccess(false);
			response.setResultCode(ExceptCodeConstants.Special.PARAM_IS_NULL);
			response.setResultMessage("request and param can't be null");
			return response;
		}
		Page page=request.getPage();
		int pageNumStart=PageUtil.getStartRowIndex(page.getPageNum(),page.getPageSize());
		int pageNumEnd=PageUtil.getEndRowIndex(page.getPageNum(),page.getPageSize());

		IResStorageStaffAtomSV resStorageStaffAtomSV=(IResStorageStaffAtomSV)ServiceFactory.getService(IResStorageStaffAtomSV.class);
		ResStorageStaffBean beanRequest=this.setAtomQuery(request);
		Map<String,Object> orderReqmap=this.setAtomQueryMap(request);
		ResStorageStaffBean[] ResStorageStaffBeans=resStorageStaffAtomSV.queryPage(beanRequest,orderReqmap,pageNumStart,pageNumEnd);
		ResStorageStaffItemVo temp=null;
		for(ResStorageStaffBean ResStorageStaffBean:ResStorageStaffBeans) {
			temp=this.setVoItem(ResStorageStaffBean);
			result.add(temp);
		}

		pageResult.setResult(result);
		pageResult.setPageCount(result.size());
		pageResult.setCount(result.size());
		pageResult.setPageNum(page.getPageNum());
		pageResult.setPageSize(page.getPageSize());
		pageResult.setSuccess(true);
		response.setResult(pageResult);
		response.setSuccess(true);
		response.setResultCode(ExceptCodeConstants.Special.SUCCESS);
		response.setResultMessage("success");
		return response;
	}

	@Override
	public Response<Long> countResStorageStaff(QueryResStorageStaffRequest request) {
		return null;
	}



	private ResStorageStaffBean setAtomSave(SaveResStorageStaffRequest src) throws AIException {
		ResStorageStaffBean res=null;
		res=new ResStorageStaffBean();
		if(src==null) return res;
		res.setState(src.getState());
		res.setStaffId(src.getStaffId());
		res.setStorageId(src.getStorageId());
		res.setStaffLevel(src.getStaffLevel());
		res.setStorageStaffId(src.getStorageStaffId());
		return res;
	}

	private ResStorageStaffBean setAtomQuery(QueryResStorageStaffRequest src) throws AIException {
		ResStorageStaffBean res=null;
		res=new ResStorageStaffBean();
		if(src==null) return res;
		res.setState(src.getState());
		res.setStaffId(src.getStaffId());
		res.setStorageId(src.getStorageId());
		res.setStaffLevel(src.getStaffLevel());
		res.setStorageStaffId(src.getStorageStaffId());
		return res;
	}

	private Map<String,Object> setAtomQueryMap(QueryResStorageStaffRequest src) {
		Map<String,Object> res=new HashMap<>();
		if(src==null) return res;
		return res;
	}

	private ResStorageStaffDetailVo setVoDetail(ResStorageStaffBean src) {
		ResStorageStaffDetailVo res=new ResStorageStaffDetailVo();
		if(src==null) return res;
		res.setState(VoConvertUtil.getValue(src.getState()));
		res.setStaffId(VoConvertUtil.getValue(src.getStaffId()));
		res.setStorageId(VoConvertUtil.getValue(src.getStorageId()));
		res.setStaffLevel(VoConvertUtil.getValue(src.getStaffLevel()));
		res.setStorageStaffId(VoConvertUtil.getValue(src.getStorageStaffId()));
		return res;
	}

	private ResStorageStaffItemVo setVoItem(ResStorageStaffBean src) {
		ResStorageStaffItemVo res=new ResStorageStaffItemVo();
		if(src==null) return res;
		res.setState(VoConvertUtil.getValue(src.getState()));
		res.setStaffId(VoConvertUtil.getValue(src.getStaffId()));
		res.setStorageId(VoConvertUtil.getValue(src.getStorageId()));
		res.setStaffLevel(VoConvertUtil.getValue(src.getStaffLevel()));
		res.setStorageStaffId(VoConvertUtil.getValue(src.getStorageStaffId()));
		return res;
	}
}
