# ���ü̳еľ���
FROM debian:unstable-slim

# ������һЩ�����ߵĻ�����Ϣ
MAINTAINER debian(unstable-slim) + nginx + python3.10 + node(Free-Node-Merga-SpeedTest) updated by "vpei" (vpei@live.com)

# ���ն���Ҫִ�е�����
RUN sed -ri -e 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list.d/debian.sources

# ����app�ļ����ǹ���Ŀ¼
WORKDIR /root/node
RUN rm -rf /root/node && mkdir -p /root/node
# �����ļ���Ŀ¼��ȥ
COPY . /root/node

RUN apt-get update
RUN apt-get -y upgrade

# RUN dpkg-reconfigure tzdata
# vim /etc/timezone
# Asia/Shanghai
#$ ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
#����
#$ cp -a /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

RUN apt-get install -y nginx
RUN apt-get install -y python3

# ����app�ļ����ǹ���Ŀ¼
WORKDIR /home/node
RUN rm -rf /home/node && mkdir -p /home/node
# �����ļ���Ŀ¼��ȥ
COPY . /home/node

# ����NODE�����ļ�Ŀ¼��NGINXĬ��Ŀ¼�¡�
RUN ln -s /home/node/out/* /var/www/html

COPY run.sh /home/node/run.sh
RUN chmod +x /home/node/run.sh
ENTRYPOINT sh /home/node/run.sh && tail -f /dev/null