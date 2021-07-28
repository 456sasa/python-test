import urllib.request,urllib.parse

url = 'http://httpbin.org/post'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Host' : 'httpbin.org',
    'who' : 'Python Scrapy'
}

#定义表单数据
dict = {
    'name' : 'Bill',
    'age' : 30
}

data = bytes(urllib.parse.urlencode(dict),encoding='utf-8')
#创建Request对象，通过Request类的构造方法制定了表单数据和HTTP请求头
req = urllib.request.Request(url=url,data=data,headers=headers)
response = urllib.request.urlopen(req)

print(response.read().decode('utf-8'))