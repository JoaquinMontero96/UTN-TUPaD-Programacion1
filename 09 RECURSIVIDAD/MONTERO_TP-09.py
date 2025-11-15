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

# # Ejercicio 3
# def potencia_rec(base, exponente):
#     if exponente == 0:
#         return 1
#     if exponente > 0:
#         return base * potencia_rec(base, exponente - 1)

# def probar_potencia():
#     try:
#         base = float(input('Ingrese la base: '))
#         exponente = int(input('Ingrese el exponente (entero): '))
#     except:
#         print('Entrada inválida')
#         return
#     if exponente < 0:
#         print('El exponente debe ser un entero no negativo')
#         return
#     resultado = potencia_rec(base, exponente)
#     print(f'{base} elevado a {exponente} = {resultado}')

# probar_potencia()

# # Ejercicio 4
# def entero_a_binario(n):
#     if n == 0:
#         return ''
#     else:
#         return entero_a_binario(n // 2) + str(n % 2)

# def probar_entero_a_binario():
#     try:
#         num = int(input('Ingrese un número entero no negativo: '))
#     except:
#         print('Número inválido')
#         return
#     if num < 0:
#         print('El número debe ser no negativo')
#         return
#     binario = entero_a_binario(num)
#     binario = binario if binario != '' else '0'
#     print(f'El número {num} en binario es: {binario}')

# probar_entero_a_binario()

# # Ejercicio 5
# def es_palindromo(palabra):
#     palabra = palabra.replace(' ', '').lower()
#     if len(palabra) <= 1:
#         return True
#     if palabra[0] != palabra[-1]:
#         return False
#     return es_palindromo(palabra[1:-1])

# def probar_es_palindromo():
#     palabra = input('Ingrese una palabra o frase: ')
#     if es_palindromo(palabra):
#         print(f'"{palabra}" es un palíndromo.')
#     else:
#         print(f'"{palabra}" no es un palíndromo.')

# probar_es_palindromo()

# # Ejercicio 6
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)

def probar_suma_digitos():
    try:
        num = int(input('Ingrese un número entero no negativo: '))
    except:
        print('Número inválido')
        return
    if num < 0:
        print('El número debe ser no negativo')
        return
    resultado = suma_digitos(num)
    print(f'La suma de los dígitos de {num} es: {resultado}')

probar_suma_digitos()