# LISTAS 

# 1.Haz un programa que lea una lista dado su tamaño e imprima el segundo elemento (si existe).
'''
largo = int(input("Dime la longitud :"))

lista_1 = []

while largo > len(lista_1):
    dato_lista = input("Dime un dato para la lista :")
    lista_1.append(dato_lista)

print(f"El tamaño de la lista es de {largo} y el segundo elemento es {lista_1[1]}")
'''


# 2.Haz un programa que lea una secuencia no vacía de enteros acabada en -1, y que escriba cuántos son iguales al último.
'''
lista_enteros = []
numero_entero = 1
print("PARA TERMINAR LISTA PONGA 00")
numero_entero = int(input("Dime un numero entero para la lista :"))

while numero_entero != 00:
    lista_enteros.append(numero_entero)
    numero_entero = int(input("Dime un numero entero para la lista :"))

print(lista_enteros)
lista_enteros.reverse()
ultimo_numero = lista_enteros[0]
print(f"Al ultimo numero son iguales {lista_enteros.count(ultimo_numero)}")
'''


# 3.Haz un programa que lea secuencias de enteros acabada en -1, y que escriba cada una invirtiendo la orden de sus elementos.
'''
lista_enteros_1 = []
numero_entero_1 = 1
print("PARA TERMINAR LISTA PONGA 00")
numero_entero_1 = int(input("Dime un numero entero para la lista :"))

while numero_entero_1 != 00:
    lista_enteros_1.append(numero_entero_1)
    numero_entero_1 = int(input("Dime un numero entero para la lista :"))

lista_enteros_1.reverse()

print(lista_enteros_1)
'''


# 4.Haz un programa que lea n palabras, y que escriba cada una invirtiendo la orden de sus caracteres.
'''
numero_palabras = int(input("Dime el nuemro de palabras a escribir: "))
lista_inversa = []

for palabra in range(0, numero_palabras):
    palabras = input("Dime una palabra: ")
    reversa = palabras [::-1] # Este corchete [::-1] se usa para invertir los strings.
    lista_inversa.append(reversa)

print (lista_inversa)
'''


# 5.Haz un programa que lea una secuencia de números mientras sean positivos y que escriba la media.
'''
numeros_varios = int(input("Dime un numero: "))
lista_positi = []
suma_lista = 0

while numeros_varios > 0 :
    lista_positi.append(numeros_varios)
    numeros_varios = input("Dime un numero: ")
for numero in lista_positi:
    suma_lista += int(numero)

media_numeros = suma_lista / (len(lista_positi))

print(f"La media seria de {media_numeros}")
'''


# 6.Haz un programa que devuelva la concatenación de v1 y v2, v1 y v2 son dos listas de tamaño n y m.
#   Es decir, hay que devolver un vector que tenga los elementos de v1 seguidos de los elementos de v2.
'''
n = int(input('Dime la longitud de la primera lista: '))
m = int(input('Dime la longitud de la segunda lista: '))
lista_v1 = []
lista_v2 = []

for letra in range(0,n):
    letra_v1 = input("Dime una letra: ")
    lista_v1.append(letra_v1)
for letra in range(0,m):
    letra_v2 = input("Dime una letra: ")
    lista_v2.append(letra_v2)

print(lista_v1 + lista_v2)
'''


# 7.Haz un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
'''
lista_precios = [50, 75, 46, 22, 80, 65, 8]
menor_numero = lista_precios[0]
mayor_numero = lista_precios[0]

for numero in (lista_precios):
    if menor_numero > numero:
        menor_numero = numero
for numero in (lista_precios):
    if mayor_numero < numero:
        mayor_numero = numero

print(f"El mayor numero es {mayor_numero} y el menor numero es {menor_numero}")
'''


# 8.Haz un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
'''
lista_asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']

for palabra in lista_asignaturas:
    print(palabra)
'''


# 9.Haz un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
'''
lista_numeross = []
numeros_separados= ''

for numero in range (1,11):
    lista_numeross.append(numero)
for numeros in lista_numeross[::-1]:
    if numeros == 10:
        numeros_separados = "10"
    else:
        numeros_separados += (f', {numeros}')
print(numeros_separados)
'''


# 10.Haz un programa que concatene dos listas del mismo tamaño n alternando elementos de una lista y otra.
'''
n = int(input('Dime la longitud de las listas: '))
lista_v1_1 = []
lista_v2_2 = []
lista_v12_12 = []

for letra in range(0,n):
    letra_v1_1 = input("Dime una letra: ")
    lista_v1_1.append(letra_v1_1)
for letra in range(0,n):
    letra_v2_2 = input("Dime una letra: ")
    lista_v2_2.append(letra_v2_2)

for numero in range(0,n):
    lista_v12_12.append(lista_v1_1[numero])
    lista_v12_12.append(lista_v2_2[numero])
    
print(lista_v12_12)

'''

# 11.Haz un programa que itere ambas listas de tamaños n y m (siendo n y m números distintos )simultáneamente e imprima sus elementos.
'''
longi_1 = int(input('Dime la longitud de la primera lista: '))
longi_2 = int(input('Dime la longitud de la segunda lista: '))
lista_v1_3 = []
lista_v2_4 = []

for letra in range(0,longi_1):
    letra_v1_3 = input("Dime una letra: ")
    lista_v1_3.append(letra_v1_3)
for letra in range(0,longi_2):
    letra_v2_4 = input("Dime una letra: ")
    lista_v2_4.append(letra_v2_4)

for letras in (lista_v1_3 + lista_v2_4):
    print(letras)

'''

# 12.Haz un programa que añada un nuevo elemento 60 a la lista [10, 50, 40, 20, 30] después de un elemento especificado por el usuario.
#    Si el elemento introducido no está presente en la lista debe mostrar el mensaje: 'Elemento no presente en la lista'.
'''
lista_grandes = [10, 50, 40, 20, 30]
numero_especifi = int(input('Dime un elemento presente en la lista: '))
numero_unir = 60

if numero_especifi in lista_grandes:
    posicion = lista_grandes.index(numero_especifi)# Con el comando .index leemos la posicion del elemento en la lista 
    lista_grandes.insert(posicion+1,numero_unir)
    print(lista_grandes)
else:
    print('Elemento no esta presente en esta lista')
'''


# 13.Haz un programa que elimine todas las apariciones de un elemento específico introducido por el usuario de la lista [10, 50, 40, 20, 60, 30].
'''
lista_grandes_2 = [10, 50, 40, 20, 60, 30]
numero_elimi = int(input('Dime un elemento a eliminar de la lista: '))

while numero_elimi in lista_grandes_2:
    lista_grandes_2.remove(numero_elimi)
print(lista_grandes_2)

'''

# TUPLAS



# 1.Haz una programa que invierta una tupla.
'''
tupla_1 = (10, 20, 30, 40, 50)

tupla_1 = tupla_1[::-1]

print(tupla_1)
'''


# 2.Haz un programa que acceda al valor 15 de la tupla.
'''
tupla_2 = ("Naranja", [10, 20, 30], (5, 15, 25))

print(tupla_2[2][1])
'''


# 3.Haz un programa que declare una tupla con un solo elemento 10.
'''
tupla_3 =  (10, )

print(tupla_3)
'''


# 4.Haz un programa que descomponga la tupla en 4 variables.
'''
tupla_4 = (10, 20, 30, 40)

a = tupla_4[0]
b = tupla_4[1]
c = tupla_4[2]
d = tupla_4[3]

# a, b, c, d = tupla_4 # Opcion muy interesante del ejercicio resuelto 

print(a)
print(b)
print(c)
print(d)

'''

# 5.Haz un programa que intercambie dos tuplas en Python.
'''
tup1 = (1, 2)
tup2 = (3, 4)

tup1, tup2 = tup2, tup1

print(tup1)
print(tup2)
'''


# 6.Haz un programa que copie elementos específicos de una tupla a una nueva tupla.
'''
tupla_5 = (11, 22, 33, 44, 55, 66)
tupla_6 = tupla_5[3],tupla_5[4]

print(tupla_6)

'''

# 7.Haz un programa que modifique una tupla.
'''
tupla_7 = (11, [22, 33], 44, 55)
tupla_7[1][0] = 222

print(tupla_7)
'''


# 8.Ordena una tupla de tuplas por el 2º elemento. (EJERCICIO MUY IMPORTANTE )
'''
tupla_8 = (('a', 23),('b', 37),('c', 11), ('d',29))

tupla_8 = list(tupla_8)
tupla_8 = tuple(sorted(list(tupla_8), key=lambda x: x[1])) # Usamos el sorted para crear una nueva variable ordenada y el key para indicar el valor a ordenar 
tupla_8 = tuple(tupla_8)

print(tupla_8)
'''


# 9.Haz un programa que cuente el número de apariciones del elemento 50 de una tupla.
'''
tupla_9 = (50, 10, 60, 70, 50)

print(tupla_9.count(50))
'''


# 10.Haz un programa que compruebe si todos los elementos de la tupla son iguales.
'''
tupla_10 = (45, 45, 45, 45)

for numero in tupla_10:
    if tupla_10[0] != numero:
        print("No todos los elementos son iguales")
        break
else:
    print("Todos los elementos son iguales ")

'''