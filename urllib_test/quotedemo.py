from urllib.parse import quote,unquote

keyword = '李宁'
#对参数进行编码
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)
#解码
url = unquote(url)
print(url)