# Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)

# Ejercicio 2
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

# Ejercicio 3
lista_frutas = list(precios_frutas.keys())

print(lista_frutas)

# Ejercicio 4
lista_contactos = {}

for i in range(5):
    nombre = input("Ingrese nombre del contacto: ")
    num = int(input("Ingrese número de contacto: "))

    lista_contactos[nombre] = num

print(lista_contactos)

nombre_consulta = input("Ingrese nombre a consultar: ")
if nombre_consulta in lista_contactos:
    print(lista_contactos[nombre_consulta])