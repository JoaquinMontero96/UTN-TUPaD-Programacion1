import time  # Importar módulo para pausar entre impresiones

# Iterar números de 0 a 15 inclusive
for i in range(0, 16):
    lista_bits = []  # lista donde construiremos la representación binaria

    # Caso especial: el número 0 tiene la representación "0"
    if i == 0:
        lista_bits = ['0']
    else:
        num = i  # copia del número para dividir sin perder el original
        # Mientras queden bits por calcular
        while num > 0:
            resto = num % 2  # obtener el bit menos significativo (0 o 1)
            lista_bits.insert(0, str(resto))  # insertar el bit al inicio para formar MSB -> LSB
            num = num // 2  # desplazar a la derecha dividiendo entre 2 (parte entera)

    # La lista ya contiene los bits en orden MSB -> LSB; unir e imprimir
    numero_binario = ''.join(lista_bits)
    print(numero_binario)
    time.sleep(1)  # esperar 1 segundo antes de pasar al siguiente número