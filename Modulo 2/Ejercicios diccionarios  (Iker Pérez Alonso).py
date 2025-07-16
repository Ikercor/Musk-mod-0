# 1. Haz un programa que convierta dos listas en un diccionario
'''
lista_1 = ['a', 'b', 'c']
lista_2 = [1, 2, 3]
dic_1 = {}

for num in range(0,3):
    dic_1[lista_1[num]] = lista_2[num]
print(dic_1)

'''

# 2. Haz un programa que fusione dos diccionarios de Python en uno solo.
'''
dict1 = {'diez': 10, 'veinte': 20, 'treinta': 30}
dict2 = {'treinta': 30, 'cuarenta': 40, 'cincuenta': 50}

for clave, valor in dict2.items():
    dict1[clave] = valor

print(dict1)

'''

# 3. Haz un programa que imprima el valor de la clave 'history' del siguiente diccionario.
'''
sampleDict ={"class": {"student": {"name": "Mike","marks": {"physics": 70,
                                                            "history": 80}}}
        }

print(sampleDict["class"]["student"]["marks"]["history"])

'''

# 4. Haz un programa que inicialice el diccionario con valores por defecto.
'''
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

diccio_1 = dict.fromkeys(employees, defaults) # .fromkeys() crea un nuevo diccionario a partir de la secuencia especificada claves y un valor que tomara para todas ellas. 

print(diccio_1)

'''

# 5. Haz un programa que cree un diccionario extrayendo las claves de un diccionario dado.
'''
sample_dict_2 = {"name": "Kelly",
               "age": 25,
               "salary": 8000,
               "city": "New york"}

keys = ["name", "salary"]

claves = {}

for clave in keys:
    claves[clave] = sample_dict_2[clave]

print(claves)

'''

# 6. Haz un programa que elimine una lista de claves de un diccionario.
'''
sample_dict_3 = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys_eliminar = ["name", "salary"]

for clave in keys_eliminar:
    sample_dict_3.pop(clave)

print(sample_dict_3)

'''

# 7. Haz un programa que compruebe si un valor existe en un diccionario.
'''
valor_comprobar = input("Dime un dato para comprobar si existe en el diccionario: ")

sample_dict_4 = {'a': 100, 'b': 200, 'c': 300}

for clave, valor in sample_dict_4.items():
    if valor_comprobar == clave or valor_comprobar == str(valor):
        print(f'{valor_comprobar} existe dentro del diccionario')

'''

# 8. Haz un programa que cambie el nombre de la clave de un diccionario.
'''
sample_dict_5 = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sample_dict_5["location"] = sample_dict_5.pop("city") # Para cambiar un elemento en la lista  hay que borrarlo para poder sustituirlo por eso es tan util el .pop()

print(sample_dict_5)

'''

# 9. Haz un programa que obtenga la clave de un valor mínimo del siguiente diccionario.
'''
valor_bajo = 350
clave_valor_min = 0
sample_dict_6 = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
for clave,valor in sample_dict_6.items():
    if valor_bajo > valor:
        valor_bajo = valor  
        clave_valor_min = clave

print(clave_valor_min)

'''

# 10. Haz un programa que cambie el valor de una clave en un diccionario anidado.
'''
sample_dict_7 = {
    'empl1': {'name' : 'Jhon', 'salary' : 7500},
    'empl2': {'name' : 'Emma', 'salary' : 8000},
    'empl3': {'name' : 'Brad', 'salary' : 6500}
}

sample_dict_7['empl3']['salary'] = 8500

print(sample_dict_7)
'''