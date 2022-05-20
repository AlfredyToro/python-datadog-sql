from conexion import conexionsql
try:
    with conexionsql.cursor() as cursor:
        consulta = "SELECT name FROM Inventory WHERE name like ?;"
        # Para Avengers Endgame
        busqueda = "per"
        cursor.execute(consulta, ("%" + busqueda + "%"))

        # Con fetchall traemos todas las filas
        fruta = cursor.fetchall()

        # Recorrer e imprimir
        for fruta in fruta:
            print(fruta)
except Exception as e:
    print("Ocurrió un error al consultar con where: ", e)
finally:
    conexionsql.close()