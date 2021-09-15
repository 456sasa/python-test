from typing import Text
import requests
from lxml import etree

r = requests.get("https://www.jd.com/")
parser = etree.HTMLParser()

html = etree.HTML(r.text)

#去除空格
def clear(list):
    list2 = []
    for l in list:
        l = l.strip()
        list2.append(l)
    return list2
#提取导航条第一部分链接文本
nodes = html.xpath('//*[@id="navitems-group1"]//a/text()')
print(clear(nodes))
#提取导航条第二部分链接文本
nodes = html.xpath('//*[@id="navitems-group2"]//a/text()')
print(clear(nodes))
#提取导航条第三部分链接文本
nodes = html.xpath('//*[@id="navitems-group3"]//a/text()')
print(clear(nodes))