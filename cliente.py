import xmlrpclib
import os

if os.name == 'posix':
    clear = lambda: os.system('clear')
else:
    clear = lambda: os.system('cls')

# proxy = xmlrpclib.ServerProxy("http://192.168.9.32:8000/")
proxy = xmlrpclib.ServerProxy("http://localhost:8000/")

result = proxy.serverInfo()

ingresado = False



#  nombre = raw_input("Ingrese su nombre : ")

#  print(proxy.hello(nombre))

while True:
    clear()
    print("Bienvenido al CHAT\n\n")
    if not ingresado:
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
            ingresado = proxy.ingresar(userInfo)
            # print("\n\n")
        elif(option == 2 ):
            clear()
            nombre = raw_input("Ingrese su nombre : ")
            password = raw_input("Ingrese su password : ")
            userInfo = [nombre,password]
            ingresado = proxy.ingresar(userInfo)
            # print("\n\n")
        # print(ingresado)
    else:
        print str(proxy.retornarMensajes())
        a = raw_input("Ingrese el mensaje (para salir digite \"/salir\"): ")
        if a == "/salir":
            print(proxy.bye(nombre))
            break
        else:
            proxy.escribir(a, nombre)
    
                
		



