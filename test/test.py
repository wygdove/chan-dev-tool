# coding=utf-8
__author__='wygdove'
__time__='2018/5/23 11:15'


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
        # print ls[0],ls[1],ls[2]
        if int(ls[2]) < 32:
            print '''alter table ''' + ls[0] + ''' modify ''' + ls[1] + ''' VARCHAR2(32);'''
            print ''
            print ''



# raw_input()





