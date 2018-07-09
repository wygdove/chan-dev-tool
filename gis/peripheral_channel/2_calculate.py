# coding=utf-8
__author__='wygdove'
__time__='2018/6/11 15:02'


from doveutils import dmongo
import json


coll=dmongo.get_coll('10.1.234.150','37017','dss001','dss001user','dss001pwd','gisfs')


fo=open('out.out','w')
fo.writelines('"id","lng","lat","gridcode","gridname","countycode","countyname"\n')


file=open('..\\gis_arealatlng_detail\\in\\pro_grid.in','r')
lines=file.readlines()
index=0
for line in lines:
    # if index>=5:break
    index+=1
    line=line.strip().replace('\n','')
    ins=line.split('	')
    if ins.__len__()!=8:
        print line
        continue
    latlngs=json.loads(ins[7])
    # print json.dumps(latlngs)
    coordinates=latlngs["geom"]["coordinates"]
    query={"geom":{"$geoWithin":{"$geometry":{"type":"Polygon","coordinates":coordinates}}},"tYPE":"CALCULATE-RIVAL"}
    # arealatlngs=dmongo.find_many(coll,query)
    try:
        arealatlngs=dmongo.find_many(coll,query)
    except:
        print json.dumps(latlngs)
        continue
    arealatlngs=json.loads(arealatlngs)
    # print arealatlngs.__len__()
    for data in arealatlngs:
        v_id=data["bUSIID"]
        v_latlng=data["geom"]["coordinates"]
        v_lng=str(v_latlng[0])
        v_lat=str(v_latlng[1])
        v_gridcode=ins[1]
        v_gridname=ins[2]
        v_countycode=ins[3]
        v_countyname=ins[4]
        # print v_id,v_gridcode,v_gridname
        # print '"'+v_id+'","'+v_gridcode+'","'+v_gridname+'"'
        # print '"'+v_id+'","'+v_lng+'","'+v_lat+'","'+v_gridcode+'","',
        # print v_gridname,
        # print '"'
        fo.writelines('"'+v_id+'","'+v_lng+'","'+v_lat+'","'+v_gridcode+'","')
        fo.writelines(v_gridname)
        fo.writelines('","'+v_countycode+'","')
        fo.writelines(v_countyname)
        fo.writelines('"'+'\n')
        # fo.writelines(out+'\n')


file.close()
fo.flush()
fo.close()
