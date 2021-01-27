# coding=utf-8
__author__='wygdove'
__time__='2019/01/16 10:56'

import os
import time
import json

# ------ do generate start ------
def doGenerate():
    generateConfig=getGenerateConfigs()
    fileConfigs=getFileConfigs(generateConfig)
    for fileConfig in fileConfigs:
        if "yes"!=fileConfig['isEffect']: continue
        ftpn=getCurPath()+fileConfig['template']+".template"
        if not isFile(ftpn):continue
        ft=open(ftpn,"r")
        content=ft.read()
        for key in generateConfig.keys():
            content=content.replace(key,generateConfig[key])
        # print content
        # continue

        fopn=fileConfig['filepath']
        # check out path, if not exists, create it
        checkOutPath(fopn)
        fopn=fopn+fileConfig['filename']
        if generateConfig["__overwritten__"]!="true" and not checkOutFile(fopn):fopn=fopn+".temp"
        fo=open(fopn,'w')
        fo.writelines(content)
        fo.flush()
        fo.close()
        ft.close()


def getGenerateConfigs():
    f=open(getCurPath()+"/keys.txt","r")
    lines=f.readlines()
    kvs={}
    for line in lines:
        if line.startswith("#") or line.find('=')==-1:continue
        kv=line.strip().replace('\n','').split('=')
        kvs[kv[0]]=kv[1]
    kvs["@date"]="@date "+getNow()
    kvs["@Date:"]="@Date: "+getNow()
    if kvs.get("__basepackage__")==None or kvs.get("__basepackage__")=='':
        kvs["__basepackage__"]="com."+kvs["__author__"]+"."+kvs["__project__"]
    kvs["__basepackagepath__"]=kvs["__basepackage__"].replace('.','/')
    f.close()
    return kvs

def getFileConfigs(kvs):
    f=open(getCurPath()+"/pg-config.json","r")
    data=f.read()
    for key in kvs.keys(): data=data.replace(key,kvs[key])
    svs=json.loads(data)
    f.close()
    return svs


# ------ do generate end ------



# ------ base start ------

def getCurPath():
    return os.getcwd()

def isFile(pathname):
    return os.path.isfile(pathname)

def checkOutPath(fop):
    if not os.path.exists(fop) or not os.path.isdir(fop):
        os.makedirs(fop)

def checkOutFile(fopn):
    # not exist, can be created
    if not os.path.exists(fopn):
        return True
    # not a file, can be created
    elif not os.path.exists(fopn):
        return True
    else:
        return False

def getNow():
    return time.strftime("%Y-%m-%d %H:%M",time.localtime())



# ------ base end ------



if __name__ == '__main__':
    doGenerate()
