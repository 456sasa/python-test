import http.cookiejar,urllib.request

#创建cookiejar对象
cookie = http.cookiejar.CookieJar()
#创建HTTPCookieProccessor对象
handler = urllib.request.HTTPCookieProcessor(cookie)
openner = urllib.request.build_opener(handler)

#给https://www.baidu.com/发送请求，并获得响应数据
response = openner.open("https://www.baidu.com/")
print("------https://www.baidu.com/------")
#输出服务端发送的所有Cookie
for item in cookie:
    print(item.name + '=' + item.value)
print("------http://127.0.0.1:5000/writeCookie------")
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
openner = urllib.request.build_opener(handler)
response = openner.open("http://127.0.0.1:5000/writeCookie")
for item in cookie:
    print(item.name + '=' + item.value)