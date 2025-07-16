import pandas as pd

class Lector:
    def __init__(self, path: str):
    # Guarda la ruta del archivo
        self.path = path

    def _comprueba_extension(self, extension):
    # Comprueba si la ruta termina con la extensión indicada
        return self.path.lower().endswith(extension.lower())

    def lee_archivo(self):
    # Método base: en la clase padre no se implementa
        raise NotImplementedError("Este método debe implementarse en las subclases")

    @staticmethod
    def convierte_dict_a_csv(data: dict):
        # Convierte un diccionario a una cadena CSV (simplificado)
        # Ejemplo básico: genera encabezados y fila de valores separados por comas
        if not data:
            return ""

        headers = ",".join(data[0].keys())
        rows = []
        for entry in data:
            row = ",".join(str(value) for value in entry.values())
            rows.append(row)
        return headers + "\n" + "\n".join(rows)


class LectorCSV(Lector):
    def __init__(self, path: str):
        super().__init__(path)

    def lee_archivo(self, datetime_columns=[]):
        import csv
        datos = []
        if not self._comprueba_extension(".csv"):
            raise ValueError("Archivo no es .csv")
        with open(self.path, newline='', encoding='utf-8') as csvfile:
            lector = csv.DictReader(csvfile)
            for fila in lector:
                # Aquí puedes convertir columnas datetime si quieres
                datos.append(fila)
        return pd.DataFrame(datos)


class LectorJSON(Lector):
    def __init__(self, path: str):
        super().__init__(path)

    def lee_archivo(self):
        import json
        if not self._comprueba_extension(".json"):
            raise ValueError("Archivo no es .json")
        with open(self.path, encoding='utf-8') as jsonfile:
            datos = json.load(jsonfile)
        return pd.DataFrame(datos)


class LectorTXT(Lector):
    def __init__(self, path: str):
        super().__init__(path)

    def lee_archivo(self):
        datos = []
        if not self._comprueba_extension(".txt"):
            raise ValueError("Archivo no es .txt")
        with open(self.path, encoding='utf-8') as txtfile:
            next(txtfile)  # Salta la cabecera
            for linea in txtfile:
                linea = linea.strip()
                if linea:
                    campos = [campo.strip() for campo in linea.split(",")]
                    datos.append({
                        "id": campos[0],
                        "fecha_llegada": campos[1],
                        "retraso": campos[2],
                        "tipo_vuelo": campos[3],
                        "destino": campos[4]
                    })
        return pd.DataFrame(datos)


