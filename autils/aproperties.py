# coding=utf-8
__author__='wygdove'
__time__='2017/12/13 19:45'


class aproperties(object):
    def __init__(self,filename):
        self.filename=filename
        self.properties={}

    def get_properties(self):
        try:
            profile=open(self.filename,'r')
            lines=profile.readlines()
            for line in lines:
                line=line.strip().replace('\n','')
        except Exception, e:
            raise e
        else:
            profile.close()
        return self.properties




    # def __getDict(self,strName,dictName,value):
    #
    #     if(strName.find('.')>0):
    #         k = strName.split('.')[0]
    #         dictName.setdefault(k,{})
    #         return self.__getDict(strName[len(k)+1:],dictName[k],value)
    #     else:
    #         dictName[strName] = value
    #         return
    # def getProperties(self):
    #     try:
    #         pro_file = open(self.fileName, 'Ur')
    #         for line in pro_file.readlines():
    #             line = line.strip().replace('\n', '')
    #             if line.find("#")!=-1:
    #                 line=line[0:line.find('#')]
    #             if line.find('=') > 0:
    #                 strs = line.split('=')
    #                 strs[1]= line[len(strs[0])+1:]
    #                 self.__getDict(strs[0].strip(),self.properties,strs[1].strip())
    #     except Exception, e:
    #         raise e
    #     else:
    #         pro_file.close()
    #     return self.properties