from models.productos import ProductoModel

class ProductoService:
    def __init__(self):
        self.model = ProductoModel()


    def obtener_todos_los_productos(self):
        """Devuelve una lista de diccionarios de productos."""
        filas = self.model.select_all_productos()
        return filas

    def agregar_producto(self, datos_producto):
        """Inserta un nuevo producto usando el modelo."""
        self.model.insert_producto(datos_producto)


    def update_producto_service(self, datos_producto):
        
        self.model.update_producto(datos_producto)
        
        
    def eliminar_producto_service(self, id):
        
        self.model.delete_producto(id)