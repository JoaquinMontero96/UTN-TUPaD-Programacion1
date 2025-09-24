import time  # importar módulo para pausar entre impresiones

# iterar números del 0 al 15 inclusive
for numero_usuario in range(0, 16):
    numero_usuario_binario = ""  # cadena donde construiremos la representación binaria (de derecha a izquierda)

    # caso especial: el número 0 tiene representación "0"
    if numero_usuario == 0:
        numero_usuario_binario = "0"
    else:
        num = numero_usuario  # copia del número para ir dividiendo sin perder el original
        # mientras queden bits por calcular
        while num > 0:
            resto = num % 2  # obtener el bit menos significativo (0 o 1)
            numero_usuario_binario += str(resto)  # concatenar el bit (se va formando invertido)
            num = num // 2  # desplazar a la derecha dividiendo entre 2 (parte entera)

    # la cadena se construyó en orden invertido (LSB -> MSB), por eso la damos vuelta antes de imprimir
    print(numero_usuario_binario[::-1])
    time.sleep(0.5)  # esperar 1 segundo antes de pasar al siguiente número