#!/bin/bash

sleep 1

# /etc/init.d/nginx start

sleep 1

nohup /etc/init.d/nginx start > node.log 2>&1 & 