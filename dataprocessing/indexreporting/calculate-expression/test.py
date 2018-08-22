# coding=utf-8
__author__='wygdove'
__time__='2018/8/2 18:51'



kpi={}
expressions={}

f=open('in2.in','r')
lines=f.readlines()
for line in lines:
    line=line.strip().replace('\n','')
    line=line.split('	')
    # print line
    if line.__len__()>=2:
        kpiname=line[0]
        kpicode=line[1]
        kpi[kpiname]=kpicode
        if line.__len__()==3:
            expression=line[2]
            expressions[kpiname]=expression

# for kpiname in kpi.keys(): print kpiname,kpi[kpiname]

for kpiname in expressions.keys():
    expression=expressions[kpiname]
    for kn in kpi.keys():
        expression=expression.replace(kn,kpi[kn])
    print kpiname+'	'+kpi[kpiname]+'	'+expression