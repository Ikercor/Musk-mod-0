# 1. Haz un programa que cree una función en Python que dada una secuencia devuelva únicamente los números pares.
'''
def func_par (l):
    lista = []
    for n in l:
        if n % 2 == 0:
            lista.append(n)
    return lista

print(func_par([5, 7, 3, 4, 2, 1]))
    
'''

# 2. Haz un programa que cree una función con longitud variable de argumentos.
'''
def func_1(*argumen):
    for n in argumen:
        print(n)

func_1(20, 40, 60)

'''

# 3. Haz un programa que devuelva múltiples valores desde una función. Crea la función calculaion() de modo que pueda aceptar dos variables y calcular sumas y restas.
#    Además, debe devolver tanto la suma como la resta en una sola llamada.
'''
def func_calculaion(a,b):

   suma = a + b
   resta = a - b
   return (suma,resta) 

print(func_calculaion(40, 10))

'''

# 4. Haz un programa que cree una función con un argumento por defecto. Crea una función show_employee() usando las siguientes condiciones.
# -Debe aceptar el nombre y el salario del empleado y mostrar ambos.
# -Si falta el salario en la llamada de función, asigne el valor predeterminado 9000 al salario.
'''
def show_employee(nombre, salario=9000):
    print("Nombre:", nombre,"    Salario:", salario)

show_employee("Ben", 12000)
show_employee("Jessa")

'''

# 5. Haz un programa que cree una función interna para calcular la suma de la siguiente manera: Crea una función externa que acepte dos parámetros, a y b.
#    Crea una función interna dentro de una función externa que calculará la suma de a y b. Por último, una función externa que sumará 5 en la suma y la devolverá.
'''
def func_exter(a, b):
    def func_inter(a, b):
        return a + b
    return func_inter(a, b) + 5

print(func_exter(5, 10))

'''

# 6. Haz un que cree una función que escriba el cuadrado y la raíz cuadrada de una secuencia de naturales.
'''
import math # Importar math es como añadir una lista con funciones matematicas.
lista = [10, 4, 1, 15]

def al_cuadrado(l):
    lista_cuadrado = []
    for num in l:
        lista_cuadrado.append(num ** 2)
    return lista_cuadrado

def raiz_cuadrada(l):
    lista_raiz = []
    for num in l:
        lista_raiz.append(math.sqrt(num))# Con el .sqrt comseguimos hacer la raiz cuadrada .
    return lista_raiz

print (raiz_cuadrada(lista))
print (al_cuadrado(lista))

'''

# 7. Haz un programa que cree una función que deje a, b y c ordenados de pequeño a grande.
#    Por ejemplo, si a =7, b = −3 y c = 1, los valores después de la llamada deben ser a =−3, b = 1 y c = 7.
'''
lista  = [7, -3, 1]
def func_orden_menmas(l):
    l.sort() # Acordarse de los apuntes de listas que .sort() nos valia para ordenar valores de menor a mayor o por orden alfabetico.
    return lista
print(func_orden_menmas(lista))

'''