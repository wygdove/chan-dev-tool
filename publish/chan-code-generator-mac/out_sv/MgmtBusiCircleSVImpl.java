package com.ai.channel.mgmt.api.chlbusicircle.impl;

import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.ai.channel.BusinessException;
import com.ai.channel.SystemException;
import com.ai.channel.mgmt.api.chlbusicircle.interfaces.IMgmtBusiCircleSV;
import com.ai.channel.mgmt.api.chlbusicircle.param.QueryMgmtBusiCircleRequest;
import com.ai.channel.mgmt.api.chlbusicircle.param.SaveMgmtBusiCircleRequest;
import com.ai.channel.mgmt.api.chlbusicircle.vo.MgmtBusiCircleDetailVo;
import com.ai.channel.mgmt.api.chlbusicircle.vo.MgmtBusiCircleItemVo;
import com.ai.channel.mgmt.service.business.interfaces.IMgmtBusiCircleBusiSV;
import com.ai.channel.base.BusinessConstants;
import com.ai.channel.base.vo.BaseResponse;
import com.ai.channel.base.vo.PageResult;
import com.alibaba.dubbo.config.annotation.Service;
import com.alibaba.fastjson.JSON;

/**
 * MgmtBusiCircleSVImpl.java
 *
 *
 * @date 2018-10-15 20:33
 * @author wygdove
 */
@Service
@Component
public class MgmtBusiCircleSVImpl implements IMgmtBusiCircleSV {
	private static Logger log=LoggerFactory.getLogger(MgmtBusiCircleSVImpl.class);

	@Autowired
	IMgmtBusiCircleBusiSV mgmtBusiCircleBusiSV;



	@Override
	public BaseResponse<String> addMgmtBusiCircle(SaveMgmtBusiCircleRequest request) throws BusinessException,SystemException {
		log.info("MgmtBusiCircleSVImpl.addMgmtBusiCircle request"+JSON.toJSONString(request));
		BaseResponse<String> response=new BaseResponse<>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		try {
			if(request==null) {
				response.setSuccess(false);
				response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
				response.setResultMessage("请求不能为空");
			} else {
				response=mgmtBusiCircleBusiSV.addMgmtBusiCircle(request);
			}
		}catch(BusinessException|SystemException e) {
			log.error("MgmtBusiCircleSVImpl.addMgmtBusiCircle error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getErrorMessage());
		}catch(Exception e) {
			log.error("MgmtBusiCircleSVImpl.addMgmtBusiCircle error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getMessage());
		}
		log.info("MgmtBusiCircleSVImpl.addMgmtBusiCircle response"+JSON.toJSONString(response));
		return response;
	}

	@Override
	public BaseResponse<String> updateMgmtBusiCircle(SaveMgmtBusiCircleRequest request) throws BusinessException,SystemException {
		log.info("MgmtBusiCircleSVImpl.updateMgmtBusiCircle request"+JSON.toJSONString(request));
		BaseResponse<String> response=new BaseResponse<>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		try {
			if(request==null) {
				response.setSuccess(false);
				response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
				response.setResultMessage("请求不能为空");
			} else {
				response=mgmtBusiCircleBusiSV.updateMgmtBusiCircle(request);
			}
		}catch(BusinessException|SystemException e) {
			log.error("MgmtBusiCircleSVImpl.updateMgmtBusiCircle error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getErrorMessage());
		}catch(Exception e) {
			log.error("MgmtBusiCircleSVImpl.updateMgmtBusiCircle error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getMessage());
		}
		log.info("MgmtBusiCircleSVImpl.updateMgmtBusiCircle response"+JSON.toJSONString(response));
		return response;
	}

	@Override
	public BaseResponse<String> deleteMgmtBusiCircle(SaveMgmtBusiCircleRequest request) throws BusinessException,SystemException {
		log.info("MgmtBusiCircleSVImpl.deleteMgmtBusiCircle request"+JSON.toJSONString(request));
		BaseResponse<String> response=new BaseResponse<>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		try {
			if(request==null) {
				response.setSuccess(false);
				response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
				response.setResultMessage("请求不能为空");
			} else {
				response=mgmtBusiCircleBusiSV.deleteMgmtBusiCircle(request);
			}
		}catch(BusinessException|SystemException e) {
			log.error("MgmtBusiCircleSVImpl.deleteMgmtBusiCircle error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getErrorMessage());
		}catch(Exception e) {
			log.error("MgmtBusiCircleSVImpl.deleteMgmtBusiCircle error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getMessage());
		}
		log.info("MgmtBusiCircleSVImpl.deleteMgmtBusiCircle response"+JSON.toJSONString(response));
		return response;
	}



	@Override
	public BaseResponse<MgmtBusiCircleDetailVo> queryDetailMgmtBusiCircle(QueryMgmtBusiCircleRequest request) throws BusinessException,SystemException {
		log.info("MgmtBusiCircleSVImpl.queryDetailMgmtBusiCircle request"+JSON.toJSONString(request));
		BaseResponse<MgmtBusiCircleDetailVo> response=new BaseResponse<>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		try {
			if(request==null) {
				response.setSuccess(false);
				response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
				response.setResultMessage("请求不能为空");
			} else {
				response=mgmtBusiCircleBusiSV.queryDetailMgmtBusiCircle(request);
			}
		}catch(BusinessException|SystemException e) {
			log.error("MgmtBusiCircleSVImpl.queryDetailMgmtBusiCircle error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getErrorMessage());
		}catch(Exception e) {
			log.error("MgmtBusiCircleSVImpl.queryDetailMgmtBusiCircle error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getMessage());
		}
		log.info("MgmtBusiCircleSVImpl.queryDetailMgmtBusiCircle response"+JSON.toJSONString(response));
		return response;
	}

	@Override
	public BaseResponse<List<MgmtBusiCircleItemVo>> queryListMgmtBusiCircle(QueryMgmtBusiCircleRequest request) throws BusinessException,SystemException {
		log.info("MgmtBusiCircleSVImpl.queryListMgmtBusiCircle request"+JSON.toJSONString(request));
		BaseResponse<List<MgmtBusiCircleItemVo>> response=new BaseResponse<>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		try {
			if(request==null) {
				response.setSuccess(false);
				response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
				response.setResultMessage("请求不能为空");
			} else {
				response=mgmtBusiCircleBusiSV.queryListMgmtBusiCircle(request);
			}
		}catch(BusinessException|SystemException e) {
			log.error("MgmtBusiCircleSVImpl.queryListMgmtBusiCircle error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getErrorMessage());
		}catch(Exception e) {
			log.error("MgmtBusiCircleSVImpl.queryListMgmtBusiCircle error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getMessage());
		}
		log.info("MgmtBusiCircleSVImpl.queryListMgmtBusiCircle response"+JSON.toJSONString(response));
		return response;
	}

	@Override
	public BaseResponse<PageResult<MgmtBusiCircleItemVo>> queryPageMgmtBusiCircle(QueryMgmtBusiCircleRequest request) throws BusinessException,SystemException {
		log.info("MgmtBusiCircleSVImpl.queryPageMgmtBusiCircle request"+JSON.toJSONString(request));
		BaseResponse<PageResult<MgmtBusiCircleItemVo>> response=new BaseResponse<>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		try {
			if(request==null) {
				response.setSuccess(false);
				response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
				response.setResultMessage("请求不能为空");
			} else {
				response=mgmtBusiCircleBusiSV.queryPageMgmtBusiCircle(request);
			}
		}catch(BusinessException|SystemException e) {
			log.error("MgmtBusiCircleSVImpl.queryPageMgmtBusiCircle error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getErrorMessage());
		}catch(Exception e) {
			log.error("MgmtBusiCircleSVImpl.queryPageMgmtBusiCircle error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getMessage());
		}
		log.info("MgmtBusiCircleSVImpl.queryPageMgmtBusiCircle response"+JSON.toJSONString(response));
		return response;
	}

	@Override
	public BaseResponse<Long> countMgmtBusiCircle(QueryMgmtBusiCircleRequest request) throws BusinessException,SystemException {
		log.info("MgmtBusiCircleSVImpl.countMgmtBusiCircle request"+JSON.toJSONString(request));
		BaseResponse<Long> response=new BaseResponse<>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		try {
			if(request==null) {
				response.setSuccess(false);
				response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
				response.setResultMessage("请求不能为空");
			} else {
				response=mgmtBusiCircleBusiSV.countMgmtBusiCircle(request);
			}
		}catch(BusinessException|SystemException e) {
			log.error("MgmtBusiCircleSVImpl.countMgmtBusiCircle error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getErrorMessage());
		}catch(Exception e) {
			log.error("MgmtBusiCircleSVImpl.countMgmtBusiCircle error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getMessage());
		}
		log.info("MgmtBusiCircleSVImpl.countMgmtBusiCircle response"+JSON.toJSONString(response));
		return response;
	}


}