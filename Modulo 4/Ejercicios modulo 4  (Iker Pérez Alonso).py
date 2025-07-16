# 1. Crea una clase Staff con los atributos role, depty y salary. Crea una clase Profesor que herede de la clase anterior y que además tenga como atributos nombre y edad. 
# Haz que sea posible instanciar un profesor dándole valor a todos los atributos.

class Staff:
    def __init__(self, role, depty, salary):
        self.role = role
        self.depty = depty
        self.salary = salary

class Profesor (Staff):
    def __init__(self, role, depty, salary, nombre, edad):
        super().__init__(role, depty, salary)
        self.nombre = nombre
        self.edad = edad


# Instancia de Profesor
profesor_1 = Profesor("Docente", "Matematicas", 2800, "Juan Lopez", 35)


print(f"Nombre: {profesor_1.nombre}")
print(f"Edad: {profesor_1.edad}")
print(f"Rol: {profesor_1.role}")
print(f"Departamento: {profesor_1.depty}")
print(f"Salario: {profesor_1.salary}")

print("----------------------------------------------------")

# 2.Representa el siguiente diagrama con sus clases, atributos y métodos correspondientes.
# Cada método display debe imprimir el nombre de la clase, atributos y valores de la instancia en ese momento. Ejemplo: In displaymethodofParent1 x=10

class Parent1 :
    def __init__(self, x):
        self.x = x
        
    def display(self):
        print(f'In displaymethodofParent1 x={self.x}') 

class Parent2 :
    def __init__(self, y):
        self.y = y
        
    def display(self):
        print(f'In displaymethodofParent2 y={self.y}') 

class Child(Parent1, Parent2):
    def __init__(self, x, y, z):
        Parent1.__init__(self, x)
        Parent2.__init__(self, y)
        self.z = z 
    
    def display(self):
        print(f'In displaymethodofChild x={self.x}, y={self.y}, z={self.z}')

# Instancia de Parent1
papa = Parent1(32)

# Instancia de Parent2
mama = Parent2(30)

# Instancia de Child
hijo = Child(34, 32, 2)

# Llamadas a los métodos
papa.display()
mama.display()
hijo.display()

print("----------------------------------------------------")

# 3. Crea una clase Car que herede de Vehicle y que sobreescriba los métodos max_speed() y change_gear(). Instancia dos objetos de cada clase y comprueba que la salida de cada método es distinta.

class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details:', self.name, self.color, self.price)

    def max_speed(self):
        print('Vehicle max speed is 150')

    def change_gear(self):
        print('Vehicle change 6 gear')

class Car(Vehicle):
    def max_speed(self):
        print('Vehicle max speed is 135')

    def change_gear(self):
        print('Vehicle change 5 gear')
    

# Instancias de Vehicle
vehicle1 = Vehicle("Camion", "verde", 25000)
vehicle2 = Vehicle("Bus", "amarillo", 50000)

# Instancias de Car
car1 = Car("Seat Leon", "rojo", 3000)
car2 = Car("Nissan GT-R R35", "azul", 100000)

# Llamadas a los métodos
vehicle1.show()
vehicle1.max_speed()
vehicle1.change_gear()

vehicle2.show()
vehicle2.max_speed()
vehicle2.change_gear()

car1.show()
car1.max_speed()
car1.change_gear()

car2.show()
car2.max_speed()
car2.change_gear()
   
print("----------------------------------------------------")

# 4. Dadas las siguientes clases con el output de sus respectivos metodos crea una interfaz formal que las implemente.

from abc import ABC, abstractmethod

class modelo(ABC):

    @abstractmethod
    def preprocess_data(self, data=None, y=None):
        pass

    @abstractmethod
    def fit(self):
        pass

    @abstractmethod
    def predict(self):
        pass


class SVM(modelo):
    
    def preprocess_data(self, data=None, y=None):
        print("preprocessimg data at SVM")

    def fit(self):
        print("Training at SVM")

    def predict(self):
        print("Evaluating at SVM")


class DecisionTree(modelo):

    def preprocess_data(self, data=None, y=None):
        print("preprocessimg data at DecisionTree")

    def fit(self):
        print("Training at DecisionTree")

    def predict(self):
        print("Evaluating at DecisionTree")

svm = SVM()
svm.preprocess_data()
svm.fit()
svm.predict()

dt = DecisionTree()
dt.preprocess_data()
dt.fit()
dt.predict()

print("----------------------------------------------------")

# 5. Repite el ejercicio anterior esta vez creando una interfaz informal.

class SVM:  
    def preprocess_data(self, data=None, y=None):
        print("Preprocessing data at SVM")

    def fit(self):
        print("Training at SVM")

    def predict(self):
        print("Evaluating at SVM")

class DecisionTree:  
    def preprocess_data(self, data=None, y=None):
        print("Preprocessing data at DecisionTree")

    def fit(self):
        print("Training at DecisionTree")

    def predict(self):
        print("Evaluating at DecisionTree")

svm = SVM()
svm.preprocess_data()
svm.fit()
svm.predict()

dt = DecisionTree()
dt.preprocess_data()
dt.fit()
dt.predict()

print("----------------------------------------------------")

# 6. Crea una clase virtual llamada Algoritmo con los atributos nombre, tarea y aprendizaje que sea superclase de la clase BaseClassifier del problema anterior. 
# Comprueba con el metodo issubclass que el Algoritmo es padre de BaseClassifier.

from abc import ABC, abstractmethod

class Algoritmo(ABC):
    
    def __init__(self, nombre, tarea, aprendizaje):
        self.nombre = nombre
        self.tarea = tarea
        self.aprendizaje = aprendizaje
       

    @abstractmethod
    def preprocess_data(self, data=None, y=None):
        pass

    @abstractmethod
    def fit(self):
        pass

    @abstractmethod
    def predict(self):
        pass

class BaseClassifier(Algoritmo):
    def __init__(self, nombre, tarea, aprendizaje):
        super().__init__(nombre, tarea, aprendizaje)
    
    def preprocess_data(self, data=None, y=None):
        print(f"Preprocessing data at {self.nombre}")

    def fit(self):
        print(f"Training at {self.nombre}")

    def predict(self):
        print(f"Evaluating at {self.nombre}")

print(issubclass(BaseClassifier, Algoritmo))

modelo = BaseClassifier("SVM", "Clasificación", "Supervisado")
modelo.preprocess_data()
modelo.fit()
modelo.predict()

print("----------------------------------------------------")

# 7. Escribe un script en Python para mostrar los distintos formatos de fecha y hora.
from datetime import  datetime

# a) Fecha y hora actuales
print(f"Fecha y hora actuales : {datetime.now()}")
# b) Año actual 
print(f"Año actual : {datetime.today().strftime('%Y')}")
# c) Mes del año 
print(f"Mes del año : {datetime.now().month}")
# d) Número de la semana del año 
print(f"Número de la semana del año : {datetime.now().strftime('%U')}")
# e) Nombre del día de la semana 
print(f"Nombre del día de la semana : {datetime.now().strftime('%A')}")
# f) Día del año 
print(f"Día del año : {datetime.now().strftime('%j')}")
# g) Día del mes 
print(f"Día del mes : {datetime.now().day}")
# h) Numero del día de la semana 
print(f"Numero del dia de la semana : {datetime.now().weekday()}")

print("----------------------------------------------------")

# 8. Escribe un programa en Python para convertir una cadena a datetime.
'''
INPUT : Jul 1 2014 2:43PM
OUTPUT : 2014-07-01 14:43:00
'''
from datetime import  datetime

date_1 = "Jul 1 2014 2:43PM"
date_conversion = datetime.strptime(date_1, '%b %d %Y %I:%M%p')
print(date_conversion)

print("----------------------------------------------------")

# 9. Escribe un programa en Python para obtener la hora actual.

from datetime import datetime

hora_actual = datetime.now().strftime("%H:%M:%S")

print(f"Hora actual: {hora_actual}")

print("----------------------------------------------------")

# 10. Escribe un programa en Python para restar cinco días a la fecha actual.

from datetime import datetime, timedelta

fecha_actual = datetime.now()

fecha_modificada = fecha_actual - timedelta(days=5)

print(f"Fecha actual : {fecha_actual.strftime('%Y-%m-%d')}")
print(f"Fecha modificada (5 días antes): {fecha_modificada.strftime('%Y-%m-%d')}")

print("----------------------------------------------------")

# 11. Escribe un programa en Python para convertir una cadena de marcas de tiempo unix en una fecha legible.
'''Al hacer la conversión en el programa y comprobarlo por diversas fuentes me encuentro que la fecha facilitada por el ejercicio debe ser erronea '''
'''
INPUT : 1284105682
OUTPUT : 2010-09-10 13:31:22
'''
from datetime import datetime

tiempo_unix = datetime.fromtimestamp(1284105682)
fecha_legible = tiempo_unix.strftime('%Y-%m-%d %H:%M:%S')
print((fecha_legible))

print("----------------------------------------------------")

# 12. Escribe un programa en Python para sumar 5 segundos con la hora actual.

from datetime import datetime, timedelta

hora_actual_1 = datetime.now()

hora_modificada = hora_actual_1 + timedelta(seconds=5)

print(f"Hora actual : {hora_actual_1.strftime('%H:%M:%S')}")
print(f"Hora modificada (5 segundos despues ): {hora_modificada.strftime('%H:%M:%S')}")

print("----------------------------------------------------")

# 13. Escribe un programa en Python para obtener el número de la semana.

from datetime import datetime

fecha_actual_ = datetime.now()

numero_semana = fecha_actual_.isocalendar()[1]

print(f"Número de la semana : {numero_semana}")

print("----------------------------------------------------")

# 14. Escribe un programa en Python para seleccionar todos los domingos de un año determinado.

from datetime import datetime, timedelta

año_ = 2025

fecha_inicio = datetime(año_, 1, 1)

fechas_domingos = []

dias_hasta_domingo = (6 - fecha_inicio.weekday()) % 7  
primer_domingo = fecha_inicio + timedelta(days=dias_hasta_domingo)

for i in range(52): 
    domingo = primer_domingo + timedelta(weeks=i)
    if domingo.year == año_: 
        fechas_domingos.append(domingo.strftime('%Y-%m-%d'))

for domingo in fechas_domingos:
    print(domingo)

print("----------------------------------------------------")

# 15. Escribe un programa en Python para contar el número de lunes del primer día del mes desde 2015 hasta 2016.

from datetime import datetime

año = 2015
contador_lunes = 0

for mes in range(1, 13):
    primer_dia = datetime(año, mes, 1)
    if primer_dia.weekday() == 0:  # 0 representa lunes
        contador_lunes += 1
        print(primer_dia.strftime('%Y-%m-%d'))
print(f"Total de lunes que fueron el primer día del mes en {año}: {contador_lunes}")

print("----------------------------------------------------")

# 16. Escribe un programa en Python para crear 12 fechas fijas a partir de una fecha especificada en un periodo determinado. La diferencia entre dos fechas será de 20.

from datetime import datetime, timedelta

fecha_inicial = datetime(2025, 8, 1)

num_fechas = 12
diferencia_dias = 20

fechas = [fecha_inicial + timedelta(days=i * diferencia_dias) for i in range(num_fechas)]

for fecha in fechas:
    print(fecha.strftime('%Y-%m-%d'))

print("----------------------------------------------------")

# 17. Implementa una función generadora que, dadas dos listas del mismo tamaño, devuelva la multiplicación entre los elementos de cada una: 
# el primer elemento de la lista 1 por el primero de la lista 2, el segundo con el segundo, y así sucesivamente. Sigue la siguiente estructura:

#def prod(l1, l2):
#   ...
#   except StopIteration:
#       pass
#   return solution
#Añadiendo el bloque except capturamos la excepción StopIteration que se produce al acabar de leer todos los elementos de un generador.

def prod(l1, l2):
    try:
        for a,b in zip(l1,l2):
            yield a*b
    except StopIteration:
        pass

#ejemplo
lista1 = [3, 6, 9, 10]
lista2 = [2, 4, 7, 8]

resultado = prod(lista1, lista2)

print(list(resultado))

print("----------------------------------------------------")

# 18. Implementa un generador que, dado un entero n, genere n números aleatorios. Puedes usar el método random de la librería random para generar números aleatorios.
import random

def generam(n):
    for _ in range(n):
        yield  random.random()

#ejemplo

numeros = generam(8)

print(list(numeros))

print("----------------------------------------------------")

# 19. Implementa un generador de Fibonacci que genere n números de la secuencia de Fibonacci, que tiene la forma:
#     0, 1, 1, 2, 3, 5, 8, 13, ...
#     Cuyos dos primeros valores son 0 y 1 por definición y el resto se calculan sumando los dos últimos valores de la sucesión.

def generador_fibonacci(n):
    a = 0 
    b = 1
    for _ in range (n):
        yield a
        a,b= b, a+b

#ejemplo

numeros_fibonacci = generador_fibonacci(8)

print(list(numeros_fibonacci))       

print("----------------------------------------------------")

# 20. Implementa un generador que, dado un entero n, imprima todos los números inferiores a n multiplicados por dos.

def generador_doble(n):
    for i in range(n):  
        yield i * 2  

# Ejemplo:
resultado = generador_doble(5)
print(list(resultado))   

print("----------------------------------------------------")

# 21. Implementa un generador que, dado un entero n, genere n números impares.

def generador_impares(n):
    primer_num = 1  
    for _ in range(n):  
        yield primer_num
        primer_num += 2 

# Ejemplo:

resultado = generador_impares(9)

print(list(resultado))

print("----------------------------------------------------")

# 22. Crea una función que genere una excepción e imprima su tipo, los argumentos de la excepción y su mensaje de error.

def generar_excepcion():
    try:
        raise ValueError("Estamos generando un errror manualmente")
    except Exception as ex:
        print(f"El tipo de excepcion es: {type(ex)}")
        print(f"El argumento es: {ex.args}")
        print(f"El mensaje es: {str(ex)}")

generar_excepcion()

print("----------------------------------------------------")

# 23. Crea una función que compute la diferencia entre dos enteros. En caso de que la diferencia sea negativa genera una excepción inventada por ti que informe sobre ello. 
# Por ejemplo. la excepción podría llamarse NegativeDifferenceException.
class NegativeDifferenceException(Exception):
    def __init__(self, menasaje="La diferencia entre los numeros es negativa"):
        super().__init__(menasaje)
    
def diferencia(a,b):
    resultado= a-b
    if resultado < 0:
        raise NegativeDifferenceException(f"Diferencia negativa: {resultado}")
    return resultado

try: 
    print("resultado:",diferencia(3,4))
except Exception as e :
    print(f"El tipo de excepcion es: {type(e)}")
    print(f"El mensaje es: {str(e)}")

print("----------------------------------------------------")

# 24. Crea una función que calcule la división entre dos números. Debe imprimir el mensaje 
# 'Los parámetros deben ser número enteros' cuando se genera una excepción de tipo y 'El divisor no puede ser 0' cuando se genera un ZeroDivisionError.

def division(a,b):
    try:
        resultado = a // b
        print(resultado)
    except TypeError:
        print(f"Los parámetros deben ser número enteros")
    except ZeroDivisionError:
        print(f"El divisor no puede ser 0")

division(10,2) 
division(10,0)
division(10,"buenas")

print("----------------------------------------------------")

# 25. Añade a la función anterior, un mensaje que se imprima al final de la ejecución de la función independientemente de si se ha generado excepción o no.

def division(a,b):
    try:
        resultado = a // b
        print(resultado)
    except TypeError:
        print(f"Los parámetros deben ser número enteros")
    except ZeroDivisionError:
        print(f"El divisor no puede ser 0")
    finally:
        print(f"La ejecucion finalizo")

division(10,2) 


