package com.cmi.res.atom.impl;

import com.ai.appframe2.util.criteria.Criteria;
import com.cmi.common.util.BeanUtil;
import com.cmi.res.atom.bo.ResStorageStaffBean;
import com.cmi.res.atom.bo.ResStorageStaffEngine;
import com.cmi.res.atom.interfaces.IResStorageStaffAtomSV;
import com.cmi.res.atom.ivalues.IResStorageStaffValue;
import org.apache.commons.lang3.StringUtils;

import java.sql.Timestamp;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @Title:
 * @Description:
 * @Date: 2018-11-07 09:42
 * @Author: wygdove
 */
public class ResStorageStaffAtomSVImpl implements IResStorageStaffAtomSV {

  @Override
  public void add(ResStorageStaffBean request) throws Exception {
    ResStorageStaffEngine.save(request);
  }

  @Override
  public void update(ResStorageStaffBean request) throws Exception {
    ResStorageStaffBean bean=ResStorageStaffEngine.getBean(request.getId());
    bean.setStsToOld();
    BeanUtil.copyPropertiesIgnoreNull(bean,request);
    ResStorageStaffEngine.save(bean);
  }


  @Override
  public ResStorageStaffBean queryById(ResStorageStaffBean request) throws Exception {
    return ResStorageStaffEngine.getBean(request.getId());
  }

  @Override
  public ResStorageStaffBean[] query(ResStorageStaffBean request,Map<String,Object> reqmap) throws Exception {
    Criteria criteria=this.getCriteria(request,reqmap);
    return ResStorageStaffEngine.getBeans(criteria);
  }

  @Override
  public ResStorageStaffBean[] queryPage(ResStorageStaffBean request,Map<String,Object> reqmap,int startNum,int endNum) throws Exception {
    Criteria criteria=this.getCriteria(request,reqmap);
    return ResStorageStaffEngine.getBeans(criteria,startNum,endNum,true);
  }

  @Override
  public long count(ResStorageStaffBean request,Map<String,Object> reqmap) throws Exception {
    Criteria criteria=new Criteria();
    String condition="";
    Map parameter=new HashMap();
    return ResStorageStaffEngine.getBeansCount(condition,parameter);
  }



  private Criteria getCriteria(ResStorageStaffBean request,Map<String,Object> reqmap) {
    Criteria criteria=new Criteria();
    if(request!=null) {
      if(request.getId()!=-1) {
        criteria.addEqual(IResStorageStaffValue.S_Id,request.getId());
      }
      if(StringUtils.isNotBlank(request.getCode())) {
        criteria.addEqual(IResStorageStaffValue.S_Code,request.getCode());
      }
    }
    if(reqmap!=null) {
//      if(reqmap.containsKey("TimeStart")&&reqmap.containsKey("TimeEnd")) {
//        Timestamp valueStart=(Timestamp)reqmap.get("TimeStart");
//        Timestamp valueEnd=(Timestamp)reqmap.get("TimeEnd");
//        criteria.addGREATEREqual(IResStorageStaffValue.S_Time,valueStart);
//        criteria.addLESSEqual(IResStorageStaffValue.S_Time,valueEnd);
//      }
//      if(reqmap.containsKey("Ids")) {
//        List values=(List)reqmap.get("Ids");
//        criteria.addIn(IResStorageStaffValue.S_Id,values);
//      }
      if(reqmap.containsKey("orderByAsc")) {
        String value=(String)reqmap.get("orderByAsc");
        criteria.addAscendingOrderByColumn(value);
      }
      if(reqmap.containsKey("orderByDesc")) {
        String value=(String)reqmap.get("orderByDesc");
        criteria.addDescendingOrderByColumn(value);
      }
    }
    return criteria;
  }

}
