# # Ejercicio 1
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# precios_frutas["Naranja"] = 1200
# precios_frutas["Manzana"] = 1500
# precios_frutas["Pera"] = 2300

# print(precios_frutas)

# # Ejercicio 2
# precios_frutas["Banana"] = 1330
# precios_frutas["Manzana"] = 1700
# precios_frutas["Melón"] = 2800

# print(precios_frutas)

# # Ejercicio 3
# lista_frutas = list(precios_frutas.keys())

# print(lista_frutas)

# # Ejercicio 4
# lista_contactos = {}

# for i in range(5):
#     nombre = input("Ingrese nombre del contacto: ")
#     num = int(input("Ingrese número de contacto: "))

#     lista_contactos[nombre] = num

# print(lista_contactos)

# nombre_consulta = input("Ingrese nombre a consultar: ")
# if nombre_consulta in lista_contactos:
#     print(lista_contactos[nombre_consulta])

# # Ejercicio 5
# from collections import Counter

# frase = input("Ingrese una frase: ")
# listado_palabras = frase.split()
# palabras = set(listado_palabras)
# cantidad_palabras = dict(Counter(listado_palabras))

# print(palabras)
# print(cantidad_palabras)

# # Ejercicio 6

# alumnos = {}

# for alumno in range(3):
#     nombre_alumno = input("Ingrese el nombre del alumno: ")
#     notas_alumno = []
#     for nota in range(3):
#         nota = int(input(f"Ingrese la nota {nota + 1}: "))
#         notas_alumno.append(nota)
#     alumnos[nombre_alumno] = tuple(notas_alumno)

# print(alumnos)

# for alumno, notas in alumnos.items():
#     promedio = round(sum(notas)/len(notas), 2)
#     print(f"El promedio de {alumno} es {promedio}")

# # Ejercicio 7

# primer_parcial = {1, 2, 4, 9, 14, 15, 16, 18, 20}
# segundo_parcial = {1, 3, 4, 5, 6, 8, 11, 14, 15, 16, 17, 18, 19}

# interseccion = primer_parcial & segundo_parcial
# diferencia_simetrica = primer_parcial ^ segundo_parcial
# union = primer_parcial | segundo_parcial
# print(f"Lista de alumnos que aprobaron ambos parciales: {interseccion}")
# print(f"Lista de alumnos que aprobaron solo un parcial: {diferencia_simetrica}")
# print(f"Lista de alumnos que aprobaron al menos un parcial: {union}")

# Ejercicio 8
import time

def consultar_stock(articulo):
    if articulo in stock:
        print(f"El stock de {articulo} es {stock[articulo]}")
    else:
        print(f"{articulo} no está cargado en el inventario")

def actualizar_stock(articulo):
    if articulo in stock:
        cantidad_actualizar = int(input("Ingrese cantidad a ingresar (en negativo para restar): "))
        stock[articulo] += cantidad_actualizar
        print("Stock actualizado con éxito")
    else:
        print(f"{articulo} no está cargado en el inventario")

def agregar_articulo(articulo):
    if articulo in stock:
        print(f"{articulo} ya se encuentra cargado en el inventario")
    else:
        stock_inicial = int(input("Ingrese el stock inicial: "))
        stock[articulo] = stock_inicial
        print(f"{articulo} fue ingresado con éxito")

stock = {
    "Tenedor": 120,
    "Cuchillo": 100,
    "Cuchara": 90,
    "Vaso": 200,
    "Taza": 120
}

while True:
    print("-----------------------")
    print("Ingrese una opción:")
    print("CONSULTAR STOCK - 1")
    print("ACTUALIZAR STOCK - 2")
    print("AGREGAR ARTÍCULO - 3")
    print("SALIR - 0")
    print("-----------------------")
    opcion_usuario = int(input())
    match opcion_usuario:
        case 0:
            break
        case 1:
            articulo = input("Ingrese el nombre del artículo a consultar: ")
            consultar_stock(articulo)
        case 2:
            articulo = input("Ingrese el nombre del artículo a actualizar: ")
            actualizar_stock(articulo)
        case 3:
            articulo = input("Ingrese el nombre del artículo que desea agregar al inventario: ")
            agregar_articulo(articulo)
        case _:
            print("Opción inválida")
    time.sleep(1)