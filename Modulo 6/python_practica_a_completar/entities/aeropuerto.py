import pandas as pd
from slot import Slot
from datetime import datetime, timedelta

class Aeropuerto:
    def __init__(self, vuelos: pd.DataFrame, slots: int, t_embarque_nat: int, t_embarque_internat: int):
        self.df_vuelos = vuelos
        self.n_slots = slots
        self.slots = {}
        self.tiempo_embarque_nat = t_embarque_nat
        self.tiempo_embarque_internat = t_embarque_internat

        for i in range(1, self.n_slots + 1):
            self.slots[i] = Slot()

        self.df_vuelos['fecha_despegue'] = pd.NaT
        self.df_vuelos['slot'] = 0

    def calcula_fecha_despegue(self, row) -> datetime:
        fecha_llegada = pd.to_datetime(row['fecha_llegada'], dayfirst=True)
        if row['retraso'] == '-' or pd.isna(row['retraso']):
            retraso = timedelta()
        else:
            h, m = map(int, row['retraso'].split(':'))
            retraso = timedelta(hours=h, minutes=m)

        if row['tipo_vuelo'].upper() == 'NAT':
            t_embarque = timedelta(minutes=self.tiempo_embarque_nat)
        else:
            t_embarque = timedelta(minutes=self.tiempo_embarque_internat)

        fecha_min_despegue = fecha_llegada + retraso + t_embarque
        return fecha_min_despegue

    def asigna_slot(self, row) -> pd.Series:
        fecha_despegue_min = self.calcula_fecha_despegue(row)

        if row['tipo_vuelo'].upper() == 'NAT':
            t_embarque = timedelta(minutes=self.tiempo_embarque_nat)
        else:
            t_embarque = timedelta(minutes=self.tiempo_embarque_internat)

        fecha_inicio_ocupacion = fecha_despegue_min - t_embarque
        fecha_fin_ocupacion = fecha_despegue_min

        slot_num = 0
        for num, slot_obj in self.slots.items():
            if slot_obj.slot_esta_libre_intervalo(fecha_inicio_ocupacion, fecha_fin_ocupacion):
                slot_num = num
                break

        if slot_num == 0:
            raise Exception(f"No hay slots disponibles para el vuelo {row['id']}")

        self.slots[slot_num].asigna_vuelo(row['id'], fecha_inicio_ocupacion, fecha_fin_ocupacion)

        return pd.Series({
            'fecha_despegue': fecha_despegue_min,
            'slot': slot_num
        })

    def asigna_slots(self):
        resultados = self.df_vuelos.apply(self.asigna_slot, axis=1)
        self.df_vuelos['fecha_despegue'] = resultados['fecha_despegue']
        self.df_vuelos['slot'] = resultados['slot']


