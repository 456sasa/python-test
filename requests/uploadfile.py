import requests
print(type(open('requests\\text.png','rb')))
#定义要上传的文件，字典中必须包含一个key为file的值，值类型为BufferedReader，可以用open函数返回
files1 = {'file':open('requests/text.png','rb')}
#将本地文件上传到upload_sever.py
r1 = requests.post('http://127.0.0.1:5000/',files=files1)
#输出响应结果
print(r1.text)
files2 = {'file':open('requests/text.png','rb')}
r2 = requests.post('http://127.0.0.1:5000/',files=files2)
print(r2.text)