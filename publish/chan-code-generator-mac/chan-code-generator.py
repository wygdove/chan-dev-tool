# coding=utf-8
__author__='wygdove'
__time__='2018/4/26 10:56'

import os
import time
import json

# ------ do sv start ------
def dosv():
    kvs=getKvs()
    # print kvs
    svs=getSvs(kvs)
    # print svs
    bovos=getBovos()
    # print bovos
    for svi in svs:
        ftpn=getCurPath()+svi['template']+".template"
        if not isFile(ftpn):continue
        ft=open(ftpn,"r")
        content=ft.read()
        for key in kvs.keys(): content=content.replace(key,kvs[key])
        content=content.replace('__SetBovos__',bovos[0])
        content=content.replace('__SetVobos__',bovos[1])
        content=content.replace('__SetBoatoms__',bovos[2])
        content=content.replace('__SetVosvs__',bovos[3])
        fopn=getCurPath()+svi['filepath']+svi['filename']
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
        if line.find('=')==-1:continue
        kv=line.strip().replace('\n','').split('=')
        kvs[kv[0]]=kv[1]
    kvs["@date"]="@date "+getNow()
    f.close()
    nkvs = {}
    for kv in kvs:
        nkvs[kv] = kvs[kv]
        if kv[:2] != '__' and kv[-2:] != '__': continue
        key = kv.replace('__', '')
        value = kvs[kv]
        if key[0] >= 'A' and key[0] <= 'Z':
            nkey = '__' + key[0].lower() + key[1:] + '__'
            nvalue = value[0].lower() + value[1:]
            nkvs[nkey] = nvalue
        if key != key.lower():
            nkey = '__' + key.lower() + '__'
            nvalue = value.lower()
            nkvs[nkey] = nvalue
    return nkvs

def getSvs(kvs):
    f=open(getCurPath()+"/svfiles.json","r")
    data=f.read()
    for key in kvs.keys(): data=data.replace(key,kvs[key])
    svs=json.loads(data)
    f.close()
    return svs


def getBovos():
    bovos={}
    setBovos=''
    setVobos=''
    setBoatoms=''
    setVosvs=''
    setVosvs2=''
    i=0
    fbo=open(getCurPath()+'/bo.txt','r')
    bolines=fbo.readlines()
    for boProperty in bolines:
        boProperty = boProperty.strip().replace('\n', '')
        if boProperty.find(";") == -1: continue
        boProperty = boProperty[boProperty.rfind(' ', 0, boProperty.find(';')) + 1:boProperty.find(';')]
        BoProperty = boProperty[0].upper() + boProperty[1:]

        i+=1
        if i!=1:
            setBovos+='\n\t\t'
            setVobos+='\n\t\t'
            setBoatoms+='\n\t\t\t'
        setBovos+='res.set'+BoProperty+'(VoConvertUtil.getValue(src.get'+BoProperty+'()));'
        setVobos+='res.set'+BoProperty+'(src.get'+BoProperty+'());'
        setBoatoms+='if(StringUtils.isNotBlank(request.get'+BoProperty+'())) {criteria.and'+BoProperty+'EqualTo(request.get'+BoProperty+'());}'
        setVosvs+='\tprivate String '+boProperty+';\n'
        setVosvs2+='\tpublic String get'+BoProperty+'() {\n\t\treturn '+boProperty+';\n\t}\n\tpublic void set'+BoProperty+'(String '+boProperty+') {\n\t\tthis.'+boProperty+'='+boProperty+';\n\t}\n'
    bovos[0]=setBovos
    bovos[1]=setVobos
    bovos[2]=setBoatoms
    bovos[3]=setVosvs+'\n\n'+setVosvs2
    return bovos

# ------ do sv end ------



# ------ base start ------
def getCurPath():
    return os.getcwd()

def isFile(pathname):
    return os.path.isfile(pathname)

def getNow():
    return time.strftime("%Y-%m-%d %H:%M",time.localtime())
# ------ base end ------



if __name__ == '__main__':
    # try:
    #     dosv()
    # except:
    #     print 'Sorry, it went wrong......'
    dosv()

