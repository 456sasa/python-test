import requests
from urllib.parse import quote,unquote

headers = {
     'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'name' : quote('李宁')
}

r = requests.get('http://httpbin.org/get',headers=headers)
print(r.text)
print('Name: ',unquote(r.json()['headers']['Name']))