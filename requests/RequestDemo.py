from  requests import Request,Session, sessions
import requests

url = 'http://httpbin.org/post'
data = {
    'name' : 'Bill',
    'age' : 30
}
headers = {
    'country' : 'China'
}
session = Session()
#封装请求数据
req =  Request('post',url,headers=headers,data=data)
#返回requests.models.Response对象
prepared = session.prepare_request(req)
#发送请求

r = session.send(prepared)
print(type(r))
print(r.text)