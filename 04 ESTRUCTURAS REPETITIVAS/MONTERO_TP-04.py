# Ejercicio 1
# for cont in range(101):
#     if cont % 2 == 0:
#         print(cont)

# Ejercicio 2
cont = 0
numero_usuario = input("Ingrese un número entero: ")

for digito in numero_usuario:
    cont += 1

print(f"{numero_usuario} tiene {cont} dígitos")