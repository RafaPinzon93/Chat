import datetime
from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib
from threading import Thread
import thread
import time

# Nombre = None
# Passw = None
lastConn = None
Contador = -1
nombres = {}

usuarios = []


server = SimpleXMLRPCServer(("localhost", 8000))


class User:

    def __init__(self, user_name, password):
        """

        :param user_name: Este sera el nombre del usuario  al cual se le creara una instancia
        :param password:
        :return:
        """
        self.user_name = user_name
        self.password = password
        self.new_messages_bool = False
        self.chats = {
            '#public': []
        }  # Este diccionario cumplira de una forma MUY SIMPLE COMO UNa tabla hash donde se alojaran las
        # conversaciones del usuario en una especie de pila
        self.users_objects = {

        }  # La idea es que el usuario pueda tener una relacion directa con los usuario con los cuales este se encuentre
        #  chateando para de esta forma enviar mensajes en su propia variable chat.
        self.hilo = None

    def get_username(self):
        return self.user_name

    def send_message(self, message, to_username):
        """
        Principalmente se busca, que atraves del diccionario de usuarios con el que un usuario se encuentre chateando
        este pueda usar su intancia usuario para actualizar sus diccionarios de chats y de esta forma que tenga los
        mensajes correctamente enviados.
        Este funcion se diferencia con la funcion de post_message ya que esta ultima es usada para poner un mensaje
        dentro de los valores del usuario, esta funcion de hecho es usada por send_message para postear un mensaje al
        usuario en cuestion.
        :param message: mensaje que va  a ser enviado
        :param to_username: nombre del usuario al cual se planea enviar el mensaje
        :return: retorna un valor de verdad si el mensaje es enviado con exito
        """
        if to_username in self.users_objects.keys():
            return self.users_objects[to_username].post_message(message, self.user_name)
        else:
            return False

    def post_message(self, message, from_username):
        """
        Esta funcion se utiliza para postear un mensaje proveniente de un usuario al cual podemos saber q
        :param from_username: un string que me dice cual es el usuario del que proviene el mensaje.
        :return:
        """
        chats = self.chats
        if from_username in chats.keys():
            chats[from_username].append(message)
        else:
            chats[from_username] = [message]

    def get_messages(self, username):
        """

        :return: diccionario: se devolvera el diccionario con todos lo mensajes de llegada de un usuario y se limpiara
        """
        chats = self.chats
        if username in chats.keys():
            messages = chats[username]
            chats[username] = []
            return messages
        else:
            return []

    def get_all_messages(self):
        """

        :return: diccionario: se devolvera el diccionario con todos lo mensajes de llegada y  de esta forma se limpiaran
                 los mensajes.
        """
        return self.chats

    def __str__(self):
        return str(self.user_name)

    def stop(self):
        self.hilo.stop()

    def test_function(self):
        """
        Esta funcion se diseno con el fin de probar si se puede ejecutar un funcion de forma remota, siendo
        independientes del usuario
        :return: None
        """
        print("Esto es una prueba y se esta comprobando que sean diferentes usuarios, el usuario que ejecuto"
              "la funcion fue = "+self.user_name)

    def crear_hilo(self):
        if not self.hilo:
            self.hilo = UserProcess(self)
            self.hilo.start()


class UserProcess(Thread):

    def __init__(self, user_object):
        Thread.__init__(self)
        self.runBool = False 
        self.user = user_object

    def run(self):
        self.runBool = True
        while self.runBool:
            usernames = nombres.keys()
            if len(usernames) != self.user.users_objects.keys():
                for key in nombres:
                    self.user.users_objects[key] = usuarios[nombres[key]]
            time.sleep(0.9)

    def stop(self):
        self.runBool = False


def cont():
    global Contador
    Contador += 1
    return Contador


def is_even(n):
    return n % 2 == 0


def today():
    today = datetime.datetime.today()
    return xmlrpclib.DateTime(today)


def server_info():
    return server.server_address

    
def bye(x):
    usuarios[nombres[x]].stop()
    return "Chao %s"%x


def ingresar(x):
    """

    :param x:
    :return:
    """
    if x[0] in nombres and nombres:
        if x[1] == usuarios[nombres[x[0]]].password:
            usuario = usuarios[nombres[x[0]]]
            usuario.crear_hilo()
            return True

        else:
            return False
    else:
        return False


def registro(x):
    """

    :param x:
    :return:
    """
    global nombres
    Nombre = x[0]
    Passw = x[1]
    nombres[Nombre] = cont()
    user = User(Nombre, Passw)
    usuarios.append(user)
    return "Ahora puede ingresar %s al servidor" % x[0]


def send_message(from_username, to_username, message):
    """
    Este metodo se encargar de crear el protocolo de envio de mensajes con la libreria xmrpc
    :param from_username:
    :param to_username:
    :param message:
    :return:
    """

    def funcion():
        """
        :return:
        """
        usuario_object = None
        if to_username == '#publico':
            for usuario in usuarios:
                usuario.post_message(message, from_username)
        else:
            if from_username in nombres.keys():
                user_position = nombres[from_username]
                usuario_object = usuarios[user_position]

            if usuario_object:
                usuario_object.send_message(message=message, to_username=to_username)
        return "success"
    thread.start_new_thread(funcion, ())
    return True

def get_new_message(from_username, other_username):
    """

    :param from_username:
    :param other_username:
    :return:
    """
    usuario_object = None
    if from_username in nombres.keys():
        user_position = nombres[from_username]
        usuario_object = usuarios[user_position]

    if usuario_object:
        return usuario_object.get_messages(other_username)
    else:
        return []


def get_all_new_messages(from_username):
    """

    :param from_usernmae:
    :return:
    """
    usuario_object = None
    if from_username in nombres.keys():
        user_position = nombres[from_username]
        usuario_object = usuarios[user_position]

    if usuario_object:
        return usuario_object.get_all_messages()
    else:
        return {}


def get_all_usernames():
    """

    :return:
    """
    return nombres.keys()


def hello(x):
    """

    :param x:
    :return:
    """
    return "Bienvenido %s\n" % x


# server = SimpleXMLRPCServer(("192.168.100.5", 8000))
print "Listening on port 8000..."

server.register_multicall_functions()  # Just send a single request for multiple calls
server.register_function(bye, 'bye')
server.register_function(hello, 'hello')
server.register_function(ingresar, 'ingresar')
server.register_function(registro, 'registro')
server.register_function(get_all_new_messages, 'get_all_new_messages')
server.register_function(get_all_usernames, 'get_all_usernames')
server.register_function(get_new_message, 'get_new_message')
server.register_function(send_message, 'send_message')


server.register_function(is_even, "is_even")
server.register_function(today, "today")
server.register_function(server_info, "serverInfo")

server.serve_forever()
