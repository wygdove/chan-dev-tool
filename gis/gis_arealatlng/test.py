# coding=utf-8
__author__='wygdove'
__time__='2018/6/7 18:05'



import cx_Oracle
import os
os.environ['NLS_LANG']='SIMPLIFIED CHINESE_CHINA.UTF8'


# connurl='tj_chan_gis/tj_chan_gis@10.1.235.25:8899/cmchl'
# dbconn=cx_Oracle.connect(connurl)
# crusor=dbconn.cursor()



file=open('in\\county.tsv','r')
lines=file.readlines()
index=1
for line in lines:
    # if index>=2410:break
    index+=1
    line=line.strip().replace('\n','')
    ins=line.split('	')
    if ins.__len__()!=7:
        print line
        continue
    sql="insert into gis_area_latlng(area_latlng_id,busi_area_type_key,busi_area_type_value,area_id,geo_id,del_flag) values('"+ins[0]+"','"+ins[1]+"','"+ins[2]+"','"+ins[3]+"','"+ins[5]+"','"+ins[6]+"');"
    print sql
    sql="update gis_area_latlng set busi_area_latlngs='"+ins[4]+"' where area_latlng_id='"+ins[0]+"';"
    print sql
    # res=crusor.execute(sql)
    # dbconn.commit()




# crusor.close()
# dbconn.close()