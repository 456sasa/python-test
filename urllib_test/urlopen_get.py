import urllib.request

url = "https://www.baidu.com"
response = urllib.request.urlopen(url)

print('tyoe','sdada',type(response))
# print(response.read().decode('utf-8'))
