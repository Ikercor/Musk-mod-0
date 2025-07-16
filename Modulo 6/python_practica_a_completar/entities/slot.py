
from datetime import datetime

class Slot:
    def __init__(self):
        self.ocupaciones = []  # Lista de tuplas (fecha_inicial, fecha_final)

    def asigna_vuelo(self, vuelo_id, fecha_inicial: datetime, fecha_final: datetime):
        self.ocupaciones.append((fecha_inicial, fecha_final))

    def slot_esta_libre_intervalo(self, fecha_inicio, fecha_fin):
        for inicio, fin in self.ocupaciones:
            # Si el intervalo nuevo se solapa con algún intervalo existente, no está libre
            if not (fecha_fin <= inicio or fecha_inicio >= fin):
                return False
        return True