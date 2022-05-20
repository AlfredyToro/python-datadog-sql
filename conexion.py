import pyodbc
import db_config as db_config

##Connection to ms sql database###
try:
    #conexion = pyodbc.connect(string.destination_driver+string.destination_host+';DATABASE='+string.destination_database+';UID='+string.destination_user+';PWD='+ string.destination_password)
    conexionsql = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+db_config.destination_host+';DATABASE='+db_config.destination_database+';UID='+db_config.destination_user+';PWD='+db_config.destination_password)
except Exception as e:
    # Atrapar error
    print("Ocurrio un error al conectar a SQL Server: ", e)