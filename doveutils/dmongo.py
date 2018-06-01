# coding=utf-8
__author__='wygdove'
__time__='2018/5/31 10:49'


import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId


def get_coll(ip,port,database,username,userpwd,collname):
    conn=pymongo.MongoClient('mongodb://'+ip+':'+port)
    db=conn.get_database(database)
    db.authenticate(username,userpwd)
    coll=db.get_collection(collname)
    return coll

def get_fullname(coll):
    return coll.full_name

def find_one(coll,query):
    data=coll.find_one(query)
    data=json.loads(dumps(data))
    return json.dumps(data)

def find_many(coll,query):
    data=coll.find(query)
    data=json.loads(dumps(data))
    return json.dumps(data)

def find_withid(coll,id):
    data=coll.find({"_id":ObjectId(id)})
    data=json.loads(dumps(data))
    return json.dumps(data)

def insert(coll,data):
    return coll.insert(data)

def delete_many(coll,query):
    coll.delete_many(query)

