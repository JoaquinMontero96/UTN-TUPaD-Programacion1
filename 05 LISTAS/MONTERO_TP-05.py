# # Ejercicio 1
# lista = [8, 7, 9, 10, 10, 6, 7, 2, 5, 4]
# cantidad_notas = len(lista)
# acum = 0
# nota_minima = lista[0]
# nota_maxima = lista[0]

# print("Notas:")
# #Recorrido de la lista
# for indice in range(cantidad_notas):
#     #Sumatoria de notas
#     acum += lista[indice]
#     #Detección de valor mínimo y máximo
#     if lista[indice] > nota_maxima:
#         nota_maxima = lista[indice]
#     if lista[indice] < nota_minima:
#         nota_minima = lista[indice]
#     #Impresión por pantalla de cada nota
#     print(lista[indice])

# #Cálculo del promedio e impresión por pantalla
# promedio_notas = acum / cantidad_notas
# print(f"El promedio es {round(promedio_notas, 2)}")

# #Impresión por panatalla de nota mínima y máxima
# print(f"La nota mas baja es {nota_minima} y la nota mas alta es {nota_maxima}")

# # Ejercicio 2

# #Definimos las variables
# lista_productos = []

# #Iteramos 5 veces para solicitar productos al usuario y agregarlos a una lista
# for i in range(5):
#     producto = input(f"Ingrese el producto {i+1}: ")
#     lista_productos.append(producto)

# #Ordenamos la lista de menor a mayor y la mostramos por pantalla
# lista_productos = sorted(lista_productos)
# print(lista_productos)

# #Consultamos qué elemento quiere eliminar el usuario
# elemento_aeliminar = input("¿Qué producto desea eliminar? ")

# #Comprobamos si el elemento está en la lista, lo eliminamos e informamos
# if elemento_aeliminar in lista_productos:
#     lista_productos.remove(elemento_aeliminar)
#     print(f"{elemento_aeliminar} fue eliminado con éxito")
#     print(lista_productos)
# else:
#     print("Producto no encontrado")

# # Ejercicio 3
# import random

# #Definimos las variables
# cant_numeros = 15
# lista_pares = []
# lista_impares = []

# #Iteramos x veces y generamos x números aleatorios, luego comprobamos si son pares o impares y lo agregamos a la lista correspondiente
# for i in range(cant_numeros):
#     numero_aleatorio = random.randint(1, 100)
#     if numero_aleatorio % 2 == 0:
#         lista_pares.append(numero_aleatorio)
#     else:
#         lista_impares.append(numero_aleatorio)

# #Mostramos la cantidad de elementos de cada lista
# print(f"Hay {len(lista_pares)} números pares y {len(lista_impares)} números impares")

# Ejercicio 4

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