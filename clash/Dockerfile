# 设置继承的镜像
FROM debian:unstable-slim

# 下面是一些创建者的基本信息
MAINTAINER debian(unstable-slim) + nginx + python3.10 + node(Free-Node-Merga-SpeedTest) updated by "vpei" (vpei@live.com)

# 在终端需要执行的命令
RUN sed -ri -e 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list.d/debian.sources

# 设置app文件夹是工作目录
WORKDIR /root/node
RUN rm -rf /root/node && mkdir -p /root/node
# 复制文件及目录过去
COPY . /root/node

RUN apt-get update
RUN apt-get -y upgrade

# RUN dpkg-reconfigure tzdata
# vim /etc/timezone
# Asia/Shanghai
#$ ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
#或者
#$ cp -a /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

RUN apt-get install -y nginx
RUN apt-get install -y python3

# 设置app文件夹是工作目录
WORKDIR /home/node
RUN rm -rf /home/node && mkdir -p /home/node
# 复制文件及目录过去
COPY . /home/node

# 链接NODE生成文件目录至NGINX默认目录下。
RUN ln -s /home/node/out/* /var/www/html

COPY run.sh /home/node/run.sh
RUN chmod +x /home/node/run.sh
ENTRYPOINT sh /home/node/run.sh && tail -f /dev/null