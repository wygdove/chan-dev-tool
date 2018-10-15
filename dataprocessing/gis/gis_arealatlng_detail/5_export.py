# coding=utf-8
__author__='wygdove'
__time__='2018/5/31 17:24'


'''
select detail_id as 手机号,latlngs as 经纬度,city_code as 地市编码,city_name as 地市名称,county_code as 分公司编码,county_name as 分公司名称,area_code as 网格编码,area_name as 网格名称
from gis_area_latlng_detail t
where typekey='peripheral_channel' 
;


select detail_id as 渠道ID,detail_code as 渠道编码,detail_name as 渠道名称,latlngs as 经纬度,city_code as 地市编码,city_name as 地市名称,county_code as 分公司编码,county_name as 分公司名称,area_code as 网格编码,area_name as 网格名称
from gis_area_latlng_detail t
where typekey='channel' 
;
'''