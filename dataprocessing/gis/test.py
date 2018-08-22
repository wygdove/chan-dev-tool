# coding=utf-8
__author__='wygdove'
__time__='2018/6/25 14:33'


import os
import cx_Oracle

os.environ['NLS_LANG']='SIMPLIFIED CHINESE_CHINA.UTF8'

connurl='tj_chan_gis/tj_chan_gis@10.1.235.25:8899/cmchl'
dbconn=cx_Oracle.connect(connurl)
cursor=dbconn.cursor()

sql='''
select ggi.grid_code,ggi.grid_name,ggi.busi_reg_county_code,ggi.busi_reg_county_name,ggi.busi_reg_city_code,ggi.busi_reg_city_name,gal.busi_area_latlngs
from gis_grid_info ggi,gis_area_latlng gal
where ggi.area_latlng_id=gal.area_latlng_id
'''
rs=cursor.execute(sql)
index=0
errorcnt=0
while True:
    if index>=3:break
    index+=1
    grid=cursor.fetchone()
    print grid



raw_input("Press enter to close......")