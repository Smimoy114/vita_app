# controllers/productos_ctr.py

from services.producto_services import ProductoService

class ProductoController:
    def __init__(self):
        self.service = ProductoService()

    def listar_productos_para_ui(self):
        """
        Obtiene los datos del servicio y los formatea para la tabla de NiceGUI.
        NiceGUI espera una lista de diccionarios donde las claves coinciden con 'field' de las columnas.
        """
        productos_bd = self.service.obtener_todos_los_productos()
        
        # Mapeamos las claves de la BD (con sufijo _producto) a las claves esperadas por NiceGUI
        productos_ui = []
        for p in productos_bd:
            productos_ui.append({
                'codigo': p['codigo_producto'],
                'nombre': p['nombre_producto'],
                'precio': p['precio_producto'],
                'descripcion': p['descripcion_producto'],
                'formato': p['formato_producto'],
            })
        return productos_ui

    def guardar_nuevo_producto(self, datos_ui):
        """
        Recibe datos de la UI y los formatea para el modelo de BD antes de guardar.
        """
        if not datos_ui.get('nombre') or not datos_ui.get('codigo'):
            raise ValueError("El nombre y el código son obligatorios.")

        # Mapeamos las claves de la UI a las claves esperadas por tu modelo de BD
        datos_bd = {
            'codigo_producto': int(datos_ui['codigo']),
            'nombre_producto': datos_ui['nombre'],
            'precio_producto': int(datos_ui['precio']),
            'descripcion_producto': datos_ui['descripcion'],
            'formato_producto': datos_ui['formato'],
        }
        
        self.service.agregar_producto(datos_bd)

