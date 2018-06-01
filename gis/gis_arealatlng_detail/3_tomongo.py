# coding=utf-8
__author__='wygdove'
__time__='2018/5/31 17:24'


import os
import cx_Oracle
import json
from doveutils import dmongo

os.environ['NLS_LANG']='SIMPLIFIED CHINESE_CHINA.UTF8'
coll=dmongo.get_coll('10.1.234.150','37017','dss001','dss001user','dss001pwd','gisfs')


connurl='tj_chan_gis/tj_chan_gis@10.1.235.25:8899/cmchl'
dbconn=cx_Oracle.connect(connurl)
cursor=dbconn.cursor()

sql="select id,typekey,source,detail_id,detail_code,detail_name,city_code,city_name,county_code,county_name,area_code,area_name,latlngs,busidata,gislatlngs from gis_area_latlng_detail where typekey='channel' order by to_number(id)"
rs=cursor.execute(sql)
index=0
errorcnt=0
while True:
    index+=1
    # if index>=3:break
    data=cursor.fetchone()
    print data
    if data==None:break
    # print data[12]
    latlng=str(data[12])
    vlng=latlng[:latlng.find(",")]
    vlat=latlng[latlng.find(",")+1:]
    try:
        vlng=float(vlng)
        vlat=float(vlat)
        if vlng==0.0 and vlat==0.0:
            errorcnt+=1
            continue
    except:
        errorcnt+=1
        # print '------ error data start ------'
        # print data
        # print data[12]
        # print '------ error data end ------'
        continue
    # print vlng,vlat
    v_latlngs={"geom":{"coordinates":[vlng,vlat],"type":"Point"},"nAME":data[5],"cHANNELCODE":data[4],"rEGCOUNTYCODE":"","rEGGRIDCODE":"","tYPE":"CALCULATE-CHANNEL"}
    print json.dumps(v_latlngs)
    dmongo.insert(coll,v_latlngs)

print errorcnt

# print dmongo.find_one(coll,{"tYPE":"GIS-BASESTATION"})

cursor.close()
dbconn.close()


