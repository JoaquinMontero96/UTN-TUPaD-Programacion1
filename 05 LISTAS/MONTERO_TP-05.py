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

# Ejercicio 2

lista_productos = []

#Solicitud de 5 productos
for i in range(5):
    producto = input(f"Ingrese el producto {i+1}: ")
    #Adición de cada producto a la lista
    lista_productos.append(producto)

#Orden de lista y muestra por pantalla
lista_productos = sorted(lista_productos)
print(lista_productos)

elemento_aeliminar = input("¿Qué producto desea eliminar? ")

if elemento_aeliminar in lista_productos:
    lista_productos.remove(elemento_aeliminar)
    print(f"{elemento_aeliminar} fue eliminado con éxito")
    print(lista_productos)
else:
    print("Producto no encontrado")