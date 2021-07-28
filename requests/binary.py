import requests
#抓取图片文件
r = requests.get('https://img2.baidu.com/it/u=2220420611,1081221264&fm=26&fmt=auto&gp=0.jpg')
print(r.content)
# 将图片保存到本地
with open('requests/text.png','wb') as f:
    f.write(r.content) 