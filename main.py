SYSTEM_NAME = "La Tienda de William"
PIECES_TO_REGISTER = 1
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
    show_pieces(catalog, "El catálogo está vacío.")
    print("\nCantidad total de piezas: " + str(len(catalog)))
    print("Categorías únicas: " + str(categories))
    print("Cantidad de categorías: " + str(len(categories)))

def show_pieces(pieces, empty_message):
    if len(pieces) == 0:
        print(empty_message)
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

def run_price_filter(catalog):
    print_section_title("Filtro por precio")
    minimum_price = ask_number("Precio mínimo: ")
    pieces = filter_by_minimum_price(catalog, minimum_price)
    show_pieces(pieces, "No se encontraron piezas con precio superior al indicado.")

def filter_by_minimum_price(catalog, minimum_price):
    result = []
    for piece in catalog:
        if piece["price"] > minimum_price:
            result.append(piece)
    return result

def filter_not_sold(catalog):
    result = []
    for piece in catalog:
        if piece["status"] != STATUS_SOLD:
            result.append(piece)
    return result

#reglas logicas

def run_logical_rules(catalog):
    print_section_title("Reglas de negocio")
    for piece in catalog:
        print(piece["name"] + ": ¿publicable? " + yes_or_no(can_be_published(piece)) + " | ¿requiere revisión? " + yes_or_no(requires_review(piece)))
    print("\nPiezas no vendidas:")
    show_pieces(filter_not_sold(catalog), "Todas las piezas están vendidas.")

def yes_or_no(condition):
    if condition:
        return "Sí"
    return "No"

def can_be_published(piece):
    return piece["price"] > 0 and piece["status"] == STATUS_AVAILABLE

def requires_review(piece):
    return piece["status"] == STATUS_RESERVED or piece["status"] == STATUS_SOLD

#cambios de strings

def run_string_exercises(catalog):
    print_section_title("Manipulación de strings")
    piece = catalog[0]

    concatenated = ("Pieza " + piece["id"] + ": " + piece["name"] + piece["category"] + " - " + str(piece["price"]) + " - " + piece["status"])
    print("Concatenación: " + concatenated)

    interpolated = (f"Pieza {piece['id']}: {piece['name']} ({piece['category']} - {piece['price']} - {piece['status']}")
    print("Interpolación: " + interpolated)

    tags_text = ask_text("\nEtiquetas separadas por comas (ej: retro,anime,limited): ", "Las etiquetas")
    tags = tags_text.split(",")
    print("Etiquetas separadas:", tags)

    print("\nDescripción original: " + piece["description"])
    print("Descripción con reemplazo: " + piece["description"].replace("usada", "certificada"))

    username = input("\nNombre de usuario: ")
    print("Sin espacios al inicio y al final: '" + username.strip() + "'")
    print("Minúsculas: " + username.lower())
    print("Mayúsculas: " + username.upper())
    print("Formato título: " + username.title())
    print("\nNombre de la pieza normalizada: " + piece["name"].strip().title())

# metricas

def calculate_total_price(catalog):
    total = 0
    for piece in catalog:
        total += piece["price"]
    return total

def calculate_average_price(catalog):
    if len(catalog) == 0:
        return 0
    return calculate_total_price(catalog) / len(catalog)

def show_numbered_pieces(catalog):
    print("\nPiezas enumeradas:")
    position = 1
    for piece in catalog:
        print(str(position) + ". " + piece["name"])
        position += 1

def show_metrics(catalog):
    print_section_title("Métricas del catálogo")
    for status in ALLOWED_STATUS:
        amount = len(filter_by_status(catalog, status))
        print("Piezas " + status + "s: " + str(amount))
    print("Total de piezas: " + str(len(catalog)))
    print(f"Suma total de precios: {calculate_total_price(catalog):.2f}")
    print(f"Precio promedio: {calculate_average_price(catalog):.2f}")
    show_numbered_pieces(catalog)


#-------------------

def main():
    show_welcome()
    catalog = capture_catalog(PIECES_TO_REGISTER)
    categories = get_categories(catalog)
    show_catalog_overview(catalog, categories)
    show_data_types(catalog, categories)
    run_status_filters(catalog)
    run_price_filter(catalog)
    run_logical_rules(catalog)
    run_string_exercises(catalog)
    show_metrics(catalog)
main()