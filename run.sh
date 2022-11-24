#!/bin/bash

sleep 1

# /etc/init.d/nginx start

sleep 1

# nohup /etc/init.d/nginx start > node.log 2>&1 & 
nohup python3 /home/node/test.py -u https://ghproxy.com/https://raw.githubusercontent.com/vpei/Free-Node-Merge/main/out/node.txt > node.log 2>&1 & 