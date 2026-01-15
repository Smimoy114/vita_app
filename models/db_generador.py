from db_manager import DbManager
from productos import ProductoModel 
from ventas import VentaModel
from productos_vendidos import ProductosVendidosModel
from egresos import EgresosModel 

def setup_db():
    
    db = DbManager()    
    
    tablas_db =[
        ProductoModel.create_table_query, 
        VentaModel.create_table_query,
        ProductosVendidosModel.create_table_query, 
        EgresosModel.create_table_query 
    ]
    
    db.conectar()
    
    for sql in tablas_db:
        db.ejecutar_sql(sql)
        
    db.cerrar_conexion()
    
      
        
setup_db()        


    