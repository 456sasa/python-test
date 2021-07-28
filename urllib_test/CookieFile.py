import http.cookiejar,urllib.request
filename1 = 'urllib_test/cookies1.txt'
filename2 = 'urllib_test/cookies2.txt'
#创建MozillaCookiJar对象
cookie1 = http.cookiejar.MozillaCookieJar(filename1)
#创建LWPCookieJar对象
cookie2 = http.cookiejar.LWPCookieJar(filename2)
handler1 = urllib.request.HTTPCookieProcessor(cookie1)
handler2 = urllib.request.HTTPCookieProcessor(cookie2)
opener1 = urllib.request.build_opener(handler1)
opener2 = urllib.request.build_opener(handler2)
opener1.open("https://www.baidu.com")
opener2.open("https://www.baidu.com")
#将Cookie保存成Moziila格式
cookie1.save(ignore_discard=True,ignore_expires=True)
#将Cookie保存成LWP格式
cookie2.save(ignore_discard=True,ignore_expires=True)