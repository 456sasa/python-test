from lxml import etree

parser = etree.HTMLParser()
html =  etree.parse("xpath/demo.html",parser)

aList = html.xpath("//a[@href='http://www.jd.com' or @href='http://www.google.com']")
for a in aList:
    print(a.text)

aList = html.xpath("//a[contains(@href,'www') and ../@value='1234']")
for a in aList:
    print(a.text,a.get("href"))