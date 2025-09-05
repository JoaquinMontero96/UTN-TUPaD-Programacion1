# Ejercicio 1
# for cont in range(101):
#     if cont % 2 == 0:
#         print(cont)

# Ejercicio 2
# cont = 0
# numero_usuario = input("Ingrese un número entero: ")

# for digito in numero_usuario:
#     cont += 1

# print(f"{numero_usuario} tiene {cont} dígitos")

# Ejercicio 3
# suma = 0
# num1 = int(input("Ingrese un número entero: "))
# num2 = int(input("Ingrese otro número entero: "))

# for cont in range(num1+1, num2):
#     suma += cont

# print(f"La suma de todos los números enteros comprendidos entre {num1} y {num2} (sin incluirlos) es {suma}")

# Ejercicio 4
# suma = 0

# while True:
#     num_usuario = int(input("Ingrese un número entero para acumularlo (ingrese 0 para finalizar): "))
#     suma += num_usuario
#     if num_usuario == 0:
#         break

# print(f"La sumatoria de los números ingresados es {suma}")

# Ejercicio 5
# import random

# numero_aleatorio = random.randint(0, 9)
# intentos = 0

# while True:
#     print("Adivine el número! Ingrese un número entre 0 y 9")
#     numero_usuario = int(input())
#     intentos += 1
#     if numero_usuario == numero_aleatorio:
#         break
#     else:
#         print("Número equivocado!")

# print(f"Genial! Adivinaste el número, te costó {intentos} intentos")

# Ejercicio 6
# for cont in range(100, 0, -1):
#     if cont % 2 == 0:
#         print(cont)

# Ejercicio 7
# numero_usuario = int(input("Ingrese un número entero: "))
# suma = 0

# for cont in range(numero_usuario+1):
#     suma += cont

# print(f"La sumatoria de todos los números enteros comprendidos entre 0 y {numero_usuario} es {suma}")

# Ejercicio 8
# pares = 0
# impares = 0
# positivos = 0
# negativos = 0
# cant_num = 100

# for cont in range(1, cant_num+1):
#     num_usuario = int(input(f"Ingrese número {cont}: "))

#     if num_usuario % 2 == 0:
#         pares += 1
#     else:
#         impares += 1

#     if num_usuario > 0:
#         positivos += 1
#     elif num_usuario < 0:
#         negativos += 1

# print(f"En los {cant_num} números que ingresaste hay {pares} pares y {impares} impares. A su vez {positivos} positivos y {negativos} negativos.")

# Ejercicio 9
import statistics
cant_num = 100
numeros = []

for cont in range(1, cant_num+1):
    num_usuario = int(input(f"Ingrese número {cont}: "))
    numeros.append(num_usuario)

print(f"La media de los números ingresados es {statistics.mean(numeros)}")