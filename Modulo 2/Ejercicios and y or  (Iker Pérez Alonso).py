#CONIDCIONALES CON AND Y OR

#1.	Par o Impar y Positivo o Negativo: Pide al usuario que ingrese un número. Imprime si el número es par e positivo, par e negativo, impar y positivo, o impar y negativo.

num1 = int(input("dime un numero"))

if num1 < 0:
    print(f"{num1} es un numero negativo" )
else:
    print(f"{num1} es un numero positivo")
if num1 % 2 == 0:
    print(f"{num1} es un numero par")
else:
    print(f"{num1} es un numero impar")



#2.	Rango de Números: Solicita al usuario que ingrese un número. Verifica si el número está en el rango de 10 a 50 (inclusive) o si es menor que 0.

num2 = int(input("dime un numero"))

if num2 <= 50 and num2 >= 10:
    print(f"{num2} esta dentro del rango 10 a 50 ")

else:
    if num2 < 0:
        print(f"{num2} es menor que 0 ")
    else:
        print(f"{num2} no esta ni dentro del rango ni es menor que 0")



#3.	Nombre de Usuario y Contraseña: Crea un programa que solicite al usuario ingresar un nombre de usuario y una contraseña. Imprime un mensaje si ambos son correctos.

usuario = "usuario"
contraseña = "contraseña"
usuario1 = str(input("Introduce el usuario"))
contraseña1 = str(input("Introduce la contraseña"))

if usuario == usuario1 and contraseña == contraseña1:
    print("Usuario y contraseña son validos")
else:
    print("El usuario o la contraseña no coinciden con los correspondientes")



