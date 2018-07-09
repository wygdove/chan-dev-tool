# coding=utf-8
__author__='wygdove'
__time__='2018/6/11 15:49'

import os
import cx_Oracle
import json
from doveutils import dmongo

coll=dmongo.get_coll('10.1.234.150','37017','dss001','dss001user','dss001pwd','gisfs')



# file=open('peripheral_channel_all.in','r')
file=open('pro_rival.in','r')
lines=file.readlines()
index=0
errorcnt=0
for line in lines:
    # if index>=10:break
    index+=1
    line=line.strip().replace('\n','')
    ins=line.split('	')
    # print ins
    if ins==None:continue
    busiid=ins[0]
    vlng=ins[3]
    vlat=ins[4]
    try:
        vlng=float(vlng)
        vlat=float(vlat)
    except:
        errorcnt+=1
        print ins
        continue
    # print vlng,vlat
    v_latlngs={"geom":{"coordinates":[vlng,vlat],"type":"Point"},"bUSIID":busiid,"nAME":"","cHANNELCODE":"","rEGCOUNTYCODE":"","rEGGRIDCODE":"","tYPE":"CALCULATE-RIVAL"}
    # print json.dumps(v_latlngs)
    dmongo.insert(coll,v_latlngs)

print errorcnt



