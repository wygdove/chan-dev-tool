package test.com.ai.channel.mgmt;

import org.junit.runner.RunWith;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import com.alibaba.fastjson.JSON;

/**
 * BaseTest.java
 * 
 * 
 * @date 2018-03-16 15:13
 * @author wygdove
 */
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration({"/context/core-context.xml"})
public class BaseTest {

	public static void print(Object o) {
		System.out.println(JSON.toJSONString(o));
		
	}
}

