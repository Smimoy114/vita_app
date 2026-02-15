"""modelo de productos, crea las consultas para realizar el CRUD a la base de datos"""

import os
from models.db_manager import DbManager


class ProductoModel:

    """string encargado de crear la tabla en caso de no existir previamente en la db mediante la funcion de db_generador"""
    create_table_query = """
        CREATE TABLE IF NOT EXISTS productos (
        codigo_producto INTEGER PRIMARY KEY,
        nombre_producto TEXT NOT NULL,
        precio_producto INTEGER NOT NULL,
        descripcion_producto TEXT,
        formato_producto TEXT);"""

    """insert_producto se encarga de crear el registro en la db, recibe un diccionario de producto"""
    def insert_producto(self, producto):

        nc = DbManager()
        nc.conectar()


        query = """
             INSERT INTO productos (
             codigo_producto,
             nombre_producto,
             precio_producto,
             descripcion_producto,
             formato_producto)
             VALUES (
             :codigo_producto,
             :nombre_producto,
             :precio_producto,
             :descripcion_producto,
             :formato_producto); """

        nc.ejecutar_sql(query, producto)
        nc.cerrar_conexion()


    """select_all_productos devuelve una lista con todos los productos en la tabla"""
    def select_all_productos(self):

        nc = DbManager()
        nc.conectar()

        query = """
             SELECT *
             FROM productos;
        """

        filas = nc.ejecutar_sql(query)
        nc.cerrar_conexion()
        return filas


    """update_producto recibe un diccionario con datos a actualizar del producto"""
    def update_producto(self, producto):

        nc = DbManager()
        nc.conectar()

        query = """
             UPDATE productos SET
             nombre_producto = :nombre_producto,
             precio_producto = :precio_producto,
             descripcion_producto = :descripcion_producto,
             formato_producto = :formato_producto
             WHERE codigo_producto =:codigo_producto; """

        nc.ejecutar_sql(query, producto)
        nc.cerrar_conexion()


    def delete_producto(self, id):

        nc = DbManager()
        nc.conectar()

        query = """ 
             DELETE FROM productos 
             WHERE codigo_producto = :codigo_producto; """

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

    pm = ProductoModel()

    filas = pm.select_all_productos()

    for fila in filas:
        print(fila)      



        #select by id test

        pm = ProductoModel()

        filas = pm.select_by_id_productos(202)

        for fila in filas:
            print(fila)   



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
