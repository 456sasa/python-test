import urllib.request

url = "https://www.jd.com"
response = urllib.request.urlopen(url)

print(f'response的类型：{type(response)}')
print(f'status(状态码):{response.status}, msg(响应消息):{response.msg}, version(http版本):{response.version}')
# print(f"headers(响应头信息): {response.getheaders()}")

print(f"Content-Type为：{response.getheader('Content-Type')}")