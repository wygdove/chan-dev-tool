# coding=utf-8
__author__='wygdove'
__time__='2018/5/31 11:46'


from doveutils import dmongo


coll=dmongo.get_coll('10.1.234.150','37017','dss001','dss001user','dss001pwd','gisfs')


coordinates=[[[117.338301,39.176059],[117.395218,39.161289],[117.41304,39.199772],[117.338301,39.176059]]]
query={"geom":{"$geoWithin":{"$geometry":{"type":"Polygon","coordinates":coordinates}}}}
print dmongo.find_many(coll,query)


