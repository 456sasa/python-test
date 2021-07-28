import requests

proxies ={
    'http': 'http://144.123.68.152:25653',
    'https': 'https://144.123.68.152:25653'
}
#通过代理请求天猫首页
r = requests.get('https://www.tmall.com/',proxies=proxies)
print(r.text)