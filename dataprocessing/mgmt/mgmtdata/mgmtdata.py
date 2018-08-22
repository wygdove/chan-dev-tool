# coding=utf-8
__author__='wygdove'
__time__='2017/12/13 16:58'

import elasticsearch
import pymongo
import json
from bson.json_util import dumps


def search_woinfo(woId):
    es=elasticsearch.Elasticsearch('http://10.19.10.85:39200/')
    res=es.search(index='flow-task-index',q='busiresult.woId:'+woId)
    return res

def search_wodata(woId):
    uri='mongodb://10.19.10.85:37017'
    conn=pymongo.MongoClient(uri)
    dsswofs=conn.dsswo.dsswofs
    res=dsswofs.find_one({"woId":woId})
    res=json.loads(dumps(res))
    return res


if __name__ == '__main__':
    # woId=raw_input("woId: ")
    woId='47906'
    woinfo=search_woinfo(woId)
    wodata=search_wodata(woId)
    ans={'woinfo':woinfo,'wodata':wodata}
    print json.dumps(ans)
    # print json.dumps(ans,indent=4,sort_keys=False,ensure_ascii=False)
