package com.ai.channel.mgmt.service.atom.interfaces;

import java.util.List;
import java.util.Map;

import com.ai.channel.mgmt.dao.mapper.bo.MgmtBasBusiCircle;


/**
 * IMgmtBusiCircleAtomSV.java
 *
 *
 * @date 2018-10-15 20:59
 * @author wygdove
 */
public interface IMgmtBusiCircleAtomSV {
	int add(MgmtBasBusiCircle request);
	int update(MgmtBasBusiCircle request);
	MgmtBasBusiCircle queryById(MgmtBasBusiCircle request);
	List<MgmtBasBusiCircle> query(MgmtBasBusiCircle request,Map<String,Object> reqmap);
	long count(MgmtBasBusiCircle request,Map<String,Object> reqmap);
}