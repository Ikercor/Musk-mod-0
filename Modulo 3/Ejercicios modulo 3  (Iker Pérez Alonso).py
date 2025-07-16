# 1. Se ha definido una clase relativa al inventario de un jet imaginario. También se ha creado una instancia de esta clase Jet. Imprime el primer atributo de la instancia.

class Jet:

    def __init__(self, name, country):
        self.name = name
        self.origin = country

primer_item = Jet("F16", "USA")


print(primer_item.name)



# 2. Usando la clase Jet, crea nuevas instancias con los siguientes nombres y orígenes:

segundo_item = Jet("SU33", "Rusia")
tercer_item = Jet("AJS37", "Suecia")
cuarto_item = Jet("Mirage2000", "Francia")
quinto_item = Jet("F14", "USA")
sexto_item = Jet("Mig29", "USSR")
septimo_item = Jet("A10", "USA")



# 3. Añade otro atributo llamado "cantidad" a la clase. El usuario le dará valor pasando un nuevo parámetro por el constructor.
#    A continuación, crear 2 instancias para: F14 y Mirage2000 con las cantidades 87 y 35.

class Jet:

    def __init__(self, name, country, cantidad):
        self.name = name
        self.origin = country
        self.cantidad = cantidad

octavo_item = Jet("F14", "Mirage200", "87")
noveno_item = Jet("F14", "Mirage200", "35")



# 4. Dada la siguiente instancia y sus atributos, crea una clase que la instancie.

class Nobel:

    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner

np2005 = Nobel("Peace", 2005, "Muhammad Yunus") 
print(np2005.category, np2005.year, np2005.winner)



# 5. Crea una clase con el nombre de Estudiante, e inicialice atributos como el nombre, la edad y el grado mientras crea un objeto.

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

alumno_1 = Estudiante("Juan", "15", "3 ESO")



# 6. Escribe un programa para crear una clase vacía válida con el nombre de Estudiante, sin propiedades.

class Estudiante:
    pass
        


# 7. Añade un método público en la clase Estudiante que calcule la grado de una lista de notas y actualice el valor del atributo grado.
#    A continuación llama a la función en tu programa principal e imprime el valor de grado.

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre 
        self.grado = None
    def medianotas(self, notas):
        if len(notas) >= 1:
         self.grado = sum(notas) / len(notas)   
        else :
            0

estudiante_1 = Estudiante("Juan") 

notas = [8,5,6,4]

estudiante_1.medianotas(notas)

print(estudiante_1.grado)



# 8. Añade a la clase anterior, un método estático que dada una lista de notas y sus asignaturas asociadas como diccionario,
#    imprima aquellas asignaturas que han recibido una nota inferior a 5.

class Estudiante:
    def __init__(self, nombre ):
        self.nombre = nombre 
        self.grado = None
    def medianotas(self, notas):
        if len(notas) >= 1:
         self.grado = sum(notas) / len(notas)   
        else :
            0
    @staticmethod
    def asignaturas_bajas(nota_asignatura):
        for asignatura, nota in nota_asignatura.items():
            if nota < 5:
                print(f"En la asignatura de {asignatura} tiene una nota de {nota}")
            else:
                0


estudiante_1 = Estudiante("Juan")

notas = [8,5,6,4]

estudiante_1.medianotas(notas)

notas_asignaturas = {"Matemáticas": 8,
                     "Historia": 5,
                     "Lengua": 6,
                     "Fisica": 4}

Estudiante.asignaturas_bajas(notas_asignaturas)



# 9. Añade un atributo de clase llamado escuela a la clase Estudiante y dale un valor predeterminado. A continuación, 
#    añade un método de clase que dado el nombre de otra escuela actualice el valor de ese atributo. Llama a tu método en el programa principal y asegúrate de que funciona.

class Estudiante:

    escuela = "Escuela Primaria"

    def __init__(self, nombre ):
        self.nombre = nombre 
        self.grado = None
    def medianotas(self, notas):
        if len(notas) >= 1:
         self.grado = sum(notas) / len(notas)   
        else :
            0

    @staticmethod
    def asignaturas_bajas(nota_asignatura):
        for asignatura, nota in nota_asignatura.items():
            if nota < 5:
                print(f"En la asignatura de {asignatura} tiene una nota de {nota}")
            else:
                0

    @classmethod
    def cambia_escuela (cls, nueva_escuela):
        cls.escuela = nueva_escuela
       

estudiante_1 = Estudiante("Juan")

notas = [8,5,6,4]

estudiante_1.medianotas(notas)

notas_asignaturas = {"Matemáticas": 8,
                     "Historia": 5,
                     "Lengua": 6,
                     "Fisica": 4}

Estudiante.asignaturas_bajas(notas_asignaturas)

Estudiante.cambia_escuela("Escuela Secundaria")
    
print(Estudiante.escuela)

# 10. Añade un método privado en la clase anterior, que dado un diccionario mes-número de asistencias, devuelva 1 si algún mes tiene una asistencia < 4,
#     devuelva 2 si algún mes tiene alguna asistencia entre [4, 8) o bien devuelva 3 en caso contrario. Para probar el método privado, 
#     encapsúlalo con una función pública que devuelva su resultado.

class Estudiante:

    escuela = "Escuela Primaria"

    def __init__(self, nombre ):
        self.nombre = nombre 
        self.grado = None
    def medianotas(self, notas):
        if len(notas) >= 1:
         self.grado = sum(notas) / len(notas)   
        else :
            0

    @staticmethod
    def asignaturas_bajas(nota_asignatura):
        for asignatura, nota in nota_asignatura.items():
            if nota < 5:
                print(f"En la asignatura de {asignatura} tiene una nota de {nota}")
            else:
                0

    @classmethod
    def cambia_escuela (cls, nueva_escuela):
        cls.escuela = nueva_escuela
    def __comprovar_asistencias(self, asistencias):
        for mes, numero in asistencias.items():
            if numero < 4:
                return 1
            elif 4 <= numero < 8:
                return 2
            return 3
    def comprovar_asistencias_publico(self, asistencias):
        return self.__comprovar_asistencias(asistencias)
       

estudiante_1 = Estudiante("Juan")

notas = [8,5,6,4]

estudiante_1.medianotas(notas)

notas_asignaturas = {"Matemáticas": 8,
                     "Historia": 5,
                     "Lengua": 6,
                     "Fisica": 4}

Estudiante.asignaturas_bajas(notas_asignaturas)

Estudiante.cambia_escuela("Escuela Secundaria")
print(Estudiante.escuela)

asistencias = { "Enero": 6,
                "Febrero": 3,
                "Marzo": 9 }

resultado_asistencias = estudiante_1.comprovar_asistencias_publico(asistencias)
print(resultado_asistencias)

