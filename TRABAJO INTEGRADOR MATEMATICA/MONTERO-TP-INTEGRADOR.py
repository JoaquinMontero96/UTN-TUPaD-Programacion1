import time

# Convierte los números del 0 al 15 a su representación binaria e imprime uno por segundo
for i in range(0, 16):
    # lista que almacenará los bits del número actual
    lista_bits = []

    # caso especial: el 0 se representa como '0'
    if i == 0:
        lista_bits = ['0']
    else:
        num = i
        # descomponer el número en bits mediante divisiones sucesivas por 2
        while num > 0:
            resto = num % 2
            lista_bits.insert(0, str(resto))
            num = num // 2

    numero_binario = ''.join(lista_bits)
    print(numero_binario)
    time.sleep(1)