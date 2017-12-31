# 基础镜像信息
FROM python:3.5.4

# 维护者信息
MAINTAINER 王晗 hanwang.0501@gmail.com

RUN apt-get update && apt-get install -y --no-install-recommends \
        nano \
        curl \
        && \
    rm -rf /var/lib/apt/lists/*

# 镜像操作指令
COPY ./requirements.txt requirements.txt

RUN pip --no-cache-dir install --upgrade pip \
    && pip --no-cache-dir install -r requirements.txt \

#定义环境变量
ENV TIME_ZONE Asia/Shanghai
# 设置时区
RUN echo "${TIME_ZONE}" >/etc/timezone \
    && ln -sf /usr/share/zoneinfo/${TIME_ZONE} /etc/localtime \
    && mkdir /shuzhifenxiang

WORKDIR /shuzhifenxiang
COPY . /

EXPOSE 5000

CMD python3 /shuzhifenxiang/manage.py
