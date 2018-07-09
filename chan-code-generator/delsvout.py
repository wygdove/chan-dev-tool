# coding=utf-8
__author__='wygdove'
__time__='2018/4/26 17:39'


import os


def delFiles(path):
    ls=os.listdir(path)
    for i in ls:
        subpath=os.path.join(path,i)
        if os.path.isdir(subpath):
            delFiles(subpath)
        elif os.path.isfile(subpath):
            os.remove(subpath)
        else:
            pass

if __name__ == '__main__':
    delFiles(os.getcwd()+'\\svout')