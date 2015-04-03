import xmlrpclib
import datetime
import httplib

# proxy = xmlrpclib.ServerProxy("http://192.168.100.2:8000/", verbose=False)
proxy = xmlrpclib.ServerProxy("http://192.168.100.5:8000/", verbose=False)
print "3 is even: %s" % str(proxy.is_even(3))
# print "100 is even: %s" % str(proxy.is_even(100))
informacionServer = proxy.serverInfo()
print "Ip del servidor: ", informacionServer[0], ", Puerto: ", informacionServer[1]

multicall = xmlrpclib.MultiCall(proxy)
multicall.add(7,3)
multicall.subtract(7,3)
multicall.multiply(7,3)
multicall.divide(7,3)
result = multicall()

print "7+3=%d, 7-3=%d, 7*3=%d, 7/3=%d" % tuple(result)

# today = proxy.today()
# # convert the ISO8601 string to a datetime object
# converted = datetime.datetime.strptime(today.value, "%Y%m%dT%H:%M:%S")
# print "Today: %s" % converted.strftime("%d.%m.%Y, %H:%M")
# print proxy
# try:
#     print proxy.examples.getStateName(41)
# except xmlrpclib.Error as v:
#     print "ERROR", v

# class ProxiedTransport(xmlrpclib.Transport):
#     def set_proxy(self, proxy):
#         self.proxy = proxy
#     def make_connection(self, host):
#         self.realhost = host
#         h = httplib.HTTP(self.proxy)
#         return h
#     def send_request(self, connection, handler, request_body):
#         connection.putrequest("POST", 'http://%s%s' % (self.realhost, handler))
#     def send_host(self, connection, host):
#         connection.putheader('Host', self.realhost)

# p = ProxiedTransport()
# p.set_proxy('proxy-server:8080')
# server = xmlrpclib.Server('http://time.xmlrpc.com/RPC2', transport=p)
# print server.currentTime.getCurrentTime()
