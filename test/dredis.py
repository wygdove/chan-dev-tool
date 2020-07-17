# coding=utf-8
__author__='wygdove'
__time__='2019/4/3 10:36'



import redis


r=redis.Redis(host='localhost', port=6379, decode_responses=True)
print(r['name'])
print(r.get('name'))
print(type(r.get('name')))





