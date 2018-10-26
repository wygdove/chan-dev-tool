# coding=utf-8
__author__='wygdove'
__time__='2018/10/16 18:32'



from doveutils import dmongo
from bson.objectid import ObjectId

coll=dmongo.get_coll('10.19.10.79','38017','dss001','dss001user','dss001pwd','gisfs')


type="GIS-BUSICIRCLE"
query={"tYPE":type}

# res=dmongo.find_one(coll,{"tYPE":type})
# res=dmongo.find_many(coll,{"tYPE":type})
# print res
# res=dmongo.delete_many(coll,query)
# if res!=None:print json.loads(res).__len__()

res=dmongo.find_many(coll,query)
print res


# id="5bc5c3e31bc137e93e2fe524"
# print coll.delete_one({"_id":ObjectId(id)})
# res=dmongo.find_withid(coll,id)
# print res
