# coding=utf-8
__author__='wygdove'
__time__='2018/6/11 18:01'



filecg=open('chnlgrid.in','r')
linescg=filecg.readlines()

filepc=open('peripheral_channel_all.in','r')
linespc=filepc.readlines()
index=0
errorcnt=0
for linepc in linespc:
    linepc=linepc.strip().replace('\n','')
    inspc=linepc.split(',')
    # print inspc
    gc=''
    gn=''
    cc=''
    cn=''
    county={}
    for linecg in linescg:
        linecg=linecg.strip().replace('\n','')
        inscg=linecg.split(',')
        if inspc[0]==inscg[0]:
            gc+=inscg[3]+','
            gn+=inscg[4]+','
            county[inscg[5]]=inscg[6]
    for key in county.keys():
        cc+=key+','
        cn+=county[key]+','
    gc=gc[:len(gc)-1]
    gn=gn[:len(gn)-1]
    cc=cc[:len(cc)-1]
    cn=cn[:len(cn)-1]
    print ''+inspc[0]+',"'+gc+'","',
    print gn,
    print '","'+cc+'","',
    print cn,
    print '"'
