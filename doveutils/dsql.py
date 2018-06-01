# coding=utf-8
__author__='wygdove'
__time__='2018/1/9 10:27'

import cx_Oracle

def queryOracle(connurl,sql):
    'UCR_CHAN_ASSET/UCR_CHAN_ASSET@10.19.10.80:1521/hnchl'
    dbconn=cx_Oracle.connect(connurl)
    c=dbconn.cursor()
    x=c.execute(sql)
    res=x.fetchall()
    c.close()
    dbconn.close()
    return res


def insertOracle(connurl,sql):
    'UCR_CHAN_ASSET/UCR_CHAN_ASSET@10.19.10.80:1521/hnchl'
    dbconn=cx_Oracle.connect(connurl)
    c=dbconn.cursor()
    c.execute(sql)
    c.close()
    dbconn.close()


def excuteOracle2(ip,port,username,userpwd,database,sql):
    'UCR_CHAN_ASSET/UCR_CHAN_ASSET@10.19.10.80:1521/hnchl'
    dbconn=cx_Oracle.connect(username+"/"+userpwd+"@"+ip+":"+port+"/"+database)
    c=dbconn.cursor()
    x=c.execute(sql)
    res=x.fetchall()
    c.close()
    dbconn.close()
    return res



def excuteMysql(connurl,sql):
    return None
