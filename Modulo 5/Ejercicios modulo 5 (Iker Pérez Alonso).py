# 1. Escribe una función en python para leer el contenido de un archivo de texto "poema.txt" línea por línea y mostrar el mismo en pantalla.

def leer_poema():
    try:
        with open("poema.txt", "r", encoding="utf-8")  as archivo :
            for linea in archivo:
                 print(linea.strip())
    except FileNotFoundError:
        print("El archivo 'poema.txt' no fue encontrado")

leer_poema()

print("----------------------------------------------------")

# 2. Escribe una función para contar el número de líneas de un archivo de texto "historia.txt":
#    Ejemplo: Si el archivo "story.txt" contiene las siguientes líneas
#       Un niño está jugando allí. 
#       Hay un parque infantil. 
#       Un avión está en el cielo.
#       El cielo es rosa. 
#       La contraseña puede contener letras y números.
#    El resultado debe ser 5.

def contador_lineas():
    try:
        with open("historia.txt", "r", encoding="utf-8") as archivo :
            lineas = archivo.readlines()
            print(f"El numero de lineas es {len(lineas)}")
    except FileNotFoundError:
        print("El archivo 'historia.txt' no fue encontrado")

contador_lineas()

print("----------------------------------------------------")

# 3. Escribe una función en Python para contar y mostrar el número total de palabras en un archivo de texto.

def contar_palabras():
    try:
        with open("poema.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            print("Número total de palabras:", len(palabras))
    except FileNotFoundError:
        print("El archivo 'poema.txt' no fue encontrado.")

contar_palabras()

print("----------------------------------------------------")

# 4. Escriba una función en Python para leer líneas de un archivo de texto "notas.txt". Su función debe encontrar y mostrar la aparición de la palabra "el".

def contar_apariciones_el():
    try:
        with open("notas.txt", "r", encoding="utf-8") as archivo:
            contador = 0
            for linea in archivo:
                # Separar palabras y contar "el" (ignorando mayúsculas)
                palabras = linea.lower().split()
                contador += palabras.count("el")
            print("La palabra 'el' aparece", contador, "veces.")
    except FileNotFoundError:
        print("El archivo 'notas.txt' no fue encontrado.")

contar_apariciones_el()

print("----------------------------------------------------")

# 5. Escriba una función display_words() en python para leer las líneas de un archivo de texto "story.txt", y mostrar aquellas palabras que tengan menos de 4 caracteres.

def display_words():
    try:
        with open("story.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                palabras = linea.split()
                for palabra in palabras:
                    if len(palabra.strip(".,;:!?")) < 4:
                        print(palabra)
    except FileNotFoundError:
        print("El archivo 'story.txt' no fue encontrado.")

display_words()

print("----------------------------------------------------")

# 6. Un archivo de texto llamado "materia.txt" contiene algún texto, que necesita ser mostrado de manera que cada carácter siguiente esté separado por un símbolo "#". 
#    Escriba una definición de función para hash_display() en Python que muestre todo el contenido del archivo matter.txt en el formato deseado.
#    Ejemplo: Si el archivo materia.txt tiene el siguiente contenido almacenado:
#       EL MUNDO ES REDONDO
#       La función hash_display() debería mostrar el siguiente contenido:
#       #T#H#E# #W#O#R#L#D# #I#S# #R#O#U#N#D#

def hash_display():
    try:
        with open("materia.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            resultado = '#' + '#'.join(contenido.strip())
            print(resultado)
    except FileNotFoundError:
        print("El archivo 'materia.txt' no fue encontrado.")

hash_display()

print("----------------------------------------------------")

# 7. Escribe un programa en Python para generar 26 archivos de texto llamados A.txt, B.txt, y así sucesivamente hasta Z.txt.

def generar_archivos_az():
    for i in range(65, 91):  
        nombre_archivo = chr(i) + ".txt"
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(f"Este es el archivo {chr(i)}.\n")
    print("¡Archivos de la A a la Z creados exitosamente!")

generar_archivos_az()

print("----------------------------------------------------")

# 8. Escribe un programa en python para añadir texto a un archivo y mostrar el texto en python.txt

def añadir_y_mostrar_texto():
    try:
        texto = input("Escribe el texto que deseas añadir al archivo: ")
        with open("python.txt", "a", encoding="utf-8") as archivo:
            archivo.write(texto + "\n")

        print("\nContenido actual del archivo 'python.txt':")
        with open("python.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            print(contenido)

    except Exception as e:
        print("Ocurrió un error:", e)

añadir_y_mostrar_texto() 

print("----------------------------------------------------")

# 9. Escribe un programa en python para calcular la frecuencia de todas las palabras de un archivo .txt.

def frecuencia_palabras():
    try:
        with open("notas.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

            contenido = contenido.lower()
            for caracter in ",.;:¡!¿?()[]\"'\n":
                contenido = contenido.replace(caracter, " ")

            palabras = contenido.split()
            frecuencia = {}

            for palabra in palabras:
                if palabra in frecuencia:
                    frecuencia[palabra] += 1
                else:
                    frecuencia[palabra] = 1

            print("Frecuencia de palabras:\n")
            for palabra, cantidad in frecuencia.items():
                print(f"{palabra}: {cantidad}")

    except FileNotFoundError:
        print("El archivo 'notas.txt' no fue encontrado.")

frecuencia_palabras()

print("----------------------------------------------------")

# 10. Escribe un programa en python para comprobar si un archivo especificado existe.

import os

def comprobar_existencia_archivo():
    nombre_archivo = input("Escribe el nombre del archivo que quieres comprobar (ej. archivo.txt): ")
    
    if os.path.isfile(nombre_archivo):
        print(f" El archivo '{nombre_archivo}' **existe**.")
    else:
        print(f" El archivo '{nombre_archivo}' **no existe**.")

comprobar_existencia_archivo()

print("----------------------------------------------------")

# 11. A partir del conjunto de datos dado, imprime las cinco primeras y últimas filas.

import pandas as pd

df = pd.read_csv('Modulo5_Automobile_data-221102-123259.csv')

print("Primeras cinco filas:")
print(df.head(5))

print("\nÚltimas cinco filas:")
print(df.tail(5))

print("----------------------------------------------------")

# 12. Limpia el conjunto de datos y actualiza el archivo CSV. Reemplaza todos los valores de las columnas que contengan ?, n.a, o NaN.

import pandas as pd

df = pd.read_csv('Modulo5_Automobile_data-221102-123259.csv', na_values=["?", "n.a"])

print("Valores nulos por columna:")
print(df.isnull().sum())

df.fillna(df.mean(numeric_only=True), inplace=True)

for col in df.select_dtypes(include='object').columns:
    if df[col].isnull().sum() > 0:
        df[col].fillna(df[col].mode()[0], inplace=True)

df.to_csv('Modulo5_Automobile_data-limpio.csv', index=False)

print("Datos limpios guardados en 'Modulo5_Automobile_data-limpio.csv'")

print("----------------------------------------------------")

# 13. Encuentra el nombre de la empresa del coche más caro. Imprime el nombre de la empresa del coche más caro y su precio.

import pandas as pd

df = pd.read_csv('Modulo5_Automobile_data-221102-123259.csv')

df['price'] = pd.to_numeric(df['price'], errors='coerce')

df = df.dropna(subset=['price'])

coche_mas_caro = df.loc[df['price'].idxmax()]

print("Empresa del coche más caro:", coche_mas_caro['company'])
print("Precio:", coche_mas_caro['price'])

print("----------------------------------------------------")

# 14. Imprime todos los datos de los coches Toyota.

import pandas as pd

df = pd.read_csv('Modulo5_Automobile_data-221102-123259.csv')

df_toyota = df[df['company'] == 'toyota']

print(df_toyota)

print("----------------------------------------------------")

# 15. Cuenta el total de coches por empresa.

import pandas as pd

df = pd.read_csv('Modulo5_Automobile_data-221102-123259.csv')

print(df.columns)

coches_por_empresa = df['company'].value_counts()

print(coches_por_empresa)

print("----------------------------------------------------")

# 16. Encuentra el coche con el precio más alto de precio de cada empresa.

import pandas as pd

df = pd.read_csv('Modulo5_Automobile_data-221102-123259.csv')

df['price'] = pd.to_numeric(df['price'], errors='coerce')

df = df.dropna(subset=['price'])

coche_mas_caro_por_empresa = df.loc[df.groupby('company')['price'].idxmax()]

print(coche_mas_caro_por_empresa[['index', 'company', 'price']])

print("----------------------------------------------------")

# 17. Encuentra el kilometraje medio de cada empresa fabricante de automóviles.

import pandas as pd

df = pd.read_csv('Modulo5_Automobile_data-221102-123259.csv')

df['average-mileage'] = pd.to_numeric(df['average-mileage'], errors='coerce')

df = df.dropna(subset=['average-mileage'])

kilometraje_medio_por_empresa = df.groupby('company')['average-mileage'].mean()

print(kilometraje_medio_por_empresa)

print("----------------------------------------------------")

# 18. Ordena todos los coches por la columna Precio.

import pandas as pd

df = pd.read_csv('Modulo5_Automobile_data-221102-123259.csv')

df['price'] = pd.to_numeric(df['price'], errors='coerce')

df = df.dropna(subset=['price'])

df_ordenado = df.sort_values(by='price', ascending=True)

print(df_ordenado)

print("----------------------------------------------------")

# 19. Concatenar dos dataframes usando las siguientes condiciones:
#     GermanCars = ('Company': ['Ford', 'Mercedes', 'BMW', 'Audi'], 'Price': [23845, 171995, 135925, 71400])
#     JapaneseCars = ('Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi'], 'Price': [29995, 23600, 61500, 58900])

import pandas as pd

GermanCars = {
    'Company': ['Ford', 'Mercedes', 'BMW', 'Audi'],
    'Price': [23845, 171995, 135925, 71400]
}

JapaneseCars = {
    'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi'],
    'Price': [29995, 23600, 61500, 58900]
}

df_german = pd.DataFrame(GermanCars)
df_japanese = pd.DataFrame(JapaneseCars)

df_concat = pd.concat([df_german, df_japanese], ignore_index=True)

print(df_concat)

print("----------------------------------------------------")

# 20. Combina dos dataframes usando la siguiente condición. Crea dos dataframes usando los siguientes dos Dicts, fusionarlos y añade el segundo dataframe como una nueva columna al primer dataframe.
#     Car_Price = {'Company': ['Toyota', 'Honda', 'BMW', 'Audi'], 'Price': [23845, 17995, 135925, 71400]}
#     car_horsepower = {'Company': ['Toyota', 'Honda', 'BMW', 'Audi'], 'horsepower': [141, 88, 182, 168]}

import pandas as pd

Car_Price = {
    'Company': ['Toyota', 'Honda', 'BMW', 'Audi'], 
    'Price': [23845, 17995, 135925, 71400]
}

car_horsepower = {
    'Company': ['Toyota', 'Honda', 'BMW', 'Audi'],
    'horsepower': [141, 88, 182, 168]
}

df_price = pd.DataFrame(Car_Price)
df_horsepower = pd.DataFrame(car_horsepower)

df_combined = pd.merge(df_price, df_horsepower, on='Company')

print(df_combined)

print("----------------------------------------------------")

# 21. Crea un array de enteros 4x2 e imprime sus atributos. Nota: El elemento debe ser de tipo unsigned int16. Imprime los siguientes atributos:
    # La shape del array.
    # Las dimensiones del array.
    # El tamaño de cada elemento del array en bytes.

import numpy as np

array = np.zeros((4, 2), dtype=np.uint16)

print("Shape del array:", array.shape)
print("Dimensiones del array:", array.ndim)
print("Tamaño de cada elemento en bytes:", array.itemsize)

print("----------------------------------------------------")

# 22. Crea una matriz de enteros 5X2 de un rango entre 100 y 200 tal que la diferencia entre cada elemento sea 10.

import numpy as np

valores = np.arange(100, 200, 10)

if valores.size >= 10:
    matriz = valores[:10].reshape(5, 2)
    print("Matriz 5x2:")
    print(matriz)
else:
    print("No hay suficientes valores para formar una matriz 5x2.")

print("----------------------------------------------------")

# 23. A continuación se muestra el array Numpy proporcionado. Devuelve un array de elementos tomando la tercera columna de todas las filas.
    # sampleArray = numpy.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])

import numpy as np

sampleArray = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
tercera_col = sampleArray[:, 2]

print(tercera_col)

print("----------------------------------------------------")

# 24. Devuelve un array de filas impares y columnas pares dado el siguiente array:
    # sampleArray = numpy.array([[3 , 6, 9, 12], [15, 18, 21, 24], [27, 30, 33, 36], [39, 42, 45, 48], [51, 54, 57, 60]])

import numpy as np

sampleArray = np.array([
    [3 , 6, 9, 12],
    [15, 18, 21, 24],
    [27, 30, 33, 36],
    [39, 42, 45, 48],
    [51, 54, 57, 60]
])

resultado = sampleArray[1::2, ::2]

print(resultado)

print("----------------------------------------------------")

# 25. Crea una matriz de resultados sumando las siguientes dos matrices de NumPy. A continuación, modifica la matriz de resultados calculando el cuadrado de cada elemento.
    # arrayOne = numpy.array([[5, 6, 9], [21, 18, 27]])
    # arrayTwo = numpy.array([[15, 33, 24], [4, 7, 1]])

import numpy as np

arrayOne = np.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = np.array([[15, 33, 24], [4, 7, 1]])

result_sum = arrayOne + arrayTwo
result_cuadr = result_sum ** 2


print("Suma de matrices:\n", result_sum)
print("\nMatriz al cuadrado:\n", result_cuadr)

print("----------------------------------------------------")

# 26. Divide la matriz en cuatro submatrices de igual tamaño. Nota: Crea una matriz de enteros 8x3 de un rango entre 10 y 34 de tal manera 
# que la diferencia entre cada elemento sea 1 y luego divide la matriz en cuatro submatrices de igual tamaño.

import numpy as np

original_array = np.arange(10, 34).reshape(8, 3)
submatrices = np.vsplit(original_array, 4)

print("Matriz original (8x3):\n", original_array)
print("\nSubmatrices:")
for i, sub in enumerate(submatrices, 1):
    print(f"\nSubmatriz {i}:\n", sub)

print("----------------------------------------------------")

# 27. Ordena el siguiente array de NumPy:
# Caso 1: Ordenar el array por la segunda fila
# Caso 2: Ordenar el array por la segunda columna
    # sampleArray = numpy.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

import numpy as np

sampleArray = np.array([[34, 43, 73], 
                        [82, 22, 12], 
                        [53, 94, 66]])

# Caso 1
sorted_indices = np.argsort(sampleArray[1, :])

sorted_by_second_row = sampleArray[:, sorted_indices]

print(sorted_by_second_row)

# Caso 2
sorted_indices = np.argsort(sampleArray[:, 1])

sorted_by_second_col = sampleArray[sorted_indices, :]

print(sorted_by_second_col)

print("----------------------------------------------------")

# 28. Imprime el máximo del eje 0 y el mínimo del eje 1 de la siguiente matriz bidimensional:
    # sampleArray = numpy.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

import numpy as np

sampleArray = np.array([[34, 43, 73], 
                        [82, 22, 12], 
                        [53, 94, 66]])

# Máximo a lo largo del eje 0 (por columnas)
max_axis0 = np.max(sampleArray, axis=0)
print("Máximo del eje 0 (por columnas):", max_axis0)

# Mínimo a lo largo del eje 1 (por filas)
min_axis1 = np.min(sampleArray, axis=1)
print("Mínimo del eje 1 (por filas):", min_axis1)

print("----------------------------------------------------")

# 29. Elimina la segunda columna de una matriz dada e inserta la siguiente columna nueva en su lugar.
    # sampleArray = numpy.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
    # newColumn = numpy.array([[10, 10, 10]])

import numpy as np

sampleArray = np.array([[34, 43, 73], 
                        [82, 22, 12], 
                        [53, 94, 66]])

newColumn = np.array([10, 10, 10])

newColumn = newColumn.T

modifiedArray = np.delete(sampleArray, 1, axis=1)

resultArray = np.insert(modifiedArray, 1, newColumn, axis=1)

print("Resultado final:")
print(resultArray)

print("----------------------------------------------------")

# 30. Lee el beneficio total de todos los meses y muéstralo mediante un gráfico de líneas. Se proporcionan los datos del beneficio total de cada mes. El gráfico de líneas generado debe incluir las siguientes propiedades:
    # Nombre de la etiqueta X = Número de mes 
    # Nombre de la etiqueta Y = Beneficio total

import matplotlib.pyplot as plt
import numpy as np

Numero_meses = np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
Beneficio_total = np.array ([211000, 183300, 224700,222700, 209600, 201400, 295500, 361400, 234000, 266700, 412800, 300200])

plt.plot(Numero_meses, Beneficio_total)

plt.xlabel("Número del mes")
plt.ylabel("Beneficio total")
plt.title("Beneficio por mes")
plt.xticks(np.arange(1, 13, 1))
plt.yticks(np.arange(100000, 600000, 100000))

plt.show()

print("----------------------------------------------------")

# 31. Obtenga el beneficio total de todos los meses y muestre un gráfico de líneas con las siguientes propiedades de estilo:
    # Estilo de línea punteada y el color de la línea debe ser rojo
    # Mostrar la leyenda en la parte inferior derecha.
    # Nombre de la etiqueta X = Número de mes
    # Nombre de la etiqueta Y = Número de unidades vendidas
    # Añadir un marcador de círculo.
    # El ancho de la línea debe ser 3

import matplotlib.pyplot as plt
import numpy as np

Numero_meses = np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
Beneficio_total = np.array ([211000, 183300, 224700,222700, 209600, 201400, 295500, 361400, 234000, 266700, 412800, 300200])

plt.plot(
    Numero_meses,
    Beneficio_total,
    linestyle='--',
    color='red',
    marker='o',
    markerfacecolor='black',   
    linewidth=3,
    label='Unidades vendidas'  
)

plt.xlabel("Número del mes")
plt.ylabel("Beneficio total")
plt.title("Beneficio por mes")
plt.xticks(np.arange(1, 13, 1))
plt.yticks(np.arange(100000, 600000, 100000))

plt.legend(loc='lower right')

plt.show()

print("----------------------------------------------------")

# 32. Lee todos los datos de ventas de productos y muéstralos mediante un gráfico multilineal.
#  Muestra el número de unidades vendidas por mes para cada producto utilizando gráficos multilineales (es decir, una línea de trazado separada para cada producto).

import matplotlib.pyplot as plt
import numpy as np

Numero_meses = np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
facecream = np.array ([2500, 2630 ,2140, 3400, 3600, 2760, 2980 ,3700, 3540, 1990, 2340, 2900])
facewash = np.array ([1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760])
toothpaste = np.array ([5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400])
bathingsoap = np.array ([9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400])
shampoo = np.array ([1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800])
moisturizer = np.array ([1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760])

plt.plot(
    Numero_meses,
    facecream,
    color='blue',
    marker='o',   
    linewidth=3,
    label='Facecream Sales Data'  
)
plt.plot(
    Numero_meses,
    facewash,
    color='orange',
    marker='o',   
    linewidth=3,
    label='Facewash Sales Data'  
)
plt.plot(
    Numero_meses,
    toothpaste,
    color='green',
    marker='o',   
    linewidth=3,
    label='Toothpaste Sales Data'  
)
plt.plot(
    Numero_meses,
    bathingsoap,
    color='red',
    marker='o',   
    linewidth=3,
    label='Bathingsoap Sales Data'  
)
plt.plot(
    Numero_meses,
    shampoo,
    color='pink',
    marker='o',   
    linewidth=3,
    label='Shampoo Sales Data'  
)
plt.plot(
    Numero_meses,
    moisturizer,
    color='brown',
    marker='o',   
    linewidth=3,
    label='Moisturizer Sales Data'  
)
plt.xlabel("Número del mes")
plt.ylabel("Unidad de ventas en numero")
plt.title("Ventas")
plt.xticks(np.arange(1, 13, 1))

plt.legend(loc='upper left')

plt.show()

print("----------------------------------------------------")

# 33. Lee los datos de ventas de pasta de dientes de cada mes y muéstralos mediante un gráfico de dispersión. Además, añade una cuadrícula al gráfico. El estilo de la cuadrícula debe ser "-".

import matplotlib.pyplot as plt
import numpy as np

Numero_meses = np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
toothpaste = np.array ([5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400])

plt.scatter(
    Numero_meses,
    toothpaste,
    label='Ventas de pasta de dientes'
)
plt.grid(
    True,
    linestyle='--'
) 

plt.xlabel("Número del mes")
plt.ylabel("Numero de unidades vendidas")
plt.title("Ventas pasta de dientes")
plt.xticks(np.arange(1, 13, 1))

plt.legend(loc='upper left')

plt.show()

print("----------------------------------------------------")

# 34. Lee los datos de ventas de los productos crema facial y lavado de cara y muéstralos mediante un gráfico de barras. El gráfico de barras debe mostrar el número de unidades vendidas por mes para cada producto.
# Añade una barra distinta para cada producto en el mismo gráfico.

import matplotlib.pyplot as plt
import numpy as np

Numero_meses = np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
facecream = np.array ([2500, 2630 ,2140, 3400, 3600, 2760, 2980 ,3700, 3540, 1990, 2340, 2900])
facewash = np.array ([1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760])

ancho = 0.3

plt.bar(
    Numero_meses - ancho/2,
    facecream,
    color='blue',
    width= ancho,
    label='Ventas crema facial' 
)
plt.bar(
    Numero_meses + ancho/2,
    facewash,
    color='orange',
    width= ancho,
    label='Ventas lavado de cara'
)

plt.xlabel("Número del mes")
plt.ylabel("Unidades de ventas en numero")
plt.title("Facewash and facecream sales data")
plt.xticks(np.arange(1, 13, 1))

plt.grid(
    True,
    linestyle='--'
)

plt.legend(loc='upper left')

plt.show()

print("----------------------------------------------------")

# 34. Lee los datos de ventas de jabón de baño de todos los meses y muéstralos mediante un gráfico de barras. Guarda este gráfico en tu disco duro.

import matplotlib.pyplot as plt
import numpy as np

Numero_meses = np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
bathingsoap = np.array ([9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400])

plt.bar(
    Numero_meses,
    bathingsoap,
    color='blue',
    width= 0.8
)

plt.xlabel("Número del mes")
plt.ylabel("Unidades de ventas en numero")
plt.title("Ventas jabon de baño")
plt.xticks(np.arange(1, 13, 1))

plt.grid(
    True,
    linestyle='--'
)

plt.savefig("ventas_jabon_baño.png")

plt.show()

print("----------------------------------------------------")

# 35. Lee el beneficio total de cada mes y muéstralo utilizando un histograma para ver los rangos de beneficio más comunes.

import matplotlib.pyplot as plt
import numpy as np

Beneficio_total = np.array([211000, 183300, 224700, 222700, 209600, 201400, 295500, 361400, 234000, 266700, 412800, 300200])

plt.hist(
    Beneficio_total, 
    bins=6, color='blue', 
    edgecolor='black'
)  

plt.xlabel("Profit en dolares")
plt.ylabel("Actual profit en dolares")
plt.title("Profit")
plt.grid(True, linestyle='--', alpha=0.7)

plt.show()

print("----------------------------------------------------")

# 36 Calcula los datos de ventas totales del último año para cada producto y muéstralos mediante un gráfico circular. 
# Nota: En el gráfico circular muestra el número de unidades vendidas por año para cada producto en porcentaje.

import numpy as np
import matplotlib.pyplot as plt

facecream = np.array([2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900])
facewash = np.array([1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760])
toothpaste = np.array([5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400])
bathingsoap = np.array([9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400])
shampoo = np.array([1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800])
moisturizer = np.array([1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760])

ventas_anuales = {
    'Crema facial': np.sum(facecream),
    'Lavado de cara': np.sum(facewash),
    'Pasta de dientes ': np.sum(toothpaste),
    'Gel de baño': np.sum(bathingsoap),
    'Shampoo': np.sum(shampoo),
    'Moisturizer': np.sum(moisturizer)
}

productos = list(ventas_anuales.keys())
ventas = list(ventas_anuales.values())

plt.figure(figsize=(8,8))
plt.pie(
    ventas, 
    labels=productos, 
    autopct='%1.1f%%', 
    startangle=140, 
    shadow=True
)
plt.title('Sales data')
plt.axis('equal')  

plt.show()

print("----------------------------------------------------")

# 37.Lee los datos de ventas de jabón de baño de todos los meses y visualízalos utilizando el Subplot.

import numpy as np
import matplotlib.pyplot as plt

Numero_meses = np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
facewash = np.array([1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760])
bathingsoap = np.array([9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400])


plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.plot(
    Numero_meses,
    bathingsoap, 
    marker='o', 
    color='black', 
    linestyle='-'
)
plt.title('Ventas gel de baño')
plt.xticks(Numero_meses)

plt.subplot(2, 1, 2)
plt.plot(
    Numero_meses, 
    facewash, 
    marker='o', 
    color='red', 
    linestyle='-'
)
plt.title('Ventas lavado de cara')
plt.xlabel('Numero del mes')
plt.ylabel('Unidades de Ventas en numero ')
plt.xticks(Numero_meses)

plt.tight_layout()

plt.show()

print("----------------------------------------------------")

# 38. Lee todos los datos de las ventas de productos y muéstralos mediante un diagrama de pila.

import numpy as np
import matplotlib.pyplot as plt

Numero_meses = np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
facecream = np.array ([2500, 2630 ,2140, 3400, 3600, 2760, 2980 ,3700, 3540, 1990, 2340, 2900])
facewash = np.array ([1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760])
toothpaste = np.array ([5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400])
bathingsoap = np.array ([9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400])
shampoo = np.array ([1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800])
moisturizer = np.array ([1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760])

plt.figure(figsize=(12, 6))
plt.stackplot(Numero_meses, facecream, facewash, toothpaste, bathingsoap, shampoo, moisturizer, 
              labels=['Crema facial', 'Lavado facial', 'Pasta de dientes', 'Gel de baño', 'Champú', 'Moisturizer'])

plt.xlabel('Numero del mes')
plt.ylabel('Unidades de ventas en numero')
plt.title('Todas las ventas de productos en un stack plot')
plt.xticks(Numero_meses)
plt.legend()

plt.tight_layout()

plt.show()

