# coding=utf-8
__author__='wygdove'
__time__='2018/5/31 17:24'


from doveutils import dmongo
import json
import cx_Oracle
import os
os.environ['NLS_LANG']='SIMPLIFIED CHINESE_CHINA.UTF8'


coll=dmongo.get_coll('10.1.234.150','37017','dss001','dss001user','dss001pwd','gisfs')
connurl='tj_chan_gis/tj_chan_gis@10.1.235.25:8899/cmchl'
dbconn=cx_Oracle.connect(connurl)
cursor=dbconn.cursor()


# file=open('in\\pro_grid.in','r')
file=open('in\\test_grid.in','r')
lines=file.readlines()
index=0
for line in lines:
    index+=1
    # if index>=2:break
    line=line.strip().replace('\n','')
    ins=line.split('	')
    if ins.__len__()!=8:
        print line
        continue
    latlngs=json.loads(ins[7])
    # print json.dumps(latlngs)
    coordinates=latlngs["geom"]["coordinates"]
    # query={"geom":{"$geoWithin":{"$geometry":{"type":"Polygon","coordinates":coordinates}}},"tYPE":"CALCULATE-PERIPHERAL-CHANNEL"}
    query={"geom":{"$geoWithin":{"$geometry":{"type":"Polygon","coordinates":coordinates}}},"tYPE":"CALCULATE-CHANNEL"}
    # arealatlngs=dmongo.find_many(coll,query)
    try:
        arealatlngs=dmongo.find_many(coll,query)
    except:
        print json.dumps(latlngs)
        continue
    arealatlngs=json.loads(arealatlngs)
    print arealatlngs.__len__()
    for data in arealatlngs:
        v_id=data["bUSIID"]
        data["rEGGRIDCODE"]=ins[1]
        data["rEGCOUNTYCODE"]=ins[3]
        v_gislatlngs=json.dumps(data)
        sql="update gis_area_latlng_detail set city_code='"+ins[5]+"',city_name='"+ins[6]+"',county_code='"+ins[3]+"',county_name='"+ins[4]+"',area_code='"+ins[1]+"',area_name='"+ins[2]+"',gislatlngs='"+v_gislatlngs+"' where id='"+str(v_id)+"'"
        # print sql
        # res=cursor.execute(sql)
        # dbconn.commit()


cursor.close()
dbconn.close()