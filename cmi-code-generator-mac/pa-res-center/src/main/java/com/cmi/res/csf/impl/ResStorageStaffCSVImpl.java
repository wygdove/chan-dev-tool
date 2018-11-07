package com.cmi.res.csf.impl;

import com.ai.appframe2.service.ServiceFactory;
import com.alibaba.fastjson.JSON;
import com.cmi.common.domain.PageResult;
import com.cmi.common.domain.Response;
import com.cmi.res.business.interfaces.IResStorageStaffBizSV;
import com.cmi.res.constants.ExceptCodeConstants;
import com.cmi.res.csf.interfaces.IResStorageStaffCSV;
import com.cmi.res.domain.resstoragestaff.params.QueryResStorageStaffRequest;
import com.cmi.res.domain.resstoragestaff.params.SaveResStorageStaffRequest;
import com.cmi.res.domain.resstoragestaff.vo.ResStorageStaffDetailVo;
import com.cmi.res.domain.resstoragestaff.vo.ResStorageStaffItemVo;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.List;

/**
 * @Title:
 * @Description:
 * @Date: 2018-11-07 09:42
 * @Author: wygdove
 */
public class ResStorageStaffCSVImpl implements IResStorageStaffCSV {
	private static Logger log=LoggerFactory.getLogger(ResStorageStaffCSVImpl.class);

	@Override
	public Response<String> addResStorageStaff(SaveResStorageStaffRequest request) throws Exception {
		log.info("ResStorageStaffCSVImpl.addResStorageStaff request: {}",JSON.toJSONString(request));
		Response<String> response=new Response<>(true,ExceptCodeConstants.Special.SUCCESS,"操作成功");
		try {
			if(request==null) {
				response.setSuccess(false);
				response.setResultCode(ExceptCodeConstants.Special.PARAM_IS_NULL);
				response.setResultMessage("请求不能为空");
			} else {
				IResStorageStaffBizSV resStorageStaffBizSV=(IResStorageStaffBizSV)ServiceFactory.getService(IResStorageStaffBizSV.class);
				response=resStorageStaffBizSV.addResStorageStaff(request);
			}
		}catch(Exception e) {
			log.error("ResStorageStaffCSVImpl.addResStorageStaff error: {}",e.getMessage(),e);
			response.setSuccess(false);
			response.setResultCode(ExceptCodeConstants.Special.SYSTEM_ERROR);
			response.setResultMessage(e.getMessage());
		}
		log.info("ResStorageStaffCSVImpl.addResStorageStaff response: {}",JSON.toJSONString(response));
		return response;
	}

	@Override
	public Response<String> addBatchResStorageStaff(SaveResStorageStaffRequest request) throws Exception {
		log.info("ResStorageStaffCSVImpl.addBatchResStorageStaff request: {}",JSON.toJSONString(request));
		Response<String> response=new Response<>(true,ExceptCodeConstants.Special.SUCCESS,"操作成功");
		try {
			if(request==null) {
				response.setSuccess(false);
				response.setResultCode(ExceptCodeConstants.Special.PARAM_IS_NULL);
				response.setResultMessage("请求不能为空");
			} else {
				IResStorageStaffBizSV resStorageStaffBizSV=(IResStorageStaffBizSV)ServiceFactory.getService(IResStorageStaffBizSV.class);
				response=resStorageStaffBizSV.addBatchResStorageStaff(request);
			}
		}catch(Exception e) {
			log.error("ResStorageStaffCSVImpl.addBatchResStorageStaff error: {}",e.getMessage(),e);
			response.setSuccess(false);
			response.setResultCode(ExceptCodeConstants.Special.SYSTEM_ERROR);
			response.setResultMessage(e.getMessage());
		}
		log.info("ResStorageStaffCSVImpl.addBatchResStorageStaff response: {}",JSON.toJSONString(response));
		return response;
	}

	@Override
	public Response<String> updateResStorageStaff(SaveResStorageStaffRequest request) throws Exception {
		log.info("ResStorageStaffCSVImpl.updateResStorageStaff request: {}",JSON.toJSONString(request));
		Response<String> response=new Response<>(true,ExceptCodeConstants.Special.SUCCESS,"操作成功");
		try {
			if(request==null) {
				response.setSuccess(false);
				response.setResultCode(ExceptCodeConstants.Special.PARAM_IS_NULL);
				response.setResultMessage("请求不能为空");
			} else {
				IResStorageStaffBizSV resStorageStaffBizSV=(IResStorageStaffBizSV)ServiceFactory.getService(IResStorageStaffBizSV.class);
				response=resStorageStaffBizSV.updateResStorageStaff(request);
			}
		}catch(Exception e) {
			log.error("ResStorageStaffCSVImpl.updateResStorageStaff error: {}",e.getMessage(),e);
			response.setSuccess(false);
			response.setResultCode(ExceptCodeConstants.Special.SYSTEM_ERROR);
			response.setResultMessage(e.getMessage());
		}
		log.info("ResStorageStaffCSVImpl.updateResStorageStaff response: {}",JSON.toJSONString(response));
		return response;
	}

	@Override
	public Response<String> deleteResStorageStaff(SaveResStorageStaffRequest request) throws Exception {
		log.info("ResStorageStaffCSVImpl.deleteResStorageStaff request: {}",JSON.toJSONString(request));
		Response<String> response=new Response<>(true,ExceptCodeConstants.Special.SUCCESS,"操作成功");
		try {
			if(request==null) {
				response.setSuccess(false);
				response.setResultCode(ExceptCodeConstants.Special.PARAM_IS_NULL);
				response.setResultMessage("请求不能为空");
			} else {
				IResStorageStaffBizSV resStorageStaffBizSV=(IResStorageStaffBizSV)ServiceFactory.getService(IResStorageStaffBizSV.class);
				response=resStorageStaffBizSV.deleteResStorageStaff(request);
			}
		}catch(Exception e) {
			log.error("ResStorageStaffCSVImpl.deleteResStorageStaff error: {}",e.getMessage(),e);
			response.setSuccess(false);
			response.setResultCode(ExceptCodeConstants.Special.SYSTEM_ERROR);
			response.setResultMessage(e.getMessage());
		}
		log.info("ResStorageStaffCSVImpl.deleteResStorageStaff response: {}",JSON.toJSONString(response));
		return response;
	}

	@Override
	public Response<ResStorageStaffDetailVo> queryDetailResStorageStaff(QueryResStorageStaffRequest request) throws Exception {
		log.info("ResStorageStaffCSVImpl.queryDetailResStorageStaff request: {}",JSON.toJSONString(request));
		Response<ResStorageStaffDetailVo> response=new Response<>(true,ExceptCodeConstants.Special.SUCCESS,"操作成功");
		try {
			if(request==null) {
				response.setSuccess(false);
				response.setResultCode(ExceptCodeConstants.Special.PARAM_IS_NULL);
				response.setResultMessage("请求不能为空");
			} else {
				IResStorageStaffBizSV resStorageStaffBizSV=(IResStorageStaffBizSV)ServiceFactory.getService(IResStorageStaffBizSV.class);
				response=resStorageStaffBizSV.queryDetailResStorageStaff(request);
			}
		}catch(Exception e) {
			log.error("ResStorageStaffCSVImpl.queryDetailResStorageStaff error: {}",e.getMessage(),e);
			response.setSuccess(false);
			response.setResultCode(ExceptCodeConstants.Special.SYSTEM_ERROR);
			response.setResultMessage(e.getMessage());
		}
		log.info("ResStorageStaffCSVImpl.queryDetailResStorageStaff response: {}",JSON.toJSONString(response));
		return response;
	}

	@Override
	public Response<List<ResStorageStaffItemVo>> queryListResStorageStaff(QueryResStorageStaffRequest request) throws Exception {
		log.info("ResStorageStaffCSVImpl.queryListResStorageStaff request: {}",JSON.toJSONString(request));
		Response<List<ResStorageStaffItemVo>> response=new Response<>(true,ExceptCodeConstants.Special.SUCCESS,"操作成功");
		try {
			if(request==null) {
				response.setSuccess(false);
				response.setResultCode(ExceptCodeConstants.Special.PARAM_IS_NULL);
				response.setResultMessage("请求不能为空");
			} else {
				IResStorageStaffBizSV resStorageStaffBizSV=(IResStorageStaffBizSV)ServiceFactory.getService(IResStorageStaffBizSV.class);
				response=resStorageStaffBizSV.queryListResStorageStaff(request);
			}
		}catch(Exception e) {
			log.error("ResStorageStaffCSVImpl.queryListResStorageStaff error: {}",e.getMessage(),e);
			response.setSuccess(false);
			response.setResultCode(ExceptCodeConstants.Special.SYSTEM_ERROR);
			response.setResultMessage(e.getMessage());
		}
		log.info("ResStorageStaffCSVImpl.queryListResStorageStaff response: {}",JSON.toJSONString(response));
		return response;
	}

	@Override
	public Response<PageResult<ResStorageStaffItemVo>> queryPageResStorageStaff(QueryResStorageStaffRequest request) throws Exception {
		log.info("ResStorageStaffCSVImpl.queryPageResStorageStaff request: {}",JSON.toJSONString(request));
		Response<PageResult<ResStorageStaffItemVo>> response=new Response<>(true,ExceptCodeConstants.Special.SUCCESS,"操作成功");
		try {
			if(request==null) {
				response.setSuccess(false);
				response.setResultCode(ExceptCodeConstants.Special.PARAM_IS_NULL);
				response.setResultMessage("请求不能为空");
			} else {
				IResStorageStaffBizSV resStorageStaffBizSV=(IResStorageStaffBizSV)ServiceFactory.getService(IResStorageStaffBizSV.class);
				response=resStorageStaffBizSV.queryPageResStorageStaff(request);
			}
		}catch(Exception e) {
			log.error("ResStorageStaffCSVImpl.queryPageResStorageStaff error: {}",e.getMessage(),e);
			response.setSuccess(false);
			response.setResultCode(ExceptCodeConstants.Special.SYSTEM_ERROR);
			response.setResultMessage(e.getMessage());
		}
		log.info("ResStorageStaffCSVImpl.queryPageResStorageStaff response: {}",JSON.toJSONString(response));
		return response;
	}

	@Override
	public Response<Long> countResStorageStaff(QueryResStorageStaffRequest request) throws Exception {
		log.info("ResStorageStaffCSVImpl.countResStorageStaff request: {}",JSON.toJSONString(request));
		Response<Long> response=new Response<>(true,ExceptCodeConstants.Special.SUCCESS,"操作成功");
		try {
			if(request==null) {
				response.setSuccess(false);
				response.setResultCode(ExceptCodeConstants.Special.PARAM_IS_NULL);
				response.setResultMessage("请求不能为空");
			} else {
				IResStorageStaffBizSV resStorageStaffBizSV=(IResStorageStaffBizSV)ServiceFactory.getService(IResStorageStaffBizSV.class);
				response=resStorageStaffBizSV.countResStorageStaff(request);
			}
		}catch(Exception e) {
			log.error("ResStorageStaffCSVImpl.countResStorageStaff error: {}",e.getMessage(),e);
			response.setSuccess(false);
			response.setResultCode(ExceptCodeConstants.Special.SYSTEM_ERROR);
			response.setResultMessage(e.getMessage());
		}
		log.info("ResStorageStaffCSVImpl.countResStorageStaff response: {}",JSON.toJSONString(response));
		return response;
	}
}
