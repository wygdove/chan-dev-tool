# coding=utf-8
__author__='wygdove'
__time__='2018/7/30 10:05'


import os

def getCurPath():
    return os.getcwd()

def dosvMulti():
    f=open(getCurPath()+"\\keys-multi.txt","r")
    lines=f.readlines()
    kvs={}
    maxcnt=0
    for line in lines:
        if line.find('=')==-1:continue
        kv=line.strip().replace('\n','').split('=')
        value=kv[1].split(',')
        kvs[kv[0]]=value
        if maxcnt<value.__len__():maxcnt=value.__len__()
    f.close()
    # print kvs
    mkvs=[]
    for i in xrange(maxcnt):
        print i
        for key in kvs:
            value=kvs[key][i] if i<kvs[key].__len__() else kvs[key][-1]
            print key+"="+value







if __name__ == '__main__':
    dosvMulti()
