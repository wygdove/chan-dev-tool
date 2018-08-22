# coding=utf-8
__author__='wygdove'
__time__='2018/8/16 14:32'


import json
from doveutils import dmongo

coll=dmongo.get_coll('10.1.234.150','37017','dss001','dss001user','dss001pwd','qhgisfs')


# res=dmongo.find_one(coll,{"tYPE":"GIS-COUNTY"})
# res=dmongo.find_many(coll,{"tYPE":"GIS-COUNTY"})
# print res
# res=dmongo.delete_many(coll,{"tYPE":"GIS-COUNTY"})
# if res!=None:print json.loads(res).__len__()

# 海晏 C70F
query={"$and":[{"geom":{"$geoIntersects":{"$geometry":{"type":"Polygon","coordinates":[[[100.746435,36.911165],[102.002051,36.870526],[101.482327,36.235968],[100.746435,36.911165]]]}}}},{"geom":{"type":"Polygon"},"tYPE":"GIS-COUNTY"}]}
# 刚察 C70D
# query={"$and":[{"geom":{"$geoIntersects":{"$geometry":{"type":"Polygon","coordinates":[[[96.777218,37.020506],[97.779871,36.835873],[97.025582,36.420661],[96.777218,37.020506]]]}}}},{"geom":{"type":"Polygon"},"tYPE":"GIS-COUNTY"}]}
res=dmongo.find_many(coll,query)
print res
