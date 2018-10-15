# coding=utf-8
__author__='wygdove'
__time__='2018/6/1 16:42'


from doveutils import dmongo
import json

'''
CALCULATE-PERIPHERAL-CHANNEL
CALCULATE-CHANNEL
CALCULATE-RIVAL
'''
coll=dmongo.get_coll('10.1.234.150','37017','dss001','dss001user','dss001pwd','gisfs')
# res=dmongo.find_one(coll,{"tYPE":"CALCULATE-PERIPHERAL-CHANNEL"})
# res=dmongo.delete_many(coll,{"tYPE":"CALCULATE-RIVAL"})
# print res
res=dmongo.find_many(coll,{"tYPE":"CALCULATE-RIVAL"})
print json.loads(res).__len__()
# print res
