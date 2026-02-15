from models.ventas import VentaModel
from datetime import datetime

class VentaService:
    def __init__(self):
        self.model = VentaModel

    def obtener_todas_las_ventas:
        filas = self.model.select_all_ventas()
        return filas

    def obtener_ventas_activas:
        filas = self.model.select_by_estado_y_fecha_ventas()
        return filas


