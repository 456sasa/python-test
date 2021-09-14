from lxml import etree

#读取products.xml文件
tree = etree.parse('lxmldemo/products.xml')
print(type(tree))
#将tree重新转化为字符串形式的XML文档
print(str(etree.tostring(tree,encoding = 'utf-8'),'utf-8'))
#获得根节点对象
root = tree.getroot()
print(type(root))
#输出根节点的名称
print('root:',root.tag)
#获得根节点的所有子节点
children = root.getchildren()
print("----------输出产品信息-----------")
for child in children:
    print('product id = ',child.get('id'))
    print('child[0].name = ',child[0].text)
    print('child[1].name = ',child[1].text)

#分析字符串形式的XML文档
root = etree.fromstring('''
<products>
    <product1 name='iphone'/>
    <product2 name='ipad'/>
</products>
''')
print("----------新产品----------")
#输出根节点的节点名
print('root = ',root.tag)
children = root.getchildren()
for child in children:
    print(child.tag,'name = ',child.get('name')) 