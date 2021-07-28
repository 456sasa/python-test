import http.cookiejar,urllib.request
filename = "urllib_test\cookies_test.txt"
cookie = http.cookiejar.LWPCookieJar()
#装载cookies.txt文件，由于使用了LWPCookieJar读取Cookie,所以Cookie文件必须是LWP格式
cookie.load(filename,ignore_discard=True,ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://127.0.0.1:5000/readCookie")
print(response.read().decode('utf-8'))