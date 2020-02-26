# 项目名称
网站导航系统

![](https://img.shields.io/badge/language-python-orange.svg)
![](https://img.shields.io/badge/Python-v3.8-red.svg?colorA=abcdef)
![](https://img.shields.io/badge/Django-v3.0.3-blue.svg?colorA=abc)


项目概要
==

基于Python3.8，Django3.0.3，根据数据库中对于网站类>网站组>网站URL的关系，自动生成前端页面，并且利用Django Admin进行后台数据库管理

部署文档
==
## ——以Centos7为例  
1、用自带的python2.7，执行yum install libffi-devel -y ，安装centos外部函数库  

2、安装python3.8,安装成功执行python —version查看当前python版本  

3、进入Django项目目录，执行  
pip3 install -r requirements.txt  
__（注意——pip3要是python3.8的版本）__    

4、找到python3.8的安装目录下的base.py，类似于...python3.8/site-packages/django/db/backends/mysql/base.py
注释以下行：  
if version < (1, 3, 13):  
    raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)  
    
 5、修改项目目录里web_site_manage/settings.py：  
 Mysql数据库连接：  
 DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'web_site_navigation',  ##___数据库名字，必须先创建该名字的数据库，否则系统报错___    
        'HOST':'192.168.227.199',       ##数据库IP  
        'PORT':3306,                    ##数据库端口  
        'USER':'root',                  ##数据库账号  
        'PASSWORD':'123456'             ##数据库密码  
    }  
}    

#自定义配置项    

CUSTOMIZE_OPTION = {  
    'web_site_name':'江苏高院网站导航',              #网站标题  
    'admin_app_name': '江苏高院网站导航系统',         #管理端中APP的名称  
}  


#后台管理界面标题  
GRAPPELLI_ADMIN_TITLE='江苏高院网站导航后台管理系统'  #更改管理端的登入title  

#允许所有主机访问  
ALLOWED_HOSTS = ['*']  

_修改完保存退出_  

    
 6、进入项目目录，删除web_site_manage/web_site_navigation/migrations下除了__init__.py以外的所有文件（__否则数据库无法正常创建表__）
 执行:  
 
 python manage.py makemigrations                       ##检查数据库差异（同步），生成迁移文件（migrations）    
 python manage.py migrate                              ##根据迁移文件生成对应的SQL语句     
 python manage.py createsuperuser                      ##创建后台管理网页的管理员用户密码  
 python manage.py runserver 服务器IP:8000 &             ##后台启动程序    
 

 
 使用文档
 ==
 1、浏览器输入服务器IP:8000即可访问  __（推荐使用google最新版本浏览器）__   
 
 2、浏览器输入服务器IP:8000/admin，或者点击页面管理员登录，即可后台管理系统   
 后台管理系统使用示例：  
 网站所属类：云平台运维  
 网站所属组：云平台监控系统  
 网站URL：ZABBIX系统；Alimonitor系统等  
 
 -----------------------------------------------
  *如有疑问或者更正的地方，请联系QQ183923316*  
 
 ___谢谢！___  
 



