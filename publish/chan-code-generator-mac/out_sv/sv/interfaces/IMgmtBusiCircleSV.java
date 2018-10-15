package com.ai.channel.mgmt.api.chlbusicircle.interfaces;

import java.util.List;

import javax.ws.rs.Consumes;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import com.ai.channel.BusinessException;
import com.ai.channel.SystemException;
import com.ai.channel.mgmt.api.chlbusicircle.param.QueryMgmtBusiCircleRequest;
import com.ai.channel.mgmt.api.chlbusicircle.param.SaveMgmtBusiCircleRequest;
import com.ai.channel.mgmt.api.chlbusicircle.vo.MgmtBusiCircleDetailVo;
import com.ai.channel.mgmt.api.chlbusicircle.vo.MgmtBusiCircleItemVo;
import com.ai.channel.base.vo.BaseResponse;
import com.ai.channel.base.vo.PageResult;

/**
 * IMgmtBusiCircleSV.java
 *
 *
 * @date 2018-10-15 20:36
 * @author wygdove
 */
@Path("/mgmtBusiCircleSV")
@Consumes({MediaType.APPLICATION_JSON})
@Produces({MediaType.APPLICATION_JSON, MediaType.TEXT_XML})
public interface IMgmtBusiCircleSV {


	/**
	 * 添加
	 * @param request
	 * @return
	 * @throws BusinessException
	 * @throws SystemException
	 * @author wygdove
	 */
    @POST
    @Path("/addMgmtBusiCircle")
    BaseResponse<String> addMgmtBusiCircle(SaveMgmtBusiCircleRequest request) throws BusinessException, SystemException;

    /**
	 * 更新
	 * @param request
	 * @return
	 * @throws BusinessException
	 * @throws SystemException
	 * @author wygdove
	 */
    @POST
    @Path("/updateMgmtBusiCircle")
    BaseResponse<String> updateMgmtBusiCircle(SaveMgmtBusiCircleRequest request) throws BusinessException, SystemException;

    /**
	 * 删除
	 * @param request
	 * @return
	 * @throws BusinessException
	 * @throws SystemException
	 * @author wygdove
	 */
    @POST
    @Path("/deleteMgmtBusiCircle")
    BaseResponse<String> deleteMgmtBusiCircle(SaveMgmtBusiCircleRequest request) throws BusinessException, SystemException;



    /**
	 * 详情查询
	 * @param request
	 * @return
	 * @throws BusinessException
	 * @throws SystemException
	 * @author wygdove
	 */
    @POST
    @Path("/queryDetailMgmtBusiCircle")
    BaseResponse<MgmtBusiCircleDetailVo> queryDetailMgmtBusiCircle(QueryMgmtBusiCircleRequest request) throws BusinessException, SystemException;



	/**
	 * 列表查询
	 * @param request
	 * @return
	 * @throws BusinessException
	 * @throws SystemException
	 * @author wygdove
	 */
    @POST
    @Path("/queryListMgmtBusiCircle")
    BaseResponse<List<MgmtBusiCircleItemVo>> queryListMgmtBusiCircle(QueryMgmtBusiCircleRequest request) throws BusinessException, SystemException;

    /**
     * 分页列表查询
     * @param request
     * @return
     * @throws BusinessException
     * @throws SystemException
     * @author wygdove
     */
    @POST
    @Path("/queryPageMgmtBusiCircle")
    BaseResponse<PageResult<MgmtBusiCircleItemVo>> queryPageMgmtBusiCircle(QueryMgmtBusiCircleRequest request) throws BusinessException, SystemException;

    /**
     * 计数
     * @param request
     * @return
     * @throws BusinessException
     * @throws SystemException
     * @author wygdove
     */
    @POST
    @Path("/countMgmtBusiCircle")
    BaseResponse<Long> countMgmtBusiCircle(QueryMgmtBusiCircleRequest request) throws BusinessException, SystemException;


}