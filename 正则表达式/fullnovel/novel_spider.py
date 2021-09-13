from sre_constants import GROUPREF
from urllib import request
import re

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}

#根据小说链接得到小说目录和对应的URL,该函数返回catelogs列表
def getCatelogs(url):
    #请求小说目录页面
    req = request.Request(url=url,headers=headers,method='GET')
    #发送请求
    response = request.urlopen(req)
    #返回数据
    result = []
    if response.status == 200 :
        #读取页面内容
        html = response.read().decode('utf-8')
        #得到<li>节点列表
        aList = re.findall('<li>.*</li>',html)
        #开始获得每一个<li>节点中的href和title属性值，分别得到URL和标题
        for a in aList:
            #过滤出URL和标题
            g = re.search('href="([^>"]*)"[\s]*title="([^>"]*)"',a)

            if g !=None:
                #组成一个完整的URL,每一个URL对应一篇小说正文
                url = 'http://doupoxs.com'+g.group(1)
                #得到章节的标题
                title = g.group(2)
                #创建一个对象，用于保存标题和URL
                chapter = {'title':title,'url':url}
                #将该对象添加到方法返回列表中
                result.append(chapter)

    return result

#根据章节目录，抓取目录对应的URL指定小说正文页面
def getChapterContent(chapters):
    for chapter in chapters:
        #定义Request对象，用于指定请求头
        req  = request.Request(url=chapter['url'],headers=headers,method='GET')
        #发送请求
        response = request.urlopen(req)
        if response.status == 200:
            #打开novel目录下的本地文件，以标题命名，扩展名是txt
            if "?" in chapter['title']:
                f = open('正则表达式/fullnovel/novel/'+chapter['title'].replace("?","？")+'.txt','a+')
            else:
                f = open('正则表达式/fullnovel/novel/'+chapter['title']+'.txt','a+')
            #将夹在<p>节点中的文本提取出来
            contents = re.findall('<p>(.*?)</p>',response.read().decode('utf-8'))
            for content in contents:
                f.write(content+'\n')
            f.close()
            print(chapter['title'],chapter['url'])

# print(getCatelogs("http://www.doupoxs.com/nalanwudi"))
getChapterContent(getCatelogs("http://www.doupoxs.com/nalanwudi"))