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



if __name__ == '__main__':
    f=open('in.in.txt','r')
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
        ls=line.split("	")
        print ls[7]
        print "DELETE FROM GN_MENU WHERE MENU_ID="+ls[0]+";"
        print "INSERT INTO GN_MENU (MENU_ID, MENU_NAME, MENU_DESC, MENU_PID, MENU_TYPE, MENU_ORDER, MENU_TARGET, MENU_URL, MENU_PIC, RIGHT_TAG, SYSTEM_ID, ACTIVE_TIME, INACTIVE_TIME, TREE_DISPLAY, CREATE_TIME, CREATE_OPER_ID, UPDATE_TIME, UPDATE_OPER_ID, FUNC_TYPE, MENU_EN_NAME, MENU_ICON, IS_SHOW) VALUES ("+ls[0]+", '"+ls[1]+"', '"+ls[2]+"', "+ls[3]+", '"+ls[4]+"', "+ls[5]+", null, '"+ls[7]+"', null, 'ORD', '11011', TO_DATE('2019-04-16 00:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2099-12-31 00:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'N', TO_DATE('2019-04-16 00:00:00', 'YYYY-MM-DD HH24:MI:SS'), 74, TO_DATE('2019-04-16 16:14:55', 'YYYY-MM-DD HH24:MI:SS'), 74, '1', 'Financial Staff Entry', null, '0');"



# raw_input()





