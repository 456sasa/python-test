# 设置请求的超时时间
import socket
import urllib.request
import urllib.error

try:
	response = urllib.request.urlopen('http://www.xxxx.com',timeout=0.01)
except urllib.error.URLError as e:
	if isinstance(e.reason,socket.timeout):
		print('Time Out')