import mysql.connector as mysql


class CConexion:

    def ConexionDB():
        try:
            conexion = mysql.connect(
                user="root",
                password="1234",
                host="127.0.0.1",
                database="prueba-tecnica",
                port="3306",
            )

            print("Conexión exitosa a la base de datos")
            return conexion

        except mysql.Error as error:
            print("Error al conectarse a la base de datos", error)

    ConexionDB()