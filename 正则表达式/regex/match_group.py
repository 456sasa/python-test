import re
m = re.match('hello','hello') #进行文本模式匹配，匹配成功
if m is not None:
    print(m.group())
print(m.__class__.__name__)

m = re.match('hello','world')
if m is not None:
    print(m.group())

print(m)
m = re.match('hello','hello world')
if m is not None:
    print(m.group())

print(m)