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

# #Ejercicio 5
# from collections import Counter

# frase = input("Ingrese una frase: ")
# listado_palabras = frase.split()
# palabras = set(listado_palabras)
# cantidad_palabras = dict(Counter(listado_palabras))

# print(palabras)
# print(cantidad_palabras)

# Ejercicio 6

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

# Ejercicio 7

primer_parcial = {1, 2, 4, 9, 14, 15, 16, 18, 20}
segundo_parcial = {1, 3, 4, 5, 6, 8, 11, 14, 15, 16, 17, 18, 19}

interseccion = primer_parcial & segundo_parcial
diferencia_simetrica = primer_parcial ^ segundo_parcial
union = primer_parcial | segundo_parcial
print(f"Lista de alumnos que aprobaron ambos parciales: {interseccion}")
print(f"Lista de alumnos que aprobaron solo un parcial: {diferencia_simetrica}")
print(f"Lista de alumnos que aprobaron al menos un parcial: {union}")