package com.ai.channel.mgmt.util;

import java.sql.Timestamp;
import java.util.Date;

import org.apache.commons.lang3.StringUtils;

import com.ai.channel.common.util.DateUtil;


/**
 * MgmtBusiCircleBusiSVImpl.java
 *
 *
 * @date 2018-10-15 20:55
 * @author wygdove
 */
public class VoConvertUtil {

	public static String getValue(String value) {
		return StringUtils.isBlank(value)?"":value;
	}

	public static String getValue(Short value) {
		return value==null?"":""+value;
	}

	public static String getValue(Integer value) {
		return value==null?"":""+value;
	}

	public static String getValue(Long value) {
		return value==null?"":""+value;
	}

	public static String getValue(Float value) {
		return value==null?"":""+value;
	}

	public static String getValue(Double value) {
		return value==null?"":""+value;
	}


	public static String getValue(Date value) {
		return getValue(value,DateUtil.DATETIME_FORMAT);
	}

	public static String getValue(Date value,String pattern) {
		String res="";
		try {
			res=DateUtil.getDateString(value,pattern);
		}catch (Exception e) {
			res="";
		}
		return res;
	}


	public static String getValue(Timestamp value) {
		return getValue(value,DateUtil.DATETIME_FORMAT);
	}

	public static String getValue(Timestamp value,String pattern) {
		String res="";
		try {
			res=DateUtil.getDateString(value,pattern);
		}catch (Exception e) {
			res="";
		}
		return res;
	}



	
	
	
}
