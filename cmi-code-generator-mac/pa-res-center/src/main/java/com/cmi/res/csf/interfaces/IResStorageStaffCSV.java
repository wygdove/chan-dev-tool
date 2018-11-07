package com.cmi.res.csf.interfaces;

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
public interface IResStorageStaffCSV {

	/**
	 * 添加
	 * @param request 请求参数
	 * @return 操作结果
	 * @Author wygdove
	 */
	Response<String> addResStorageStaff(SaveResStorageStaffRequest request) throws Exception;

	/**
	 * 批量添加
	 * @param request 请求参数
	 * @return 操作结果
	 * @Author wygdove
	 */
	Response<String> addBatchResStorageStaff(SaveResStorageStaffRequest request) throws Exception;

	/**
	 * 更新
	 * @param request 请求参数
	 *                   主键不能为空
	 * @return 操作结果
	 * @Author wygdove
	 */
	Response<String> updateResStorageStaff(SaveResStorageStaffRequest request) throws Exception;

	/**
	 * 删除
	 * @param request 请求参数
	 *                   主键不能为空
	 *                   逻辑删除，可撤销删除
	 * @return 操作结果
	 * @Author wygdove
	 */
	Response<String> deleteResStorageStaff(SaveResStorageStaffRequest request) throws Exception;


	/**
	 * 详情查询
	 * @param request 请求参数
	 * @return 操作结果
	 * @Author wygdove
	 */
	Response<ResStorageStaffDetailVo> queryDetailResStorageStaff(QueryResStorageStaffRequest request) throws Exception;


	/**
	 * 列表查询
	 * @param request 请求参数
	 * @return 操作结果
	 * @Author wygdove
	 */
	Response<List<ResStorageStaffItemVo>> queryListResStorageStaff(QueryResStorageStaffRequest request) throws Exception;

	/**
	 * 分页列表查询
	 * @param request 请求参数
	 * @return 操作结果
	 * @Author wygdove
	 */
	Response<PageResult<ResStorageStaffItemVo>> queryPageResStorageStaff(QueryResStorageStaffRequest request) throws Exception;

	/**
	 * 计数
	 * @param request 请求参数
	 * @return 操作结果
	 * @Author wygdove
	 */
	Response<Long> countResStorageStaff(QueryResStorageStaffRequest request) throws Exception;


}
