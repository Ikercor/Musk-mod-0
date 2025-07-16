# 1. Haz un programa que lea dos números a y b, y que escriba todos los números enteros a y b. Debe cumplirse que a < b. En caso que a > b, escribe los número de manera descendente.
'''
numero_a = int(input("Dime un numero "))
numero_b = int(input("Dime un numero "))

if numero_a > numero_b:
    for numero in range (numero_a,numero_b,-1):
        print(numero)
else:
    for numero in range (numero_b,numero_a,-1):
        print(numero)

'''

# 2. Haz un programa que lea una secuencia de 10 números y que escriba la media.
'''
numero_rango = int(input("Dime un rango"))
suma = 0

for numero in range( numero_rango, 0,-1):
    numero_variable = int(input("Dime un numero ")) 
    suma += numero_variable
    
print(suma / 10 )
'''

# 3. Haz un programa que dada una lista de naturales de tamaño n, indique la posición del primer número par.
'''
n = int(input("Dime un numero para el rango"))
if n > 0:
    for posicion in range(1, n):
        numero = int(input("Dime un numero"))
        if numero % 2 == 0:
            print(f" El {numero} es par y esta en la posicion de {posicion} ")
        break   
'''


# 4. Haz un programa que lea un número n y que escriba la “tabla de multiplicar” de n.
'''
num = int(input("Dime un numero"))

for numero in range(0, 11):
    print(f"{num} * {numero} = {(num)*(numero)}")

'''

# 5. Haz un programa que lea un número y que lo escriba del revés.
'''
numer = int(input("Dime un numero"))
revertir = 0

while numer > 0:
    residuo = numer % 10
    revertir = (revertir * 10) + residuo
    numer //= 10                                         
print(f"El inverso del número ingresado es: {revertir}") # Todas estas operaciones son simples forulas matematicas. 

'''

# 6. Haz un programa que lea un número y que escriba el número de dígitos.
'''
nume = int(input("Dime un numero"))
nume1 = str(nume)
'''
'''
print(f"En el numero {nume}la cantidad de dijitos es {len (nume)}") # En este ejercicio tambien se podria usar el comando "len" ya que se usa precisamente para ler las
                                                                    lonjitudes de "str" listas etc...
'''
'''
digitos = 0

for digi in nume1: # El propio bucle se ejecuta hasta  terminar su str, cadena o lo que le pongamos, entonces al hacerlo sobre una variable nueva creada y por cada vuelta
                    de bucle sumarle 1 tenemos ahi mismo la manera facil de reconocer el numero de caracteres
    digitos += 1
    

print(f"En el numero {nume}la cantidad de dijitos es {digitos}")
'''


# 7. Haz un programa que diga si un natural n es capicua o no.
    # Esta forma es sin bucles
'''
numeroi= int(input("Dime un numero"))
numeroinverso = str(numeroi)
numeroinverso1 = numeroinverso[::-1] # Con este comando/operacion lo que hacemos es invertir el numero 
if numeroinverso1 == numeroinverso:
    print(f"{numeroi} es capicua")
else:
    print(f"{numeroi} no es capicua")
'''  
    # Esta forma es con bucles   
'''
numeroo = int(input("Dime un numero"))
numeroprinci = numeroo 
revertirr = 0

while numeroo > 0:
    residuo = numeroo % 10
    revertirr = (revertirr * 10) + residuo
    numeroo //= 10   

if numeroprinci == revertirr:
    print(f"{numeroprinci} es capicua")
else:
    print(f"{numeroprinci} no es capicua")
'''


# 8. Haz un programa que dada una secuencia de años acabada en 0 nos diga cuántos hay del siglo 20.
'''
años = int(input('Dime un año'))
    
numero_años = 0
while años != 0:
    n1 = años // 100
    
    if n1 + 1 == 20:
        numero_años += 1
    años = int(input('Dime otro año, si ya quieres acabar pon 0:'))
    
print(f'Hay {numer_oaños} años que perteneccan al siglo XX')
'''    


# 9. Haz un programa que reciba una secuencia de naturales de tamaño n y nos devuelva cuál es el primer natural que tiene un valor inferior al primer natural leído.
'''
n1 = int(input('Dime el tamaño de la secuencia a leer: '))
primer_num = -1

for numeros in range(0, n1):
    numero = int(input('Dime un número: '))
    if numeros == 0: # Al indicar que numeros = 0 estamos especificando que va a ser el primer numero que digamos y nos lo guarda  
        primer_num = numero
    elif numero < primer_num:
        print(f'El primer natural inferior a {primer_num} es {numero}')
        
        break # Y aqui como ya hemos terminado rompemos el bucle para que no se siga ejecutando
    '''



# 10. Haz un programa que cuente cuántos valores hay en una secuencia de enteros acabada en 0.
'''
numer_1 = int(input('Dime un número: '))
n_de_valores = 0

while numer_1 != 0:
    n_de_valores += 1
    numer_1 = int(input('Dime un número: '))
else:
    print(f" En la secuencia hay {n_de_valores} numero enteros")

'''

# 11. Haz un programa que devuelva el máximo de una secuencia de temperaturas acabada en 1000.
'''
numer_2 = int(input('Dime un número: '))
numero_max = 0

while numer_2 != 1000:
    if numer_2 > numero_max:  # Lo que estamos haciendo en este if es actualizar el valor de una variable para que siempre nos guarde el valor maximo 
        numero_max = numer_2
    numer_2 = int(input('Dime un número: '))
    
print(f'El numero máximo de la secuencia es {numero_max}')
'''


# 12. Haz un programa que dada una secuencia de valores acabada en 0 compruebe que ningún valor supera 50.
'''
numer_3 = int(input('Dime un número: '))

while numer_3 != 0:  
    if numer_3 > 50:
         break
    numer_3 = int(input('Dime un número: '))

if numer_3 > 50:
    print(f"En la secuencia hay un numero que supera el valor 50")
else:
    print(f"En la secuencia no hay un numero que supera el valor 50")

'''

# 13. Haz un programa que dada una secuencia de valores acabada en 0 compruebe que ningún valor supera 50 y que no hay más de tres que superen 40.
'''
numer_4 = int(input('Dime un número: '))
veces = 0
while numer_4 != 0:  
    if numer_4 > 50:
         break
    if numer_4 > 40:
        veces +=1
    if veces == 3:
         break
    numer_4 = int(input('Dime un número: '))

if numer_4 > 50:
    print(f"En la secuencia hay un numero que supera el valor 50")
else:
    print(f"En la secuencia no hay un numero que supera el valor 50")
if veces == 3:
    print(f"En la secuencia hay mas de 3 numero que supera el valor 40")
else:
    print(f"En la secuencia no hay mas de 3 numero  que supera el valor 40")
'''


# 14. Haz un programa que dada una secuencia de valores acabada en 0 diga si hay más positivos o negativos.
'''
numer_5 = int(input('Dime un número: '))
positivos = 0
negativos = 0

while numer_5 != 0:  
    if numer_5 > 0:
        positivos += 1
    if numer_5 < 0:
        negativos += 1
    numer_5 = int(input('Dime un número: '))

if positivos == negativos:
   print("Hay el mismo numero de positivos que de negativos") 
elif positivos > negativos:
    print("Hay mas positivos que negativos")
else:
    print("Hay mas negativos que positivos")

'''

# 15. Haz un programa que dada una secuencia de valores enteros acabada en 0 diga cuál es el número que hay antes de primer negativo encontrado.
'''
numer_6 = int(input('Dime un número: '))
numero_ante = 0

while numer_6 != 0:
    if  numer_6 > 0 :  
        numero_ante = numer_6
    else:
        break
    numer_6 = int(input('Dime un número: '))
if numer_6 < 0:
    print(f'El numero {numero_ante} es el anterior al primer negativo ')
else:
    print("No hay numeros previos")
'''


# 16. Haz un programa que dada una secuencia de valores enteros acabada en 0 diga cuántos son múltiples del primero.
'''
numero_7 = int(input('Dime un número: '))

primer_numero = 0
orden = 0
multiples = 0

while numero_7 != 0:
    if orden == 0:
        primer_numero = numero_7
        orden += 1
    elif numero_7 % primer_numero == 0:
        multiples += 1  
    numero_7 = int(input('Dime un número: '))

print(f'Existen {multiples} múltiples de {primer_numero}')
'''   


# 17. Haz un programa que lea varias descripciones de rectángulos y de círculos, y que para cada una escriba el área correspondiente. La entrada empieza con un número n, seguido de
# n descripciones. Si es de un rectángulo, se tiene la palabra “rectángulo” seguida de dos reales estrictamente positivos que indican la longitud y la anchura. 
# Si es de un círculo, se tiene la palabra “círculo” seguida de un real estrictamente positivo que indica el radio.
'''
n8 = int(input('Dime la longitud de la secuencia: '))

for i in range(0, n8):
    figura = input('Dime el nombre del polígono: ')
    area = 0
    
    if figura == 'rectangulo':
        ancho = float(input('Dime la anchura del rectángulo '))
        longitud = float(input('Dime la longitud del rectángulo '))
        area = ancho * longitud
        
    elif figura == 'circulo':
        radio = float(input('Dime el radio del círculo: '))
        area = pow(radio, 2) * 3.141621
        
    print(f'El {figura} tiene de area {area}')
'''


# 18. Haz un programa que lea un natural n, y que escriba el resultado de la suma siguiente: 1^2 + 2^2 + … + (n−1)^2 + n^2 y el aspecto de la secuencia. 
'''
n9 = int(input('Introduce la longitud de la secuencia: '))

suma = 0
secuencia = None
for numeros in range(0, n9 + 1):
    suma += numeros ** 2
    
    if numeros == 0:
        secuencia =f'{numeros}^{2}'
    else:
        secuencia += f' + {numeros}^{2} '
    
print(f'El resultado de la secuencia {secuencia} es {suma}')
'''