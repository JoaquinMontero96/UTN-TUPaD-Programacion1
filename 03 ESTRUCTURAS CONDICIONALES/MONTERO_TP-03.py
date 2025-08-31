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
"""
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