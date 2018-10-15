package com.ai.channel.mgmt.service.atom.impl;

import java.util.List;
import java.util.Map;

import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.ai.channel.common.util.CollectionUtil;
import com.ai.channel.mgmt.dao.mapper.bo.MgmtBasBusiCircle;
import com.ai.channel.mgmt.dao.mapper.bo.MgmtBasBusiCircleExample;
import com.ai.channel.mgmt.dao.mapper.interfaces.MgmtBasBusiCircleMapper;
import com.ai.channel.mgmt.service.atom.interfaces.IMgmtBusiCircleAtomSV;

/**
 * MgmtBusiCircleAtomSVImpl.java
 *
 *
 * @date 2018-10-15 20:59
 * @author wygdove
 */
@Component
public class MgmtBusiCircleAtomSVImpl implements IMgmtBusiCircleAtomSV {

	@Autowired
	MgmtBasBusiCircleMapper mgmtBasBusiCircleMapper;

	@Override
	public int add(MgmtBasBusiCircle request) {
		return mgmtBasBusiCircleMapper.insertSelective(request);
	}

	@Override
	public int update(MgmtBasBusiCircle request) {
		return mgmtBasBusiCircleMapper.updateByPrimaryKeySelective(request);
	}


	@Override
	public MgmtBasBusiCircle queryById(MgmtBasBusiCircle request) {
		return mgmtBasBusiCircleMapper.selectByPrimaryKey(request);
	}

	@Override
	public List<MgmtBasBusiCircle> query(MgmtBasBusiCircle request,Map<String,Object> reqmap) {
		MgmtBasBusiCircleExample example=this.getExample(request,reqmap);
		return mgmtBasBusiCircleMapper.selectByExample(example);
	}
	
	@Override
	public long count(MgmtBasBusiCircle request,Map<String,Object> reqmap) {
		MgmtBasBusiCircleExample example=this.getExample(request,reqmap);
		return mgmtBasBusiCircleMapper.countByExample(example);
	}
	
	private MgmtBasBusiCircleExample getExample(MgmtBasBusiCircle request,Map<String,Object> reqmap) {
		MgmtBasBusiCircleExample example=new MgmtBasBusiCircleExample();
		MgmtBasBusiCircleExample.Criteria criteria=example.createCriteria();
		if(request!=null) {
		    if(StringUtils.isNotBlank(request.getBusinessCircleCodeOrName())) {criteria.andBusinessCircleCodeOrNameEqualTo(request.getBusinessCircleCodeOrName());}
			if(StringUtils.isNotBlank(request.getBusinessCircleId())) {criteria.andBusinessCircleIdEqualTo(request.getBusinessCircleId());}
			if(StringUtils.isNotBlank(request.getBusinessCircleName())) {criteria.andBusinessCircleNameEqualTo(request.getBusinessCircleName());}
			if(StringUtils.isNotBlank(request.getBusinessCircleType())) {criteria.andBusinessCircleTypeEqualTo(request.getBusinessCircleType());}
			if(StringUtils.isNotBlank(request.getBusinessLevel())) {criteria.andBusinessLevelEqualTo(request.getBusinessLevel());}
			if(StringUtils.isNotBlank(request.getBusinessMainStreet())) {criteria.andBusinessMainStreetEqualTo(request.getBusinessMainStreet());}
			if(StringUtils.isNotBlank(request.getCoreMerchantName())) {criteria.andCoreMerchantNameEqualTo(request.getCoreMerchantName());}
			if(StringUtils.isNotBlank(request.getMerchantNum())) {criteria.andMerchantNumEqualTo(request.getMerchantNum());}
			if(StringUtils.isNotBlank(request.getOperId())) {criteria.andOperIdEqualTo(request.getOperId());}
			if(StringUtils.isNotBlank(request.getCreateTime())) {criteria.andCreateTimeEqualTo(request.getCreateTime());}
			if(StringUtils.isNotBlank(request.getUpdateOperId())) {criteria.andUpdateOperIdEqualTo(request.getUpdateOperId());}
			if(StringUtils.isNotBlank(request.getUpdateTime())) {criteria.andUpdateTimeEqualTo(request.getUpdateTime());}
			if(StringUtils.isNotBlank(request.getState())) {criteria.andStateEqualTo(request.getState());}
			if(StringUtils.isNotBlank(request.getCoreMerchantCode())) {criteria.andCoreMerchantCodeEqualTo(request.getCoreMerchantCode());}
			if(StringUtils.isNotBlank(request.getRemark())) {criteria.andRemarkEqualTo(request.getRemark());}
			if(StringUtils.isNotBlank(request.getEastDescribe())) {criteria.andEastDescribeEqualTo(request.getEastDescribe());}
			if(StringUtils.isNotBlank(request.getWestDescribe())) {criteria.andWestDescribeEqualTo(request.getWestDescribe());}
			if(StringUtils.isNotBlank(request.getSouthDescribe())) {criteria.andSouthDescribeEqualTo(request.getSouthDescribe());}
			if(StringUtils.isNotBlank(request.getNorthDescribe())) {criteria.andNorthDescribeEqualTo(request.getNorthDescribe());}
			if(StringUtils.isNotBlank(request.getThirdBusiAreaCode())) {criteria.andThirdBusiAreaCodeEqualTo(request.getThirdBusiAreaCode());}
			if(StringUtils.isNotBlank(request.getThirdAreaCode())) {criteria.andThirdAreaCodeEqualTo(request.getThirdAreaCode());}
			if(StringUtils.isNotBlank(request.getAdmRegProvinceCode())) {criteria.andAdmRegProvinceCodeEqualTo(request.getAdmRegProvinceCode());}
			if(StringUtils.isNotBlank(request.getAdmRegCityCode())) {criteria.andAdmRegCityCodeEqualTo(request.getAdmRegCityCode());}
			if(StringUtils.isNotBlank(request.getAdmRegCountyCode())) {criteria.andAdmRegCountyCodeEqualTo(request.getAdmRegCountyCode());}
			if(StringUtils.isNotBlank(request.getAdmRegTownCode())) {criteria.andAdmRegTownCodeEqualTo(request.getAdmRegTownCode());}
			if(StringUtils.isNotBlank(request.getAdmRegVillageCode())) {criteria.andAdmRegVillageCodeEqualTo(request.getAdmRegVillageCode());}
			if(StringUtils.isNotBlank(request.getAdmRegCode())) {criteria.andAdmRegCodeEqualTo(request.getAdmRegCode());}
			if(StringUtils.isNotBlank(request.getAdmRegName())) {criteria.andAdmRegNameEqualTo(request.getAdmRegName());}
			if(StringUtils.isNotBlank(request.getBusiRegProvinceCode())) {criteria.andBusiRegProvinceCodeEqualTo(request.getBusiRegProvinceCode());}
			if(StringUtils.isNotBlank(request.getBusiRegCityCode())) {criteria.andBusiRegCityCodeEqualTo(request.getBusiRegCityCode());}
			if(StringUtils.isNotBlank(request.getBusiRegCountyCode())) {criteria.andBusiRegCountyCodeEqualTo(request.getBusiRegCountyCode());}
			if(StringUtils.isNotBlank(request.getBusiRegAreaCode())) {criteria.andBusiRegAreaCodeEqualTo(request.getBusiRegAreaCode());}
			if(StringUtils.isNotBlank(request.getBusiRegGridCode())) {criteria.andBusiRegGridCodeEqualTo(request.getBusiRegGridCode());}
			if(StringUtils.isNotBlank(request.getBusiRegMicroAreaCode())) {criteria.andBusiRegMicroAreaCodeEqualTo(request.getBusiRegMicroAreaCode());}
			if(StringUtils.isNotBlank(request.getBusiRegCode())) {criteria.andBusiRegCodeEqualTo(request.getBusiRegCode());}
			if(StringUtils.isNotBlank(request.getBusiRegName())) {criteria.andBusiRegNameEqualTo(request.getBusiRegName());}
			if(StringUtils.isNotBlank(request.getBusinessCircleCode())) {criteria.andBusinessCircleCodeEqualTo(request.getBusinessCircleCode());}
			if(StringUtils.isNotBlank(request.getBusiCircleFuncDesc())) {criteria.andBusiCircleFuncDescEqualTo(request.getBusiCircleFuncDesc());}
			if(StringUtils.isNotBlank(request.getRegionCoverArea())) {criteria.andRegionCoverAreaEqualTo(request.getRegionCoverArea());}
			if(StringUtils.isNotBlank(request.getCommercialLandArea())) {criteria.andCommercialLandAreaEqualTo(request.getCommercialLandArea());}
			if(StringUtils.isNotBlank(request.getResidentPopulationNum())) {criteria.andResidentPopulationNumEqualTo(request.getResidentPopulationNum());}
			if(StringUtils.isNotBlank(request.getPopulationCharacter())) {criteria.andPopulationCharacterEqualTo(request.getPopulationCharacter());}
			if(StringUtils.isNotBlank(request.getPopulationDensity())) {criteria.andPopulationDensityEqualTo(request.getPopulationDensity());}
			if(StringUtils.isNotBlank(request.getPerCapitaIncome())) {criteria.andPerCapitaIncomeEqualTo(request.getPerCapitaIncome());}
			if(StringUtils.isNotBlank(request.getPerConsumption())) {criteria.andPerConsumptionEqualTo(request.getPerConsumption());}
			if(StringUtils.isNotBlank(request.getConsumerGroup())) {criteria.andConsumerGroupEqualTo(request.getConsumerGroup());}
			if(StringUtils.isNotBlank(request.getConsumerGroupCharacter())) {criteria.andConsumerGroupCharacterEqualTo(request.getConsumerGroupCharacter());}
			if(StringUtils.isNotBlank(request.getBaseStationName())) {criteria.andBaseStationNameEqualTo(request.getBaseStationName());}
			if(StringUtils.isNotBlank(request.getBaseStationSerial())) {criteria.andBaseStationSerialEqualTo(request.getBaseStationSerial());}
			if(StringUtils.isNotBlank(request.getBusiCircleClass())) {criteria.andBusiCircleClassEqualTo(request.getBusiCircleClass());}
			if(StringUtils.isNotBlank(request.getBusiCircleLatlngId())) {criteria.andBusiCircleLatlngIdEqualTo(request.getBusiCircleLatlngId());}
		}
		if(reqmap!=null) {
			if(reqmap.containsKey("codes")) {
				@SuppressWarnings("unchecked")
				List<String> values=(List<String>)reqmap.get("codes");
//				criteria.andCodeIn(values);
			}
		}
		if(reqmap!=null&&reqmap.containsKey("orderByClause")) {
			String value=(String)reqmap.get("orderByClause");
			example.setOrderByClause(value);
//		}else {
//			example.setOrderByClause("");	// 加else则必填
		}
		return example;
	}

}