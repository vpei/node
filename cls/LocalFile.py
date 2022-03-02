#!/usr/bin/env python3

import requests
import os
import time

class LocalFile(): # 将订阅链接中YAML，Base64等内容转换为 Url 链接内容

    # 从本地文本文件中读取字符串
    def read_LocalFile(fname):
        retxt = ""
        try:
            #with open(fname, "r", encoding='unicode_escape') as f:  # 打开文件
            with open(fname, "r", encoding='unicode_escape') as f:  # 打开文件
                retxt = f.read()  # 读取文件
        except Exception as ex:
            print("Line-15-LocalFile: open local file error. \n" + + str(ex))
        return retxt

    # 写入字符串到本地文件
    def write_LocalFile(fname, fcont):
        try:
            res = fcont.encode("utf-8")
            #os.makedirs(os.path.split(fname)[0])    #创建目录
            if(fname.find('/') > -1):
                dirs = fname.rsplit('/', 1)[0]
                if not os.path.exists(dirs):
                    os.makedirs(dirs)
            #”w"代表着每次运行都覆盖内容 #只需要将之前的”w"改为“a"即可，代表追加内容
            #_file = open(fname, 'w', encoding='utf-8')
            if(fname.find('.log') == -1):
                _file = open(fname, 'w', encoding='utf-8')  #一般文件覆盖
            else:
                _file = open(fname, 'a', encoding='utf-8')  #日志文件追加
            _file.write(res.decode("utf-8"))
            _file.close()
        except Exception as ex:
            print("Line-26-LocalFile: write local file error. \n" + str(ex))
