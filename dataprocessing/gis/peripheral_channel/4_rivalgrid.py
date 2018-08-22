# coding=utf-8
__author__='wygdove'
__time__='2018/6/13 14:56'


file=open('rivalgrid.in','r')
lines=file.readlines()
index=0
errorcnt=0
for line in lines:
    # if index>=10:break
    index+=1
    line=line.strip().replace('\n','')
    ins=line.split(',')
    # print ins
    if ins==None:continue