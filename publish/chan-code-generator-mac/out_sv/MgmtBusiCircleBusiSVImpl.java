package com.ai.channel.mgmt.service.business.impl;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Transactional;

import com.ai.channel.mgmt.api.chlbusicircle.param.QueryMgmtBusiCircleRequest;
import com.ai.channel.mgmt.api.chlbusicircle.param.SaveMgmtBusiCircleRequest;
import com.ai.channel.mgmt.api.chlbusicircle.vo.MgmtBusiCircleDetailVo;
import com.ai.channel.mgmt.api.chlbusicircle.vo.MgmtBusiCircleItemVo;
import com.ai.channel.mgmt.base.constants.SeqConstants;
import com.ai.channel.mgmt.dao.mapper.bo.MgmtBasBusiCircle;
import com.ai.channel.mgmt.service.atom.interfaces.IMgmtBusiCircleAtomSV;
import com.ai.channel.mgmt.service.business.interfaces.IMgmtBusiCircleBusiSV;
import com.ai.channel.base.BusinessConstants;
import com.ai.channel.base.vo.BaseResponse;
import com.ai.channel.base.vo.PageResult;
import com.ai.channel.common.cmpt.sequence.util.SeqUtil;
import com.ai.channel.common.util.CollectionUtil;
import com.github.pagehelper.Page;
import com.github.pagehelper.PageHelper;

/**
 * MgmtBusiCircleBusiSVImpl.java
 *
 *
 * @date 2018-10-15 20:33
 * @author wygdove
 */
@Component
public class MgmtBusiCircleBusiSVImpl implements IMgmtBusiCircleBusiSV {

	@Autowired
	IMgmtBusiCircleAtomSV mgmtBusiCircleAtomSV;



	@Transactional
	@Override
	public BaseResponse<String> addMgmtBusiCircle(SaveMgmtBusiCircleRequest request) {
		BaseResponse<String> response=new BaseResponse<String>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);

		// Long itemId=SeqUtil.getNewId(SeqConstants.GIS_GRID_INFO_ID);
		// request.setId(""+itemId);

		MgmtBasBusiCircle mgmtBasBusiCircleRequest=this.setAtomSave(request);
		int res=mgmtBusiCircleAtomSV.add(mgmtBasBusiCircleRequest);
		if(res<=0) {
			response.setResult("");
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage("保存失败");
			return response;
		}

		// response.setResult(request.getId());
		// response.setInfo("");
		response.setSuccess(true);
		response.setResultCode(BusinessConstants.BUSI_SUCCESS_CODE);
		response.setResultMessage(BusinessConstants.BUSI_SUCCESS_MESSAGE);
		return response;
	}

	@Transactional
	@Override
	public BaseResponse<String> updateMgmtBusiCircle(SaveMgmtBusiCircleRequest request) {
		BaseResponse<String> response=new BaseResponse<String>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		// if(StringUtils.isBlank(request.getId())) {
		// 	response.setResult("");
		// 	response.setSuccess(false);
		// 	response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
		// 	response.setResultMessage("请求不能为空");
		// 	return response;
		// }

		MgmtBasBusiCircle mgmtBasBusiCircleRequest=this.setAtomSave(request);
		mgmtBusiCircleAtomSV.update(mgmtBasBusiCircleRequest);

		// response.setResult(request.getId());
		// response.setInfo("");
		response.setSuccess(true);
		response.setResultCode(BusinessConstants.BUSI_SUCCESS_CODE);
		response.setResultMessage(BusinessConstants.BUSI_SUCCESS_MESSAGE);
		return response;
	}



	@Transactional
	@Override
	public BaseResponse<String> deleteMgmtBusiCircle(SaveMgmtBusiCircleRequest request) {
		BaseResponse<String> response=new BaseResponse<String>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		// if(StringUtils.isBlank(request.getId())) {
		// 	response.setResult("");
		// 	response.setSuccess(false);
		// 	response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
		// 	response.setResultMessage("请求不能为空");
		// 	return response;
		// }

		MgmtBasBusiCircle mgmtBasBusiCircleRequest=new MgmtBasBusiCircle();
		// mgmtBusiCircleRequest.setId(request.getId());
		// mgmtBusiCircleRequest.setDelFlag(delFlag);
		// mgmtBusiCircleRequest.setUpdateUser(request.getUserId());
		// mgmtBusiCircleRequest.setUpdateTime(Calendar.getInstance().getTime());
		int res=mgmtBusiCircleAtomSV.update(mgmtBasBusiCircleRequest);
		if(res<=0) {
			response.setResult("");
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage("删除失败");
			return response;
		}

		// response.setResult(request.getId());
		response.setSuccess(true);
		response.setResultCode(BusinessConstants.BUSI_SUCCESS_CODE);
		response.setResultMessage(BusinessConstants.BUSI_SUCCESS_MESSAGE);
		return response;
	}



	@Override
	public BaseResponse<MgmtBusiCircleDetailVo> queryDetailMgmtBusiCircle(QueryMgmtBusiCircleRequest request) {
		BaseResponse<MgmtBusiCircleDetailVo> response=new BaseResponse<>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		MgmtBusiCircleDetailVo res=new MgmtBusiCircleDetailVo();
		MgmtBasBusiCircle mgmtBasBusiCircle=null;
//		if(StringUtils.isNotBlank(request.getId())) {
//			mgmtBasBusiCircle=mgmtBusiCircleAtomSV.queryById(request.getId());
//		}else if(StringUtils.isNotBlank(request.getCode())) {
			MgmtBasBusiCircle mgmtBasBusiCircleRequest=new MgmtBasBusiCircle();
//			mgmtBasBusiCircleRequest.setCode(request.getCode());
			List<MgmtBasBusiCircle> mgmtBasBusiCircleList=mgmtBusiCircleAtomSV.query(mgmtBasBusiCircleRequest,null);
			if(!CollectionUtil.isEmpty(mgmtBasBusiCircleList)) {
				mgmtBasBusiCircle=mgmtBasBusiCircleList.get(0);
			}
//		}
		if(mgmtBasBusiCircle==null) {
			response.setResult(res);
			response.setSuccess(false);
			response.setResultCode(BusinessConstants.BUSI_FAILURE_CODE);
			response.setResultMessage("详情查询出错");
			return response;
		}
		res=this.setVoDetail(mgmtBasBusiCircle);
		response.setResult(res);
		response.setSuccess(true);
		response.setResultCode(BusinessConstants.BUSI_SUCCESS_CODE);
		response.setResultMessage(BusinessConstants.BUSI_SUCCESS_MESSAGE);
		return response;
	}



	@Override
	public BaseResponse<List<MgmtBusiCircleItemVo>> queryListMgmtBusiCircle(QueryMgmtBusiCircleRequest request) {
		BaseResponse<List<MgmtBusiCircleItemVo>> response=new BaseResponse<>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		List<MgmtBusiCircleItemVo> result=new ArrayList<>();

		MgmtBasBusiCircle queryRequest=this.setAtomQuery(request);
		Map<String,Object> reqmap=this.setAtomQueryMap(request);
		List<MgmtBasBusiCircle> resList=mgmtBusiCircleAtomSV.query(queryRequest,reqmap);
		if(!CollectionUtil.isEmpty(resList)) {
			MgmtBusiCircleItemVo itemVo=null;
			for(MgmtBasBusiCircle item:resList) {
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
	public BaseResponse<PageResult<MgmtBusiCircleItemVo>> queryPageMgmtBusiCircle(QueryMgmtBusiCircleRequest request) {
		BaseResponse<PageResult<MgmtBusiCircleItemVo>> response=new BaseResponse<>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		PageResult<MgmtBusiCircleItemVo> pageResult=new PageResult<>();
		List<MgmtBusiCircleItemVo> result=new ArrayList<>();

		MgmtBasBusiCircle queryRequest=this.setAtomQuery(request);
		Map<String,Object> reqmap=this.setAtomQueryMap(request);
		int pageNum=request.getPage().getPageNum();
		int pageSize=request.getPage().getPageSize();
		PageHelper.startPage(pageNum,pageSize);

		List<MgmtBasBusiCircle> resList=new ArrayList<>();
		try {
			resList=mgmtBusiCircleAtomSV.query(queryRequest,reqmap);
		}finally {
			PageHelper.clearPage();
		}
		if(!CollectionUtil.isEmpty(resList)) {
			MgmtBusiCircleItemVo itemVo=null;
			for(MgmtBasBusiCircle item:resList) {
				itemVo=this.setVoItem(item);
				result.add(itemVo);
			}
			pageResult.setCount(((Page<MgmtBasBusiCircle>)resList).getTotal());
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

	@Override
	public BaseResponse<Long> countMgmtBusiCircle(QueryMgmtBusiCircleRequest request) {
		BaseResponse<Long> response=new BaseResponse<>(true,BusinessConstants.BUSI_SUCCESS_CODE,BusinessConstants.BUSI_SUCCESS_MESSAGE);
		MgmtBasBusiCircle queryRequest=this.setAtomQuery(request);
		Map<String,Object> reqmap=this.setAtomQueryMap(request);
		long result=mgmtBusiCircleAtomSV.count(queryRequest,reqmap);
		response.setResult(result);
		return response;
	}



	private MgmtBasBusiCircle setAtomSave(SaveMgmtBusiCircleRequest src) {
		MgmtBasBusiCircle res=new MgmtBasBusiCircle();
		res.setBusinessCircleCodeOrName(src.getBusinessCircleCodeOrName());
		res.setBusinessCircleId(src.getBusinessCircleId());
		res.setBusinessCircleName(src.getBusinessCircleName());
		res.setBusinessCircleType(src.getBusinessCircleType());
		res.setBusinessLevel(src.getBusinessLevel());
		res.setBusinessMainStreet(src.getBusinessMainStreet());
		res.setCoreMerchantName(src.getCoreMerchantName());
		res.setMerchantNum(src.getMerchantNum());
		res.setOperId(src.getOperId());
		res.setCreateTime(src.getCreateTime());
		res.setUpdateOperId(src.getUpdateOperId());
		res.setUpdateTime(src.getUpdateTime());
		res.setState(src.getState());
		res.setCoreMerchantCode(src.getCoreMerchantCode());
		res.setRemark(src.getRemark());
		res.setEastDescribe(src.getEastDescribe());
		res.setWestDescribe(src.getWestDescribe());
		res.setSouthDescribe(src.getSouthDescribe());
		res.setNorthDescribe(src.getNorthDescribe());
		res.setThirdBusiAreaCode(src.getThirdBusiAreaCode());
		res.setThirdAreaCode(src.getThirdAreaCode());
		res.setAdmRegProvinceCode(src.getAdmRegProvinceCode());
		res.setAdmRegCityCode(src.getAdmRegCityCode());
		res.setAdmRegCountyCode(src.getAdmRegCountyCode());
		res.setAdmRegTownCode(src.getAdmRegTownCode());
		res.setAdmRegVillageCode(src.getAdmRegVillageCode());
		res.setAdmRegCode(src.getAdmRegCode());
		res.setAdmRegName(src.getAdmRegName());
		res.setBusiRegProvinceCode(src.getBusiRegProvinceCode());
		res.setBusiRegCityCode(src.getBusiRegCityCode());
		res.setBusiRegCountyCode(src.getBusiRegCountyCode());
		res.setBusiRegAreaCode(src.getBusiRegAreaCode());
		res.setBusiRegGridCode(src.getBusiRegGridCode());
		res.setBusiRegMicroAreaCode(src.getBusiRegMicroAreaCode());
		res.setBusiRegCode(src.getBusiRegCode());
		res.setBusiRegName(src.getBusiRegName());
		res.setBusinessCircleCode(src.getBusinessCircleCode());
		res.setBusiCircleFuncDesc(src.getBusiCircleFuncDesc());
		res.setRegionCoverArea(src.getRegionCoverArea());
		res.setCommercialLandArea(src.getCommercialLandArea());
		res.setResidentPopulationNum(src.getResidentPopulationNum());
		res.setPopulationCharacter(src.getPopulationCharacter());
		res.setPopulationDensity(src.getPopulationDensity());
		res.setPerCapitaIncome(src.getPerCapitaIncome());
		res.setPerConsumption(src.getPerConsumption());
		res.setConsumerGroup(src.getConsumerGroup());
		res.setConsumerGroupCharacter(src.getConsumerGroupCharacter());
		res.setBaseStationName(src.getBaseStationName());
		res.setBaseStationSerial(src.getBaseStationSerial());
		res.setBusiCircleClass(src.getBusiCircleClass());
		res.setBusiCircleLatlngId(src.getBusiCircleLatlngId());
		return res;
	}

	private MgmtBasBusiCircle setAtomQuery(QueryMgmtBusiCircleRequest src) {
		MgmtBasBusiCircle res=new MgmtBasBusiCircle();
		if(src==null) return res;
		res.setBusinessCircleCodeOrName(src.getBusinessCircleCodeOrName());
		res.setBusinessCircleId(src.getBusinessCircleId());
		res.setBusinessCircleName(src.getBusinessCircleName());
		res.setBusinessCircleType(src.getBusinessCircleType());
		res.setBusinessLevel(src.getBusinessLevel());
		res.setBusinessMainStreet(src.getBusinessMainStreet());
		res.setCoreMerchantName(src.getCoreMerchantName());
		res.setMerchantNum(src.getMerchantNum());
		res.setOperId(src.getOperId());
		res.setCreateTime(src.getCreateTime());
		res.setUpdateOperId(src.getUpdateOperId());
		res.setUpdateTime(src.getUpdateTime());
		res.setState(src.getState());
		res.setCoreMerchantCode(src.getCoreMerchantCode());
		res.setRemark(src.getRemark());
		res.setEastDescribe(src.getEastDescribe());
		res.setWestDescribe(src.getWestDescribe());
		res.setSouthDescribe(src.getSouthDescribe());
		res.setNorthDescribe(src.getNorthDescribe());
		res.setThirdBusiAreaCode(src.getThirdBusiAreaCode());
		res.setThirdAreaCode(src.getThirdAreaCode());
		res.setAdmRegProvinceCode(src.getAdmRegProvinceCode());
		res.setAdmRegCityCode(src.getAdmRegCityCode());
		res.setAdmRegCountyCode(src.getAdmRegCountyCode());
		res.setAdmRegTownCode(src.getAdmRegTownCode());
		res.setAdmRegVillageCode(src.getAdmRegVillageCode());
		res.setAdmRegCode(src.getAdmRegCode());
		res.setAdmRegName(src.getAdmRegName());
		res.setBusiRegProvinceCode(src.getBusiRegProvinceCode());
		res.setBusiRegCityCode(src.getBusiRegCityCode());
		res.setBusiRegCountyCode(src.getBusiRegCountyCode());
		res.setBusiRegAreaCode(src.getBusiRegAreaCode());
		res.setBusiRegGridCode(src.getBusiRegGridCode());
		res.setBusiRegMicroAreaCode(src.getBusiRegMicroAreaCode());
		res.setBusiRegCode(src.getBusiRegCode());
		res.setBusiRegName(src.getBusiRegName());
		res.setBusinessCircleCode(src.getBusinessCircleCode());
		res.setBusiCircleFuncDesc(src.getBusiCircleFuncDesc());
		res.setRegionCoverArea(src.getRegionCoverArea());
		res.setCommercialLandArea(src.getCommercialLandArea());
		res.setResidentPopulationNum(src.getResidentPopulationNum());
		res.setPopulationCharacter(src.getPopulationCharacter());
		res.setPopulationDensity(src.getPopulationDensity());
		res.setPerCapitaIncome(src.getPerCapitaIncome());
		res.setPerConsumption(src.getPerConsumption());
		res.setConsumerGroup(src.getConsumerGroup());
		res.setConsumerGroupCharacter(src.getConsumerGroupCharacter());
		res.setBaseStationName(src.getBaseStationName());
		res.setBaseStationSerial(src.getBaseStationSerial());
		res.setBusiCircleClass(src.getBusiCircleClass());
		res.setBusiCircleLatlngId(src.getBusiCircleLatlngId());
		return res;
	}
	private Map<String,Object> setAtomQueryMap(QueryMgmtBusiCircleRequest src) {
		Map<String,Object> res=new HashMap<>();
		if(src==null) return res;
		return res;
	}

	private MgmtBusiCircleDetailVo setVoDetail(MgmtBasBusiCircle src) {
		MgmtBusiCircleDetailVo res=new MgmtBusiCircleDetailVo();
		if(src==null) return res;
		res.setBusinessCircleCodeOrName(src.getBusinessCircleCodeOrName());
		res.setBusinessCircleId(src.getBusinessCircleId());
		res.setBusinessCircleName(src.getBusinessCircleName());
		res.setBusinessCircleType(src.getBusinessCircleType());
		res.setBusinessLevel(src.getBusinessLevel());
		res.setBusinessMainStreet(src.getBusinessMainStreet());
		res.setCoreMerchantName(src.getCoreMerchantName());
		res.setMerchantNum(src.getMerchantNum());
		res.setOperId(src.getOperId());
		res.setCreateTime(src.getCreateTime());
		res.setUpdateOperId(src.getUpdateOperId());
		res.setUpdateTime(src.getUpdateTime());
		res.setState(src.getState());
		res.setCoreMerchantCode(src.getCoreMerchantCode());
		res.setRemark(src.getRemark());
		res.setEastDescribe(src.getEastDescribe());
		res.setWestDescribe(src.getWestDescribe());
		res.setSouthDescribe(src.getSouthDescribe());
		res.setNorthDescribe(src.getNorthDescribe());
		res.setThirdBusiAreaCode(src.getThirdBusiAreaCode());
		res.setThirdAreaCode(src.getThirdAreaCode());
		res.setAdmRegProvinceCode(src.getAdmRegProvinceCode());
		res.setAdmRegCityCode(src.getAdmRegCityCode());
		res.setAdmRegCountyCode(src.getAdmRegCountyCode());
		res.setAdmRegTownCode(src.getAdmRegTownCode());
		res.setAdmRegVillageCode(src.getAdmRegVillageCode());
		res.setAdmRegCode(src.getAdmRegCode());
		res.setAdmRegName(src.getAdmRegName());
		res.setBusiRegProvinceCode(src.getBusiRegProvinceCode());
		res.setBusiRegCityCode(src.getBusiRegCityCode());
		res.setBusiRegCountyCode(src.getBusiRegCountyCode());
		res.setBusiRegAreaCode(src.getBusiRegAreaCode());
		res.setBusiRegGridCode(src.getBusiRegGridCode());
		res.setBusiRegMicroAreaCode(src.getBusiRegMicroAreaCode());
		res.setBusiRegCode(src.getBusiRegCode());
		res.setBusiRegName(src.getBusiRegName());
		res.setBusinessCircleCode(src.getBusinessCircleCode());
		res.setBusiCircleFuncDesc(src.getBusiCircleFuncDesc());
		res.setRegionCoverArea(src.getRegionCoverArea());
		res.setCommercialLandArea(src.getCommercialLandArea());
		res.setResidentPopulationNum(src.getResidentPopulationNum());
		res.setPopulationCharacter(src.getPopulationCharacter());
		res.setPopulationDensity(src.getPopulationDensity());
		res.setPerCapitaIncome(src.getPerCapitaIncome());
		res.setPerConsumption(src.getPerConsumption());
		res.setConsumerGroup(src.getConsumerGroup());
		res.setConsumerGroupCharacter(src.getConsumerGroupCharacter());
		res.setBaseStationName(src.getBaseStationName());
		res.setBaseStationSerial(src.getBaseStationSerial());
		res.setBusiCircleClass(src.getBusiCircleClass());
		res.setBusiCircleLatlngId(src.getBusiCircleLatlngId());
		return res;
	}
	private MgmtBusiCircleItemVo setVoItem(MgmtBasBusiCircle src) {
		MgmtBusiCircleItemVo res=new MgmtBusiCircleItemVo();
		if(src==null) return res;
		res.setBusinessCircleCodeOrName(src.getBusinessCircleCodeOrName());
		res.setBusinessCircleId(src.getBusinessCircleId());
		res.setBusinessCircleName(src.getBusinessCircleName());
		res.setBusinessCircleType(src.getBusinessCircleType());
		res.setBusinessLevel(src.getBusinessLevel());
		res.setBusinessMainStreet(src.getBusinessMainStreet());
		res.setCoreMerchantName(src.getCoreMerchantName());
		res.setMerchantNum(src.getMerchantNum());
		res.setOperId(src.getOperId());
		res.setCreateTime(src.getCreateTime());
		res.setUpdateOperId(src.getUpdateOperId());
		res.setUpdateTime(src.getUpdateTime());
		res.setState(src.getState());
		res.setCoreMerchantCode(src.getCoreMerchantCode());
		res.setRemark(src.getRemark());
		res.setEastDescribe(src.getEastDescribe());
		res.setWestDescribe(src.getWestDescribe());
		res.setSouthDescribe(src.getSouthDescribe());
		res.setNorthDescribe(src.getNorthDescribe());
		res.setThirdBusiAreaCode(src.getThirdBusiAreaCode());
		res.setThirdAreaCode(src.getThirdAreaCode());
		res.setAdmRegProvinceCode(src.getAdmRegProvinceCode());
		res.setAdmRegCityCode(src.getAdmRegCityCode());
		res.setAdmRegCountyCode(src.getAdmRegCountyCode());
		res.setAdmRegTownCode(src.getAdmRegTownCode());
		res.setAdmRegVillageCode(src.getAdmRegVillageCode());
		res.setAdmRegCode(src.getAdmRegCode());
		res.setAdmRegName(src.getAdmRegName());
		res.setBusiRegProvinceCode(src.getBusiRegProvinceCode());
		res.setBusiRegCityCode(src.getBusiRegCityCode());
		res.setBusiRegCountyCode(src.getBusiRegCountyCode());
		res.setBusiRegAreaCode(src.getBusiRegAreaCode());
		res.setBusiRegGridCode(src.getBusiRegGridCode());
		res.setBusiRegMicroAreaCode(src.getBusiRegMicroAreaCode());
		res.setBusiRegCode(src.getBusiRegCode());
		res.setBusiRegName(src.getBusiRegName());
		res.setBusinessCircleCode(src.getBusinessCircleCode());
		res.setBusiCircleFuncDesc(src.getBusiCircleFuncDesc());
		res.setRegionCoverArea(src.getRegionCoverArea());
		res.setCommercialLandArea(src.getCommercialLandArea());
		res.setResidentPopulationNum(src.getResidentPopulationNum());
		res.setPopulationCharacter(src.getPopulationCharacter());
		res.setPopulationDensity(src.getPopulationDensity());
		res.setPerCapitaIncome(src.getPerCapitaIncome());
		res.setPerConsumption(src.getPerConsumption());
		res.setConsumerGroup(src.getConsumerGroup());
		res.setConsumerGroupCharacter(src.getConsumerGroupCharacter());
		res.setBaseStationName(src.getBaseStationName());
		res.setBaseStationSerial(src.getBaseStationSerial());
		res.setBusiCircleClass(src.getBusiCircleClass());
		res.setBusiCircleLatlngId(src.getBusiCircleLatlngId());
		return res;
	}

}