# coding=utf-8
__author__='wygdove'
__time__='2018/6/25 14:33'

from doveutils import dmongo
import json

coll=dmongo.get_coll('10.1.234.150','37017','dss001','dss001user','dss001pwd','gisfs')


mongocnt=0
# res=dmongo.find_one(coll,{"tYPE":"CALCULATE-PERIPHERAL_CHANNEL"})
res=dmongo.find_many(coll,{"tYPE":"CALCULATE-PERIPHERAL_CHANNEL"})
# res=dmongo.delete_many(coll,{"tYPE":"CALCULATE-PERIPHERAL_CHANNEL"})
# print res
if res!=None:mongocnt=json.loads(res).__len__()
print mongocnt
print '\n\n\n'
