package test.com.cmi.res;

import com.cmi.common.ServiceHelper;
import com.cmi.common.domain.Page;
import com.cmi.common.domain.PageResult;
import com.cmi.common.domain.Response;
import com.cmi.common.util.DateUtil;
import com.cmi.res.csf.impl.ResStorageStaffCSVImpl;
import com.cmi.res.csf.interfaces.IResStorageStaffCSV;
import com.cmi.res.domain.resstoragestaff.params.QueryResStorageStaffRequest;
import com.cmi.res.domain.resstoragestaff.params.SaveResStorageStaffRequest;
import com.cmi.res.domain.resstoragestaff.vo.ResStorageStaffDetailVo;
import com.cmi.res.domain.resstoragestaff.vo.ResStorageStaffItemVo;
import org.junit.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.List;
import java.util.Locale;

/**
 * @Title:
 * @Description:
 * @Date: 2018-11-07 09:42
 * @Author: wygdove
 */
public class ResStorageStaffCSVTest {
	private static final Logger log=LoggerFactory.getLogger(ResStorageStaffCSVTest.class);


	@Test
	public void add() throws Exception {
		SaveResStorageStaffRequest request=new SaveResStorageStaffRequest();
		IResStorageStaffCSV resStorageStaffCSV=new ResStorageStaffCSVImpl();
		Response<String> response=resStorageStaffCSV.addResStorageStaff(request);
		log.info(JSON.toJSONString(response));
	}

	@Test
	public void addBatch() throws Exception {
		SaveResStorageStaffRequest request=new SaveResStorageStaffRequest();
		Response<Long> response=ServiceHelper.call("ord_IResStorageStaffCSV_addBatchResStorageStaff_request",request);
		log.info(JSON.toJSONString(response));
	}

	@Test
	public void update() throws Exception {
		SaveResStorageStaffRequest request=new SaveResStorageStaffRequest();
		IResStorageStaffCSV resStorageStaffCSV=new ResStorageStaffCSVImpl();
		Response<String> response=resStorageStaffCSV.updateResStorageStaff(request);
		log.info(JSON.toJSONString(response));
	}

	@Test
	public void delete() throws Exception {
		SaveResStorageStaffRequest request=new SaveResStorageStaffRequest();
		Response<Long> response=ServiceHelper.call("ord_IResStorageStaffCSV_deleteResStorageStaff_request",request);
		log.info(JSON.toJSONString(response));
	}



	@Test
	public void queryDetail() throws Exception {
		QueryResStorageStaffRequest request=new QueryResStorageStaffRequest();
		request.setLocale(Locale.CHINA);
		IResStorageStaffCSV resStorageStaffCSV=new ResStorageStaffCSVImpl();
		Response<ResStorageStaffDetailVo> response=resStorageStaffCSV.queryDetailResStorageStaff(request);
		log.info(JSON.toJSONString(response));
	}

	@Test
	public void queryList() throws Exception {
		QueryResStorageStaffRequest request=new QueryResStorageStaffRequest();
		request.setLocale(Locale.CHINA);
		IResStorageStaffCSV resStorageStaffCSV=new ResStorageStaffCSVImpl();
		Response<List<ResStorageStaffItemVo>> response=resStorageStaffCSV.queryListResStorageStaff(request);
		log.info(JSON.toJSONString(response));
	}

	@Test
	public void queryPage() throws Exception {
		QueryResStorageStaffRequest request=new QueryResStorageStaffRequest();
		request.setLocale(Locale.CHINA);
		request.setPage(new Page(1,5));
		IResStorageStaffCSV resStorageStaffCSV=new ResStorageStaffCSVImpl();
		Response<PageResult<ResStorageStaffItemVo>> response=resStorageStaffCSV.queryPageResStorageStaff(request);
		log.info(JSON.toJSONString(response));
	}
	@Test
	public void count() throws Exception {
		QueryResStorageStaffRequest request=new QueryResStorageStaffRequest();
		Response<Long> response=ServiceHelper.call("ord_IResStorageStaffCSV_countResStorageStaff_request",request);
		log.info(JSON.toJSONString(response));
	}
}
