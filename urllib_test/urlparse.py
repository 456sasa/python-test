from urllib.parse import urlparse,urlunparse
#拆分url
result = urlparse('http://search.jd.com/Searchprint;hello?keyword=Python从菜鸟到高手&enc=utf-8#comment')
print('scheme: ',result.scheme)
print('netloc: ',result.netloc)
print('path: ',result.path)
print('params: ',result.params)
print('query: ',result.query)
print('fragment: ',result.fragment)
print("-----------------------------")
#拆分url，指定默认的scheme，并且忽略fragment部分
result = urlparse('search.jd.com/Searchprint;hello?keyword=Python从菜鸟到高手&enc=utf-8#comment'\
        ,scheme='ftp',allow_fragments=False)
print('scheme: ',result.scheme)
print('fragment: ',result.fragment)
print("-----------------------------")

#合并不同部分，组成一个完整的url
data = ['https','search.jd.com','Searchprint','world','keyword=Python从菜鸟到高手&enc=utf-8','comment']
print(urlunparse(data))