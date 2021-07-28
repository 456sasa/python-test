from typing import ByteString
import urllib.request
from urllib.parse import unquote,urlencode
import base64

url = 'http://httpbin.org/post'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Host' : 'httpbin.org',
    'Chinese1' : urlencode({'name':'李宁'}),#设置中文HTTP请求头，用url编码格式
    #设置中文HTTP请求头，用base64编码格式
    'Mychinese':base64.b64encode(bytes('这是中文请求头',encoding='utf-8')),
    'who' : 'Python Scrapy'
}

dict = {
    'name' : 'Bill',
    'age' : 30
}
data = bytes(urlencode(dict),encoding='utf-8')
req = urllib.request.Request(url=url,data=data,headers=headers,method='POST')

#通过add_header方法添加中文请求头，url编码格式
req.add_header('Chinese2',urlencode({'国籍':'中国'}))

response = urllib.request.urlopen(req)
#获取服务器端的响应信息
value = response.read().decode('utf-8')
print(value)

import json
#将返回值转换为json对象
responseObj = json.loads(value)
#解码url编码格式的HTTP请求头
print(unquote(responseObj['headers']['Chinese1']))
print(unquote(responseObj['headers']['Chinese2']))
#解码base64编码格式的HTTP请求头
print(str(base64.b64decode(responseObj['headers']['Mychinese']),'utf-8'))