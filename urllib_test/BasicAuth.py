from urllib import request
from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
from urllib.error import URLError

username = 'bill'
password = '1234'
url = 'http://localhost:5000/'

p = HTTPPasswordMgrWithDefaultRealm()
#封装realm,url、用户名和密码
p.add_password('localhost',url,username,password)
auth_handler = HTTPBasicAuthHandler(p)

#发送HTTP请求
opener = build_opener(auth_handler)

result = opener.open(url)
#获取服务器响应数据
html = result.read().decode('utf-8')
print(html)