import os
from db_manager import DbManager


class EgresosModel:
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS egresos (
        id_egreso INTEGER PRIMARY KEY, 
        monto INTEGER NOT NULL, 
        descripcion_egreso TEXT NOT NULL, 
        categoriaTEXT NOT NULL, 
        fecha_egreso TEXT NOT NULL, 
        hora_egreso TEXT NOT NULL);"""
        
        
        def insert_producto(self, egreso):
             
             nc = DbManager()
             nc.conectar() 
                
             
             query = """ 
             INSERT INTO egresos (
             monto, 
             descripcion_egreso, 
             categoria, 
             fecha_egreso, 
             hora_egreso) 
             VALUES (
             :monto, 
             :descripcion_egreso, 
             :categoria, 
             :fecha_egreso, 
             :hora_egreso); """
       
             nc.ejecutar_sql(query, egreso)
             nc.cerrar_conexion()
      

        def select_all_egresos(self):
            
             nc = DbManager()
             nc.conectar() 
             
             query = """ 
             SELECT *
             FROM egresos;
             """
       
             filas = nc.ejecutar_sql(query)
             nc.cerrar_conexion()
             return filas
            
        def select_by_fecha_egreso(self, fecha):
            
              nc = DbManager()             
             
              query = """ 
              SELECT *
              FROM egresos 
              WHERE fecha_egreso = :fecha_egreso;
              """
                 
              nc.conectar()
              filas = nc.ejecutar_sql(query, { 'fecha_egreso' : fecha })
              nc.cerrar_conexion()
              return filas 
             
             
             
        def select_by_id_egresos(self, id):
            
             nc = DbManager()             
              
             if isinstance(id, int):
                 
                 query = """ 
                 SELECT *
                 FROM egrsos 
                 WHERE id_egreso = :id_egreso;
                 """
                 
                 nc.conectar()
                 filas = nc.ejecutar_sql(query, {'id_egreso' : id })
                 nc.cerrar_conexion()
                 return filas
             else:
                 print("el código debe ser un entero")
             
             
             
            
        def update_egreso(self, egreso):
            
             nc = DbManager()
             nc.conectar() 
                
             
             query = """ 
             UPDATE egresos SET 
             monto = :monto, 
             descripcion_egreso = :descripcion_egreso, 
             categoria = :categoria,  
             WHERE id_egreso = :id_egreso; """
       
             nc.ejecutar_sql(query, egreso)
             nc.cerrar_conexion()
      

        def delete_egreso(self, id):
                        
             nc = DbManager()
             nc.conectar()
             
             query = """ 
             DELETE FROM egreso 
             WHERE id_egreso = :id_egreso; """
       
             nc.ejecutar_sql(query, { 'id_egreso' : id })
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
      """
      
      pm = ProductoModel()
      
      filas = pm.select_all_productos()
      
      for fila in filas:
          print(fila)      
      
      
      
      #select by id test
      
      pm = ProductoModel()
      
      filas = pm.select_by_id_productos(202)
      
      for fila in filas:
          print(fila)   
          
         
      """
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