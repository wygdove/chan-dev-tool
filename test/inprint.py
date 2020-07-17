# coding=utf-8
__author__='wygdove'
__time__='2018/5/23 11:15'

import sys


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



index=0
ans=[]

def inprint(aaa,bbb):
    f=open('in.txt','r')
    lines=f.readlines()
    for line in lines:
        line=line.strip().replace('\n','')
        # if line.find(";")==-1:continue
        # line=line[line.find('private String ')+15:line.find(';')]    # line="fieldName"
        # line=line[line.rfind(' ',0,line.find(';'))+1:line.find(';')]#     # line="fieldName"
        # line=line[0].upper()+line[1:len(line)]    # line="FieldName"
        # line=str(upperline(line))    # line="field_name"
        # line=str(lineupper(line))    # line="fieldName"

        # print '''<if test="request.'''+line+''' !=null and request.'''+line+''' !=''">and '''+str(upperline(line))+'''='${request.'''+line+'''}'</if>'''
        # print '''if(StringUtils.isBlank(saveRequest.get'''+line+'''())) saveRequest.set'''+line+'''("");'''

        # print line
        # print '"'+line+'",',
        # ls=line.split("	")
        # print ls
        # print ls[7]
        # print "DELETE FROM GN_MENU WHERE MENU_ID="+ls[0]+";"
        # print "INSERT INTO GN_MENU (MENU_ID, MENU_NAME, MENU_DESC, MENU_PID, MENU_TYPE, MENU_ORDER, MENU_TARGET, MENU_URL, MENU_PIC, RIGHT_TAG, SYSTEM_ID, ACTIVE_TIME, INACTIVE_TIME, TREE_DISPLAY, CREATE_TIME, CREATE_OPER_ID, UPDATE_TIME, UPDATE_OPER_ID, FUNC_TYPE, MENU_EN_NAME, MENU_ICON, IS_SHOW) VALUES ("+ls[0]+", '"+ls[1]+"', '"+ls[2]+"', "+ls[3]+", '"+ls[4]+"', "+ls[5]+", null, '"+ls[7]+"', null, 'ORD', '11011', TO_DATE('2019-04-16 00:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2099-12-31 00:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'N', TO_DATE('2019-04-16 00:00:00', 'YYYY-MM-DD HH24:MI:SS'), 74, TO_DATE('2019-04-16 16:14:55', 'YYYY-MM-DD HH24:MI:SS'), 74, '1', 'Financial Staff Entry', null, '0');"



        line=line.replace("__aaaaaa__",aaa)
        line=line.replace("__bbbbbb__",bbb)
        print line



if __name__ == '__main__':
    replaceStr=["__aaaaaa__","__bbbbbb__"]
    aaa=["小区","楼宇","区域"]
    bbb=["接入","覆盖用户","移动渗透","潜在客户","异网宽带用户","在网用户","意向办理用户","宽带续约","受理竣工","实装","中小微宽带用户","专线用户","外场营销","接触用户（外呼）","营销成功用户"]
    aaa=["区域"]
    # bbb=[""]
    for i in aaa:
        for j in bbb:
            inprint(i,j)


# raw_input()





