# coding=utf-8
__author__='wygdove'
__time__='2018/7/9 11:23'

import os

def getbovos():
    bovos=''
    fbo=open('bo.txt','r')
    bolines=fbo.readlines()
    for boProperty in bolines:
        boProperty=boProperty.strip().replace('\n','')
        if boProperty.find(";")==-1: continue
        boProperty=boProperty[boProperty.rfind(' ',0,boProperty.find(';'))+1:boProperty.find(';')]
        BoProperty=boProperty[0].upper()+boProperty[1:]
        bovos+='res.set'+BoProperty+'(src.get'+BoProperty+'());\n'
    fbo.close()
    return bovos


if __name__ == '__main__':
    getbovos()