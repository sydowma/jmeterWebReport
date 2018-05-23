# Dispaly JMeter Report for HTML 更好的展示 JMeter 网页版数据

更好的展示 JMeter 的 HTML 报告

## Why ? 为什么要做这个

JMeter 通常自带 HTML 报告展示, 但是依旧需要下载到本地观看, 当然你也可以直接在服务器上配置好 nginx 访问. 但是查找和切换时依旧不够方便, 例如不能展示所有的报告信息, 需要手动拼接访问链接. 本项目就是为了解决这个问题, 可以展示指定报告目录, 自动拼接URL, 点击即可访问

### Configration 配置

1. 配置好 [Nginx](jmeterWebReportNginx.conf) , 并更改 server_name
2. dirs_name 更改 PATH
3. template/home.html 更改为你自己的域名
4. 调试时 manage.py 中 `app.debug` 改为 `True` , 上线前改为 `False`

### Install 安装方式

1. 需要 Python3 ,暂时没有试验 python2
2. 安装 FLask `pip install -r requirements.txt` 或者直接安装 `pip install jmeterWebReport`

### Run 启动方法

#### Local 本地

```shell
cd jmeter_web_report
flask run
```

#### Deploy 服务器部署

`pip install uwsgi`

uwsgi 启动 ： `uwsgi config.ini`
uwsgi 关闭： `killall -9 uwsgi`