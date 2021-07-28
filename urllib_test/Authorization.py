from urllib import request
import base64

url = 'http://localhost:5000/'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Host' : 'localhost:5000',
    'Authorization':'Basic ' +
                    str(base64.b64encode(bytes('bill:1222234','utf-8')),'utf-8')
}
req = request.Request(url=url,headers=headers,method="GET")
response = request.urlopen(req)
print(response.read().decode('utf-8'))