# coding=utf-8
__author__='wygdove'
__time__='2018/4/26 10:56'

import os
import time


__project__='gis'

def dosv(svkey,svkeyl):
    svs=[{'fp':'\\out\\sv\\','fn':'version.ini','tflag':'svini'},
         {'fp':'\\out\\sv\\interfaces\\','fn':'I'+svkey+'SV.java','tflag':'svinterfaces'},
         {'fp':'\\out\\sv\\param\\','fn':'Save'+svkey+'Request.java','tflag':'svparamsave'},
         {'fp':'\\out\\sv\\param\\','fn':'Query'+svkey+'Request.java','tflag':'svparamquery'},
         {'fp':'\\out\\sv\\vo\\','fn':svkey+'ItemVo.java','tflag':'svvoitem'},
         {'fp':'\\out\\sv\\vo\\','fn':svkey+'DetailVo.java','tflag':'svvodetail'},
         {'fp':'\\out\\sv\\constants\\','fn':svkey+'Constants.java','tflag':'svconstants'},
         {'fp':'\\out\\','fn':svkey+'SVImpl.java','tflag':'svimpl'},
         {'fp':'\\out\\','fn':'I'+svkey+'BusiSV.java','tflag':'busiinterface'},
         {'fp':'\\out\\','fn':svkey+'BusiSVImpl.java','tflag':'busiimpl'},
         {'fp':'\\out\\','fn':'I'+svkey+'AtomSV.java','tflag':'atominterface'},
         {'fp':'\\out\\','fn':svkey+'AtomSVImpl.java','tflag':'atomimpl'},
         {'fp':'\\out\\','fn':svkey+'SVTest.java','tflag':'svtest'}]
    for svi in svs:
        fn=open(getCurPath()+svi['fp']+svi['fn'],'w')
        content=getTemplate(svi['tflag'],svkey,svkeyl)
        fn.writelines(content)
        fn.flush()
        fn.close()


def getTemplate(flag,svkey,svkeyl):
    data=''
    if flag=='svini':
        data='1.0-SNAPSHOT'
    elif flag=='svinterfaces':
        data='''package com.ai.channel.__project__.api.__svkey__.interfaces;

import java.util.List;

import javax.ws.rs.Consumes;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import com.ai.channel.BusinessException;
import com.ai.channel.SystemException;
import com.ai.channel.__project__.api.__svkey__.param.Query__SVKEY__Request;
import com.ai.channel.__project__.api.__svkey__.param.Save__SVKEY__Request;
import com.ai.channel.__project__.api.__svkey__.vo.__SVKEY__DetailVo;
import com.ai.channel.__project__.api.__svkey__.vo.__SVKEY__ItemVo;
import com.ai.channel.base.vo.BaseResponse;
import com.ai.channel.base.vo.PageResult;

/** 
 * I__SVKEY__SV.java
 * 
 * 
 * @date 
 * @author wygdove
 */
@Path("/__sVKEY__SV")
@Consumes({MediaType.APPLICATION_JSON})
@Produces({MediaType.APPLICATION_JSON, MediaType.TEXT_XML})
public interface I__SVKEY__SV {


	/**
	 * 添加
	 * @param request
	 * @return
	 * @throws BusinessException
	 * @throws SystemException
	 * @author wygdove
	 */
    @POST
    @Path("/add__SVKEY__")
    BaseResponse<String> add__SVKEY__(Save__SVKEY__Request request) throws BusinessException, SystemException;

    /**
	 * 更新
	 * @param request
	 * @return
	 * @throws BusinessException
	 * @throws SystemException
	 * @author wygdove
	 */
    @POST
    @Path("/update__SVKEY__")
    BaseResponse<String> update__SVKEY__(Save__SVKEY__Request request) throws BusinessException, SystemException;

    /**
	 * 删除
	 * @param request
	 * @return
	 * @throws BusinessException
	 * @throws SystemException
	 * @author wygdove
	 */
    @POST
    @Path("/delete__SVKEY__")
    BaseResponse<String> delete__SVKEY__(Save__SVKEY__Request request) throws BusinessException, SystemException;



    /**
	 * 详情查询
	 * @param request
	 * @return
	 * @throws BusinessException
	 * @throws SystemException
	 * @author wygdove
	 */
    @POST
    @Path("/queryDetail__SVKEY__")
    BaseResponse<__SVKEY__DetailVo> queryDetail__SVKEY__(Query__SVKEY__Request request) throws BusinessException, SystemException;



	/**
	 * 列表查询
	 * @param request
	 * @return
	 * @throws BusinessException
	 * @throws SystemException
	 * @author wygdove
	 */
    @POST
    @Path("/queryList__SVKEY__")
    BaseResponse<List<__SVKEY__ItemVo>> queryList__SVKEY__(Query__SVKEY__Request request) throws BusinessException, SystemException;

    /**
     * 分页列表查询
     * @param request
     * @return
     * @throws BusinessException
     * @throws SystemException
     * @author wygdove
     */
    @POST
    @Path("/queryPage__SVKEY__")
    BaseResponse<PageResult<__SVKEY__ItemVo>> queryPage__SVKEY__(Query__SVKEY__Request request) throws BusinessException, SystemException;

}'''
    elif flag=='svparamsave':
        data='''package com.ai.channel.__project__.api.__svkey__.param;

import java.io.Serializable;

import org.codehaus.jackson.annotate.JsonIgnoreProperties;

/** 
 * Save__SVKEY__Request.java
 * 
 * 
 * @date 
 * @author wygdove
 */
@JsonIgnoreProperties(ignoreUnknown=true)
public class Save__SVKEY__Request implements Serializable {

}'''
    elif flag=='svparamquery':
        data='''package com.ai.channel.__project__.api.__svkey__.param;

import java.io.Serializable;

import org.codehaus.jackson.annotate.JsonIgnoreProperties;

import com.ai.channel.base.vo.BaseInfo;

/** 
 * Query__SVKEY__Request.java
 * 
 * 
 * @date 
 * @author wygdove
 */
@JsonIgnoreProperties(ignoreUnknown=true)
public class Query__SVKEY__Request extends BaseInfo implements Serializable {
}'''
    elif flag=='svvoitem':
        data='''package com.ai.channel.__project__.api.__svkey__.vo;

import java.io.Serializable;

import org.codehaus.jackson.annotate.JsonIgnoreProperties;

/** 
 * __SVKEY__ItemVo.java
 * 
 * 
 * @date 
 * @author wygdove
 */
@JsonIgnoreProperties(ignoreUnknown=true)
public class __SVKEY__ItemVo implements Serializable {
}'''
    elif flag=='svvodetail':
        data='''package com.ai.channel.__project__.api.__svkey__.vo;

import java.io.Serializable;

import org.codehaus.jackson.annotate.JsonIgnoreProperties;

/**
 * __SVKEY__DetailVo.java
 * 
 * 
 * @date 
 * @author wygdove
 */
@JsonIgnoreProperties(ignoreUnknown=true)
public class __SVKEY__DetailVo implements Serializable {
}'''
    elif flag=='svconstants':
        data='''package com.ai.channel.__project__.api.__svkey__.constants;

/** 
 * __SVKEY__Constants.java
 * 
 * 
 * @date 
 * @author wygdove
 */
public final class __SVKEY__Constants {
	public __SVKEY__Constants() {}
	
	public final static class Aaa {
		public final static String BBB="0";
	}
	
}
'''
    elif flag=='svimpl':
        data='''package com.ai.channel.__project__.api.__svkey__.impl;

import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import com.alibaba.dubbo.config.annotation.Service;

import com.ai.channel.BusinessException;
import com.ai.channel.SystemException;
import com.ai.channel.__project__.api.__svkey__.interfaces.I__SVKEY__SV;
import com.ai.channel.__project__.api.__svkey__.param.Query__SVKEY__Request;
import com.ai.channel.__project__.api.__svkey__.param.Save__SVKEY__Request;
import com.ai.channel.__project__.api.__svkey__.vo.__SVKEY__DetailVo;
import com.ai.channel.__project__.api.__svkey__.vo.__SVKEY__ItemVo;
import com.ai.channel.__project__.service.business.interfaces.I__SVKEY__BusiSV;
import com.ai.channel.base.BusinessConstants;
import com.ai.channel.base.vo.BaseResponse;
import com.ai.channel.base.vo.PageResult;
import com.alibaba.fastjson.JSON;

/** 
 * __SVKEY__SVImpl.java
 * 
 * 
 * @date 
 * @author wygdove
 */
@Service
@Component
public class __SVKEY__SVImpl implements I__SVKEY__SV {
	private static Logger log=LoggerFactory.getLogger(__SVKEY__SVImpl.class);

	@Autowired
	I__SVKEY__BusiSV __sVKEY__BusiSV;



	@Override
	public BaseResponse<String> add__SVKEY__(Save__SVKEY__Request request) throws BusinessException,SystemException {
		log.info("__SVKEY__SVImpl.add__SVKEY__ request"+JSON.toJSONString(request));
		BaseResponse<String> response=new BaseResponse<>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		try {
			if(request==null) {
				response.setSuccess(false);
				response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
				response.setResultMessage("请求不能为空");
			} else {
				response=__sVKEY__BusiSV.add__SVKEY__(request);
			}
		}catch(BusinessException|SystemException e) {
			log.error("__SVKEY__SVImpl.add__SVKEY__ error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getErrorMessage());
		}catch(Exception e) {
			log.error("__SVKEY__SVImpl.add__SVKEY__ error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getMessage());
		}
		log.info("__SVKEY__SVImpl.add__SVKEY__ response"+JSON.toJSONString(response));
		return response;
	}

	@Override
	public BaseResponse<String> update__SVKEY__(Save__SVKEY__Request request) throws BusinessException,SystemException {
		log.info("__SVKEY__SVImpl.update__SVKEY__ request"+JSON.toJSONString(request));
		BaseResponse<String> response=new BaseResponse<>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		try {
			if(request==null) {
				response.setSuccess(false);
				response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
				response.setResultMessage("请求不能为空");
			} else {
				response=__sVKEY__BusiSV.update__SVKEY__(request);
			}
		}catch(BusinessException|SystemException e) {
			log.error("__SVKEY__SVImpl.update__SVKEY__ error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getErrorMessage());
		}catch(Exception e) {
			log.error("__SVKEY__SVImpl.update__SVKEY__ error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getMessage());
		}
		log.info("__SVKEY__SVImpl.update__SVKEY__ response"+JSON.toJSONString(response));
		return response;
	}

	@Override
	public BaseResponse<String> delete__SVKEY__(Save__SVKEY__Request request) throws BusinessException,SystemException {
		log.info("__SVKEY__SVImpl.delete__SVKEY__ request"+JSON.toJSONString(request));
		BaseResponse<String> response=new BaseResponse<>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		try {
			if(request==null) {
				response.setSuccess(false);
				response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
				response.setResultMessage("请求不能为空");
			} else {
				response=__sVKEY__BusiSV.delete__SVKEY__(request);
			}
		}catch(BusinessException|SystemException e) {
			log.error("__SVKEY__SVImpl.delete__SVKEY__ error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getErrorMessage());
		}catch(Exception e) {
			log.error("__SVKEY__SVImpl.delete__SVKEY__ error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getMessage());
		}
		log.info("__SVKEY__SVImpl.delete__SVKEY__ response"+JSON.toJSONString(response));
		return response;
	}



	@Override
	public BaseResponse<__SVKEY__DetailVo> queryDetail__SVKEY__(Query__SVKEY__Request request) throws BusinessException,SystemException {
		log.info("__SVKEY__SVImpl.queryDetail__SVKEY__ request"+JSON.toJSONString(request));
		BaseResponse<__SVKEY__DetailVo> response=new BaseResponse<>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		try {
			if(request==null) {
				response.setSuccess(false);
				response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
				response.setResultMessage("请求不能为空");
			} else {
				response=__sVKEY__BusiSV.queryDetail__SVKEY__(request);
			}
		}catch(BusinessException|SystemException e) {
			log.error("__SVKEY__SVImpl.queryDetail__SVKEY__ error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getErrorMessage());
		}catch(Exception e) {
			log.error("__SVKEY__SVImpl.queryDetail__SVKEY__ error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getMessage());
		}
		log.info("__SVKEY__SVImpl.queryDetail__SVKEY__ response"+JSON.toJSONString(response));
		return response;
	}

	@Override
	public BaseResponse<List<__SVKEY__ItemVo>> queryList__SVKEY__(Query__SVKEY__Request request) throws BusinessException,SystemException {
		log.info("__SVKEY__SVImpl.queryList__SVKEY__ request"+JSON.toJSONString(request));
		BaseResponse<List<__SVKEY__ItemVo>> response=new BaseResponse<>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		try {
			if(request==null) {
				response.setSuccess(false);
				response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
				response.setResultMessage("请求不能为空");
			} else {
				response=__sVKEY__BusiSV.queryList__SVKEY__(request);
			}
		}catch(BusinessException|SystemException e) {
			log.error("__SVKEY__SVImpl.queryList__SVKEY__ error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getErrorMessage());
		}catch(Exception e) {
			log.error("__SVKEY__SVImpl.queryList__SVKEY__ error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getMessage());
		}
		log.info("__SVKEY__SVImpl.queryList__SVKEY__ response"+JSON.toJSONString(response));
		return response;
	}

	@Override
	public BaseResponse<PageResult<__SVKEY__ItemVo>> queryPage__SVKEY__(Query__SVKEY__Request request) throws BusinessException,SystemException {
		log.info("__SVKEY__SVImpl.queryPage__SVKEY__ request"+JSON.toJSONString(request));
		BaseResponse<PageResult<__SVKEY__ItemVo>> response=new BaseResponse<>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		try {
			if(request==null) {
				response.setSuccess(false);
				response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
				response.setResultMessage("请求不能为空");
			} else {
				response=__sVKEY__BusiSV.queryPage__SVKEY__(request);
			}
		}catch(BusinessException|SystemException e) {
			log.error("__SVKEY__SVImpl.queryPage__SVKEY__ error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getErrorMessage());
		}catch(Exception e) {
			log.error("__SVKEY__SVImpl.queryPage__SVKEY__ error: "+e.getMessage());
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage(e.getMessage());
		}
		log.info("__SVKEY__SVImpl.queryPage__SVKEY__ response"+JSON.toJSONString(response));
		return response;
	}

}'''
    elif flag=='busiinterface':
        data='''package com.ai.channel.__project__.service.business.interfaces;

import java.util.List;

import com.ai.channel.__project__.api.__svkey__.param.Query__SVKEY__Request;
import com.ai.channel.__project__.api.__svkey__.param.Save__SVKEY__Request;
import com.ai.channel.__project__.api.__svkey__.vo.__SVKEY__DetailVo;
import com.ai.channel.__project__.api.__svkey__.vo.__SVKEY__ItemVo;
import com.ai.channel.base.vo.BaseResponse;
import com.ai.channel.base.vo.PageResult;

/** 
 * I__SVKEY__BusiSV.java
 * 
 * 
 * @date 
 * @author wygdove
 */
public interface I__SVKEY__BusiSV {

	BaseResponse<String> add__SVKEY__(Save__SVKEY__Request request);
	BaseResponse<String> update__SVKEY__(Save__SVKEY__Request request);

	BaseResponse<String> delete__SVKEY__(Save__SVKEY__Request request);

	BaseResponse<__SVKEY__DetailVo> queryDetail__SVKEY__(Query__SVKEY__Request request);

	BaseResponse<List<__SVKEY__ItemVo>> queryList__SVKEY__(Query__SVKEY__Request request);
	BaseResponse<PageResult<__SVKEY__ItemVo>> queryPage__SVKEY__(Query__SVKEY__Request request);

}'''
    elif flag=='busiimpl':
        data='''package com.ai.channel.__project__.service.business.impl;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.ai.channel.__project__.api.__svkey__.param.Query__SVKEY__Request;
import com.ai.channel.__project__.api.__svkey__.param.Save__SVKEY__Request;
import com.ai.channel.__project__.api.__svkey__.vo.__SVKEY__DetailVo;
import com.ai.channel.__project__.api.__svkey__.vo.__SVKEY__ItemVo;
import com.ai.channel.__project__.base.constants.SeqConstants;
import com.ai.channel.__project__.dao.mapper.bo.AlertSendRecord;
import com.ai.channel.__project__.service.atom.interfaces.I__SVKEY__AtomSV;
import com.ai.channel.__project__.service.business.interfaces.I__SVKEY__BusiSV;
import com.ai.channel.base.BusinessConstants;
import com.ai.channel.base.vo.BaseResponse;
import com.ai.channel.base.vo.PageResult;
import com.ai.channel.common.cmpt.sequence.util.SeqUtil;
import com.ai.channel.common.util.CollectionUtil;
import com.github.pagehelper.Page;
import com.github.pagehelper.PageHelper;

/** 
 * __SVKEY__BusiSVImpl.java
 * 
 * 
 * @date 
 * @author wygdove
 */
@Service
@Component
public class __SVKEY__BusiSVImpl implements I__SVKEY__BusiSV {

	@Autowired
	I__SVKEY__AtomSV __sVKEY__AtomSV;



	@Transactional
	@Override
	public BaseResponse<String> add__SVKEY__(Save__SVKEY__Request request) {
		BaseResponse<String> response=new BaseResponse<String>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);

		Long itemId=SeqUtil.getNewId(SeqConstants.GIS_GRID_INFO_ID);
		// request.setGridId(""+itemId);

		__SVKEY__ __sVKEY__Request=this.setSaveAtom(request);
		// __sVKEY__Request.setCreateUser(request.getUserId());
		// __sVKEY__Request.setCreateTime(Calendar.getInstance().getTime());
		// __sVKEY__Request.setUpdateUser(request.getUserId());
		// __sVKEY__Request.setUpdateTime(Calendar.getInstance().getTime());
		int res=__sVKEY__AtomSV.add(__sVKEY__Request);
		if(res<=0) {
			response.setResult("");
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage("保存失败");
			return response;
		}

		// response.setResult(request.getGridId());
		// response.setInfo(gridCode);
		response.setSuccess(true);
		response.setResultCode(BusinessConstants.BUSI_SUCCESS_CODE);
		response.setResultMessage(BusinessConstants.BUSI_SUCCESS_MESSAGE);
		return response;
	}

	private __SVKEY__ setSaveAtom(Save__SVKEY__Request request) {
		__SVKEY__ res=new __SVKEY__();
		return res;
	}



	@Transactional
	@Override
	public BaseResponse<String> update__SVKEY__(Save__SVKEY__Request request) {
		BaseResponse<String> response=new BaseResponse<String>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		// if(StringUtils.isBlank(request.getGridId())) {
		// 	response.setResult("");
		// 	response.setSuccess(false);
		// 	response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
		// 	response.setResultMessage("请求不能为空");
		// 	return response;
		// }

		__SVKEY__ __sVKEY__Request=this.setSaveAtom(request);
		// __sVKEY__Request.setUpdateUser(request.getUserId());
		// __sVKEY__Request.setUpdateTime(Calendar.getInstance().getTime());
		__sVKEY__AtomSV.update(__sVKEY__Request);

		// response.setResult(request.getGridId());
		// response.setInfo(request.getGridCode());
		response.setSuccess(true);
		response.setResultCode(BusinessConstants.BUSI_SUCCESS_CODE);
		response.setResultMessage(BusinessConstants.BUSI_SUCCESS_MESSAGE);
		return response;
	}



	@Transactional
	@Override
	public BaseResponse<String> delete__SVKEY__(Save__SVKEY__Request request) {
		BaseResponse<String> response=new BaseResponse<String>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		// if(StringUtils.isBlank(request.getGridId())) {
		// 	response.setResult("");
		// 	response.setSuccess(false);
		// 	response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
		// 	response.setResultMessage("请求不能为空");
		// 	return response;
		// }

		__SVKEY__ __sVKEY__Request=new __SVKEY__();
		// __sVKEY__Request.setGridId(request.getGridId());
		// __sVKEY__Request.setDelFlag(delFlag);
		// __sVKEY__Request.setUpdateUser(request.getUserId());
		// __sVKEY__Request.setUpdateTime(Calendar.getInstance().getTime());
		int res=__sVKEY__AtomSV.update(__sVKEY__Request);
		if(res<=0) {
			response.setResult("");
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage("删除失败");
			return response;
		}

		// response.setResult(request.getGridId());
		response.setSuccess(true);
		response.setResultCode(BusinessConstants.BUSI_SUCCESS_CODE);
		response.setResultMessage(BusinessConstants.BUSI_SUCCESS_MESSAGE);
		return response;
	}



	@Override
	public BaseResponse<__SVKEY__DetailVo> queryDetail__SVKEY__(Query__SVKEY__Request request) {
		BaseResponse<__SVKEY__DetailVo> response=new BaseResponse<>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		__SVKEY__DetailVo res=new __SVKEY__DetailVo();
		__SVKEY__ __sVKEY__=null;
		// if(StringUtils.isNotBlank(request.getGridId())) {
		// 	__sVKEY__=__sVKEY__AtomSV.queryById(request.getGridId());
		// }else if(StringUtils.isNotBlank(request.getGridCode())) {
		// 	Map<String,Object> __sVKEY__ReqMap=new HashMap<>();
		// 	__SVKEY__ __sVKEY__Request=new __SVKEY__();
		// 	__sVKEY__Request.setGridCode(request.getGridCode());
		// 	List<__SVKEY__> __sVKEY__List=__sVKEY__AtomSV.query(__sVKEY__Request,__sVKEY__ReqMap);
		// 	if(!CollectionUtil.isEmpty(__sVKEY__List)) {
		// 		__sVKEY__=__sVKEY__List.get(0);
		// 	}
		// }
		if(__sVKEY__==null) {
			response.setResult(res);
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage("详情查询出错");
			return response;
		}
		res=this.setVoDetail(__sVKEY__);
		response.setResult(res);
		response.setSuccess(true);
		response.setResultCode(BusinessConstants.BUSI_SUCCESS_CODE);
		response.setResultMessage(BusinessConstants.BUSI_SUCCESS_MESSAGE);
		return response;
	}
	private __SVKEY__DetailVo setVoDetail(__SVKEY__ __sVKEY__) {
		__SVKEY__DetailVo res=new __SVKEY__DetailVo();
		if(__sVKEY__==null) return res;
		return res;
	}



	@Override
	public BaseResponse<List<__SVKEY__ItemVo>> queryList__SVKEY__(Query__SVKEY__Request request) {
		BaseResponse<List<__SVKEY__ItemVo>> response=new BaseResponse<>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		List<__SVKEY__ItemVo> result=new ArrayList<>();

		__SVKEY__ queryRequest=this.setQueryAtom(request);
		Map<String,Object> reqmap=this.setQueryAtomMap(request);
		List<__SVKEY__> resList=__sVKEY__AtomSV.query(queryRequest,reqmap);
		if(!CollectionUtil.isEmpty(resList)) {
			__SVKEY__ItemVo itemVo=null;
			for(__SVKEY__ item:resList) {
				itemVo=this.setVoItem(item);
				result.add(itemVo);
			}
		}
		response.setSuccess(true);
		response.setResult(result);
		response.setResultCode(BusinessConstants.BUSI_SUCCESS_CODE);
		response.setResultMessage(BusinessConstants.BUSI_SUCCESS_MESSAGE);
		return response;
	}
	@Override
	public BaseResponse<PageResult<__SVKEY__ItemVo>> queryPage__SVKEY__(Query__SVKEY__Request request) {
		BaseResponse<PageResult<__SVKEY__ItemVo>> response=new BaseResponse<>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		PageResult<__SVKEY__ItemVo> pageResult=new PageResult<>();
		List<__SVKEY__ItemVo> result=new ArrayList<>();

		__SVKEY__ queryRequest=this.setQueryAtom(request);
		Map<String,Object> reqmap=this.setQueryAtomMap(request);
		int pageNum=request.getPage().getPageNum();
		int pageSize=request.getPage().getPageSize();
		PageHelper.startPage(pageNum,pageSize);

		List<__SVKEY__> resList=new ArrayList<>();
		try {
			resList=__sVKEY__AtomSV.query(queryRequest,reqmap);
		}finally {
			PageHelper.clearPage();
		}
		if(!CollectionUtil.isEmpty(resList)) {
			__SVKEY__ItemVo itemVo=null;
			for(__SVKEY__ item:resList) {
				itemVo=this.setVoItem(item);
				result.add(itemVo);
			}
			pageResult.setCount(((Page<__SVKEY__>)resList).getTotal());
			pageResult.setSuccess(true);
		} else {
			pageResult.setSuccess(false);
		}

		pageResult.setPageNum(pageNum);
		pageResult.setPageSize(pageSize);
		pageResult.setResult(result);
        response.setResult(pageResult);
        response.setSuccess(true);
		response.setResultCode(BusinessConstants.BUSI_SUCCESS_CODE);
		response.setResultMessage(BusinessConstants.BUSI_SUCCESS_MESSAGE);
		return response;
	}
	private __SVKEY__ setQueryAtom(Query__SVKEY__Request request) {
		__SVKEY__ res=new __SVKEY__();
		if(request==null) return res;
		return res;
	}
	private Map<String,Object> setQueryAtomMap(Query__SVKEY__Request request) {
		Map<String,Object> res=new HashMap<>();
		if(request==null) return res;
		return res;
	}
	private __SVKEY__ItemVo setVoItem(__SVKEY__ src) {
		__SVKEY__ItemVo res=new __SVKEY__ItemVo();
		if(src==null) return res;
		return res;
	}

}'''
    elif flag=='atominterface':
        data='''package com.ai.channel.__project__.service.atom.interfaces;

import java.util.List;

import com.ai.channel.__project__.api.__svkey__.param.Query__SVKEY__Request;
import com.ai.channel.__project__.api.__svkey__.param.Save__SVKEY__Request;
import com.ai.channel.__project__.api.__svkey__.vo.__SVKEY__DetailVo;
import com.ai.channel.__project__.api.__svkey__.vo.__SVKEY__ItemVo;
import com.ai.channel.base.vo.BaseResponse;
import com.ai.channel.base.vo.PageResult;

/** 
 * I__SVKEY__AtomSV.java
 * 
 * 
 * @date 
 * @author wygdove
 */
public interface I__SVKEY__AtomSV {
	int add(__SVKEY____SVKEY__ request);
	int update(__SVKEY____SVKEY__ request);
	__SVKEY____SVKEY__ queryById(__SVKEY____SVKEY__ request);
	List<__SVKEY____SVKEY__> query(__SVKEY____SVKEY__ request,Map<String,Object> reqmap);
}'''
    elif flag=='atomimpl':
        data='''package com.ai.channel.__project__.service.atom.impl;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.ai.channel.__project__.service.atom.interfaces.IAlertSendAtomSV;

/** 
 * __SVKEY__AtomSVImpl.java
 * 
 * 
 * @date 
 * @author wygdove
 */
@Component
public class __SVKEY__AtomSVImpl implements I__SVKEY__AtomSV {

	@Autowired
	__SVKEY____SVKEY__Mapper __sVKEY____SVKEY__Mapper;

	@Override
	public int add(__SVKEY____SVKEY__ request) {
		return __sVKEY____SVKEY__Mapper.insertSelective(request);
	}

	@Override
	public int update(__SVKEY____SVKEY__ request) {
		return __sVKEY____SVKEY__Mapper.updateByPrimaryKeySelective(request);
	}


	@Override
	public __SVKEY____SVKEY__ queryById(__SVKEY____SVKEY__ request) {
		return __sVKEY____SVKEY__Mapper.selectByPrimaryKey(request);
	}

	@Override
	public List<__SVKEY____SVKEY__> query(__SVKEY____SVKEY__ request,Map<String,Object> reqmap) {
		__SVKEY____SVKEY__Example example=new __SVKEY____SVKEY__Example();
		__SVKEY____SVKEY__Example.Criteria criteria=example.createCriteria();
		if(request!=null) {
		}
		if(reqmap!=null) {
		}
		example.setOrderByClause("");
		return __sVKEY____SVKEY__Mapper.selectByExample(example);
	}

}'''
    elif flag=='svtest':
        data='''package test.com.ai.channel.__project__.__svkey__;

import java.util.List;

import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;

import com.ai.channel.__project__.api.__svkey__.interfaces.I__SVKEY__SV;
import com.ai.channel.__project__.api.__svkey__.param.Query__SVKEY__Request;
import com.ai.channel.__project__.api.__svkey__.param.Save__SVKEY__Request;
import com.ai.channel.__project__.api.__svkey__.vo.__SVKEY__DetailVo;
import com.ai.channel.__project__.api.__svkey__.vo.__SVKEY__ItemVo;
import com.ai.channel.base.vo.BaseResponse;
import com.ai.channel.base.vo.PageArg;
import com.ai.channel.base.vo.PageResult;

import test.com.ai.channel.__project__.BaseTest;

/** 
 * __SVKEY__SVTest.java
 * 
 * 
 * @date 
 * @author wygdove
 */
public class __SVKEY__SVTest extends BaseTest {

	@Autowired
	I__SVKEY__SV __sVKEY__SV;
	
	@Test
	public void add() {
		Save__SVKEY__Request request=new Save__SVKEY__Request();
		BaseResponse<String> response=__sVKEY__SV.add__SVKEY__(request);
		print(response);
	}
	
	@Test
	public void update() {
		Save__SVKEY__Request request=new Save__SVKEY__Request();
		BaseResponse<String> response=__sVKEY__SV.update__SVKEY__(request);
		print(response);
	}
	
	@Test
	public void delete() {
		Save__SVKEY__Request request=new Save__SVKEY__Request();
		BaseResponse<String> response=__sVKEY__SV.delete__SVKEY__(request);
		print(response);
	}
	
	
	
	@Test
	public void queryDetail() {
		Query__SVKEY__Request request=new Query__SVKEY__Request();
		BaseResponse<__SVKEY__DetailVo> response=__sVKEY__SV.queryDetail__SVKEY__(request);
		print(response);
	}
	
	@Test
	public void queryList() {
		Query__SVKEY__Request request=new Query__SVKEY__Request();
		BaseResponse<List<__SVKEY__ItemVo>> response=__sVKEY__SV.queryList__SVKEY__(request);
		print(response);
	}
	
	@Test
	public void queryPage() {
		Query__SVKEY__Request request=new Query__SVKEY__Request();
		request.setPage(new PageArg(1,10));
		BaseResponse<PageResult<__SVKEY__ItemVo>> response=__sVKEY__SV.queryPage__SVKEY__(request);
		print(response);
	}
	
	
}'''
    else: data=''
    data=data.replace(' * @date ',' * @date '+getNow())
    data=data.replace('__SVKEY__',svkey)
    data=data.replace('__sVKEY__',svkeyl)
    data=data.replace('__svkey__',svkey.lower())
    data=data.replace('__project__',__project__)
    return data


def delFiles(path):
    ls=os.listdir(path)
    for i in ls:
        subpath=os.path.join(path,i)
        if os.path.isdir(subpath):
            delFiles(subpath)
        elif os.path.isfile(subpath):
            os.remove(subpath)
        else:
            pass


def getCurPath():
    return os.getcwd()


def getNow():
    return time.strftime("%Y-%m-%d %H:%M",time.localtime())


if __name__=='__main__':
    fi=open('in.txt','r')
    line=fi.readline()
    svkey=line.strip().replace('\n','')
    svkeyl=line[0].lower()+line[1:len(line)]
    fi.close()
    print svkey
    dosv(svkey,svkeyl)