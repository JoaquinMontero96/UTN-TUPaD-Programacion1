# # Ejercicio 1
# def imprimir_hola_mundo():
#     print("Hola Mundo!")

# imprimir_hola_mundo()

# #Ejercicio 2
# def saludar_usuario(nombre):
#     print(f"Hola {nombre}!")

# nombre = input("Cual es tu nombre? ")
# saludar_usuario(nombre)

# Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

print("Ingrese sus datos")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)