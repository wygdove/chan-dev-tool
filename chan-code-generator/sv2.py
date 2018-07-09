# coding=utf-8
__author__='wygdove'
__time__='2018/5/21 10:57'

import os
import time
import json


def dosv():
    print 'lalala'
    kvs=getKvs()
    # print kvs
    svs=getSvs(kvs)
    # print svs
    for svi in svs:
        ftpn=getCurPath()+svi['template']+".template"
        if not isFile(ftpn):continue
        ft=open(ftpn,"r")
        content=ft.read()
        for key in kvs.keys(): content=content.replace(key,kvs[key])
        fo=open(getCurPath()+svi['filepath']+svi['filename'],'w')
        fo.writelines(content)
        fo.flush()
        fo.close()
        ft.close()



def getKvs():
    f=open(getCurPath()+"\\keys.txt","r")
    lines=f.readlines()
    kvs={}
    for line in lines:
        kv=line.strip().replace('\n','').split('=')
        kvs[kv[0]]=kv[1]
    kvs["@date"]="@date "+getNow()
    f.close()
    return kvs

def getSvs(kvs):
    f=open(getCurPath()+"\\svfiles.json","r")
    data=f.read()
    for key in kvs.keys(): data=data.replace(key,kvs[key])
    svs=json.loads(data)
    f.close()
    return svs



def getCurPath():
    return os.getcwd()

def isFile(pathname):
    return os.path.isfile(pathname)

def getNow():
    return time.strftime("%Y-%m-%d %H:%M",time.localtime())



if __name__ == '__main__':
    try:
        dosv()
    except:
        print 'Sorry, it went wrong......'


