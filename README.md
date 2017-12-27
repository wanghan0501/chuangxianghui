# chuangxianghui

创享汇扫码评论

1. 开发环境
  - 编程语言：Python3
  - Web框架：flask
  - 数据库： mysql
  
1. docker搭建:
```
sudo docker pull pysaber/python:2-3
sudo docker run --name api_deepbc -p 7202:7202 -p 7201:7201 -P -it -v $PWD/bc_workspace:/home/workspace pysaber/python:2-3
```

2. 数据库搭建
```
sudo docker pull mysql:5.7.20
sudo docker run --name APIDeepBC_Mysql -p 7203:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7.19
docker exec -it APIDeepBC_Mysql bash
mysql -h 127.0.0.1 -P 7203 -p