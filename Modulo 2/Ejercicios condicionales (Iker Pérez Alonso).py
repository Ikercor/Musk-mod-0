# 1. Haz un programa que lea dos palabras y que indique el orden lexicográfico. Escribe en una línea indicando si a < b, a > b o a = b. Ejemplo: a = Anna, b = Javier, Anna < Javier.

a = "Anna"
b = "Javier"
if (a == b):
    print(f"{a} igual a {b}")
if (a > b):
    print(f"{a} > {b}")
else:
    print(f"{b} > {a}")



# 2. Haz un programa que lea una letra y que indique por pantalla si es una mayúscula, si es una minúscula, si es una vocal, y si es una consonante.

letra = input("dime una leta")

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print(f"{letra} es una vocal")
else:
    print(f"{letra} es una consonante")

if letra.islower(): # el comando .islower() se utiliza para leer el texto que se le asigne y te revuelve en boolean(true o false) las respuesta de si lo leido es todo minusculas   
    print(f"{letra} es una minuscula")
else:
    print(f"{letra} es una mayuscula") 

#Tambien se podria haber usado el comando .isupper() ya que tiene el mismo funcionamiento que .islower() pero en ver de minusculas el lo hace con las mayusculas                 



# 3. Haz un programa que lea un entero que representa una temperatura en grados Celsius, y que diga si hace calor, si hace frío, o si se está bien. Suponed que hace calor si la temperatura es más alta que 30 grados, que hace frío si es más baja que 10 grados, y que se está bien en otro caso.

temperatura = float(input("Dime una temperatura en grados Celsius")) 

if temperatura >= 30:
    print("hace calor")
elif temperatura < 30 and temperatura >10:
    print("se esta bien")
else:
    print("hace frío") 



# 4. Haz un programa que, dados dos intervalos, calcule el intervalo correspondiente a la intersección o indique que esta es vacía.

inter1_1 = 10
inter1_2 = 20

inter2_1 = 30
inter2_2 = 40

if inter1_2 >= inter2_2 and inter1_1 >= inter2_1 and inter2_2 >= inter1_1:
    inter3_1 = inter2_2
    inter3_2 = inter1_1
    print(f"[{inter3_1} {inter3_2}]")
if inter1_2 <= inter2_2 and inter1_1 <= inter2_1 and inter2_2 <= inter1_1:
    inter3_1 = inter2_2
    inter3_2 = inter1_1
    print(f"[{inter3_1} {inter3_2}]")
else:
    inter3_1 = inter1_2
    inter3_2 = inter2_1
    print(f"[{inter3_1} {inter3_2}]")
   


# 5. Haz un programa que indique si un año es bisiesto o no. Un año bisiesto tiene 366 días. Después de la reforma gregoriana, los años bisiestos son los múltiplos de cuatro que no acaban en dos ceros, y también los acabados en dos ceros tales que el número que queda después de sacar los dos ceros finales es divisible por cuatro. Así, 1800 y 1900, a pesar de ser múltiples de cuatro, no fueran bisiestos; en cambio, 2000 lo fue.

numero = int(input("dime un año"))

if numero % 4 == 0 and (numero % 400 == 0 or numero % 100 != 0):
    print(f"{numero} es un año bisiesto")
else:
    print(f"{numero} no es un año bisiesto")



# 6. Haz un programa que añada un segundo en una hora del día, dadas sus horas, minutos y segundos.

horas = int(input('Dime la hora'))
minuts = int(input('Dime los minutos'))
seguns = int(input('Dime los segundos'))

if seguns + 1 > 59:
    seguns = 0
    minuts = minuts + 1
    if minuts +1 > 59:
        minuts = 0
        horas = horas+1 
        print(f"{horas}h, {minuts}m, {seguns}s")
    else:
        print(f"{horas}h, {minuts}m, {seguns}s")
else:
    seguns =seguns +1
    print(f"{horas}h, {minuts}m, {seguns}s")



# 7. Haz un programa que lea un real x≥0 y que escriba ⌊x⌋ (la parte entera inferior de x), ⌈x⌉ (la parte entera superior de x), y el redondeo de x.

numerodeci= float(input('Dime un número decimal:'))
numeroent = int(numerodeci)

if numerodeci == numeroent:
    print(f"parte entera superior {numerodeci}, parte entera inferior {numerodeci}, redondeo {numerodeci}")
else:
    parte_superior = numeroent + 1
    parte_inferior = numeroent
    redondeo = numerodeci + 0.5 
    print(f"parte entera superior {parte_superior}, parte entera inferior {parte_inferior}, redondeo {int(redondeo)}")
