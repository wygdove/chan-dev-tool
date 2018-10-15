package test.com.ai.channel.mgmt.chlbusicircle;

import java.util.List;

import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;

import com.ai.channel.mgmt.api.chlbusicircle.interfaces.IMgmtBusiCircleSV;
import com.ai.channel.mgmt.api.chlbusicircle.param.QueryMgmtBusiCircleRequest;
import com.ai.channel.mgmt.api.chlbusicircle.param.SaveMgmtBusiCircleRequest;
import com.ai.channel.mgmt.api.chlbusicircle.vo.MgmtBusiCircleDetailVo;
import com.ai.channel.mgmt.api.chlbusicircle.vo.MgmtBusiCircleItemVo;
import com.ai.channel.base.vo.BaseResponse;
import com.ai.channel.base.vo.PageArg;
import com.ai.channel.base.vo.PageResult;

import test.com.ai.channel.mgmt.BaseTest;

/**
 * MgmtBusiCircleSVTest.java
 *
 *
 * @date 2018-10-15 21:05
 * @author wygdove
 */
public class MgmtBusiCircleSVTest extends BaseTest {

	@Autowired
	IMgmtBusiCircleSV mgmtBusiCircleSV;

	@Test
	public void add() {
		SaveMgmtBusiCircleRequest request=new SaveMgmtBusiCircleRequest();
		BaseResponse<String> response=mgmtBusiCircleSV.addMgmtBusiCircle(request);
		print(response);
	}

	@Test
	public void update() {
		SaveMgmtBusiCircleRequest request=new SaveMgmtBusiCircleRequest();
		BaseResponse<String> response=mgmtBusiCircleSV.updateMgmtBusiCircle(request);
		print(response);
	}

	@Test
	public void delete() {
		SaveMgmtBusiCircleRequest request=new SaveMgmtBusiCircleRequest();
		BaseResponse<String> response=mgmtBusiCircleSV.deleteMgmtBusiCircle(request);
		print(response);
	}



	@Test
	public void queryDetail() {
		QueryMgmtBusiCircleRequest request=new QueryMgmtBusiCircleRequest();
		BaseResponse<MgmtBusiCircleDetailVo> response=mgmtBusiCircleSV.queryDetailMgmtBusiCircle(request);
		print(response);
	}

	@Test
	public void queryList() {
		QueryMgmtBusiCircleRequest request=new QueryMgmtBusiCircleRequest();
		BaseResponse<List<MgmtBusiCircleItemVo>> response=mgmtBusiCircleSV.queryListMgmtBusiCircle(request);
		print(response);
	}

	@Test
	public void queryPage() {
		QueryMgmtBusiCircleRequest request=new QueryMgmtBusiCircleRequest();
		request.setPage(new PageArg(1,10));
		BaseResponse<PageResult<MgmtBusiCircleItemVo>> response=mgmtBusiCircleSV.queryPageMgmtBusiCircle(request);
		print(response);
	}


}