import xmlrpclib
import datetime
from SimpleXMLRPCServer import SimpleXMLRPCServer
from threading import Thread
import time

# Nombre = None
# Passw = None
lastConn = None
Contador = -1
Nombres = {}
mensajes = ""

Usuarios= []

class User():
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        self.hilo = None

    def __str__(self):
        return str(self.userName)

    def stop(self):
        self.hilo.stop()

    def crearHilo(self):
        if not self.hilo:
            self.hilo = UserProcess(self.userName)
            self.hilo.start()

class UserProcess(Thread):
    def __init__(self, nombre):
        Thread.__init__(self)
        self.runBool = False
        self.nombre = nombre

    def run(self):
        self.runBool = True
        while self.runBool:
            # print "hola " + str(self.nombre)
            print mensajes
            time.sleep(1)

    def stop(self):
        self.runBool = False

def cont():
    global Contador
    Contador += 1
    return Contador

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
    Usuarios[Nombres[x]].stop()
    return "Chao %s"%x

def ingresar(x):
    if x[0] in Nombres and Nombres:
        if x[1] == Usuarios[Nombres[x[0]]].password:
            server.register_function(add, 'add')
            server.register_function(subtract, 'subtract')
            server.register_function(multiply, 'multiply')
            server.register_function(divide, 'divide')
            Usuarios[Nombres[x[0]]].crearHilo()
            return True

        else:
            return False
    else:
        return False
def registro(x):
    global Nombres
    Nombre = x[0]
    Passw = x[1]
    Nombres[Nombre] = cont()
    user = User(Nombre, Passw)
    Usuarios.append(user)
    return "Ahora puede ingresar %s al servidor" %x[0]


def hello(x):
    return "Bienvenido %s\n"%x

def escribir(mensaje, nombre):
    global mensajes
    mensajes += mensaje + nombre + "\n"

def retornarMensajes():
    return mensajes


server = SimpleXMLRPCServer(("192.168.100.5", 8000))
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
