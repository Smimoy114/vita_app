import os
from db_manager import DbManager


class ProductosVendidosModel:
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS productos_vendidos (
        id_producto_vendido INTEGER PRIMARY KEY AUTOINCREMENT, 
        id_producto_fk INTEGER NOT NULL, 
        id_venta_fk INTEGER NOT NULL, 
        cantidad INTEGER NOT NULL,
        precio_unitario INTEGER NOT NULL,
        FOREIGN KEY (id_producto_fk) REFERENCES productos(codigo_producto) ON DELETE RESTRICT, 
        FOREIGN KEY (id_venta_fk) REFERENCES ventas(id_venta) ON DELETE CASCADE);
        """
        
        
        def insert_pv(self, pv):
             
             nc = DbManager()
             nc.conectar() 
              
              
             
             query = """ 
             INSERT INTO productos_vendidos (
             id_producto_fk, 
             id_venta_fk, 
             cantidad, 
             precio_unitario) 
             VALUES (
             :id_producto_fk, 
             :id_venta_fk, 
             :cantidad, 
             :precio_unitario); """
       
             nc.ejecutar_sql(query, pv)
             nc.cerrar_conexion()
      

        def select_all_pv(self):
            
             nc = DbManager()
             nc.conectar() 
             
             query = """ 
             SELECT *
             FROM productos_vendidos;
             """
       
             filas = nc.ejecutar_sql(query)
             nc.cerrar_conexion()
             return filas
            
        def select_by_venta_pv(self, id):
            
             nc = DbManager()             
              
             if isinstance(id, int):
                 
                 query = """ 
                 SELECT *
                 FROM productos_vendidos 
                 WHERE id_venta_fk = :id_venta_fk;
                 """
                 
                 nc.conectar()
                 filas = nc.ejecutar_sql(query, {'id_venta_fk' : id })
                 nc.cerrar_conexion()
                 return filas
             else:
                 print("el id debe ser un entero")
             
             
            
        def update_pv(self, pv):
            
             nc = DbManager()
             nc.conectar() 
                
             
             
             query = """ 
             UPDATE productos_vendidos SET 
             cantidad = :cantidad
             WHERE id_producto_vendido = :id_producto_vendido; """
       
             nc.ejecutar_sql(query, pv)
             nc.cerrar_conexion()
      

        def delete_pv(self, id):
                        
             nc = DbManager()
             nc.conectar()
             
             query = """ 
             DELETE FROM productos_vendidos 
             WHERE id_producto_vendido = :id_producto_vendido; """
       
             nc.ejecutar_sql(query, { 'id_producto_vendido' : id })
             nc.cerrar_conexion()
             
             
 
       