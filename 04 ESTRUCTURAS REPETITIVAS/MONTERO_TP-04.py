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
suma = 0

while True:
    num_usuario = int(input("Ingrese un número entero para acumularlo (ingrese 0 para finalizar): "))
    suma += num_usuario
    if num_usuario == 0:
        break

print(f"La sumatoria de los números ingresados es {suma}")