import requests

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
}

r = requests.get('http://www.jianshu.com/',headers=headers)
print(type(r.status_code),r.status_code)
print(type(r.headers),r.headers)
print(type(r.cookies),r.cookies)
print(type(r.url),r.url)

#输出请求历史
print(type(r.history),r.history)
#根据codes中的值判断状态码
if not r.status_code == requests.codes.ok:
    print('failed')
else:
    print('ok')