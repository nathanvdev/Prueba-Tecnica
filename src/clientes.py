from conexion import *

class CClientes:

    def agregarCliente(nombre, apellido, nacimiento, celular, dpi):
        try:
            conexion = CConexion.ConexionDB()
            cursor = conexion.cursor()

            sql = "INSERT INTO Cliente (nombre, apellido, nacimiento, celular, dpi) VALUES (%s, %s, %s, %s, %s)"
            valores = (nombre, apellido, nacimiento, celular, dpi)

            cursor.execute(sql, valores)
            conexion.commit()
            print(cursor.rowcount, "Cliente agregado con exito")
            conexion.close()
            return True
        
        except mysql.Error as error:
            print("Error al agregar un nuevo Cliente", error)
            return False


    def obtenerClientes():
        try:
            conexion = CConexion.ConexionDB()
            cursor = conexion.cursor()

            sql = "SELECT * FROM Cliente"
            cursor.execute(sql)
            clientes = cursor.fetchall()
            conexion.close()

            return clientes

        except mysql.Error as error:
            print("Error al obtener los clientes", error)
            return False

    def obtenerCliente(id):
        try:
            conexion = CConexion.ConexionDB()
            cursor = conexion.cursor()

            sql = "SELECT * FROM Cliente WHERE id = %s"
            valores = (id,)

            cursor.execute(sql, valores)
            Cliente = cursor.fetchone()
            conexion.close()

            return Cliente

        except mysql.Error as error:
            print("Error al obtener el Cliente", error)
            return False

    def actualizarCliente(id, nombre, apellido, nacimiento, celular, dpi):
        try:
            conexion = CConexion.ConexionDB()
            cursor = conexion.cursor()

            sql = "UPDATE Cliente SET nombre = %s, apellido = %s, nacimiento = %s, celular = %s, dpi = %s WHERE id = %s"
            valores = (nombre, apellido, nacimiento, celular, dpi, id)

            cursor.execute(sql, valores)
            conexion.commit()
            print(cursor.rowcount, "Cliente actualizado con exito")
            conexion.close()
            return True
        
        except mysql.Error as error:
            print("Error al actualizar el Cliente", error)
            return False

    def eliminarCliente(id):
        try:
            conexion = CConexion.ConexionDB()
            cursor = conexion.cursor()

            sql = "DELETE FROM Cliente WHERE id = %s"
            valores = (id,)

            cursor.execute(sql, valores)
            conexion.commit()
            print(cursor.rowcount, "Cliente eliminado con exito")
            conexion.close()
            return True

        except mysql.Error as error:
            print("Error al eliminar el Cliente", error)
            return False

    
    
            
