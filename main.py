import csv

# Carga los países desde un archivo CSV
def cargar_paises(nombre_archivo):
    
    paises = []

    try:

        with open(nombre_archivo, "r", encoding="utf-8") as archivo:

            lector = csv.DictReader(archivo)

            for fila in lector:

                try:

                    pais = {
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]
                    }

                    paises.append(pais)
                
                except ValueError:
                    print("Fila inválida ignorada")
                        
    except FileNotFoundError:
        print("Archivo no encontrado")

    except Exception as error:
        print(f"Error: {error}")

    return paises

# Muestra todos los paises cargados
def mostrar_paises(paises):

    if len(paises) == 0:
        print("No hay países cargados")
        return

    print("\nLISTA DE PAISES")

    for pais in paises:

        print("-----------------------")

        print(f"Nombre: {pais['nombre']}")

        print(f"Población: {pais['poblacion']}")

        print(f"Superficie: {pais['superficie']}")

        print(f"Continente: {pais['continente']}")

# Muestra el menú principal
def mostrar_menu():

    print("\n===== MENU =====")

    print("1 - Mostrar países")

    print("2 - Buscar país")

    print("3 - Agregar país")

    print("4 - Actualizar país")

    print("5 - Filtrar por continente")

    print("6 - Filtrar por población")

    print("7 - Filtrar por superficie")

    print("8 - Ordenar por nombre")

    print("9 - Ordenar por población")

    print("10 - Ordenar por superficie")

    print("11 - Estadísticas")

    print("12 - Eliminar país")

    print("13 - Salir")

    opcion = input("Ingrese una opción: ")

    return opcion

# Busca un país por nombre (coincidencia parcial o exacta)
def buscar_pais(paises):

    nombre_buscar = input("Ingrese nombre del país: ")

    if nombre_buscar.strip() == "":

        print("Nombre inválido")

        return

    encontrado = False

    for pais in paises:

        if nombre_buscar.lower() in pais["nombre"].lower():

            print("\nPAIS ENCONTRADO")

            print(f"Nombre: {pais['nombre']}")

            print(f"Población: {pais['poblacion']}")

            print(f"Superficie: {pais['superficie']}")

            print(f"Continente: {pais['continente']}")

            print("----------------")

            encontrado = True

    if not encontrado:

        print("País no encontrado")


# Agrega un nuevo país a la lista
def agregar_pais(paises):

    try:

        nombre = input("Nombre del país: ")

        poblacion = int(input("Población: "))

        superficie = int(input("Superficie: "))

        continente = input("Continente: ")

        if nombre.strip() == "":

            print("Nombre inválido")

            return

        if poblacion < 0 or superficie < 0:

            print("Población y superficie deben ser positivas")

            return
        
        if continente.strip() == "":

             print("Continente inválido")

             return
        
        for pais in paises:

            if pais["nombre"].lower() == nombre.lower():

                print("Ese país ya existe")

                return

        nuevo_pais = {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }

        paises.append(nuevo_pais)

        print("País agregado correctamente")

    except ValueError:

        print("Error: población y superficie deben ser números")

# Actualiza población y superficie de un país existente
def actualizar_pais(paises):

    nombre_buscar = input("Ingrese país a actualizar: ")

    if nombre_buscar.strip() == "":

        print("Nombre inválido")

        return

    encontrado = False

    for pais in paises:

        if pais["nombre"].lower() == nombre_buscar.lower():

            encontrado = True

            print("\nDatos actuales:")

            print(f"País: {pais['nombre']}")

            print(f"Población: {pais['poblacion']}")

            print(f"Superficie: {pais['superficie']}")

            print(f"Continente: {pais['continente']}")

            try:

                nueva_poblacion = int(
                    input("Nueva población: ")
                )

                nueva_superficie = int(
                    input("Nueva superficie: ")
                )

                if nueva_poblacion < 0 or nueva_superficie < 0:

                    print("Valores inválidos")

                    return

                pais["poblacion"] = nueva_poblacion

                pais["superficie"] = nueva_superficie

                print("País actualizado correctamente")

            except ValueError:

                print("Datos inválidos")

            break

    if not encontrado:

        print("País no encontrado")

# Filtra paises por continente
def filtrar_continente(paises):

    continente_buscar = input("Ingrese continente: ")

    if continente_buscar.strip() == "":

        print("Continente inválido")

        return

    encontrados = False

    print("\nRESULTADOS")

    for pais in paises:

        if pais["continente"].lower() == continente_buscar.lower():

            print("----------------")

            print(f"Nombre: {pais['nombre']}")

            print(f"Población: {pais['poblacion']}")

            print(f"Superficie: {pais['superficie']}")

            print(f"Continente: {pais['continente']}")

            encontrados = True

    if encontrados == False:

        print("No hay países en ese continente")

# Filtra países por rango de población
def filtrar_poblacion(paises):

    try:

        minimo = int(input("Población mínima: "))

        maximo = int(input("Población máxima: "))

        if minimo < 0 or maximo < 0:

            print("Valores inválidos")

            return
        
        if minimo > maximo:

            print("El mínimo no puede ser mayor al máximo")

            return

        encontrados = False

        print("\nRESULTADOS")

        for pais in paises:

            if minimo <= pais["poblacion"] <= maximo:

                print("----------------")

                print(f"Nombre: {pais['nombre']}")

                print(f"Población: {pais['poblacion']}")

                print(f"Superficie: {pais['superficie']}")

                print(f"Continente: {pais['continente']}")

                encontrados = True

        if not encontrados:

            print("No hay resultados")

    except ValueError:

        print("Debe ingresar números")

# Filtra países por rango de superficie
def filtrar_superficie(paises):

    try:

        minimo = int(input("Superficie mínima: "))

        maximo = int(input("Superficie máxima: "))

        if minimo < 0 or maximo < 0:

            print("Valores inválidos")

            return
        
        if minimo > maximo:

            print("El mínimo no puede ser mayor al máximo")

            return

        encontrados = False

        print("\nRESULTADOS")

        for pais in paises:

            if minimo <= pais["superficie"] <= maximo:

                print("----------------")

                print(f"Nombre: {pais['nombre']}")

                print(f"Población: {pais['poblacion']}")

                print(f"Superficie: {pais['superficie']}")

                print(f"Continente: {pais['continente']}")

                encontrados = True

        if not encontrados:

            print("No hay resultados")

    except ValueError:

        print("Debe ingresar números")

# Ordena los países alfabeticamente por nombre
def ordenar_nombre(paises):

    paises_ordenados = paises.copy()

    cantidad = len(paises_ordenados)

    for i in range(cantidad):

        for j in range(cantidad -i - 1):

            nombre_actual = paises_ordenados[j]["nombre"]

            nombre_siguiente = paises_ordenados[j + 1]["nombre"]

            if nombre_actual.lower() > nombre_siguiente.lower():

                auxiliar = paises_ordenados[j]

                paises_ordenados[j] = paises_ordenados[j + 1]

                paises_ordenados[j + 1] = auxiliar

    mostrar_paises(paises_ordenados)

# Ordena los países de menor a mayor población
def ordenar_poblacion(paises):

    paises_ordenados = paises.copy()

    cantidad = len(paises_ordenados)

    for i in range(cantidad):

        for j in range(cantidad - i - 1):

            if paises_ordenados[j]["poblacion"] > paises_ordenados[j + 1]["poblacion"]:

                auxiliar = paises_ordenados[j]

                paises_ordenados[j] = paises_ordenados[j + 1]

                paises_ordenados[j + 1] = auxiliar

    mostrar_paises(paises_ordenados)

# Ordena países por superficie ascendente o descendente
def ordenar_superficie(paises):

    orden = input(
        "Ingrese ASC para ascendente o DESC para descendente: "
    ).lower()

    if orden not in ["asc", "desc"]:

        print("Opción inválida")

        return

    paises_ordenados = paises.copy()

    cantidad = len(paises_ordenados)

    for i in range(cantidad):

        for j in range(cantidad -i - 1):

            cambiar = False

            if orden == "asc":

                cambiar = (
                    paises_ordenados[j]["superficie"] >
                    paises_ordenados[j + 1]["superficie"]
                )

            else:

                cambiar = (
                    paises_ordenados[j]["superficie"] <
                    paises_ordenados[j + 1]["superficie"]
                )

            if cambiar:

                auxiliar = paises_ordenados[j]

                paises_ordenados[j] = paises_ordenados[j + 1]

                paises_ordenados[j + 1] = auxiliar

    mostrar_paises(paises_ordenados)

# Calcula y muestra estadísticas generales de los países cargados
def estadisticas(paises):

    if len(paises) == 0:

        print("No hay datos")

        return

    mayor = paises[0]

    menor = paises[0]

    suma_poblacion = 0

    suma_superficie = 0

    continentes = {}

    for pais in paises:

        if pais["poblacion"] > mayor["poblacion"]:

            mayor = pais

        if pais["poblacion"] < menor["poblacion"]:

            menor = pais

        suma_poblacion += pais["poblacion"]

        suma_superficie += pais["superficie"]

        continente = pais["continente"]

        if continente in continentes:

            continentes[continente] += 1

        else:

            continentes[continente] = 1

    promedio_poblacion = suma_poblacion / len(paises)

    promedio_superficie = suma_superficie / len(paises)

    print("\n===== ESTADISTICAS =====")

    print(f"Mayor población: {mayor['nombre']} {mayor['poblacion']}")

    print(f"Menor población: {menor['nombre']} {menor['poblacion']}")

    print(f"Promedio población: {round(promedio_poblacion, 2)}")

    print(f"Promedio superficie: {round(promedio_superficie, 2)}")

    print("\nPaíses por continente:")

    for continente in continentes:

        print(f"{continente}: {continentes[continente]}")

# Elimina un país de la lista según su nombre
def eliminar_pais(paises):

    nombre_buscar = input("Ingrese país a eliminar: ")

    if nombre_buscar.strip() == "":

        print("Nombre inválido")

        return

    encontrado = False

    for pais in paises:

        if pais["nombre"].lower() == nombre_buscar.lower():

            paises.remove(pais)

            encontrado = True

            print("País eliminado correctamente")

            break

    if encontrado == False:

        print("País no encontrado")

# Guarda la lista actualizada de países en el archivo CSV
def guardar_paises(nombre_archivo, paises):

    try:

        with open(
            nombre_archivo,
            "w",
            newline="",
            encoding="utf-8"
        ) as archivo:

            campos = [
                "nombre",
                "poblacion",
                "superficie",
                "continente"
            ]

            escritor = csv.DictWriter(
                archivo,
                fieldnames=campos
            )

            escritor.writeheader()

            escritor.writerows(paises)

        print("Datos guardados correctamente")

    except Exception as error:

        print(f"Error al guardar: {error}")

# Carga inicial de datos desde el archivo CSV
lista_paises = cargar_paises("paises.csv")

opcion = ""

# Bucle principal del sistema
while opcion != "13":

    opcion = mostrar_menu()

    if opcion == "1":

        mostrar_paises(lista_paises)

    elif opcion == "2":

        buscar_pais(lista_paises)

    elif opcion == "3":

        agregar_pais(lista_paises)
    
    elif opcion == "4":

        actualizar_pais(lista_paises)

    elif opcion == "5":

        filtrar_continente(lista_paises)

    elif opcion == "6":

        filtrar_poblacion(lista_paises)

    elif opcion == "7":

        filtrar_superficie(lista_paises)
    
    elif opcion == "8":

        ordenar_nombre(lista_paises)

    elif opcion == "9":

        ordenar_poblacion(lista_paises)

    elif opcion == "10":
        
        ordenar_superficie(lista_paises) 

    elif opcion == "11":

       estadisticas(lista_paises) 

    elif opcion == "12":

        eliminar_pais(lista_paises)

    elif opcion == "13":

        guardar_paises("paises.csv", lista_paises)

        print("Saliendo del sistema")

    else:

        print("Opción inválida")