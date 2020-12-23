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
        contentExpand=['__AddPropertyDefine__','__AddGetterSetter__','__AddCriteria__','__AddQueryWrapper__']
        for ce in contentExpand:
            if generateConfig["__FieldFrom__"]=='bo':
                content=content.replace(ce,getBovos(ce,generateConfig["__BoKey__"]))
            elif generateConfig["__FieldFrom__"]=='table':
                content=content.replace(ce,getTableVos(ce,generateConfig["__BoKey__"]))

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
    kvs["__basepackagepath__"]=kvs["__basepackage__"].replace('.','/')
    if kvs["__FieldFrom__"]=="table":kvs["__BoKey__"]=getBoKeyByTable(kvs["__Table__"])
    f.close()

    nkvs={}
    for kv in kvs:
        nkvs[kv]=kvs[kv]
        if kv[:2] != '__' and kv[-2:] != '__': continue
        key=kv.replace('__', '')
        value=kvs[kv]
        if key[0] >= 'A' and key[0] <= 'Z' and str(value)!="":
            nkey='__'+key[0].lower()+key[1:]+'__'
            nvalue=value[0].lower()+value[1:]
            nkvs[nkey]=nvalue
        if key != key.lower():
            nkey='__'+key.lower()+'__'
            nvalue=value.lower()
            nkvs[nkey]=nvalue
    return nkvs

def getFileConfigs(kvs):
    f=open(getCurPath()+"/cg-config.json","r")
    data=f.read()
    for key in kvs.keys(): data=data.replace(key,kvs[key])
    svs=json.loads(data)
    f.close()
    return svs


def getBovos(flag,bokey):
    res=""
    fbo=open(getCurPath()+'/bo.txt','r')
    bolines=fbo.readlines()
    for boline in bolines:
        boline=boline.strip().replace('\n', '')
        if boline.find(";")==-1: continue
        boline=boline.strip().replace('	', '')
        boline=boline.strip().replace(';', '')
        words=boline.split(" ")
        if len(words)!=3:continue
        type=words[1]
        property=words[2]
        if flag=='__AddPropertyDefine__':
            res+=getPropertyDefine(bokey,type,property)
        elif flag=='__AddGetterSetter__':
            res+=getGetterSetter(bokey,type,property)
        elif flag=='__AddCriteria__':
            res+=getCriteria(bokey,type,property)
        elif flag=='__AddQueryWrapper__':
            res+=getQueryWrapper(bokey,type,property)
        else:
            continue
    return res

def getTableVos(flag,bokey):
    res=""
    fbo=open(getCurPath()+'/table.txt','r')
    fieldlines=fbo.readlines()
    for fieldline in fieldlines:
        fieldline=fieldline.strip().replace('\n', '')
        fieldline=fieldline.strip().replace('	', '')
        fieldline=fieldline.strip().replace(',', '')
        while fieldline.count('  ')>0:fieldline=fieldline.strip().replace('  ', ' ')
        words=fieldline.split(" ")
        if len(words)<2:continue
        fieldName=words[0]
        fieldType=words[1]

        type=''
        property=lineupper(fieldName.lower())

        if fieldType.startswith('VARCHAR'):type='String'
        elif fieldType.startswith('CLOB'):type='String'
        elif fieldType.startswith('NUMBER'):type='Long'
        elif fieldType.startswith('Date'):type='Timestamp'
        else:continue

        if flag=='__AddPropertyDefine__':res+=getPropertyDefine(type,property)
        elif flag=='__AddGetterSetter__':res+=getGetterSetter(type,property)
        elif flag=='__AddCriteria__':res+=getCriteria(type,property)
        elif flag=='__AddQueryWrapper__':res+=getQueryWrapper(bokey,type,property)
        else:continue
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

def getQueryWrapper(bokey,type,property):
    propertyu=property[0].upper()+property[1:len(property)]
    res="\t\t\t"
    if type=="String":
        res+='''if(StringUtils.hasText(request.get'''+propertyu+'''())){queryWrapper.lambda().eq('''+bokey+'''::get'''+propertyu+''',request.get'''+propertyu+'''());}'''
    elif type=="Short" or type=="short" or type=="Integer" or type=="int" or type=="Long" or type=="long" or type=="Float" or type=="float" or type=="Double" or type=="double":
        res+='''if(request.get'''+propertyu+'''()!=null&&request.get'''+propertyu+'''()>0){queryWrapper.lambda().eq('''+bokey+'''::get'''+propertyu+''',request.get'''+propertyu+'''());}'''
    else :
        res+='''if(request.get'''+propertyu+'''()!=null){queryWrapper.lambda().eq('''+bokey+'''::get'''+propertyu+''',request.get'''+propertyu+'''());}'''
    res+='\r\n'
    return res

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

def upperline(value):
    res=''
    if str(value)=="":return res
    for c in value:
        if c>='A' and c<='Z':
            res+='_'+c.lower()
        else:
            res+=c
    return res

def lineupper(value):
    res=''
    if str(value)=="":return res
    bl=False
    for c in value:
        if c=='_':
            res+=''
            bl=True
        else:
            if bl:
                res+=c.upper()
                bl=False
            else:
                res+=c
    return res

def getBoKeyByTable(value):
    res=''
    if str(value)=="":return res
    value=value.lower()
    bl=False
    for c in value:
        if c=='_':
            res+=''
            bl=True
        else:
            if bl:
                res+=c.upper()
                bl=False
            else:
                res+=c
    res=res[0].upper()+res[1:]
    return res

# ------ base end ------



if __name__ == '__main__':
    doGenerate()
