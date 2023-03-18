#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: jd_superBrand.py(超级品牌日12豆2)
Author: HarbourJ
Date: 2023/1/15 08:00
TG: https://t.me/HarbourToulu
cron: 1 1 1 1 1 *
new Env('超级品牌日12豆22');
ActivityEntry: APP搜索"超级品牌日222"
"""

import base64
import sys
import time
import operator
# import sys
# sys.path.append('./vpei_node/')
import os
print('workdir:' + os.getcwd())
# os.chdir('/ql/data/repo/vpei_node/')
from cls import IsValid
from cls import LocalFile
from cls import ListFile
from cls import NetFile
from cls import PingIP

workdir = os.getcwd()

# 获取传递的参数
try:
    #0表示文件名，1后面都是参数 0.py, 1, 2, 3
    url = sys.argv[1:][0]
    if(len(sys.argv[1:]) > 1):
        url = sys.argv[1:][1]
    elif(len(sys.argv[1:]) > 2):
        url = sys.argv[1:][2]
except:
    url = 'init'

confile = './clients/v2ray-core/config.json'
url = 'http://114.116.213.73:8080/ipfs/QmXhAn3EQza9oiudQHuuT2evtajmTfSSKpBG3yiSTZpeSY/'
url = 'http://122.225.207.101:8080/ipns/k2k4r8kms1l1k3wljk4o8eopnb2dltfvh8pypr0zkeyjunyagft3aqvs/'
url = 'https://ghproxy.com/https://raw.githubusercontent.com/vpei/Free-Node-Merge/main/o/node.txt#'
print('url: ' + url)

# 测试单个节点
# j = 'trojan://8cf83f44-79ff-4e50-be1a-585c82338912@t2.ssrsub.com:8443?sni=douyincdn.com#v2cross.com'
# onenode = PingIP.node_config_json(j, confile)
# kbs = PingIP.nodespeedtest()

Departs = []#待排序列表
class Department:#自定义的元素
    def __init__(self,id,name,kbs):
        self.id = id
        self.name = name
        self.kbs= kbs

localnode = LocalFile.read_LocalFile(workdir + "/out/node.txt")
localnode = base64.b64decode(localnode).decode("utf-8", "ignore")

clashnodes = NetFile.url_to_str(url + 'node.txt', 240, 120)
if(IsValid.isBase64(clashnodes) and clashnodes.find('\n') == -1):
    clashnodes = base64.b64decode(clashnodes).decode("utf-8")
ii = 0
allnode = ''
expire = ''
netnode = NetFile.url_to_str(url + 'index.html', 240, 120)

# expire = NetFile.url_to_str(url + 'expire.txt', 240, 120)
# url = 'https://ql.vmess.com/'
# expire = expire + '\n' + NetFile.url_to_str(url + 'expire.txt', 240, 120)
# expire = expire + '\n' + LocalFile.read_LocalFile('./out/expire.txt')

clashnodes = localnode.strip('\n') + '\n' + clashnodes.strip('\n') + '\n' + netnode.strip('\n')
# clashnodes = NetFile.url_to_str('http://192.168.14.5/dat.txt', 240, 120)
clashnodes = clashnodes.replace('\r', '')

for i in clashnodes.split('\n'):
    if(allnode.find(i) == -1):
        allnode = allnode + '\n' + i
allnode = allnode.replace(' ', '').replace('\n\n', '\n').strip('\n')
i = 0
onenode = ''
for j in allnode.split('\n'):
    try:
        #if(j.strip(' ') != ''):
        i += 1
        #else:
        #    continue
        print(time.strftime('%Y-%m-%d %H:%M:%S'))
        onenode = PingIP.node_config_json(j, confile)
        if(onenode.find(':') > -1):
            ###以上已生成config.json文件###
            kbs = PingIP.nodespeedtest(onenode, confile)
            print('kbs:' + str(kbs))
            if(kbs > 0):            
                #创建元素和加入列表
                Departs.append(Department(int(kbs), j , str(kbs)))
                print('Line-77-' + str(i) + '-已添加节点:' + j + '\n')
            else:
                if(expire.find(j) == -1):
                    expire = expire + '\n' + j
                print('Line-80-' + str(i) + '-已出错节点:' + j + '\n')
        else:
            print('Line-82-' + str(i) + '-已过滤节点' + '\n')
    except Exception as ex:
        print('Line-213-' + str(i) + '-Exception:' + str(ex) + '\nonenode:' + onenode + '\nj:' + j + '\n')

# if(os.path.exists(confile)):
# os.remove(confile)

#划重点#划重点#划重点----排序操作
cmpfun = operator.attrgetter('id','name')#参数为排序依据的属性，可以有多个，这里优先id，使用时按需求改换参数即可
Departs.sort(key = cmpfun, reverse=True)#使用时改变列表名即可
#划重点#划重点#划重点----排序操作
 
#此时Departs已经变成排好序的状态了，排序按照id优先，其次是name，遍历输出查看结果
newallnode = ''
for depart in Departs:
    newallnode = newallnode + '\n' + depart.name
    print(str(depart.id) + '-' + depart.name + '-' + depart.kbs)
# Base64加密后保存
newallnode = base64.b64encode(newallnode.strip('\n').encode("utf-8")).decode("utf-8")
# 保留处理后的结果
if(len(newallnode) > 1024):
    # LocalFile.write_LocalFile(workdir + '/out/node.txt', newallnode) 
    LocalFile.write_LocalFile('/ql/static/dist/node.txt', newallnode) 
    print('node.txt-is-ok')
else:
    print('node.txt-is-err-filesize:' + str(len(newallnode)))

# LocalFile.write_LocalFile(workdir + '/out/expire.txt', expire.strip('\n'))
LocalFile.write_LocalFile('/ql/static/dist/expire.txt', expire.strip('\n'))

print(time.strftime('%Y-%m-%d %H:%M:%S'))