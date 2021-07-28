from flask import Flask, app
import urllib.request

from werkzeug.wrappers import response

app = Flask(__name__)

@app.route('/readCookie')
def readCookie():
    # print(urllib.request.cookies)
    # print(urllib.request.cookies.get('MyCookie'))
    return "hello world"



@app.route("/writeCookie")
def writeCookie():
    response = app.make_response('write cookie')
    response.set_cookie("id",value="12345678")
    return response

if __name__ == "__main__":
    app.run()