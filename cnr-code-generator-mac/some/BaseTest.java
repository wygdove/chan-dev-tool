package com.ai.cnr.mgmt.test;

import com.alibaba.fastjson.JSON;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;


/**
 * BaseTest.java
 * 
 * 
 * @date 2018-03-16 15:13
 * @author wygdove
 */
@RunWith(SpringRunner.class)
@SpringBootTest
public class BaseTest {

	public static void print(Object o) {
		System.out.println(JSON.toJSONString(o));
		
	}
}

