## Parte 3. Almacenamiento de la información

# Al finalizar la captura:

# - el catálogo deberá contener como mínimo 10 piezas.
# - Cada pieza debe conservar todos sus datos.
# - El catálogo debe permitir recorrer y consultar las piezas individualmente.
# - Los datos deben estar organizados de forma que sea posible acceder al identificador, nombre, categoría, precio, estado y descripción de cada pieza.

## Parte 4. Información adicional del catálogo

# Crear también un set con las categorías utilizadas en las piezas registradas.

# El set debe:
# - Contener únicamente categorías.
# - Eliminar automáticamente las categorías repetidas.
# - Permitir conocer cuántas categorías diferentes existen.

SYSTEM_NAME = "La Tienda de William"
PIECES_TO_REGISTER = 1 #input("Digite cantidad de piezas a ingresar: ")
STATUS_AVAILABLE = "disponible"
STATUS_RESERVED = "reservada"
STATUS_SOLD = "vendida"
ALLOWED_STATUS = [STATUS_AVAILABLE, STATUS_RESERVED, STATUS_SOLD]

def show_welcome():
    print("Bienvenido a " + SYSTEM_NAME)
    print("Ha ingresado al catálogo de piezas coleccionables.")

def print_section_title(title):
    print("\n========== " + title + " ==========")

# pedir datos

def capture_catalog(pieces_amount):
    catalog = []
    position = 1
    while position <= pieces_amount:
        print("\nPieza " + str(position) + " de " + str(pieces_amount))
        piece = ask_for_piece(catalog)
        catalog.append(piece)
        position += 1
    return catalog

def ask_for_piece(catalog):
    piece = {
        "id": ask_id("Identificador: ", catalog),
        "name": ask_text("Nombre: ", "El nombre"),
        "category": ask_text("Categoría: ", "La categoría"),
        "price": ask_price("Precio: "),
        "status": ask_status("Estado (disponible/reservada/vendida): "),
        "description": ask_description("Descripción ('usada' o 'certificada'): "),
    }
    return piece

def ask_id(prompt, catalog):
    while True:
        piece_id = ask_text(prompt, "El identificador")
        if id_exists(catalog, piece_id):
            print("Error: ya existe una pieza con ese identificador.")
        else:
            return piece_id

def ask_text(prompt, field_label):
    while True:
        text = input(prompt).strip()
        if text == "":
            print("Error: " + field_label + " no puede estar vacío.")
        else:
            return text

def id_exists(catalog, piece_id):
    for piece in catalog:
        if piece["id"] == piece_id:
            return True
    return False

def ask_price(prompt):
    while True:
        price = ask_number(prompt)
        if price > 0:
            return price
        print("Error: el precio debe ser mayor que cero.")

def ask_number(prompt):
    while True:
        text = input(prompt)
        if is_number(text):
            return float(text.strip().replace(",", "."))
        print("Error: debes introducir un valor numérico.")

def is_number(text):
    text = text.strip().replace(",", ".")
    if text.startswith("-"):
        text = text[1:]
    if text.count(".") > 1:
        return False
    return text.replace(".", "").isdecimal()

def ask_status(prompt):
    while True:
        status = input(prompt).strip().lower()
        if status in ALLOWED_STATUS:
            return status
        print("Error: el estado debe ser: disponible, reservada o vendida.")

def ask_description(prompt):
    while True:
        description = ask_text(prompt, "La descripción")
        text = description.lower()
        if "usada" in text or "certificada" in text:
            return description
        print("Error: la descripción debe contener 'usada' o 'certificada'.")

def get_categories(catalog):
    categories = set()
    for piece in catalog:
        categories.add(piece["category"])
    return categories

# mostrar

def show_catalog_overview(catalog, categories):
    print_section_title("Catálogo completo")
    show_pieces(catalog)
    print("\nCantidad total de piezas: " + str(len(catalog)))
    print("Categorías únicas: " + str(categories))
    print("Cantidad de categorías: " + str(len(categories)))

def show_pieces(pieces):
    if len(pieces) == 0:
        print("El catálogo está vacío.")
    else:
        for piece in pieces:
            show_piece(piece)

def show_piece(piece):
    print("[" + piece["id"] + "] " + piece["name"] + " | " + piece["category"] + " | " + f"{piece['price']:.2f}" + " | " + piece["status"] + " | " + "Descripción: " + piece["description"])

def show_data_types(catalog, categories):
    print_section_title("Tipos de datos")
    piece = catalog[0]
    print("catalog:", type(catalog))
    print("piece:", type(piece))
    print("categories:", type(categories))
    print("id:", type(piece["id"]))
    print("name:", type(piece["name"]))
    print("price:", type(piece["price"]))
    print("status:", type(piece["status"]))

#filtros

def run_status_filters(catalog):
    print_section_title("Filtro por estado")
    for status in ALLOWED_STATUS:
        print("\nPiezas en estado '" + status + "':")
        pieces = filter_by_status(catalog, status)
        show_pieces(pieces, "No hay piezas en estado '" + status + "'.")

def filter_by_status(catalog, status):
    result = []
    for piece in catalog:
        if piece["status"] == status:
            result.append(piece)
    return result


#-------------------
def main():
    show_welcome()
    catalog = capture_catalog(PIECES_TO_REGISTER)
    categories = get_categories(catalog)
    show_catalog_overview(catalog, categories)
    show_data_types(catalog, categories)
    run_status_filters(catalog)
main()