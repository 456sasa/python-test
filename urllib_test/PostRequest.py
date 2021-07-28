import urllib.request

#将表单数据转化为bytes类型，用utf-8编码
data = bytes(urllib.parse.urlencode({'name':'Bill','age':30}),encoding='utf-8')
#提交http POST请求
response = urllib.request.urlopen('http://httpbin.org/post',data = data)
# 输出响应数据
print(response.read().decode('utf-8'))