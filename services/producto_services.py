from models.productos import ProductoModel

class ProductoService:
    def __init__(self):
        self.model = ProductoModel()
        # Asegúrate de crear la tabla al iniciar el servicio (si no existe)
        # Esto depende de cómo implementaste ejecutar_sql para DDL
        # self.model.create_table_if_not_exists() 

    def obtener_todos_los_productos(self):
        """Devuelve una lista de diccionarios de productos."""
        filas = self.model.select_all_productos()
        return filas

    def agregar_producto(self, datos_producto):
        """Inserta un nuevo producto usando el modelo."""
        # Tu modelo ya maneja los valores por defecto para descripción y formato
        self.model.insert_producto(datos_producto)
