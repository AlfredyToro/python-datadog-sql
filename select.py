from conexion import conexionsql
try:
    with conexionsql.cursor() as cursor:
        consulta = "SELECT error FROM api_response_log WHERE error like ?;"
        # Para Avengers Endgame
        busqueda = "50"
        cursor.execute(consulta, ("%" + busqueda + "%"))

        # Con fetchall traemos todas las filas
        msje = cursor.fetchall()

        # Recorrer e imprimir
        for msje in msje:
            print(msje)
except Exception as e:
    print("Ocurrió un error al consultar con where: ", e)
finally:
    conexionsql.close()