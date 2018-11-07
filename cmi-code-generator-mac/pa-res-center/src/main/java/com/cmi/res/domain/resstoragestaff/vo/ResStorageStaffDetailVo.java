package com.cmi.res.domain.resstoragestaff.vo;

import org.codehaus.jackson.annotate.JsonIgnoreProperties;

import java.io.Serializable;

/**
 * @Title:
 * @Description:
 * @Date: 2018-11-07 09:42
 * @Author: wygdove
 */
@JsonIgnoreProperties(ignoreUnknown=true)
public class ResStorageStaffDetailVo implements Serializable {
	private String state;
	private String staffId;
	private String storageId;
	private String staffLevel;
	private String storageStaffId;


	public String getState() {
		return state;
	}
	public void setState(String state) {
		this.state=state;
	}
	public String getStaffId() {
		return staffId;
	}
	public void setStaffId(String staffId) {
		this.staffId=staffId;
	}
	public String getStorageId() {
		return storageId;
	}
	public void setStorageId(String storageId) {
		this.storageId=storageId;
	}
	public String getStaffLevel() {
		return staffLevel;
	}
	public void setStaffLevel(String staffLevel) {
		this.staffLevel=staffLevel;
	}
	public String getStorageStaffId() {
		return storageStaffId;
	}
	public void setStorageStaffId(String storageStaffId) {
		this.storageStaffId=storageStaffId;
	}

}
