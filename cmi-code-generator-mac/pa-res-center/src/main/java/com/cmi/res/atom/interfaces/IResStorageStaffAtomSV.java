package com.cmi.res.atom.interfaces;

import com.cmi.res.atom.bo.ResStorageStaffBean;

import java.util.Map;

/**
 * @Title:
 * @Description:
 * @Date: 2018-11-07 09:42
 * @Author: wygdove
 */
public interface IResStorageStaffAtomSV {
  void add(ResStorageStaffBean request) throws Exception;
  void update(ResStorageStaffBean request) throws Exception;
  ResStorageStaffBean queryById(ResStorageStaffBean request) throws Exception;
  ResStorageStaffBean[] query(ResStorageStaffBean request,Map<String,Object> reqmap) throws Exception;
  ResStorageStaffBean[] queryPage(ResStorageStaffBean request,Map<String,Object> reqmap,int startNum,int endNum) throws Exception;
  long count(ResStorageStaffBean request,Map<String,Object> reqmap) throws Exception;
}