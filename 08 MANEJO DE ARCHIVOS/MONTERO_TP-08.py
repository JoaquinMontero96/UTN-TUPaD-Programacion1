with open("08 MANEJO DE ARCHIVOS/productos.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        print(f"Producto: {datos[0]} | Precio: {datos[1]} | Cantidad: {datos[2]}")

with open("08 MANEJO DE ARCHIVOS/productos.txt", "a") as archivo:
    producto = input("Ingrese un nuevo producto: ")
    precio = float(input("Ingrese su precio: "))
    stock = int(input("Ingrese la cantidad: "))
    archivo.write(f"\n{producto},{precio},{stock}\n")

with open("08 MANEJO DE ARCHIVOS/productos.txt", "r") as archivo:
    lista = []
    for linea in archivo:
        datos = linea.strip().split(",")
        lista.append({
            "nombre" :  datos[0],
            "precio" :  datos[1],
            "cantidad" :  datos[2]
        })

nombre_buscar = input("Ingrese producto a buscar: ").lower()
producto_existe = False

for producto in lista:
    if producto["nombre"] == nombre_buscar:
        producto_existe = True
        print(f"Nombre: {producto["nombre"]} | Precio: {producto["precio"]} | Cantidad: {producto["cantidad"]}")
        break
if not producto_existe:
    print("El producto no se encontró")

with open("08 MANEJO DE ARCHIVOS/productos.txt", "w") as archivo:
    for producto in lista:
        archivo.write(f"{producto["nombre"]},{producto["precio"]},{producto["cantidad"]}\n")