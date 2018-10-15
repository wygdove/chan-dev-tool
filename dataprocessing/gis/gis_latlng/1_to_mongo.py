# coding=utf-8
__author__='wygdove'
__time__='2018/6/25 14:33'


import json
from doveutils import dmongo

coll=dmongo.get_coll('10.1.234.150','37017','dss001','dss001user','dss001pwd','gisfs')


file=open('in.in','r')
lines=file.readlines()
index=0
errorcnt=0
for line in lines:
    # if index>=10:break
    index+=1
    line=line.strip().replace('\n','')
    ins=line.split(',')
    # print ins
    if ins==None:break
    try:
        vlng=float(ins[1])
        vlat=float(ins[2])
        if vlng==0.0 and vlat==0.0:
            errorcnt+=1
            print line
            continue
    except:
        errorcnt+=1
        print line
        continue
    # print vlng,vlat
    v_latlngs={"geom":{"coordinates":[vlng,vlat],"type":"Point"},"bUSIID":ins[0],"tYPE":"CALCULATE-PERIPHERAL_CHANNEL"}
    # print json.dumps(v_latlngs)
    dmongo.insert(coll,v_latlngs)
    # coll.insert(data)

print errorcnt
print '\n\n\n'



# res=dmongo.find_one(coll,{"tYPE":"CALCULATE-PERIPHERAL_CHANNEL"})
res=dmongo.find_many(coll,{"tYPE":"CALCULATE-PERIPHERAL_CHANNEL"})
# res=dmongo.delete_many(coll,{"tYPE":"CALCULATE-PERIPHERAL_CHANNEL"})
# print res
if res!=None:print json.loads(res).__len__()
print '\n\n\n'




