# coding=utf-8
__author__='wygdove'
__time__='2018/6/25 14:33'


import os
import cx_Oracle
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId

os.environ['NLS_LANG']='SIMPLIFIED CHINESE_CHINA.UTF8'

ip='10.1.234.150'
port='37017'
database='dss001'
username='dss001user'
userpwd='dss001pwd'
collname='gisfs'
conn=pymongo.MongoClient('mongodb://'+ip+':'+port)
db=conn.get_database(database)
db.authenticate(username,userpwd)
coll=db.get_collection(collname)

connurl='tj_chan_gis/tj_chan_gis@10.1.235.25:8899/cmchl'
dbconn=cx_Oracle.connect(connurl)
cursor=dbconn.cursor()

answer={}

sql='''
select ggi.grid_code,ggi.grid_name,ggi.busi_reg_county_code,ggi.busi_reg_county_name,ggi.busi_reg_city_code,ggi.busi_reg_city_name,
gal.busi_area_latlngs
from gis_grid_info ggi,gis_area_latlng gal
where ggi.area_latlng_id=gal.area_latlng_id
'''
rs=cursor.execute(sql)
index=0
errorcnt=0
while True:
    if index>=1:break
    index+=1
    grid=cursor.fetchone()
    print grid
    print grid[6]
    latlngs=json.loads(str(grid[6]))
    coordinates=latlngs["geom"]["coordinates"]
    query={"geom":{"$geoWithin":{"$geometry":{"type":"Polygon","coordinates":coordinates}}},"tYPE":"CALCULATE-PERIPHERAL_CHANNEL"}
    try:
        data=coll.find(query)
        data=json.loads(dumps(data))
        arealatlngs=json.dumps(data)
    except:
        print json.dumps(latlngs)
        continue
    arealatlngs=json.loads(arealatlngs)
    # print arealatlngs.__len__()
    for data in arealatlngs:
        v_id=data["bUSIID"]
        print v_id+" ,",
        for i in xrange(0,6):
            if i!=0:print ",",
            if grid[i]==None: print '',
            else: print grid[i],
        print ''




print '\n\n\n'