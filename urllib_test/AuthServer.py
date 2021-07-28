from os import name
import re
from flask import Flask
from flask import request
import base64

from werkzeug.wrappers import response



app = Flask(__name__)

#判断客户端是否提交了用户名和密码，如果未提交设置状态码为401，并设置WWW-Authenticate相应头
#auth:Authorization请求头字段的值，response：响应对象
def hasAuth(auth,response):
    if auth == None or auth.strip()=="":
        #设置响应状态码为401
        response.status_code = 401
        #设置相应头中WWW-Authenticate字段，其中localhost是需要验证的范围
        response.headers["WWW-Authenticate"] = 'Basic realm=localhost""'
        #返回false，表示客户端未提交用户和密码
        return False
    return True

#跟路由
@app.route("/")
def index():
    #创建响应对象，并指定为输入用户名和密码（单机“取消”按钮）或输入错误后的返回内容
    response = app.make_response('username or password error')
    #输出所有的http请求头
    print(request.headers)
    #得到Authorization请求头的值
    auth = request.headers.get('Authorization')
    #输出Authorization的值
    print('Authorization',auth)
    #如果客户端提交了用户名和密码，进行验证
    if hasAuth(auth,response):
        #将用户名和密码按Base64编码格式解码，这里按空格拆分成两个值，第一个是Basic，第二个是
        #Base64编码后用户名和密码
        auth = str(base64.b64decode(auth.split(' ')[1]),'utf-8')
        #用户名和密码之间用冒号(:)分隔，所以需要将他们拆开
        values = auth.split(':')
        #获取用户名
        username = values[0]
        #获取密码
        password = values[1]
        print('username',username)
        print('password',password)
        #判断用户名何面目是否正确，如果正确，返回success
        if username=='bill' and password=='1234':
            return "success"
    
    return response

if __name__ == '__main__':
    app.run()