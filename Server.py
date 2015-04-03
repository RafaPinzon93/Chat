import xmlrpclib
import datetime
from SimpleXMLRPCServer import SimpleXMLRPCServer


def is_even(n):
    return n%2 == 0


def today():
    today = datetime.datetime.today()
    return xmlrpclib.DateTime(today)


def serverInfo():
    return server.server_address


def add(x,y):
    return x+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):
    return x/y

# server = SimpleXMLRPCServer(("192.168.100.2", 8000))
server = SimpleXMLRPCServer(("localhost", 8000))
print "Listening on port 8000..."

server.register_multicall_functions() # Just send a single request for multiple calls
server.register_function(add, 'add')
server.register_function(subtract, 'subtract')
server.register_function(multiply, 'multiply')
server.register_function(divide, 'divide')


server.register_function(is_even, "is_even")
server.register_function(today, "today")
server.register_function(serverInfo, "serverInfo")
server.serve_forever()
