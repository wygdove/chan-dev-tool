# coding=utf-8
__author__='wygdove'
__time__='2018/5/31 16:21'




import cx_Oracle
import os
os.environ['NLS_LANG']='SIMPLIFIED CHINESE_CHINA.UTF8'


connurl='tj_chan_gis/tj_chan_gis@10.1.235.25:8899/cmchl'
dbconn=cx_Oracle.connect(connurl)
crusor=dbconn.cursor()


# file=open('in\\chlbase.in','r')
# file=open('in\\chlbase2.in','r')
file=open('in\\chlbase3.in','r')
lines=file.readlines()
index=2400
for line in lines:
    # if index>=2410:break
    line=line.strip().replace('\n','')
    ins=line.split(',')
    if ins.__len__()!=25:
        print line
        continue
    v_latlngs=ins[18]+','+ins[19]
    v_busidata='{"ID":"'+ins[0]+'","CHANNEL_ID":"'+ins[1]+'","STATE":"'+ins[2]+'","CHANNEL_CODE":"'+ins[3]+'","CHANNEL_NAME":"'+ins[4]+'","CHL_FIRST_KIND_ID":"'+ins[5]+'","CHL_SECOND_KIND_ID":"'+ins[6]+'","CHL_THIRD_KIND_ID":"'+ins[7]+'","CHL_FORTH_KIND_ID":"'+ins[8]+'","CHL_KIND_ID":"'+ins[9]+'","CHL_KIND_NAME":"'+ins[10]+'","BUSI_REG_PROVINCE_CODE":"'+ins[11]+'","BUSI_REG_CITY_CODE":"'+ins[12]+'","BUSI_REG_COUNTY_CODE":"'+ins[13]+'","CHANNEL_MANAGER_ID":"'+ins[14]+'","CHANNEL_MANAGER_NAME":"'+ins[15]+'","CHANNEL_MANAGER_PHONE":"'+ins[16]+'","CHANNEL_ADDRESS":"'+ins[17]+'","LONGITUDE":"'+ins[18]+'","LATITUDE":"'+ins[19]+'","CHNL_CARD_NO":"'+ins[20]+'","BUSI_OPERATION_NO":"'+ins[21]+'","PHONE_OPEN_NO":"'+ins[22]+'","REL_CHANNEL_CODE":"'+ins[23]+'","REL_CHANNEL_ID":"'+ins[24]+'"}'
    sql="insert into gis_area_latlng_detail(id,typekey,source,detail_id,detail_code,detail_name,city_code,city_name,county_code,county_name,area_code,area_name,latlngs,busidata,gislatlngs) values("+str(index)+",'channel','pro_mgmtchlbase','"+ins[1]+"','"+ins[3]+"','"+ins[4]+"','','','','','','','"+v_latlngs+"','"+v_busidata+"','')"
    # print sql
    res=crusor.execute(sql)
    dbconn.commit()


    index+=1

crusor.close()
dbconn.close()