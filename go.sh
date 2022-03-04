#!/bin/bash /etc/rc.common
#========================================================================
#
# This file is licensed under the terms of the GNU General Public
# License version 2. This program is licensed "as is" without any
# warranty of any kind, whether express or implied.
#
# This file is a part of the make OpenWrt for Amlogic s9xxx tv box
# https://github.com/ophub/amlogic-s9xxx-openwrt
#
# Description: Automatically Packaged OpenWrt for Amlogic s9xxx tv box
# Copyright (C) 2020- https://github.com/unifreq
# Copyright (C) 2020- https://github.com/tuanqing/mknop
# Copyright (C) 2020- https://github.com/ophub/amlogic-s9xxx-openwrt
#
#===== Install the basic packages of make openwrt for Ubuntu 20.04 ======
#
# sudo apt-get update -y
# sudo apt-get full-upgrade -y
# sudo apt-get install -y $(curl -fsSL git.io/ubuntu-2004-openwrt)
#
# Command: sudo ./make -d
# Command optional parameters please refer to the source code repository
#
#============================ Functions list ============================

# PATH=/mnt/mmcblk2p4/NodeSpeed
# export PATH

date +%Y-%m-%d-%H:%M:%S
cd /mnt/mmcblk2p4/NodeSpeed
#pip install requests
#pip install pysocks
#pip install socks
# python -m pip install -U wheel
# pip install qqwry-py3
# sudo -E apt-get -qq update
# sudo -E apt-get -qq install inetutils-ping
#  pip install -r ./requirements.txt
# git pull
chmod -R 7777 ../NodeSpeed
sleep 10
date +%Y-%m-%d-%H:%M:%S
echo CID-7777 
# git push
# sleep 10
# echo CID-push
# git pull
# sleep 10
# echo CID-pull
# sleep 10
# git add . && git commit -m "Update config for Speed-Node-OP" -a && git push
# sleep 10
# echo CID-git-push
date +%Y-%m-%d-%H:%M:%S
# chmod 7777 ./clients/config.json
# chmod 7777 ./clients/xray/xray
# chmod 7777 ./clients/v2ray-core/v2ray
# chmod 7777 ./clients/v2ray-core/v2ctl
# python ./main.py -u "http://13.212.72.222:8080/ipns/k51qzi5uqu5dlfnig6lej7l7aes2d5oed6a4435s08ccftne1hq09ac1bulz2f/node.txt"
# python ./test.py -u https://raw.githubusercontent.com/vpei/Free-Node-Merge/main/res/node-1.txt
# python ./test.py -u https://sub.maoxiongnet.com/sub?target=v2ray&url=https%3A%2F%2Ffree.kingfu.cf%2Fvmess%2Fsub
file1=./tmp/001.out
# nohup python ./test.py -u http://13.212.72.222:8080/ipns/k51qzi5uqu5dlfnig6lej7l7aes2d5oed6a4435s08ccftne1hq09ac1bulz2f/node.txt >$file1 2>&1 &
python ./test.py -u http://13.212.72.222:8080/ipns/k51qzi5uqu5dlfnig6lej7l7aes2d5oed6a4435s08ccftne1hq09ac1bulz2f/node.txt >$file1 2>&1 &
sleep 3600
echo CID-python
# git push
# sleep 10
# echo CID-push
# git add . && git commit -m "Update config for Speed-Node-OP" -a && git push
# sleep 10
# echo CID-git-push
dataline1=$(ipfs add -r ./out)
echo $dataline1
date +%Y-%m-%d-%H:%M:%S
#echo 获取最后50个字符（46 + 4），数字50需要根据文件发布的目录调整./out，目录长度增长，50数字增加。
CID=${dataline1: -50}
echo $CID
# echo 删除空格后所有
CID=${CID% *}
# CID=${CID:0:46}
echo ID:$CID
date +%Y-%m-%d-%H:%M:%S
# ipfs id
echo 将文件夹CID改名
# ipfs files cp /ipfs/$CID /2$CID
# ipfs pin add $CID
echo 运行软件客户端
file1=./tmp/002.out
nohup ipfs daemon >$file1 2>&1 &
sleep 30
#echo 下载缓存
#nohup sudo wget http://127.0.0.1:8080/ipfs/Qmczp7Sp6bsia8f6kxdMRvzqHKzrQM6NMYec9RfQJ3ksnq/ -O $file1 >$file1 &
date +%Y-%m-%d-%H:%M:%S
# echo 将软件文件夹CID添加到发布文件夹
#sleep 30
#ipfs files cp /ipfs/Qmczp7Sp6bsia8f6kxdMRvzqHKzrQM6NMYec9RfQJ3ksnq /clash/soft
#sleep 30
# echo 重新获取CID-1
#dataline1=$(ipfs files stat "/clash" )
#echo $dataline1
# echo 重新获取CID-2
#CID=${dataline1:0:46}
echo ID:$CID
#sleep 5
# echo 对发布文件夹的新CID进行远程固定
# curl -X POST http://116.207.131.38:5001/api/v0/pin/add?arg=/ipfs/Qmczp7Sp6bsia8f6kxdMRvzqHKzrQM6NMYec9RfQJ3ksnq
# curl -X POST https://ipfs.infura.io:5001/api/v0/pin/add?arg=/ipfs/$CID
# curl -X POST http://122.9.166.5:5001/api/v0/pin/add?arg=/ipfs/Qmczp7Sp6bsia8f6kxdMRvzqHKzrQM6NMYec9RfQJ3ksnq
# echo 对发布文件夹的新CID进行本地固定
# ipfs pin add $CID
# 对发布的文件进行加载, CID从001.out文件获取或直接传递
# nohup sudo wget http://127.0.0.1:8080/ipfs/$CID/ -O $file1 >$file1 &
# echo 对网络文件进行循环加载，提高IPFS发布成功率
python ./ipfs.py ipfs $CID
#echo 退出ipfs软件 ipfs #kill ipfs
#ipfs shutdown
#sleep 30
#echo 显示所有进程
#ps -A
date +%Y-%m-%d-%H:%M:%S
echo 离线发布ipfs name publish /ipfs/$CID --allow-offline=true --lifetime=24h
# ipfs name publish /ipfs/$CID --allow-offline=true --lifetime=24h
# CID=${dataline1: -50}
ipfs name publish /ipfs/$CID
sleep 30
ipfs name publish /ipfs/$CID
sleep 30
date +%Y-%m-%d-%H:%M:%S
# echo 后台运行ipfs软件
# file1=./ipfs/tmp/003.out
# nohup ipfs daemon >$file1 &
# sleep 30
# echo ipfs run
python ./ipfs.py ipns
date +%Y-%m-%d-%H:%M:%S

exit 0