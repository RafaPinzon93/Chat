__author__ = 'noescobar'

import xmlrpclib
import os
from threading import Thread
import time
import platform

if platform.system() != 'Windows':
    clear = lambda: os.system('clear')
else:
    clear = lambda: os.system('cls')


# proxy = xmlrpclib.ServerProxy("http://192.168.100.5:8000/")
proxy = xmlrpclib.ServerProxy("http://localhost:8000/")

result = proxy.serverInfo()


class UserClient:
    def __init__(self, username, proxy_instance):
        self.username = username
        self.current_username_chat = None
        self.current_chat_messages = None
        self.general_messages = {}
        self.new_messages = False
        self.usernames = []
        self.hilos = []
        self.proxy = proxy_instance

    def get_messages(self):
        """

        :return:
        """
        if self.current_username_chat:
            from_username = self.username
            other_username = self.current_username_chat
            self.current_chat_messages = self.proxy.get_new_message(from_username, other_username)

    def get_all_messages(self):
        self.general_messages = self.proxy.get_all_new_messages(self.username)

    def run_client_process(self):
        for hilo in self.hilos:
            hilo.run()

    def stop_client_process(self):
        for hilo in self.hilos:
            hilo.stop()

    def get_current_chat(self):
        return self.current_username_chat


class UserProcessNotificator(Thread):
    def __init__(self, user_client_object):
        Thread.__init__(self)
        self.runBool = False
        self.user_object = user_client_object

    def run(self):
        self.runBool = True
        while self.runBool:
            if self.user_object.current_username_chat:
                if self.user_object.current_chat_messages:
                    chat_username = self.user_object.current_username_chat
                    messages = self.user_object.current_chat_messages
                    for message in messages:
                        print(chat_username+" : " + message)
            if self.user_object.new_messages:
                print('Alguien te esta escribiendo')
            time.sleep(1)

    def stop(self):
        self.runBool = False

class UserProcessInspection(Thread):

    def __init__(self, user_client_object):
        """

        :param user_client_object:
        :return:
        """
        Thread.__init__(self)
        self.runBool = False
        self.user_object = user_client_object

    def run(self):
        self.runBool = True
        while self.runBool:
            self.user_object.usernames = proxy.get_all_usernames()
            self.user_object.get_messages()
            self.user_object.get_all_messages()
            time.sleep(1)

    def stop(self):
        self.runBool = False


print("Bienvenido al cliente\n\n")

while True:
    print("1. Registrarse")
    print("2. Ingresar")
    print("3. Salir")
    option = input('ingrese la opcion a elegir: ')

    if option == 1:
        clear()
        nombre = raw_input("Ingrese su nombre : ")
        password = None
        while True:
            password = raw_input("Ingrese su password : ")
            confPass = raw_input("Confirme su password : ")
            if password == confPass:
                break
        userInfo = [nombre, password]
        print(str(proxy.registro(userInfo)))
        print("\n\n")
    elif option == 2:
        clear()
        nombre = raw_input("Ingrese su nombre : ")
        password = raw_input("Ingrese su password : ")
        userInfo = [nombre, password]
        ingresado = proxy.ingresar(userInfo)
        print("\n\n")
        print(ingresado)
        if ingresado:
            user_object = UserClient(nombre)
            while True:
                print("1. Chat publico")
                print("2. Chat privado")
                print("3. Salir")
                option = input('ingrese la opcion a elegir: ')
                if option == 1:
                    clear()
                    print("\n\n")
                elif option == 2:
                    clear()
                    a = input("primer numero: ")
                    b = input("segundo numero: ")
                    print("\n\n")
                    print(str(a) + "-" + str(b) + " = " + str(proxy.subtract(a, b)))
                    print("\n\n")
                elif option == 3:
                    print(proxy.bye(nombre))
                    break
    elif option == 3:
        print('Adios')
        break
