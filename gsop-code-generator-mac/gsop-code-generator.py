# coding=utf-8
__author__='wygdove'
__time__='2019/01/16 10:56'

import os
import time
import json

# ------ do sv start ------
def dosv():
    kvs=getKvs()
    overwritten=kvs["__overwritten__"]
    # print kvs["__overwritten__"]
    svs=getSvs(kvs)
    # print svs
    for svi in svs:
        if "yes"!=svi['isEffect']: continue
        ftpn=getCurPath()+svi['template']+".template"
        if not isFile(ftpn):continue
        ft=open(ftpn,"r")
        content=ft.read()
        for key in kvs.keys():
            content=content.replace(key,kvs[key])
        contentExpand=['__AddPropertyDefine__','__AddGetterSetter__','__AddCriteria__']
        for ce in contentExpand:
            content=content.replace(ce,getBovos(ce))

        fopn=svi['filepath']
        # check out path, if not exists, create it
        checkOutPath(fopn)
        fopn=fopn+svi['filename']
        if overwritten!="true" and not checkOutFile(fopn):fopn=fopn+".temp"
        fo=open(fopn,'w')
        fo.writelines(content)
        fo.flush()
        fo.close()
        ft.close()


def getKvs():
    f=open(getCurPath()+"/keys.txt","r")
    lines=f.readlines()
    kvs={}
    for line in lines:
        if line.startswith("#") or line.find('=')==-1:continue
        kv=line.strip().replace('\n','').split('=')
        kvs[kv[0]]=kv[1]
    kvs["@date"]="@date "+getNow()
    kvs["@Date:"]="@Date: "+getNow()
    kvs["__basepackagepath__"]=kvs["__basepackage__"].replace('.','/')
    f.close()
    nkvs={}
    for kv in kvs:
        nkvs[kv]=kvs[kv]
        if kv[:2] != '__' and kv[-2:] != '__': continue
        key=kv.replace('__', '')
        value=kvs[kv]
        if key[0] >= 'A' and key[0] <= 'Z':
            nkey='__'+key[0].lower()+key[1:]+'__'
            nvalue=value[0].lower()+value[1:]
            nkvs[nkey]=nvalue
        if key != key.lower():
            nkey='__'+key.lower()+'__'
            nvalue=value.lower()
            nkvs[nkey]=nvalue
    return nkvs

def getSvs(kvs):
    f=open(getCurPath()+"/cg-config.json","r")
    data=f.read()
    for key in kvs.keys(): data=data.replace(key,kvs[key])
    svs=json.loads(data)
    f.close()
    return svs


def getBovos(flag):
    res=""
    fbo=open(getCurPath()+'/bo.txt','r')
    bolines=fbo.readlines()
    for boline in bolines:
        boline=boline.strip().replace('\n', '')
        if boline.find(";")==-1: continue
        boline=boline.strip().replace('	', '')
        boline=boline.strip().replace(';', '')
        words=boline.split(" ")
        if words.__len__()!=3:continue
        type=words[1]
        property=words[2]
        if flag=='__AddPropertyDefine__':
            res+=getPropertyDefine(type,property)
        elif flag=='__AddGetterSetter__':
            res+=getGetterSetter(type,property)
        elif flag=='__AddCriteria__':
            res+=getCriteria(type,property)
        else:
            continue
    return res


def getPropertyDefine(type,property):
    res="\tprivate "+type+" "+property+";\r\n"
    return res

def getGetterSetter(type,property):
    propertyu=property[0].upper()+property[1:len(property)]
    res=""
    res+='''\tpublic '''+type+''' get'''+propertyu+'''(){return '''+property+''';}\r\n'''
    res+='''\tpublic void set'''+propertyu+'''('''+type+''' '''+property+''') {this.'''+property+'''='''+property+''';}\r\n'''
    return res

def getCriteria(type,property):
    propertyu=property[0].upper()+property[1:len(property)]
    res="\t\t\t"
    if type=="String":
        res+='''if(!StringUtil.isBlank(request.get'''+propertyu+'''())){criteria.and'''+propertyu+'''EqualTo(request.get'''+propertyu+'''());}'''
    elif type=="Short" or type=="short" or type=="Integer" or type=="int" or type=="Long" or type=="long" or type=="Float" or type=="float" or type=="Double" or type=="double":
        res+='''if(request.get'''+propertyu+'''()!=null&&request.get'''+propertyu+'''()>0){criteria.and'''+propertyu+'''EqualTo(request.get'''+propertyu+'''());}'''
    else :
        res+='''if(request.get'''+propertyu+'''()!=null){criteria.and'''+propertyu+'''EqualTo(request.get'''+propertyu+'''());}'''
    res+='\r\n'
    return res

# ------ do sv end ------



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
    # try:
    #     dosv()
    # except:
    #     print 'Sorry, it went wrong......'
    dosv()

