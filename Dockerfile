FROM python:3.9-alpine as base
FROM base as builder
#COPY ./requirements.txt /requirements.txt
#RUN pip install --user -r ./requirements.txt -i https://pypi.douban.com/simple

# FROM alpine

FROM base
# copy only the dependencies installation from the 1st stage image
#COPY --from=builder /root/.local /root/.local

RUN rm -rf /home/node && mkdir -p /home/node
# 设置app文件夹是工作目录
WORKDIR /home/node
# 复制文件及目录过去
# ADD . /home/node
COPY * /home/node/


# update PATH environment variable
ENV PATH=/home/node/.local/bin:$PATH



#RUN mkdir /code \
#&&apt-get update \
#&&apt-get -y install freetds-dev \
#&&apt-get -y install unixodbc-dev



# RUN apt-get install -y nginx
# RUN apt-get install -y python3
# RUN set -xe
# RUN apt-get install -y python3-pip
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
# RUN ln -s /usr/local/bin/python3.10 /usr/bin/python3
# RUN ln -s /usr/local/bin/pip3.10 /usr/bin/pip3
# RUN ln -s /root/Python-3.10/bin/pip /usr/local/bin/pip

# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r /home/node/requirements.txt
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pillow
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple requests
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple requests[socks]
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pysocks
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple flask
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple flask-cors
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pyyaml
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple aiohttp
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple aiohttp_socks
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pynat
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple beautifulsoup4
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple selenium
# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple ssrspeed


CMD ["/bin/sh"]
#CMD ["/bin/bash", "run.sh"]

# 打包命令
# docker login && docker buildx build -t vpei/node:latest --platform linux/amd64 --push .

# 批量打包命令
# docker buildx install
# docker buildx create --use --name build --node build --driver-opt network=host
# docker login && docker buildx build -t vpei/node:latest --platform linux/arm/v7,linux/arm64/v8,linux/386,linux/amd64 --push .
