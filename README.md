# 孰知分享

创享汇扫码获取随机评论

1. 开发环境
  - 编程语言：python3
  - Web框架：flask
  - 数据库： sqlite
  
2. 通过docker部署应用:

```
docker build -t "wanghan0501/flask:chuangxianghui" .
```
3. 运行docker
```
docker run -it -p 80:5000 --name shuzhifenxiang wanghan0501/flask:chuangxianghui
```