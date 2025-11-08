# Ejercicio 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def mostrar_factoriales():
    try:
        num = int(input('Ingrese un número entero: '))
    except:
        print('Número inválido')
    for i in range(1, num+1):
        print(f'Factorial de {i}: {factorial(i)}')

mostrar_factoriales()