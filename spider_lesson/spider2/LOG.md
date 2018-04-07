#8.23

##url管理器

+ 内存：python内存 set（）
+ 关系数据库：MySQL  urls（url，is_crawled）
+ 缓存数据库：redis

##网页下载器

+ request
+ urllib2（官方模块）

***

####方法1

    import urllib2

    #直接请求
    response = urllib2.urlopen('http://www.baidu.com')

    #获取状态码，200表示获取成功
    print(response.getcode())

    #读取内容
    cont = response.read()

####方法2

    import urllib2
    
    #创建Request对象
    request = urllib2.Request(url)

    #添加数据
    request.add_data('a','1')

    #添加http的header
    request.add_header('user-Agent','Mozilla/5.0')

    #发送请求获取结果
    response = urllib2.urlopen(request)

####方法3

![方法图](lesson/5.png "方法3")

#####eg:

    import urllib2,cookielib

    #创建cookie容器
    cj = cookielib.CookieJar()

    #创建一个opener
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    #给urllib2安装opener
    urllib2.install_opener(opener)

    #使用带有cookie的urllib2访问网页
    response = urllib2.urlopen('http://www.baidu.com')

####PS:以上方法适用于python2，对于python3作出更改

    from urllib import request
    import http.cookiejar
    #原代码中：
    #urllib2替换成request
    #cooklib替换成http.cookiejar

***

##网页解析器

+ 正则表达式(模糊匹配)
+ html.parser结构化解析--DOM树
+ Beautiful Soup 拥有html.parser,lxml的功能
+ lxml   

####安装Beautiful Soup4

***

###### Python2.7安装方法：
sudo python2.7 -m pip install --upgrade pip 
sudo python -m pip install beautifulsoup4           
储存在python2.7/site-packages

######python3安装方法
pip3 install beautifulsoup4      
安装Python中会自带pip3.使用pip3安装的模块会储存在python3.6/site-packages

***

####beautifulsoup4语法

***

######创建BeautifulSoup对象

    from bs4 import BeautifulSoup

    #根据HTML网页字符串创建BeautifulSoup对象
    soup = BeautifulSoup (
               html_doc,                  #HTML文档字符串
               'html.parser',             #HTML解析器
               from_encoding = 'utf-8'    #HTML文档的编码
           )  

######搜索节点

    #方法:find_all(name,attrs,string) 

    #查找所有标签为a的节点
    soup.find_all('a')

    #查找所有标签为a，连接符合/view/123.htm形式的节点
    soup.find_all('a',href = '/view/123.htm')
    soup.find_all('a',href = re.compile(r'/view/\d+\.htm'))
    #匹配正则表达式要import re 模块

    #查找所有标签为div，class为abc，文字为python的节点
    soup.find_all('div',class_ = 'abc',string = 'python')

######访问节点信息

    #得到节点；<a herf = '1,html'>python</a>
    
    #获取查找到的节点的标签名称
    node.name

    #获取查找到的a节点的href属性
    node['herf']

    #获取查找到的a节点的链接文字
    node.get_text()

***

##实例

***

+ 目标：百度百科python词条相关词条网页-标题和简介
+ 入口页：https://baike.baidu.com/item/Python
+ URL格式：
    + 词条url：/item/Python
+ 数据格式：
    + 标题：```<dd class = "lemmaTitle-title"><<h1>***</h1></dd>```
    + 简介：```<div class="lemma-summary">***</div>```

***