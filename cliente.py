__author__ = 'noescobar'

import xmlrpclib
import os

clear = lambda: os.system('clear')

proxy = xmlrpclib.ServerProxy("http://192.168.100.5:8000/")

result = proxy.serverInfo()

print("Bienvenido al cliente\n\n")

#  nombre = raw_input("Ingrese su nombre : ")

#  print(proxy.hello(nombre))

while True:
    print proxy.retornarMensajes
    print("1. Registrarse")
    print("2. Ingresar")
    option = input('ingrese la opcion a elegir: ')

    if(option == 1 ):
        clear()
        nombre = raw_input("Ingrese su nombre : ")
        while(True):
            password = raw_input("Ingrese su password : ")
            confPass = raw_input("Confirme su password : ")
            if(password == confPass):
                break
        userInfo = [nombre,password]
        print(str(proxy.registro(userInfo)))
        print("\n\n")
    elif(option == 2 ):
        clear()
        nombre = raw_input("Ingrese su nombre : ")
        password = raw_input("Ingrese su password : ")
        userInfo = [nombre,password]
        ingresado = proxy.ingresar(userInfo)
        print("\n\n")
        print(ingresado)
        if(ingresado):
            print("1. sumar dos numeros")
            print("2. Restar dos numeros")
            print("3. multiplicar dos numeros")
            print("4. Dividir dos numeros")
            print("5. Todas las operaciones anteriores")
            print("6. Direccion ip y puerto del servidor")
            print("7. Mandar mensaje")
            print("8. Salir")
            option = input('ingrese la opcion a elegir: ')
            if(option == 1 ):
                clear()
                a = input("primer numero: ")
                b = input("segundo numero: ")
                print("\n\n")
                print(str(a)+"+"+str(b)+" = "+str(proxy.add(a,b)))
                print("\n\n")
            elif(option == 2):
                clear()
                a = input("primer numero: ")
                b = input("segundo numero: ")
                print("\n\n")
                print(str(a)+"-"+str(b)+" = "+str(proxy.subtract(a,b)))
                print("\n\n")
            elif(option == 3 ):
                clear()
                a = input("primer numero: ")
                b = input("segundo numero: ")
                print("\n\n")
                print(str(a)+"*"+str(b)+" = "+str(proxy.multiply(a,b)))
                print("\n\n")
            elif(option == 4 ):
                clear()
                a = input("primer numero: ")
                b = input("segundo numero: ")
                print("\n\n")
                print(str(a)+"/"+str(b)+" = "+str(proxy.divide(a,b)))
                print("\n\n")
            elif(option == 5 ):
                clear()
                a = input("primer numero: ")
                b = input("segundo numero: ")
                multicall = xmlrpclib.MultiCall(proxy)
                multicall.add(7,3)
                multicall.subtract(7,3)
                multicall.multiply(7,3)
                multicall.divide(7,3)
                result = multicall()
                results = tuple(result)
                print("\n\n")
                print(str(a)+"+"+str(b)+" = "+str(results[0]))
                print(str(a)+"-"+str(b)+" = "+str(results[1]))
                print(str(a)+"*"+str(b)+" = "+str(results[2]))
                print(str(a)+"/"+str(b)+" = "+str(results[3]))
                print("\n\n")
            elif(option == 6 ):
                clear()
                print(proxy.serverInfo())
                print("\n\n")
            elif(option == 7):
                print "ingrese el mensaje"
                a = input()
                proxy.escribir(a, nombre)
            elif(option == 8 ):
                print(proxy.bye(nombre))
                break
		



