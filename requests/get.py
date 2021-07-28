import requests

data = {
    'name' : 'Bill',
    'country' : 'China',
    'age' : '20'
}

r =requests.get('http://httpbin.org/get?name=Mike&country=美国&age=40',params=data)
print(r.text)
print(r.json())
print(r.json()['args']['country'])