import requests
# from requests import cookies
'''
r1 = requests.get('http://www.baidu.com')
print(r1.cookies)
#获取每一个Cookie
for key,value in r1.cookies.items():
    print(key,'=',value)

headers = {
    'host':'www.jianshu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
         (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Cookie':'UM_distinctid=179f8f643246ae-06099343e0f1d2-f7f1939-100200-179f8f64325abb; locale=zh-CN; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1627266986,1627368115; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2F; read_mode=day; default_font=font2; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22179f8f639bb40b-09aadeeb1a2539-f7f1939-1049088-179f8f639bca53%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22179f8f639bb40b-09aadeeb1a2539-f7f1939-1049088-179f8f639bca53%22%7D; CNZZDATA1279807957=1796600996-1627266945-https%253A%252F%252Fwww.baidu.com%252F%7C1627437055; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1627439127'
}
#通过headers参数发送Cookie
r2 = requests.get('https://www.jianshu.com/',headers=headers)
print(r2.text)
'''

#另一种设置Cookie的方式
headers = {
    'host':'www.jianshu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
         (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}
cookies = 'UM_distinctid=179f8f643246ae-06099343e0f1d2-f7f1939-100200-179f8f64325abb; locale=zh-CN; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1627266986,1627368115; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2F; read_mode=day; default_font=font2; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22179f8f639bb40b-09aadeeb1a2539-f7f1939-1049088-179f8f639bca53%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22179f8f639bb40b-09aadeeb1a2539-f7f1939-1049088-179f8f639bca53%22%7D; CNZZDATA1279807957=1796600996-1627266945-https%253A%252F%252Fwww.baidu.com%252F%7C1627437055; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1627439127'
jar = requests.cookies.RequestsCookieJar()

#将多个Cookie拆开，多个Cookie之间用(;)分隔
for cookie in cookies.split(';'):
    #得到Cookie的key和value，每一个Cookie的key和value之间用等号(=)分隔
    key,value = cookie.split("=",1)
    #将Cookie添加到RequestsCookieJar对象中
    jar.set(key,value)

r3 =  requests.get('https://www.jianshu.com/',cookies = jar,headers=headers)
print(r3.text)