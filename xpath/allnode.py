from lxml import etree

parser = etree.HTMLParser()
html = etree.parse('xpath/demo.html',parser)
#选取demo.html文件中的所有节点
nodes = html.xpath("//*")
print('共',len(nodes),'个节点')
print(nodes)

#输出所有节点节点名
for node in nodes:
   print(node.tag,end=' ')

#按层次输出节点，indent时缩进
def printNodeTree(node,indent):
    print(indent + node.tag)
    indent +="  "
    children = node.getchildren()
    if (len(children)>0):
        for child in children:
            printNodeTree(child,indent)
#按层次输出节点的节点
printNodeTree(nodes[0],"")

alist = html.xpath("//a")

print(len(alist))
for a in alist:
    print(a.text)