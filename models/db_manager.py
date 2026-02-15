#creacion, coneccion y desconeccion a la db usando sqlite3

#dependencias
import sqlite3
from pathlib import Path


class DbManager:


    def __init__(self):
        base_dir = Path(__file__).resolve().parent
        self.db_name = str(base_dir /'database'/'la_vitaminica.db')
        self.conn = None 
        self.cursor = None 



    def conectar(self):
        try:

            self.conn = sqlite3.connect(self.db_name) 
            self.conn.row_factory = sqlite3.Row 
            self.cursor = self.conn.cursor() 
            print(f"Conexión a '{self.db_name}' establecida exitosamente.") 
            self.conn.execute("PRAGMA foreign_keys = ON;")
            self.conn.execute("PRAGMA journal_mode = WAL;")



        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}") 


    def ejecutar_sql(self, query, params=()):
        if not self.cursor: 
            print("No hay conexión activa.") 
            return None 
        try: 
            self.cursor.execute(query, params) 
            if query.strip().upper().startswith("SELECT"): 
                return self.cursor.fetchall() # Para consultas SELECT 
            else: 
                self.conn.commit() # Para INSERT, UPDATE, DELETE 
                print("Consulta ejecutada exitosamente.") 
                return None 
        except sqlite3.Error as e: 
            print(f"Error al ejecutar la consulta: {e}") 
            self.conn.rollback() # Deshace cambios si hay error 
            return None 


    def cerrar_conexion(self):
        if self.conn:
            self.conn.close() 
            print("Conexión cerrada.") 



if __name__ == "__main__":

    nueva_db = DbManager()
    nueva_db.conectar()

    filas = nueva_db.ejecutar_sql('SELECT * FROM productos;')

    for fila in filas:
        print(fila)

    nueva_db.cerrar_conexion()

    del nueva_db
    print('se elimino el objeto nueva_db')



