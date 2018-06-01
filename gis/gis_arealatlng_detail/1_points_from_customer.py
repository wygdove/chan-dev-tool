# coding=utf-8
__author__='wygdove'
__time__='2018/5/31 16:20'



import cx_Oracle
import os
os.environ['NLS_LANG']='SIMPLIFIED CHINESE_CHINA.UTF8'


connurl='tj_chan_gis/tj_chan_gis@10.1.235.25:8899/cmchl'
dbconn=cx_Oracle.connect(connurl)
crusor=dbconn.cursor()


file=open('in\\points_from_customer.in','r')
lines=file.readlines()
index=10
for line in lines:
    # if index>=10:break
    line=line.strip().replace('\n','')
    ins=line.split(',')
    v_latlngs=ins[1]+','+ins[2]
    v_busidata='{"phone":"'+ins[0]+'","longitude":"'+ins[1]+'","latitude":"'+ins[2]+'"}'
    sql="insert into gis_area_latlng_detail(id,typekey,source,detail_id,detail_code,detail_name,city_code,city_name,county_code,county_name,area_code,area_name,latlngs,busidata,gislatlngs) values("+str(index)+",'peripheral_channel','points_from_customer',"+ins[0]+",'','','','','','','','','"+v_latlngs+"','"+v_busidata+"','')"
    print sql
    # res=crusor.execute(sql)
    # dbconn.commit()


    index+=1

crusor.close()
dbconn.close()