from lxml import etree
parser = etree.HTMLParser()
tree = etree.parse('xpath/test.html',parser)
#使用XPath定位title节点，返回一个节点集合
titles = tree.xpath('/html/head/title')
if len(titles) > 0:
    print('title: ',titles[0].text)

html ='''
<div>
   <ul>
      <li class='item1'><a href='http://geekori.com'>geekori.com</a></li>
      <li class='item2'><a href='http://www.jd.com'>京东</a></li>
      <li class='item3'><a href='http://www.taobao.com'>淘宝</a></li>
   </ul>
</div>
'''
#分析HTML代码
tree = etree.HTML(html)
#使用XPath定位class属性值为item2的<li>节点
aTags = tree.xpath("//li[@class='item2']")

if len(aTags) > 0:
    print(aTags[0][0].get('href'),aTags[0][0].text)