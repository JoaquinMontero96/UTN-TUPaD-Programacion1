# # Ejercicio 1
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# def mostrar_factoriales():
#     try:
#         num = int(input('Ingrese un número entero: '))
#     except:
#         print('Número inválido')
#     for i in range(1, num+1):
#         print(f'Factorial de {i}: {factorial(i)}')

# mostrar_factoriales()

# # Ejercicio 2
# def fibonacci(posicion):
#     if posicion == 0 or posicion == 1:
#         return posicion
#     else:
#         return fibonacci(posicion - 1) + fibonacci(posicion - 2)

# def mostrar_fibonacci():
#     try:
#         num = int(input('Ingrese un número entero: '))
#     except:
#         print('Número inválido')
#     if num < 1:
#         print('El número debe ser mayor a 1')
#     else:
#         for i in range(1, num + 1):
#             print(f'Fibonacci {i}: {fibonacci(i)}')

# mostrar_fibonacci()

# Ejercicio 3
def potencia_rec(base, exponente):
    if exponente == 0:
        return 1
    if exponente > 0:
        return base * potencia_rec(base, exponente - 1)

def probar_potencia():
    try:
        base = float(input('Ingrese la base: '))
        exponente = int(input('Ingrese el exponente (entero): '))
    except:
        print('Entrada inválida')
        return
    if exponente < 0:
        print('El exponente debe ser un entero no negativo')
        return
    resultado = potencia_rec(base, exponente)
    print(f'{base} elevado a {exponente} = {resultado}')

probar_potencia()