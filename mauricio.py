# ==============================================================================
# EJEMPLO: CONSULTAR POR CUALQUIER CAMPO (identificador, nombre, etc.) SIN ÍNDICES
# ==============================================================================

claves = ["identificador", "nombre", "categoria", "precio","estado","descripcion"]

diccionario={}
lista_de_diccionarios=[]
cant = int(input("¿Cuántos items quieres añadir?"))
for x in range (0, cant):
  for c in claves:
    valor = input(f"Introduce el valor para {c}:")
    diccionario[c] = valor
  lista_de_diccionarios.append(diccionario)
  diccionario = {}
print(lista_de_diccionarios)

# --- OPCIÓN A: Buscar en la lista por la clave y valor que tú elijas ---
print("\n--- Búsqueda dinámica por cualquier clave/valor ---")
campo_busqueda = input("¿Por qué campo quieres buscar? (ej. identificador, nombre, categoria): ").strip().lower()
valor_buscado = input(f"Introduce el valor de '{campo_busqueda}' que quieres encontrar: ").strip()

encontrados = [elem for elem in lista_de_diccionarios if elem.get(campo_busqueda) == valor_buscado]

if not encontrados:
  print(f"No se encontró ningún item con {campo_busqueda} = '{valor_buscado}'.")
else:
  print(f"Se encontraron {len(encontrados)} item(s):")
  for item in encontrados:
    print(item)