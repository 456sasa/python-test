import requests
from requests import sessions

#不使用Session对象发送请求，其中set/cookies/Bill相当于向服务器写入一个名为name的Cookie，值为Bill
requests.get('http://httpbin.org/cookies/set/name/Bill')
#第二次发送请求，这两次请求不在同一个Session中，第一次请求发送的Cookie在第二次请求中是无法获取道德
r1 = requests.get('http://httpbin.org/cookies')
print(r1.text)

#使用Session，创建Session对象
session = requests.Session()
#第一次发送请求
session.get('http://httpbin.org/cookies/set/name/Bill')
#第二次发送请求
r2 = session.get('http://httpbin.org/cookies')
print(r2.text)