# coding=utf-8
__author__='wygdove'
__time__='2018/6/29 11:13'


import json

kvs={
'__author__': 'wygdove',
'@date': '@date 2018-07-25 17:05',

'__project__': 'gis',
'__package__': 'gridbase',
'__SvKey__': 'GridBase',
'__BoKey__': 'GisGridInfo',

'__datebase__': 'tj_chan_gis/tj_chan_gis@10.1.235.25:8899:cmchl',
'__table__': 'gis_grid_info',

}

nkvs={}
for kv in kvs:
    nkvs[kv]=kvs[kv]
    if kv[:2]!='__' and kv[-2:]!='__':continue
    key=kv.replace('__','')
    value=kvs[kv]
    print key,value
    nkey='__'+key[0].lower()+key[1:]+'__'
    nvalue=value[0].lower()+value[1:]
    nkvs[nkey]=nvalue
    nkey='__'+key.lower()+'__'
    nvalue=value.lower()
    nkvs[nkey]=nvalue
# print nkvs
print json.dumps(nkvs)
