# 基础镜像信息
FROM python:3.5.4

# 维护者信息
MAINTAINER 王晗 hanwang.0501@gmail.com

# 镜像操作指令 
ADD ./requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN mkdir /shuzhifenxiang
WORKDIR /shuzhifenxiang
Add . /shuzhifenxiang

EXPOSE 5000

CMD python3 /shuzhifenxiang/manage.py
