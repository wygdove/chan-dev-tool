package com.ai.channel.mgmt.service.business.interfaces;

import java.util.List;

import com.ai.channel.mgmt.api.chlbusicircle.param.QueryMgmtBusiCircleRequest;
import com.ai.channel.mgmt.api.chlbusicircle.param.SaveMgmtBusiCircleRequest;
import com.ai.channel.mgmt.api.chlbusicircle.vo.MgmtBusiCircleDetailVo;
import com.ai.channel.mgmt.api.chlbusicircle.vo.MgmtBusiCircleItemVo;
import com.ai.channel.base.vo.BaseResponse;
import com.ai.channel.base.vo.PageResult;

/**
 * IMgmtBusiCircleBusiSV.java
 *
 *
 * @date 2018-10-15 20:33
 * @author wygdove
 */
public interface IMgmtBusiCircleBusiSV {

	BaseResponse<String> addMgmtBusiCircle(SaveMgmtBusiCircleRequest request);
	BaseResponse<String> updateMgmtBusiCircle(SaveMgmtBusiCircleRequest request);

	BaseResponse<String> deleteMgmtBusiCircle(SaveMgmtBusiCircleRequest request);

	BaseResponse<MgmtBusiCircleDetailVo> queryDetailMgmtBusiCircle(QueryMgmtBusiCircleRequest request);

	BaseResponse<List<MgmtBusiCircleItemVo>> queryListMgmtBusiCircle(QueryMgmtBusiCircleRequest request);
	BaseResponse<PageResult<MgmtBusiCircleItemVo>> queryPageMgmtBusiCircle(QueryMgmtBusiCircleRequest request);
	BaseResponse<Long> countMgmtBusiCircle(QueryMgmtBusiCircleRequest request);

}