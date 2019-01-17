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


def getCriteria(type,property):
    property=property[0].upper()+property[1:len(property)]
    res=""
    if type=="String":
        res='''if(!StringUtil.isBlank(request.get'''+property+'''())){criteria.and'''+property+'''EqualTo(request.get'''+property+'''());}'''
    elif type=="Short" or type=="Integer" or type=="Long" or type=="Float" or type=="Double":
        res='''if(request.get'''+property+'''()!=null&&request.get'''+property+'''()>0){criteria.and'''+property+'''EqualTo(request.get'''+property+'''());}'''
    else :
        res='''if(request.get'''+property+'''()!=null){criteria.and'''+property+'''EqualTo(request.get'''+property+'''());}'''

    return res

def getGetterSetter(type,property):
    propertyu=property[0].upper()+property[1:len(line)]
    res=""
    res+='''public '''+type+''' get'''+propertyu+'''(){return '''+property+''';}\r\n'''
    res+='''public void set'''+propertyu+'''('''+type+''' '''+property+''') {this.'''+property+'''='''+property+''';}\r\n'''
    return res



if __name__ == '__main__':
    f=open('in.txt','r')
    lines=f.readlines()
    for line in lines:
        line=line.strip().replace('\n','')
        if line.find(";")==-1:continue
        line = line.strip().replace('	', '')
        line = line.strip().replace(';', '')
        words=line.split(" ")
        if words.__len__()!=3:continue
        type=words[1]
        property=words[2]
        # line=line[line.find('private String ')+15:line.find(';')]    # line="fieldName"
        # line=line[line.rfind(' ',0,line.find(';'))+1:line.find(';')]#     # line="fieldName"
        # line=line[0].upper()+line[1:len(line)]    # line="FieldName"
        # line=str(upperline(line))    # line="field_name"
        # line=str(lineupper(line))    # line="fieldName"

        # print line
        # print '"'+line+'",',
        # print '''<if test="request.'''+line+''' !=null and request.'''+line+''' !=''">and '''+str(upperline(line))+'''='${request.'''+line+'''}'</if>'''
        # print '''if(StringUtils.isBlank(saveRequest.get'''+line+'''())) saveRequest.set'''+line+'''("");'''


        # print words
        # print type
        # print property

        # res=getCriteria(type,property)
        res=getGetterSetter(type,property)
        print res




# raw_input()





