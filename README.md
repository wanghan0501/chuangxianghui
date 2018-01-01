# shuzhifenxiang(孰知分享)

Scan QR code and get a random comment.

## Environment 
  - Language：Python3
  - Web framework：Flask
  - Database： Sqlite

## Quick Use

If you want to use this without docker, you can following below:

```bash
python3 manage.py
```
### Change Port

Default port is `5000`

If you want to change the default port, please set the port which you want to the following statement.
```python
app.run(debug=False, port=5000, host='0.0.0.0', threaded=True)
```

## Development

1. develop project by docker
```bash
docker build -t "wanghan0501/flask:chuangxianghui" .
```
2. run docker
```
docker run -it -p 80:5000 --name shuzhifenxiang wanghan0501/flask:chuangxianghui
```
3. control docker with running
   
   - Go into the existing docker.
   
   ```Control+C``` will kill the docker.    
    ```
    docker attach chuangxianghui
    ```
   -  Start a new terminal.
    
   ```Control+C``` will not kill the docker. 
    ```
    docker exec -it shuzhifenxiang /bin/bash
    ```  

## Contact Me
If you have some questions about this project, please contact me.
[hanwang.0501@gmail.com](hanwang.0501@gmail.com)    