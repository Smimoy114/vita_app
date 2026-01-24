import os
from datetime import datetime
from db_manager import DbManager


class VentaModel:
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS ventas (
        id_venta INTEGER PRIMARY KEY, 
        cliente TEXT NOT NULL, 
        total INTEGER NOT NULL DEFAULT 0, 
        estado_pago TEXT NOT NULL CHECK (estado_pago IN ('PENDIENTE', 'PAGADO')),
        forma_pago TEXT CHECK (forma_pago IN ('EFECTIVO', 'TARJETA', 'TRANSFERENCIA')), 
        propina INTEGER DEFAULT 0,
        hora_venta TEXT NOT NULL DEFAULT '00:00', 
        fecha_venta TEXT NOT NULL DEFAULT '01-01-2026');"""
        
        
        def insert_venta(self, venta):
             
             nc = DbManager()
             nc.conectar()
             
             ahora = datetime.now()
             fecha_venta = ahora.strftime("%d-%m-%Y")
             hora_venta = ahora.strftime("%H:%M")
             #print(f"fecha = {fecha_venta}")
             #print(f"hora = {hora_venta}")
             
             venta.update({'fecha_venta' : fecha_venta,  'hora_venta' : hora_venta})

                
             if 'forma_pago' not in venta:
                 venta.update({'forma_pago' : ''})
                 
             if 'propina' not in venta:
                 venta.update({'propina' : ''})
             
             if 'estado_pago' not in venta:
                 venta.update({'estado_pago' : 'pendiente'} )

             
             query = """ 
             INSERT INTO ventas (
             cliente, 
             total, 
             estado_pago, 
             forma_pago, 
             propina,
             hora_venta,
             fecha_venta
             ) 
             VALUES (
             :cliente, 
             :total, 
             :estado_pago, 
             :forma_pago, 
             :propina, 
             :hora_venta, 
             :fecha_venta); """
       
             cursor = nc.conexion.cursor() # Accedemos al cursor directamente 
             cursor.execute(query, venta) id_generado = cursor.lastrowid # <--- ESTE ES EL DATO CLAVE 
             nc.conexion.commit() 
             nc.cerrar_conexion() 
             return id_generado
      

        def select_all_ventas(self):
            
             nc = DbManager()
             nc.conectar() 
             
             query = """ 
             SELECT *
             FROM ventas;
             """
       
             filas = nc.ejecutar_sql(query)
             nc.cerrar_conexion()
             return filas
            
        def select_by_id_ventas(self, id):
            
             nc = DbManager()             
              
             if isinstance(id, int):
                 
                 query = """ 
                 SELECT *
                 FROM ventas 
                 WHERE id_venta = :id_venta;
                 """
                 
                 nc.conectar()
                 filas = nc.ejecutar_sql(query, {'id_venta'  : id })
                 nc.cerrar_conexion()
                 return filas
             else:
                 print("el código debe ser un entero")
             
             
        def select_by_fecha_ventas(self, fecha):
            
             nc = DbManager()             
             query = """ 
             SELECT *
             FROM ventas 
             WHERE fecha_venta = :fecha_venta;
             """
                 
             nc.conectar()
             filas = nc.ejecutar_sql(query, { 'fecha_venta' : fecha })
             nc.cerrar_conexion()
             return filas   
             
                
        
        def update_venta(self, venta):
            
             nc = DbManager()
             nc.conectar() 
                
                
             if 'forma_pago' not in venta:
                 venta.update({'forma_pago' : ''})
                 
             if 'propina' not in venta:
                 venta.update({'propina' : ''})
             
             if 'estado_pago' not in venta:
                 venta.update({'estado_pago' : 'PENDIENTE'} )

             
             query = """ 
             UPDATE ventas SET 
             cliente = :cliente, 
             total = :total, 
             estado_pago = :estado_pago, 
             forma_pago =:forma_pago, 
             propina = :propina  
             WHERE id_venta = :id_venta; """
       
             nc.ejecutar_sql(query, venta)
             nc.cerrar_conexion()
      

        def delete_venta(self, id):
                        
             nc = DbManager()
             nc.conectar()
             
             query = """ 
             DELETE FROM ventas 
             WHERE id_venta = :id_venta; """
       
             nc.ejecutar_sql(query, { 'id_venta' : id })
             nc.cerrar_conexion()
             
             
 
  