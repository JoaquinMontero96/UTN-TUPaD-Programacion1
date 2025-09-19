# Ejercicio 1 -------------------------------------------------------------------------------------------------------------------------------------
lista = [8, 7, 9, 10, 10, 6, 7, 2, 5, 4]
cantidad_notas = len(lista)
acum = 0
nota_minima = lista[0]
nota_maxima = lista[0]

print("Notas:")
#Recorrido de la lista
for indice in range(cantidad_notas):
    #Sumatoria de notas
    acum += lista[indice]
    #Detección de valor mínimo y máximo
    if lista[indice] > nota_maxima:
        nota_maxima = lista[indice]
    if lista[indice] < nota_minima:
        nota_minima = lista[indice]
    #Impresión por pantalla de cada nota
    print(lista[indice])

#Cálculo del promedio e impresión por pantalla
promedio_notas = acum / cantidad_notas
print(f"El promedio es {round(promedio_notas, 2)}")

#Impresión por panatalla de nota mínima y máxima
print(f"La nota mas baja es {nota_minima} y la nota mas alta es {nota_maxima}")

# Ejercicio 2 -------------------------------------------------------------------------------------------------------------------------------------

#Definimos las variables
lista_productos = []

#Iteramos 5 veces para solicitar productos al usuario y agregarlos a una lista
for i in range(5):
    producto = input(f"Ingrese el producto {i+1}: ")
    lista_productos.append(producto)

#Ordenamos la lista de menor a mayor y la mostramos por pantalla
lista_productos = sorted(lista_productos)
print(lista_productos)

#Consultamos qué elemento quiere eliminar el usuario
elemento_aeliminar = input("¿Qué producto desea eliminar? ")

#Comprobamos si el elemento está en la lista, lo eliminamos e informamos
if elemento_aeliminar in lista_productos:
    lista_productos.remove(elemento_aeliminar)
    print(f"{elemento_aeliminar} fue eliminado con éxito")
    print(lista_productos)
else:
    print("Producto no encontrado")

# Ejercicio 3 -------------------------------------------------------------------------------------------------------------------------------------
import random

#Definimos las variables
cant_numeros = 15
lista_pares = []
lista_impares = []

#Iteramos x veces y generamos x números aleatorios, luego comprobamos si son pares o impares y lo agregamos a la lista correspondiente
for i in range(cant_numeros):
    numero_aleatorio = random.randint(1, 100)
    if numero_aleatorio % 2 == 0:
        lista_pares.append(numero_aleatorio)
    else:
        lista_impares.append(numero_aleatorio)

#Mostramos la cantidad de elementos de cada lista
print(lista_pares, lista_impares)
print(f"Hay {len(lista_pares)} números pares y {len(lista_impares)} números impares")

# Ejercicio 4 -------------------------------------------------------------------------------------------------------------------------------------

#Inicializamos la variables
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_unicos = []

#Recorremos la lista y agregamos cada elemento que no esté en la nueva lista
for dato in datos:
    if not dato in datos_unicos:
        datos_unicos.append(dato)

#Mostramos ambas listas para corroborar el funcionamiento del algoritmo
print(datos)
print(datos_unicos)

# Ejercicio 5 -------------------------------------------------------------------------------------------------------------------------------------

#Inicializamos las variables
lista_alumnos = ["Joaquin", "Gabriel", "Pedro", "Sofia", "Celeste", "Federico", "Simon", "Lucas"]

#Mostramos por pantalla el listado para corroborar el algoritmo
print("Listado de alumnos:")
print(lista_alumnos)

#Consultamos al usuario si desea agregar o eliminar algun alumno y verificamos que elija una de las dos opciones
while True:
    opcion_usuario = input("Desea agregar o eliminar un alumno? A/E ")

#Solicitamos el nombre del alumno a ingresar, lo agregamos a la lista y mostramos por pantalla
    if opcion_usuario.lower() == "a":
        alumno_seleccionado = input("Indique el nombre del alumno que desea ingresar: ")
        lista_alumnos.append(alumno_seleccionado)
        print("Alumno ingresado correctamente")
        print(lista_alumnos)
        break
#Solicitamos el nombre del alumno a eliminar, si está lo eliminamos de la lista y mostramos por pantalla sino informamos
    elif opcion_usuario.lower() == "e":
        alumno_seleccionado = input("Indique el nombre del alumno que desea eliminar: ")
        if alumno_seleccionado in lista_alumnos:
            lista_alumnos.remove(alumno_seleccionado)
            print("Alumno eliminado correctamente")
            print(lista_alumnos)
        else:
            print("Alumno no encontrado")
        break
    else:
        print("Opción incorrecta")

# Ejercicio 6 -------------------------------------------------------------------------------------------------------------------------------------

#Definimos las variables
lista_elementos = [1, 2, 3, 4, 5, 6, 7]
longitud_lista = len(lista_elementos)
ultimo_elemento = lista_elementos[-1]

#Mostramos por pantalla la lista
print(lista_elementos)

#Recorremos la lista en forma decreciente, cambiando el valor de cada elemento a su anterior
for i in range(longitud_lista - 1, 0, -1):
    lista_elementos[i] = lista_elementos[i-1]

#Colocamos el último elemento de la lista al principio
lista_elementos[0] = ultimo_elemento

#Mostramos por pantalla el resultado
print(lista_elementos)

# Ejercicio 7 -------------------------------------------------------------------------------------------------------------------------------------
lista = [[15, 33],[13, 24],[11, 28],[7, 20],[8, 24],[9, 26],[14, 29]]
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
suma_maximas = 0
suma_minimas = 0
dia_maxima_amplitud = 0
maxima_amplitud_termica = 0

for i in range(7):
    suma_maximas += lista[i][1]
    suma_minimas += lista[i][0]
    amplitud_termica = lista[i][1] - lista[i][0]
    if amplitud_termica > maxima_amplitud_termica:
        maxima_amplitud_termica = amplitud_termica
        dia_maxima_amplitud = i


promedio_maximas = round((suma_maximas / 7), 2)
promedio_minimas = round((suma_minimas / 7), 2)

print(f"El promedio de las máximas fue {promedio_maximas} y el promedio de las mínimas fue {promedio_minimas}")
print(f"El día de mas amplitud térmica fue el {dias[dia_maxima_amplitud]} con {maxima_amplitud_termica} grados de diferencia entre la mínima y la máxima")

# Ejercicio 8 -------------------------------------------------------------------------------------------------------------------------------------

# Definimos las variables
matriz_notas = [[6, 8, 8], [7, 4, 10], [6, 7, 9], [9, 10, 9], [5, 7, 9]]
cantidad_alumnos = len(matriz_notas)
promedios_materias = [0, 0, 0]
cantidad_materias = len(promedios_materias)

# Recorremos cada alumno
for alumno in range(cantidad_alumnos):
    suma_notas = 0

# Recorremos cada nota del alumno
    for nota in range(cantidad_materias):
        suma_notas += matriz_notas[alumno][nota] # Sumamos sus calificaciones
        promedios_materias[nota] = promedios_materias[nota] + matriz_notas[alumno][nota] # Sumamos cada nota a la materia correspondiente

    promedio_alumno = round((suma_notas / cantidad_materias), 2) # Calculamos el promedio del alumno
    print(f"El promedio del alumno {alumno + 1} es {promedio_alumno}") # y lo mostramos por pantalla

# Recorremos cada materia
for i in range(cantidad_materias):
    promedios_materias[i] = promedios_materias[i] / cantidad_alumnos # Calculamos el promedio de cada materia
    print(f"El promedio de la materia {i + 1} es {promedios_materias[i]}") # y lo mostramos por pantalla

# Ejercicio 9 -------------------------------------------------------------------------------------------------------------------------------------

# Definimos las variables
tablero = [[" ", 1, 2, 3], ["1", "-", "-", "-"], ["2", "-", "-","-"], ["3", "-", "-","-"]]

# Mostramos el tablero vacío
for fila in tablero:
    print(*fila)

# Iteramos 9 veces (cantidad de turnos posibles)
for i in range(9):
    # Definimos el ícono del jugador de turno
    if i % 2 == 0:
        team = "X"
    else:
        team = "O"

    # Anunciamos de quién es turno
    print(f"Turno de {team}")

    # Solicitamos al usuario ingresar número de fila y columna, verificamos que sea dentro del rango permitido
    while True:
        while True:
            fila_usuario = int(input("Ingrese n° de fila (1 a 3): "))
            if fila_usuario < 1 or fila_usuario > 3:
                print("Por favor ingrese del 1 al 3")
            else:
                break
        while True:
            columna_usuario = int(input("Ingrese n° de columna (1 a 3): "))
            if columna_usuario < 1 or columna_usuario > 3:
                print("Por favor ingrese del 1 al 3")
            else:
                break

        # Verificamos que el casillero no esté ocupado
        if tablero[fila_usuario][columna_usuario] != "-":
            print("Casillero ya ocupado")
        else:
            tablero[fila_usuario][columna_usuario] = team # Asignamos el lugar ingresado
            break

    # Mostramos por pantalla como queda el tablero
    for fila in tablero:
        print(*fila)

# Finalizamos la partida
print("Partida finalizada")

# Ejercicio 10 -------------------------------------------------------------------------------------------------------------------------------------

# Definimos las variables
ventas_diarias = [
    [10000, 15000, 12000, 13000, 9000, 8000, 12000],
    [15000, 3000, 4000, 3300, 4700, 6200, 2100],
    [2800, 5000, 4000, 3800, 7440, 6500, 3100],
    [9000, 16000, 21000, 30000, 40000, 25000, 12000]]
cantidad_productos = len(ventas_diarias)
importe_mayor_ventas = 0
dia_mayor_ventas = 0
producto_mas_vendido = [0, 0]
totales_diarios = [["Lunes", 0], ["Martes", 0], ["Miercoles", 0], ["Jueves", 0], ["Viernes", 0], ["Sabado", 0], ["Domingo", 0]]

# Recorremos cada producto
for producto in range(cantidad_productos):
    total_vendido_producto = 0 # Inicializamos en 0 para cada producto

    # Recorremos cada dia y almacenamos lo que se vendió de cada uno
    for dia in range(7):
        total_vendido_producto += ventas_diarias[producto][dia]
        totales_diarios[dia][1] = totales_diarios[dia][1] + ventas_diarias[producto][dia]

    print(f"Total vendido del producto {producto + 1}: {total_vendido_producto}") # Mostramos el total vendido de cada producto

    # Definimos qué producto se vendió mas y almacenamos su índice e importe
    if total_vendido_producto > producto_mas_vendido[0]:
        producto_mas_vendido[0] = total_vendido_producto
        producto_mas_vendido[1] = producto + 1

print(f"El producto mas vendido fue el {producto_mas_vendido[1]} con $ {producto_mas_vendido[0]}") # Mostramos el producto mas vendido y su facturación total

# Recorremos el listado de facturación diaria y determinamos cual fue el dia con mayor volumen
for dia in range(7):
    if totales_diarios[dia][1] > importe_mayor_ventas:
        importe_mayor_ventas = totales_diarios[dia][1]
        dia_mayor_ventas = dia

print(f"El día de mayor ventas fue el {totales_diarios[dia_mayor_ventas][0]} con $ {totales_diarios[dia_mayor_ventas][1]}") # Mostramos el día con mayor facturación