import os
from db_manager import DbManager


class CajaModel:
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS caja (
        id_caja INTEGER PRIMARY KEY, 
        fecha TEXT NOT NULL, 
        saldo_inicial INTEGER, 
        saldo_final_efectivo INTEGER, 
        movimientos_efectivo INTEGER, 
        movimientos_tarjeta INTEGER, 
        movimientos_transferencia INTEGER, 
        diferencia_efectivo INTEGER, 
        observaciones TEXT);"""
        
        
        def insert_caja(self, caja):
             
             nc = DbManager()
             nc.conectar() 
                   
             query = """ 
             INSERT INTO caja (
             fecha, 
             saldo_inicial, 
             saldo_final_efectivo, 
             movimientos_efectivo, 
             movimientos_tarjeta, 
             movimientos_transferencia,
             diferencia_efectivo, 
             observaciones) 
             VALUES (
             :fecha, 
             :saldo_inicial, 
             :saldo_final_efectivo, 
             :movimientos_efectivo, 
             :movimientos_tarjeta, 
             :movimientos_transferencia, 
             :diferencia_efectivo, 
             :observaciones); """
       
             nc.ejecutar_sql(query, caja)
             nc.cerrar_conexion()
      

        def select_all_caja(self):
            
             nc = DbManager()
             nc.conectar() 
             
             query = """ 
             SELECT *
             FROM caja;
             """
       
             filas = nc.ejecutar_sql(query)
             nc.cerrar_conexion()
             return filas
 
            

        def select_by_fecha_caja(self, fecha):
            
             nc = DbManager()
             nc.conectar() 
             
             query = """ 
             SELECT *
             FROM caja
             WHERE fecha = :fecha;
             """
       
             filas = nc.ejecutar_sql(query, { 'fecha' : fecha })
             nc.cerrar_conexion()
             return filas
                       
                                             
        def select_by_id_caja(self, id):
            
             nc = DbManager()             
              
             if isinstance(id, int):
                 
                 query = """ 
                 SELECT *
                 FROM caja 
                 WHERE id_caja = :id_caja;
                 """
                 
                 nc.conectar()
                 filas = nc.ejecutar_sql(query, { 'id_caja' : id })
                 nc.cerrar_conexion()
                 return filas
             else:
                 print("el código debe ser un entero")
             
             
            
        def update_caja(self, caja):
            
             nc = DbManager()
             nc.conectar() 
             
             query = """ 
             UPDATE productos SET 
             fecha = :fecha, 
             saldo_inicial = :saldo_inicial, 
             saldo_final_efectivo = :saldo_final_efectivo, 
             movimientos_efectivo = :movimientos_efectivo, 
             movimientos_tarjeta = :movimientos_tarjeta, 
             movimientos_transferencia = :movimientos_transferencia,
             diferencia_efectivo = :diferencia_efectivo, 
             observaciones = :observaciones 
             WHERE id_caja = :id_caja; """
       
             nc.ejecutar_sql(query, caja)
             nc.cerrar_conexion()
      

        def delete_caja(self, id):
                        
             nc = DbManager()
             nc.conectar()
             
             query = """ 
             DELETE FROM caja 
             WHERE id_caja = :id_caja; """
       
             nc.ejecutar_sql(query, { 'codigo_producto' : id })
             nc.cerrar_conexion()
             
             
 
       
#######     TEST     #######


if __name__ == "__main__":
      
      #insert test
      '''
      pdt = {'codigo_producto' : '22', 'nombre_producto' : 'crema + ensalada2', 'descripcion_producto' : 'null', 'formato_producto' : 'unidad', 'precio_producto' : 4500}
      pm = ProductoModel()
      
      pm.insert_producto(pdt)
      '''
      '''
      pdt2 = {'codigo_producto' : '20', 'nombre_producto' : 'crema', 'descripcion_producto' : 'null', 'formato_producto' : 'unidad', 'precio_producto' : 3500}
      pm = ProductoModel()
      
      pm.insert_producto(pdt2)
      '''
      
      #select all test
      '''
      pm = ProductoModel()
      
      filas = pm.select_all_productos()
      
      for fila in filas:
          print(fila)      
      
      
      
      #select by id test
      
      pm = ProductoModel()
      
      filas = pm.select_by_id_productos(202)
      
      for fila in filas:
          print(fila)   
          
         
      '''
      #update test
      '''
      
      pdt3 = {'codigo_producto' : '20', 'nombre_producto' : 'ensalada', 'descripcion_producto' : 'null', 'formato_producto' : 'unidad', 'precio_producto' : 2500}
      
      pm = ProductoModel()
      
      pm.update_producto(pdt3)
      
      pm = ProductoModel()
      
      filas = pm.select_all_productos()
      
      for fila in filas:
          print(fila)       
      
      '''
      
      #delete test
      '''
      pm = ProductoModel()
      
      pm.delete_producto(22)
      
      pm = ProductoModel()
      
      filas = pm.select_all_productos()
      
      for fila in filas:
          print(fila)  
      
      
      '''