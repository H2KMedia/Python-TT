#condicional simpre
print("CONDICIONAL SIMPLE")
print()
#si edad > 18 entonces
#   escribir "mayor de edad"
#finsi
edad = int(input("ingrese su edad: "))
if edad >= 18:
    print("mayor de edad")
print("fin del programa")

#condicional doble
print()
print("CONDICIONAL DOBLE")
print()
# si edad es <= 18 entonces
#   instrucciones por verdadero
# sino
#   instrucciones por falso

if edad >= 18:
    print("MAYOR DE EDAD")
else:
    print("MENOR DE EDAD")

#anidamiento condicionales
print()
print("ANIDAMIENTO CONDICIONALES")
print()
NAME = "admin"
PASSWORD = "1234"

user_name = input("INGRESE SU USUARIO:")
print()
if user_name == NAME:
    user_pwd = input("INGRESE SU CONTRASEÑA:")
    if user_pwd == PASSWORD:
        print("LOGIN EXITOSO!")
    else:
        print("CONTRASEÑA INCORRECTA")
else:
    print("USUARIO INCORRECTO")
print()
print("FIN DEL PROGRAMA")

#por cuestiones de seguridad se hace la siguiente acción
NAME = "admin"
PASSWORD = "1234"

user_name = input("INGRESE SU USUARIO:")
print()
user_pwd = input("INGRESE SU CONTRASEÑA:")
print()
if user_name == NAME and user_pwd == PASSWORD:
    print("LOGIN EXITOSO")
    print("BIENVENIDO AL SISTEMA")
else:
    print("NOMBRE O CLAVE INCORRECTO")

# aritmeticos y algebraicos
#
#  relaciones


#prioridad en operadores logicos
# ()
# not
#  and
#   or   

#condicional multiple