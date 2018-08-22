# coding=utf-8
__author__='wygdove'
__time__='2018/5/31 16:21'


from doveutils import dmongo
import cx_Oracle
import json
import os
os.environ['NLS_LANG']='SIMPLIFIED CHINESE_CHINA.UTF8'


# connurl='tj_chan_gis/tj_chan_gis@10.1.235.25:8899/cmchl'
# dbconn=cx_Oracle.connect(connurl)
# crusor=dbconn.cursor()
#
#
# sql='''insert into gis_area_latlng_detail values('2','typekey','source','100100','DX1001','测试渠道','0022','天津市','B2','南开红桥分公司','WGB2001','测试网格','101.101,102.102','{"name":"测试","msg":"啦啦啦"}','')'''
# res=crusor.execute(sql)
# dbconn.commit()
# print res
#
# sql='select * from gis_area_latlng_detail'
# rs=crusor.execute(sql)
# print rs.fetchall()
#
# crusor.close()
# dbconn.close()





coll=dmongo.get_coll('10.1.234.150','37017','dss001','dss001user','dss001pwd','gisfs')
# res=dmongo.find_one(coll,{"tYPE":"CALCULATE-PERIPHERAL-CHANNEL"})
# res=dmongo.delete_many(coll,{"tYPE":"CALCULATE-CHANNEL"})
# print res
res=dmongo.find_many(coll,{"tYPE":"CALCULATE-CHANNEL"})
print json.loads(res).__len__()
# print res










