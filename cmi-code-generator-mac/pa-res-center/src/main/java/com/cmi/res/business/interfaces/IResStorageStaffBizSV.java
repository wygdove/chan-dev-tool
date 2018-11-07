package com.cmi.res.business.interfaces;

import com.cmi.common.domain.PageResult;
import com.cmi.common.domain.Response;
import com.cmi.res.domain.resstoragestaff.params.QueryResStorageStaffRequest;
import com.cmi.res.domain.resstoragestaff.params.SaveResStorageStaffRequest;
import com.cmi.res.domain.resstoragestaff.vo.ResStorageStaffDetailVo;
import com.cmi.res.domain.resstoragestaff.vo.ResStorageStaffItemVo;

import java.util.List;

/**
 * @Title:
 * @Description:
 * @Date: 2018-11-07 09:42
 * @Author: wygdove
 */
public interface IResStorageStaffBizSV {
	public Response<String> addResStorageStaff(SaveResStorageStaffRequest request) throws Exception;
	public Response<String> addBatchResStorageStaff(SaveResStorageStaffRequest request) throws Exception;
	public Response<String> updateResStorageStaff(SaveResStorageStaffRequest request) throws Exception;
	public Response<String> deleteResStorageStaff(SaveResStorageStaffRequest request) throws Exception;
	public Response<ResStorageStaffDetailVo> queryDetailResStorageStaff(QueryResStorageStaffRequest request) throws Exception;
	public Response<List<ResStorageStaffItemVo>> queryListResStorageStaff(QueryResStorageStaffRequest request) throws Exception;
	public Response<PageResult<ResStorageStaffItemVo>> queryPageResStorageStaff(QueryResStorageStaffRequest request) throws Exception;
	public Response<Long> countResStorageStaff(QueryResStorageStaffRequest request) throws Exception;
}
