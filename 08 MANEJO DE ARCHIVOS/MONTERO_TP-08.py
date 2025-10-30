with open("08 MANEJO DE ARCHIVOS/productos.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        print(f"Producto: {datos[0]} | Precio: {datos[1]} | Cantidad: {datos[2]}")

with open("08 MANEJO DE ARCHIVOS/productos.txt", "a") as archivo:
    producto = input("Ingrese un nuevo producto: ")
    precio = float(input("Ingrese su precio: "))
    stock = int(input("Ingrese la cantidad: "))
    archivo.write(f"\n{producto},{precio},{stock}\n")