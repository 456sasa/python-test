import re
from flask import Flask,request
import os
#定义服务端保存上传文件的位置
UPLOAD_FOLDER = 'uploads'
app = Flask(__name__)
#用于接收上传文件的路由需要使用POST方法
@app.route('/',methods=['POST'])
def upload_file():
    #获取上传文件内容
    file = request.files['file']
    if file:
        #将上传文件保存到uploads子目录中
        file.save(os.path.join(UPLOAD_FOLDER, os.path.basename(file.filename)))
        msg = '文件保存在'+os.path.join(UPLOAD_FOLDER, os.path.basename(file.filename))
        return msg
    
if __name__ =='__main__':
    app.run()