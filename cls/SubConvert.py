#!/usr/bin/env python3

import base64
import json
from cls.LocalFile import LocalFile
from cls.StrText import StrText

class SubConvert():
    # clash格式vmess转换成v2ray格式
    def vmess_clash_to_v2ray(onenode):
        #print('newnode-1:\n' + onenode)
        if(onenode.find('alterId":')>-1):
            onenode = onenode.replace('name":', 'ps":')
            onenode = onenode.replace('cipher":', 'scy":')
            onenode = onenode.replace('network":', 'net":')
            onenode = onenode.replace('server":', 'add":')
            onenode = onenode.replace('alterId":', 'aid":')
            onenode = onenode.replace('uuid":', 'id":')
            onenode = onenode.replace('ws-path":', 'path":')
            #onenode = onenode.replace('"host":', '"host":')
        # 默认net类型为tcp
        onenode = onenode.replace('"net": "none"', '"net": "none"')
        # 默认type类型为none
        onenode = onenode.replace('"type": "null"', '"type": "none"')
        onenode = onenode.replace('"type": ""', '"type": "none"')

        #互相转换: 文本转换成字典
        if(onenode.find('"ps":') == -1):
            onenode = onenode.replace('\n}', ',\n  "ps": "tmp"\n}')
            print('[ps] is added.')
        if(onenode.find('"type":') == -1):
            onenode = onenode.replace('\n}', ',\n  "type": "none"\n}')
            print('[type] is added.')
        # 如果type类型为vmess，则还原为none，其他状态为tcp,kcp,QUIC,grpc等
        onenode = onenode.replace('"type": "vmess"', '"type": "none"')
        return onenode

    # 非标准格式的vmess明文地址转化为标准格式的vmess明文json
    def clash_to_josn(onenode):
        try:
            #{alterId: 2,  cipher: auto,  name: '[11-07]|oslook|_2',  network: ws,  port: 80,  server: 7.yyds123.com,  tls: false,  type: vmess,  uuid: bac18e70-9964-3f99-805a-d809c4bdc6cb,  ws-path: /ny}
            #  - {name: 🇨🇦 @SSRSUB-加拿大ss01-付费推荐:dlj.tf/ssrsub, server: ss1.ssrsub.com, port: 10443, type: ss, cipher: aes-128-gcm, password: suo.yt/ssrsub, plugin: obfs, plugin-opts: {mode: tls, host: n46hm52773.wns.windows.com}, udp: true}
            #{
            #  "v": "2",
            #  "ps": "name-1.1.1.1",
            #  "add": "1.1.1.1",
            #  "port": "443",
            #  "id": "892ebb75-7055-3007-8d16-356e65c6a49a",
            #  "aid": "32",
            #  "scy": "auto",
            #  "net": "tcp",
            #  "type": "http",
            #  "host": "domain.com",
            #  "path": "/v112EtCE3uAcU",
            #  "tls": "tls",
            #  "sni": "sni123"
            #}
            #- {name: US-107.173.157.168, server: 107.173.157.168, port: 443, type: vmess, uuid: 4f6aa0c3-7be1-4eaa-a64c-a23418070422, alterId: 6, cipher: auto, skip-cert-vertify: false, network: ws, ws-path: /b06fde1/, tls: True, ws-headers: {Host: www.shunxin.ml}}
            # onenode = '{"add":"104.255.66.87","v":"2","ps":"CA_940:001","port":38922,"id":"f3e846c1-d8e4-42df-86d4-f4e5028630d8","aid":"8","net":"tcp","type":"","host":"","path":"/:011","tls":""}'
            # onenode = '{"add": "v7.ssrsub.com", "v": "2", "ps": "\'v7.ssrsub.com\'", "port": "168", "id": "e54a480c-77e3-41ca-8f8b-17ffb50dbd08", "aid": "0", "net": "ws", "type": "", "host": "", "path": "/ssrsub", "tls": "tls"}'
            # onenode = '{name: 🇯🇵JP-35.77.5.55, server: 034.ap.pop.bigairport.net, port: 12356, type: vmess, uuid: a6f82e7d-6e99-4a4e-8981-8e91453c13f7, alterId: 1, cipher: auto, skip-cert-vertify: false, network: ws, ws-path: /, tls: True, ws-headers: {Host: t.me/vpnhat}}'
            # onenode = '{add:v1-asw-sg-14.niaoyun.online,port:666,id:b9cc1e88-5db0-37ff-840a-b882345e22d1,aid:1,scy:auto,net:ws,host:v1-asw-sg-14.niaoyun.online,path:/niaocloud,tls:,sni:,v:2,ps:Relay_新加坡-_7234,type:none,serverPort:0,nation:}'
            if(len(onenode) == 0):
                print('Line-92-onenode长度不能为0\nonenode:' + onenode)
                return ''
            else:
                print('Line-95-oldnode:' + onenode)
            #onenode = onenode.strip('- ')
            onenode = onenode.replace(' ', '')
            onenode = onenode.replace('\r', ',').replace('\n', ',')
            onenode = onenode.replace('"', '').replace('\'', '')
            if(onenode.startswith('{')):
                onenode = onenode[1:]
            if(onenode.endswith('}')):
                onenode = onenode[:-1]
            newnode = '{'
            for i in onenode.split(','):
                if(i.find(':') > -1):
                    a = i.split(':', 1)[0]
                    b = i.split(':', 1)[1]
                    if(len(a) > 0):
                        newnode = newnode + '  "' + a + '": "' + b + '",\n'
            onenode = newnode.strip(',\n') + '\n}'
            # 转换为字典格式
            #onenode = onenode.replace('{  ', '{').replace('\n}', '}').replace('": "', '":"')
            # vmess转换成v2ray格式
            #onenode = json.loads(onenode)
            #if(isinstance(onenode, dict)):
            #    print('Line-137-newnode:\n' + onenode)
            #else:
            #    print('Line-139-newnode-not-dict-newnode:' + onenode)
            #    onenode = ''
            print('Line-137-newnode:\n' + onenode)
            return onenode
        except Exception as ex:
            print('Line-167-StrText: ' + str(ex) + '\n' + onenode)
            LocalFile.write_LocalFile('./ipfs/tmp/err.log', 'Line-167-StrText: ' + str(ex) + '\n' + onenode)
            return ''

    # 非标准格式的vmess明文地址转化为标准格式的vmess明文json
    def surge_to_josn(onenode):
        try:
            # ssrsub__02 = ss, 211.99.96.10, 11316, encrypt-method=aes-256-gcm, password=gTVvCY
            if(onenode.find(',') == -1):
                return ''
            if(len(onenode) == 0):
                print('Line-104-onenode长度不能为0\nonenode:' + onenode)
                return ''
            else:
                print('Line-107-oldnode:' + onenode)
            #onenode = onenode.strip('- ')
            onenode = onenode.replace(' ', '')
            onenode = onenode.replace('encrypt-method=', 'cipher=')
            onenode = onenode.replace('username=', 'uuid=')
            newnode = '{\n'
            onenode = onenode.split('=', 1)[1]
            ii = 0
            for i in onenode.split(','):
                ii += 1
                if(ii == 1):
                    newnode = newnode + '  "type": "' + i + '",\n'
                elif(ii == 2):
                    newnode = newnode + '  "server": "' + i + '",\n'
                elif(ii == 3):
                    newnode = newnode + '  "port": "' + i + '",\n'
                else:
                    if(i.find('=') > -1):
                        a = i.split('=', 1)[0]
                        b = i.split('=', 1)[1]
                        if(len(a) > 0):
                            newnode = newnode + '  "' + a + '": "' + b + '",\n'
            if(onenode.find('uuid') > -1 and onenode.find('alterId') == -1):
                newnode = newnode + '  "alterId": "0",\n'
            onenode = newnode.strip(',\n') + '\n}'
            # 转换为字典格式
            #onenode = onenode.replace('{  ', '{').replace('\n}', '}').replace('": "', '":"')
            # vmess转换成v2ray格式
            #onenode = json.loads(onenode)
            #if(isinstance(onenode, dict)):
            #    print('Line-137-newnode:\n' + onenode)
            #else:
            #    print('Line-139-newnode-not-dict-newnode:' + onenode)
            #    onenode = ''
            print('Line-137-newnode:\n' + onenode)
            return onenode
        except Exception as ex:
            print('Line-167-StrText: ' + str(ex) + '\n' + onenode)
            LocalFile.write_LocalFile('./ipfs/tmp/err.log', 'Line-167-StrText: ' + str(ex) + '\n' + onenode)
            return ''

    # v2ray格式vmess转换成clash格式，类型替换
    def vmess_v2ray_to_clash(onenode):
        if (onenode.find('"name":') == -1):
            onenode = onenode.replace('"ps":', '"name":')
        if(onenode.find('"name":') == -1):
            onenode = onenode.replace('\n}', ',\n  "name": "tmpname"\n}')
            print('[name] is added.')

        if (onenode.find('"cipher":') == -1):
            onenode = onenode.replace('"scy":', '"cipher":')
        if (onenode.find('"network":') == -1):
            onenode = onenode.replace('"net":', '"network":')
        if (onenode.find('"server":') == -1):
            onenode = onenode.replace('"add":', '"server":')
        if (onenode.find('"alterId":') == -1):
            onenode = onenode.replace('"aid":', '"alterId":')
        if (onenode.find('"uuid":') == -1):
            onenode = onenode.replace('"id":', '"uuid":')
        if (onenode.find('"ws-path":') == -1):
            onenode = onenode.replace('"path":', '"ws-path":')

        if(onenode.find('"type":') == -1):
            onenode = onenode.replace('\n}', ',\n  "type": "vmess"\n}')
            print('[type] is added.')
        return onenode

    # 标准格式的json转换成clash格式
    def josn_to_clash(onenode):
        try:
            onenode = onenode.replace('\'', '')
            node = json.loads(onenode)
            onenode = ''
            for key, value in node.items():
                value = value.replace(' ', '')
                if(key == 'name'):
                    onenode = onenode + '\n  name: ' + '\'' + value + '\''
                elif(key == 'password'):
                    onenode = onenode + '\n  ' + key + ': ' + value
                elif(key == 'port'):
                    if(isinstance(value, int)):
                        onenode = onenode + '\n  ' + key + ': ' + value
                    else:
                        onenode = onenode + '\n  ' + key + ': 443'
                elif(key == 'ws-headers'):
                    value = value.replace('{', '').replace('}', '')
                    if(value.find(',') > 0):
                        onenode = onenode + '\n  ' + key + ':'
                        for ivalue in value.split(','):
                            if(ivalue.find(':') > 0 and ivalue.find(ivalue.split(':')[0]) == -1):
                                onenode = onenode + '\n    ' + ivalue.split(':')[0] + ': ' + ivalue.split(':')[1]
                    elif(value.find(':') > 0 and ivalue.find(value.split(':')[0]) == -1):
                        onenode = onenode + '\n  ' + key + ':\n    ' + value.split(':')[0] + ': ' + value.split(':')[1]
                elif(key == 'tls'):
                    if(value == 'tls' or value == 'true'):
                        onenode = onenode + '\n  tls: true'
                    else:
                        onenode = onenode + '\n  tls: false'
                else:
                    if(len(key) > 0):
                        onenode = onenode + '\n  ' + key + ': ' + value
            onenode = onenode.strip('\n  ')

            if(onenode.find('cipher') == -1):
                onenode = onenode + '\n  cipher: auto'
            #onenode = onenode.lstrip('\n')
            #onenode = j.rstrip('\n')
            if(onenode.find('cipher: rc4') > -1 ):
                print('Line-218-not-supported-node:\n' + onenode)
                onenode = ''
            return onenode
        except Exception as ex:
            print('Line-167-StrText: ' + str(ex) + '\n' + onenode)
            LocalFile.write_LocalFile('./ipfs/tmp/err.log', 'Line-167-StrText: ' + str(ex) + '\n' + onenode)
            return ''

    # all-to-ss
    def all_to_ss(onenode):
        try:
            if (onenode.find("#") == -1):
                onenode= onenode + "#0"
            #j = "ss://YWVzLTI1Ni1nY206bjh3NFN0bmJWRDlkbVhZbjRBanQ4N0VBQDIxMi4xMDIuNTQuMTYzOjMxNTcy#title"
            #j = "ss://YWVzLTI1Ni1nY206bjh3NFN0bmJWRDlkbVhZbjRBanQ4N0VB@212.102.54.163:31572#title"
            #j = "ss://YWVzLTEyOC1nY206c3VvLnl0L3NzcnN1Yg==@212.102.54.163:10443/?plugin=obfs-123
            onenode = onenode.replace("/?", "#")
            if (onenode.find("@") == -1):
                jjs = onenode.split("#", 1) # 第二个参数为 1，返回两个参数列表
                onenode = "ss://"+(base64.b64decode(jjs[0][5:].encode("utf-8")).decode("utf-8"))+"#"+jjs[1]
            else:
                jjs = onenode.split("@", 1) # 第二个参数为 1，返回两个参数列表
                onenode = "ss://"+(base64.b64decode(jjs[0][5:].encode("utf-8")).decode("utf-8"))+"@"+jjs[1]
            #ss://aes-256-gcm:n8w4StnbVD9dmXYn4Ajt87EA@212.102.54.163:31572#title
            oldname = onenode.split("#", 1)[1]
            onenode = 'ss://' + base64.b64encode(onenode.split("#", 1)[0][5:].encode("utf-8")).decode("utf-8") + '#' + oldname
            return onenode
        except Exception as ex:
            print('Line-199-StrText: ' + str(ex) + '\n' + onenode)
            #LocalFile.write_LocalFile('./ipfs/tmp/err.log', '\nLine-199-StrText: ' + str(ex) + '\n' + onenode)
            return ''

    # 非标准格式的vmess明文地址转化为标准格式的vmess明文
    def all_to_ssr(onenode):
        oldname = onenode
        print('NewNode1:\n' + onenode)
        if(onenode.find('ps:') > -1):
            if(oldname.find('ps:\'') > -1):
                oldname = StrText.get_str_btw(oldname, 'ps:\'', '\',')
            elif(oldname.find('ps:"') > -1):
                oldname = StrText.get_str_btw(oldname, 'ps:"', '\",')
            else:
                oldname = StrText.get_str_btw(oldname, 'ps:', ',')
            if(len(oldname) > 0):
                onenode = onenode.replace(oldname, 'tmpname')
        else:
            if(oldname.find('name:\'') > -1):
                oldname = StrText.get_str_btw(oldname, 'name:\'', '\',')  #空格全替换掉，名称IP:PORT的就会出错。
            elif(oldname.find('name:"') > -1):
                oldname = StrText.get_str_btw(oldname, 'name:"', '\",')
            else:
                oldname = StrText.get_str_btw(oldname, 'name:', ',')

        if(len(oldname)  > 0):
            onenode = onenode.replace(oldname, 'tmpname')
        onenode = onenode.replace('\'', '').replace('"', '')
        onenode = onenode.replace(' ', '') #空格全替换掉，名称IP:PORT的就会出错。现已经对名称进行替换，故可以去掉全部空格。
        #onenode = onenode.replace(',}', '}')
        onenode = onenode.replace('\n', ',')
        onenode = onenode.replace('\r', ',')
        onenode = onenode.replace(',,', ',')
        onenode = onenode.replace(',,', ',')
        onenode = onenode.replace(',,', ',')
        onenode = onenode.replace('{,','{')
        onenode = onenode.replace(',}','}')

        #忽略{name: 🇯🇵JP-35.77.5.55, server: 034.ap.pop.bigairport.net, port: 12356, type: vmess, uuid: a6f82e7d-6e99-4a4e-8981-8e91453c13f7, alterId: 1, cipher: auto, skip-cert-vertify: false, network: ws, ws-path: /, tls: True, ws-headers: {Host: t.me/vpnhat}}

        if(onenode.find('alterId:')>-1):
            #onenode = onenode.replace('name:', 'ps:')
            onenode = onenode.replace('server:', 'add:')
            onenode = onenode.replace('uuid:', 'id:')
            onenode = onenode.replace('alterId:', 'aid:')
            onenode = onenode.replace('cipher:', 'scy:')
            onenode = onenode.replace('network:', 'net:')
            onenode = onenode.replace('ws-path:', 'path:')
            #onenode = onenode.replace('"host":', '"host":')
        print('NewNode2:\n' + onenode)
        onenode = onenode.strip('- ')
        onenode = onenode.replace(',,', ',')
        onenode = onenode.replace(' ', '')
        onenode = onenode.replace(':', '": "')
        onenode = onenode.replace(',', '",\n  "')
        onenode = onenode.replace('{', '{\n  "')
        onenode = onenode.replace('\n\n', '\n')
        onenode = onenode.replace('"\n', '"')
        onenode = onenode.replace('"}', '"\n}')
        onenode = onenode.replace(': ",', ': "",')
        onenode = onenode.replace(': "\n', ': ""\n')
        onenode = onenode.replace(',\n  "}', '"\n}')
        onenode = onenode.replace('}",\n  "', '}')

        if(onenode.find('\n}') == -1 and onenode.find('"}') == -1):
            onenode = onenode.replace('}', '"\n}')
            
        print('NewNode3:\n' + onenode)
        if(onenode.find('\n}') == -1 and onenode.find('"}') == -1 and onenode.find(',}') == -1):
            onenode = onenode.replace('}', '"\n}')
        #{"add":"104.255.66.87","v":"2","ps":"CA_940","port":38922,"id":"f3e846c1-d8e4-42df-86d4-f4e5028630d8","aid":"8","net":"tcp","type":"","host":"","path":"/","tls":""}
        #{"add": "v7.ssrsub.com", "v": "2", "ps": "'v7.ssrsub.com'", "port": "168", "id": "e54a480c-77e3-41ca-8f8b-17ffb50dbd08", "aid": "0", "net": "ws", "type": "", "host": "", "path": "/ssrsub", "tls": "tls"}
        
        if(onenode.find('{name: \'') > -1):
            print('Line-446:\n'+ base64.b64decode(j[8:]).decode('utf-8') + '\n' + onenode)
        #    print(onenode)
        #elif(onenode.find('"v":')>-1):
        #    if(onenode.find('"ps":')==-1):
        #        temp = onenodeson.loads(onenode)
        #        temp.update({"ps": "tmp"})
        #        onenode = onenodeson.dumps(temp)                    
        #互相转换: 文本转换成字典
        if(onenode.find('"ps":') == -1):
            onenode = onenode.replace('\n}', ',\n  "ps": "tmp"\n}')
            print('[ps] is added.')
