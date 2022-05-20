from conexion import conexionsql
try:
    with conexionsql.cursor() as cursor:
        consulta = "select error,execution_date from api_response_log WHERE error != 'NULL' AND execution_date > dateadd(dd,-30,getdate());"
        # Cursor consulta
        cursor.execute(consulta)

        # Con fetchall traemos todas las filas
        msje = cursor.fetchall()

        # Recorrer e imprimir
        for msje in msje:
            print(msje)
except Exception as e:
    print("Datadog-python connection problem: ", e)
finally:
    conexionsql.close()