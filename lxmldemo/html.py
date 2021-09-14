from lxml import etree

#创建lxml.etree.HTMLParser对象
parser = etree.HTMLParser()
print(type(parser))
#读取并解析html文件
tree = etree.parse('lxmldemo/test.html',parser)
print(tree)
#获取根节点
root = tree.getroot()
#将html转化为可读格式
result = etree.tostring(root,encoding='utf-8',pretty_print=True,method='html')
print(str(result,'utf-8'))
print(root.tag)
print('lang: ',root.get('lang'))
print('charset= ',root[0][0].get('charset'))
print('charset= ',root[0][1].text)