from twisted.internet import protocol,reactor
from time import ctime
port = 9876
class MyProtocol(protocol.Protocol):
    #当客户端连接到服务器后，调用该方法
    def connectionMade(self):
        #获取客户端的IP
        client = self.transport.getPeer().host
        print('客户端',client,'已经连接')
    def dataReceived(self, data):
        print(ctime().encode(encoding='utf_8')+data)
        #接收到客户端发送过来的数据后，向客户端返回服务器的数据
        self.transport.write(ctime().encode(encoding='utf_8')+data)
#创建Factory对象
factory = protocol.Factory()
factory.protocol = MyProtocol
print('正在等待客户端连接')
#监听端口号，等待客户端的请求
reactor.listenTCP(port,factory)
reactor.run()
