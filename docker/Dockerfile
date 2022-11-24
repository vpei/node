# 设置继承的镜像
FROM minirailgun/openwrt-aarch64


# 下面是一些创建者的基本信息
MAINTAINER debian(unstable-slim) + nginx + python3.10 + node(Free-Node-Merga-SpeedTest) updated by "vpei" (vpei@live.com)


# 在终端需要执行的命令
#RUN sed -ri -e 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list.d/debian.sources


#RUN apt-get update
# RUN apt-get -y upgrade


# RUN dpkg-reconfigure tzdata
# vim /etc/timezone
# Asia/Shanghai
#$ ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
#或者
#$ cp -a /usr/share/zoneinfo/Asia/Shanghai /etc/localtime


RUN rm -rf /home/node && mkdir -p /home/node
# 设置app文件夹是工作目录
WORKDIR /home/node
# 复制文件及目录过去
# COPY . /home/node
ADD . /home/node


#RUN apt-get install -y nginx
RUN apt-get install -y python3
# RUN set -xe
RUN apt-get install -y python3-pip
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
# RUN ln -s /usr/local/bin/python3.10 /usr/bin/python3
# RUN ln -s /usr/local/bin/pip3.10 /usr/bin/pip3
# RUN ln -s /root/Python-3.10/bin/pip /usr/local/bin/pip
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r /home/node/requirements.txt
#RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pillow
#RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple requests
#RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple requests[socks]
#RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pysocks
#RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple flask
#RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple flask-cors
#RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pyyaml
#RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple aiohttp
#RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple aiohttp_socks
#RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pynat
#RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple beautifulsoup4
#RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple selenium


# 链接NODE生成文件目录至NGINX默认目录下。
#RUN ln -s /home/node/out/* /var/www/html

# COPY run.sh /home/node/run.sh
#RUN chmod u+x /home/node/run.sh
#RUN sed -i 's/\r//' /home/node/run.sh
#ENTRYPOINT bash /home/node/run.sh && tail -f /dev/null
# RUN rm -R /home/node/.git