# coding=utf-8
__author__='wygdove'
__time__='2018/6/25 15:46'


import os
import cx_Oracle
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
os.environ['NLS_LANG']='SIMPLIFIED CHINESE_CHINA.UTF8'

answer={}


print 'connect to oracle ......'
connurl='tj_chan_gis/tj_chan_gis@10.1.235.25:8899/cmchl'
dbconn=cx_Oracle.connect(connurl)
cursor=dbconn.cursor()
print 'success\n'

print 'connect to mongodb ......'
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
print 'success\n'


mongotype="CALCULATE-PERIPHERAL_CHANNEL"
print 'clear mongo latlng data,type: '+mongotype
res=coll.delete_many({"tYPE":mongotype})
print 'finshed\n'


print 'opening file in.in ......'
file=open('in.in','r')
lines=file.readlines()
print 'success\n'
index_in=0
errorcnt=0
print 'insert data to mongodb ......'
for line in lines:
    # if index>=10:break
    index_in+=1
    line=line.strip().replace('\n','')
    ins=line.split(',')
    # print ins
    if ins==None:break
    busiid=ins[0]
    try:
        vlng=float(ins[1])
        vlat=float(ins[2])
        if vlng==0.0 and vlat==0.0:
            errorcnt+=1
            # print line
            continue
    except:
        errorcnt+=1
        # print line
        continue
    # print vlng,vlat
    v_latlngs={"geom":{"coordinates":[vlng,vlat],"type":"Point"},"bUSIID":busiid,"tYPE":mongotype}
    # print json.dumps(v_latlngs)
    coll.insert(v_latlngs)
print 'finshed\n'
file.close()

mongocnt=0
data=coll.find({"tYPE":mongotype})
data=json.loads(dumps(data))
res=json.dumps(data)
# res=coll.delete_many({"tYPE":mongotype})
# print res
if res!=None:mongocnt=json.loads(res).__len__()
print 'total: '+str(index_in)
print 'success: '+str(mongocnt)
print 'fail: '+str(errorcnt)
print '\n'



print 'opening file out.csv ......'
fo=open('out.csv','w')
fo.write("id,gridcode,gridname,countycode,countyname,citycode,cityname\n")
print 'success\n\n'



print 'calculating ......'
sql='''
select ggi.grid_code,ggi.grid_name,ggi.busi_reg_county_code,ggi.busi_reg_county_name,ggi.busi_reg_city_code,ggi.busi_reg_city_name,gal.busi_area_latlngs
from gis_grid_info ggi,gis_area_latlng gal
where ggi.del_flag=0
and ggi.area_latlng_id=gal.area_latlng_id
'''
sql='''
select grid_code, grid_name, busi_reg_county_code, busi_reg_county_name, busi_reg_city_code, busi_reg_city_name, busi_area_latlngs 
from gis_grid_product_20180626
'''
rs=cursor.execute(sql)
index=0
errorcnt=0
while True:
    # if index>=1:break
    index+=1
    grid=cursor.fetchone()
    if grid==None:break
    # print grid
    print grid[0]+" "+grid[1]
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
    print arealatlngs.__len__()
    for data in arealatlngs:
        v_id=data["bUSIID"]
        if not answer.has_key(v_id): answer[v_id]=[]
        answer[v_id].append(grid)
    fo.flush()

# print json.dumps(answer)
for i in xrange(1,index_in+1):
    v_id=str(i)
    if answer.has_key(v_id):
        grids=answer[v_id]
        for grid in grids:
            fo.write(v_id+",")
            for i in xrange(0,6):
                if i!=0:fo.write(",")
                if grid[i]==None: fo.write('')
                else: fo.write(grid[i])
        fo.write("\n")
    else: fo.write(v_id+",,,,,,\n")

fo.flush()
fo.close()
print 'finshed\n\n\n'



print 'all complete'
# raw_input('press enter to close ......')
