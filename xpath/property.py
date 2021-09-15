from lxml import etree

parser = etree.HTMLParser()
html = etree.parse("xpath/demo.html",parser)

nodes =  html.xpath("//a[@href='http://geekori.com']")
for node in nodes:
    print(node.text)

nodes = html.xpath("//a[contains(@href,'www')]")
for node in nodes:
    print(node.text)