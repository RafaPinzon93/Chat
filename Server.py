import xmlrpclib
import datetime
from SimpleXMLRPCServer import SimpleXMLRPCServer

Nombre = None
Passw = None
lastConn = None

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
    
def bye(x):
	return "Chao %s"%x
	
def ingresar(x):
	if x[0] == Nombre and Nombre:
		if x[1] == Passw and Passw:
			server.register_function(add, 'add')
			server.register_function(subtract, 'subtract')
			server.register_function(multiply, 'multiply')
			server.register_function(divide, 'divide')
			return True
		else:
			return False
	else:
		return False
def registro(x):
	global Nombre, Passw
	Nombre = x[0]
	Passw = x[1]
	return "Ahora puede ingresar %s al servidor" %x[0]
	

def hello(x):
	return "Bienvenido %s\n"%x


server = SimpleXMLRPCServer(("192.168.9.76", 8000))
#server = SimpleXMLRPCServer(("localhost", 8000))
print "Listening on port 8000..."

server.register_multicall_functions() # Just send a single request for multiple calls
#server.register_function(add, 'add')
#server.register_function(subtract, 'subtract')
#server.register_function(multiply, 'multiply')
#server.register_function(divide, 'divide')
server.register_function(bye, 'bye')
server.register_function(hello, 'hello')
server.register_function(ingresar, 'ingresar')
server.register_function(registro, 'registro')


server.register_function(is_even, "is_even")
server.register_function(today, "today")
server.register_function(serverInfo, "serverInfo")
server.serve_forever()
