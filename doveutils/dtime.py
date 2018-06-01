# coding=utf-8
__author__='wygdove'
__time__='2018/1/9 10:23'

import time

def getnow():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())