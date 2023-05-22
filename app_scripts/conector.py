import mysql.connector

def conexionAdmindb():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='mcdbAdmin',
            password='mariasCookies2023ADMIN/',
            database='mcdb'
            )
        print('Conexion Exitosa.')
        return conexion
    except mysql.connector.Error as error:
        print('Ha ocurrido un inconveniente: {}'.format(error))

def desconexion(conexion):
    if conexion:
        conexion.close()
        print('Desconexion de la base de datos.')

def ejecutarComando(conexion, comando):
    try:
        #cursor=conexion.cursor(buffered=True)
        cursor=conexion.cursor(buffered=True,dictionary=True)
        cursor.execute(comando)
        conexion.commit()
        if comando[0:6] == 'SELECT':
            filas=cursor.fetchall()
            return filas
        """for fila in filas:
            for columna, valor in fila.items():
                print(f'{columna}:{valor}')"""
    except mysql.connector.Error as error:
        print('Ha ocurrido un inconveniente: {}'.format(error))

def ejecutarBusqueda(sentencia):
    conexion=conexionAdmindb()
    diccionario=ejecutarComando(conexion,sentencia)
    desconexion(conexion)
    return diccionario

def insertarBorrarActualizar(sentencia):
    conexion=conexionAdmindb()
    ejecutarComando(conexion,sentencia)
    desconexion(conexion)

"""if __name__ == "__main__":
    conexion=conexionAdmindb()
    #ejecutarComando(conexion, 'SELECT * FROM cliente;')
    desconexion(conexion)"""
