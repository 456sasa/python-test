from urllib3 import * 
from urllib.parse import urlencode

#调用disabled_warnings函数可以阻止显示警告消息
disable_warnings()
#创建PoolManager的实例
http = PoolManager()

url = 'http://www.baidu.com/s?' + urlencode({'wd':'极客'})
print(url)
response = http.request('GET',url)

url = 'http://www.baidu.com/s?'
#直接使用fields关键字参数指定GET请求字段
response = http.request('GET',url,fields={'wd':'极客'})
data = response.data.decode('UTF-8')

print(data)