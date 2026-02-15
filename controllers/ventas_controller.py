
class VentasController:



# Dentro de VentasController
    def guardar_venta_completa(self, venta_dict, lista_productos):
        if venta_dict['id_venta'] is None:
        # INSERT en VentaModel y obtener nuevo ID
            id_nueva = self.m_ventas.insert_venta(venta_dict)
        else:
            # UPDATE en VentaModel
            self.m_ventas.update_venta(venta_dict)
            id_nueva = venta_dict['id_venta']
            # Limpiar productos vendidos anteriores para esta ID (evita duplicados)
            self.m_pv.delete_by_venta(id_nueva) 

        # Insertar los productos de la lista en ProductosVendidosModel
        for p in lista_productos:
            self.m_pv.insert_pv({
                'id_producto_fk': p['codigo_producto'],
                'id_venta_fk': id_nueva,
                'cantidad': p['cantidad'],
                'precio_unitario': p['precio_producto']
            })
        return id_nueva

    def eliminar_venta_total(self, id_venta):
    # Gracias a ON DELETE CASCADE en tu SQL, eliminar la venta borra los productos_vendidos
        self.m_ventas.delete_venta(id_venta)
    