#Ejercicio 1
"""
edad_usuario = int(input("Ingrese su edad: "))

if edad_usuario >= 18:
    print("Es mayor de edad.")

#Ejercicio 2
nota_usuario = int(input("Ingrese su nota: "))

if nota_usuario >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3
numero_usuario = int(input("Ingrese un numero par: "))

if numero_usuario % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor ingrese un número par")
"""
#Ejercicio 4
edad_usuario = int(input("Ingrese su edad: "))

if edad_usuario < 12:
    print("Usted es niño/a")
elif edad_usuario >= 12 and edad_usuario < 18:
    print("Usted es adolescente")
elif edad_usuario >= 18 and edad_usuario < 30:
    print("Usted es adulto/a joven")
else:
    print("Usted es adulto/a")
