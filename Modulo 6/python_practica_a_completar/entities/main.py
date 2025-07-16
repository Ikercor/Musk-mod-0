import os
import pandas as pd
from lector import LectorTXT, LectorCSV, LectorJSON
from aeropuerto import Aeropuerto

def preprocess_data(df_list):
    # Unir todos los DataFrames en uno solo y limpiar datos si es necesario
    df = pd.concat(df_list, ignore_index=True)
    # Por ejemplo, limpiar espacios, convertir columnas, etc. (opcional)
    df['retraso'] = df['retraso'].replace('-', '00:00')  # Para uniformizar
    return df

if __name__ == '__main__':
    path_1 = os.path.abspath('data\Vuelos_1.txt')
    path_2 = os.path.abspath('data\Vuelos_2.csv')
    path_3 = os.path.abspath('data\Vuelos_3.json')

    # Crear lectores
    lector_txt = LectorTXT(path_1)
    lector_csv = LectorCSV(path_2)
    lector_json = LectorJSON(path_3)

    # Leer datos
    df_txt = lector_txt.lee_archivo()
    df_csv = lector_csv.lee_archivo()
    df_json = lector_json.lee_archivo()

    # Preprocesar datos
    df_vuelos = preprocess_data([df_txt, df_csv, df_json])

    # Parámetros del aeropuerto
    n_slots = 5
    t_embarque_nat = 30      # minutos
    t_embarque_internat = 60 # minutos

    # Crear aeropuerto
    aeropuerto = Aeropuerto(df_vuelos, n_slots, t_embarque_nat, t_embarque_internat)

    # Asignar slots
    aeropuerto.asigna_slots()

    # Mostrar resultados
    print(aeropuerto.df_vuelos)


