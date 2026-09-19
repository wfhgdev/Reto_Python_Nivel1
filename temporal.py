# Lista para almacenar todos los productos
inventario = []

# Pedir cuántos productos se van a registrar
cantidad = int(input("¿Cuántos productos deseas agregar? "))

# Bucle para solicitar los datos de cada producto
for i in range(cantidad):
    print(f"\n--- Datos para Producto {i + 1} ---")
    
    # Capturar los valores mediante inputs
    identificador = int(input("Identificador (ID): "))
    nombre = input("Nombre: ")
    categoria = input("Categoría: ")
    precio = float(input("Precio: "))
    estado = input("Estado (ej. Nuevo/Usado): ")
    descripcion = input("Descripción: ")
    
    # Crear el diccionario con los datos ingresados
    producto = {
        "identificador": identificador,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "estado": estado,
        "descripcion": descripcion
    }
    
    # Agregar el producto a la lista
    inventario.append(producto)

# Mostrar el resultado final
print("\n=== INVENTARIO REGISTRADO ===")
for p in inventario:
    print(f"[{p['identificador']}] {p['nombre']} | Cat: {p['categoria']} | ${p['precio']:.2f} | Estado: {p['estado']}")
    print(f"    Descripción: {p['descripcion']}")