# coding=utf-8
__author__='wygdove'
__time__='2018/6/29 11:13'



if __name__ == '__main__':
    f=open('in.txt','r')
    lines=f.readlines()
    for line in lines:
        line=line.strip().replace('\n','')
        if line.find(";")==-1:continue
        line=line[line.rfind(' ',0,line.find(';'))+1:line.find(';')]
        print line