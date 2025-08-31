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

#Ejercicio 5
password = input("Ingrese una contraseña: ")

if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana < moda:
    print("Hay sesgo negativo")
elif media == mediana and mediana == moda:
    print("No hay sesgo")

print(media, moda, mediana)

#Ejercicio 7
palabra_ingresada = input("Ingrese una frase o palabra: ")

if palabra_ingresada[-1] in "aeiou":
    print(f"{palabra_ingresada}!")
else:
    print(palabra_ingresada)

#Ejercicio 8
nombre_usuario = input("Ingrese su nombre: ")
opcion_nombre = int(input("Ingrese la opcion deseada (1, 2 o 3):"))

if opcion_nombre == 1:
    print(nombre_usuario.upper())
elif opcion_nombre == 2:
    print(nombre_usuario.lower())
elif opcion_nombre == 3:
    print(nombre_usuario.title())

#Ejercicio 9
magnitud_terremoto = float(input("Ingrese la magnitud de un terremoto: "))

if magnitud_terremoto < 3:
    print("La magnitud es muy leve")
elif 3 <= magnitud_terremoto < 4:
    print("La magnitud es leve")
elif 4 <= magnitud_terremoto < 5:
    print("La magnitud es moderada")
elif 5 <= magnitud_terremoto < 6:
    print("La magnitud es fuerte")
elif 6 <= magnitud_terremoto < 7:
    print("La magnitud es muy fuerte")
else:
    print("La magnitud es extrema")
"""
#Ejercicio 10
hemisferio_usuario = input("Ingrese el hemisferio en que se encuentra (N/S): ").upper()
mes_usuario = int(input("Ingrese el mes en el que se encuentra (1 al 12): "))
dia_usuario = int(input("Ingrese el día en el que se encuentra (1 al 31): "))

if 1 <= mes_usuario < 3 or (mes_usuario == 12 and dia_usuario >= 21) or (mes_usuario == 3 and dia_usuario <= 20):
    estacion = "Verano" if hemisferio_usuario == "S" else "Invierno"
elif 3 < mes_usuario < 6 or (mes_usuario == 3 and dia_usuario >= 21) or (mes_usuario == 6 and dia_usuario <= 20):
    estacion = "Otoño" if hemisferio_usuario == "S" else "Primavera"
elif 6 < mes_usuario < 9 or (mes_usuario == 6 and dia_usuario >= 21) or (mes_usuario == 9 and dia_usuario <= 20):
    estacion = "Invierno" if hemisferio_usuario == "S" else "Verano"
elif 9 < mes_usuario < 12 or (mes_usuario == 9 and dia_usuario >= 21) or (mes_usuario == 12 and dia_usuario <= 20):
    estacion = "Primavera" if hemisferio_usuario == "S" else "Otoño"

print(f"Usted está en {estacion}")