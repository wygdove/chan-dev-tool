# coding=utf-8
__author__='wygdove'
__time__='2019/7/10 10:20'


import os
import sys
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
os.environ['NLS_LANG']='SIMPLIFIED CHINESE_CHINA.UTF8'
reload(sys)
sys.setdefaultencoding("utf-8")


mongoConf={"mongoServer":"10.1.234.150:37017","database":"dss001","userName":"dss001user","password":"dss001pwd","bucket":"gisfs" }
pointType="basestation"
answer={"busidata":{},"ingrid":{}}




print 'connect to mongodb ......'
conn=pymongo.MongoClient('mongodb://'+mongoConf["mongoServer"])
db=conn.get_database(mongoConf["database"])
db.authenticate(mongoConf["userName"],mongoConf["password"])
coll=db.get_collection(mongoConf["bucket"])
print 'success\n'


mongotype="GIS-CALCULATE-"+pointType.upper()

# data=coll.find({"tYPE":mongotype})
# data=json.loads(dumps(data))
# print json.dumps(data)
print 'clear mongo latlng data type: '+mongotype
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
    if not answer["busidata"].has_key(busiid): answer["busidata"][busiid]={}
    answer["busidata"][busiid]=ins
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
fo.write("id,lng,lat,gridcode,gridname\n")
print 'success\n\n'



print 'calculating ......'

data=coll.find({"tYPE":"GIS-GRID"})
gridList=json.loads(dumps(data))
# print json.dumps(gridList)
index=0
errorcnt=0
for grid in gridList:
    # if index>=1:break
    index+=1
    if grid==None:break
    # print json.dumps(grid)
    coordinates=grid["geom"]["coordinates"]
    # print coordinates
    query={"geom":{"$geoWithin":{"$geometry":{"type":"Polygon","coordinates":coordinates}}},"tYPE":mongotype}
    try:
        data=coll.find(query)
        data=json.loads(dumps(data))
        arealatlngs=json.dumps(data)
        # print arealatlngs
    except:
        print json.dumps(grid)
        continue
    arealatlngs=json.loads(arealatlngs)
    print arealatlngs.__len__()
    for data in arealatlngs:
        v_id=data["bUSIID"]
        if not answer["ingrid"].has_key(v_id): answer["ingrid"][v_id]={}
        answer["ingrid"][v_id]=grid
        busidata=answer["busidata"][v_id]
        fo.write(busidata[0]+","+busidata[1]+","+busidata[2]+",")
        fo.write(grid["rEGGRIDCODE"])
        fo.write(",")
        fo.write(grid["nAME"])
        fo.write("\n")
fo.flush()
fo.close()
print 'finshed\n\n\n'
# print json.dumps(answer)



print 'all complete'
# raw_input('press enter to close ......')



