# coding=utf-8
__author__='wygdove'
__time__='2018/4/26 10:56'

import os
import time
import json
import cx_Oracle


# ------ do sv start ------
def dosv():
    kvs=getKvs()
    # print kvs
    svs=getSvs(kvs)
    # print svs
    bovos=getBovos(kvs)
    # print bovos
    for svi in svs:
        ftpn=getCurPath()+svi['template']+".template"
        if not isFile(ftpn):continue
        ft=open(ftpn,"r")
        content=ft.read()
        for key in kvs.keys(): content=content.replace(key,kvs[key])
        content=content.replace('__SetBovos__',bovos[0])
        content=content.replace('__SetBoatoms__',bovos[1])
        content=content.replace('__SetVosvs__',bovos[2])
        fopn=getCurPath()+svi['filepath']+svi['filename']
        fo=open(fopn,'w')
        fo.writelines(content)
        fo.flush()
        fo.close()
        ft.close()


def getKvs():
    f=open(getCurPath()+"\\keys.txt","r")
    lines=f.readlines()
    kvs={}
    for line in lines:
        if line.find('=')==-1:continue
        kv=line.strip().replace('\n','').split('=')
        kvs[kv[0]]=kv[1]
    kvs["@date"]="@date "+getNow()
    f.close()
    nkvs={}
    for kv in kvs:
        nkvs[kv]=kvs[kv]
        if kv[:2]!='__' and kv[-2:]!='__': continue
        key=kv.replace('__','')
        value=kvs[kv]
        if key[0]>='A' and key[0]<='Z':
            nkey='__'+key[0].lower()+key[1:]+'__'
            nvalue=value[0].lower()+value[1:]
            nkvs[nkey]=nvalue
        if key!=key.lower():
            nkey='__'+key.lower()+'__'
            nvalue=value.lower()
            nkvs[nkey]=nvalue
    return nkvs

def getSvs(kvs):
    f=open(getCurPath()+"\\svfiles.json","r")
    data=f.read()
    for key in kvs.keys(): data=data.replace(key,kvs[key])
    svs=json.loads(data)
    f.close()
    return svs


def getBovos(kvs):
    connurl=kvs["__datebase__"]
    dbconn=cx_Oracle.connect(connurl)
    cur=dbconn.cursor()
    x=cur.execute("select * from "+kvs["__table__"])
    tablefields=cur.description
    bolines=[]
    for field in tablefields:
        boProperty=lineupper(str(field[0]).lower())
        bolines.append(boProperty)
    # print bolines
    cur.close()
    dbconn.close()

    bovos={}
    setBovos=''
    setBoatoms=''
    setVosvs=''
    i=0
    for boProperty in bolines:
        i+=1
        if i!=1:
            setBovos+='\n\t\t'
            setBoatoms+='\n\t\t\t'
        BoProperty=boProperty[0].upper()+boProperty[1:]
        setBovos+='res.set'+BoProperty+'(src.get'+BoProperty+'());'
        setBoatoms+='if(StringUtils.isNotBlank(request.get'+BoProperty+'())) {criteria.and'+BoProperty+'EqualTo(request.get'+BoProperty+'());}'
        setVosvs+='\tprivate String '+boProperty+';\n'
    setVosvs+='\n\n\n'
    for boProperty in bolines:
        boProperty=boProperty.strip().replace('\n','')
        if boProperty.find(";")==-1: continue
        boProperty=boProperty[boProperty.rfind(' ',0,boProperty.find(';'))+1:boProperty.find(';')]
        BoProperty=boProperty[0].upper()+boProperty[1:]
        setVosvs+='\tpublic String get'+BoProperty+'() {\n\t\treturn '+boProperty+';\n\t}\n\tpublic void set'+BoProperty+'(String '+boProperty+') {\n\t\tthis.'+boProperty+'='+boProperty+';\n\t}\n'
    bovos[0]=setBovos
    bovos[1]=setBoatoms
    bovos[2]=setVosvs
    return bovos

# ------ do sv end ------



# ------ base start ------
def getCurPath():
    return os.getcwd()

def isFile(pathname):
    return os.path.isfile(pathname)

def getNow():
    return time.strftime("%Y-%m-%d %H:%M",time.localtime())

def lineupper(str):
    res=''
    bl=False
    for c in str:
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

def upperline(str):
    res=''
    for c in str:
        if c>='A' and c<='Z':
            res+='_'+c.lower()
        else:
            res+=c
    return res

# ------ base end ------



if __name__ == '__main__':
    try:
        dosv()
    except:
        print 'Sorry, it went wrong......'


