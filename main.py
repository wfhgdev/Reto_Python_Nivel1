from catalog import (
    add_piece,
    list_pieces,
    find_piece_by_id,
    piece_exists,
    remove_piece,
    get_catalog_summary,
    get_categories,
    get_pieces_by_category,
    get_average_price,
    filter_by_status,
    filter_by_min_price,
)
from validations import (
    STATUS_AVAILABLE,
    validate_not_empty,
    validate_number,
    validate_price,
    validate_status,
    validate_description,
)

SYSTEM_NAME = "La Tienda de William"

def show_welcome():
    print("Bienvenido a " + SYSTEM_NAME)
    print("Ha ingresado al catálogo de piezas coleccionables.")

def print_section_title(title):
    print("\n========== " + title + " ==========")

def ask_text(prompt, field_name):
    while True:
        try:
            return validate_not_empty(input(prompt), field_name)
        except ValueError as error:
            print("Error: " + str(error))

def ask_id(prompt, catalog):
    while True:
        piece_id = ask_text(prompt, "identificador")
        if piece_exists(catalog, piece_id):
            print("Error: ya existe una pieza con ese identificador.")
        else:
            return piece_id


def ask_number(prompt, field_name):
    while True:
        try:
            return validate_number(input(prompt), field_name)
        except ValueError as error:
            print("Error: " + str(error))


def ask_price(prompt):
    while True:
        try:
            return validate_price(input(prompt))
        except ValueError as error:
            print("Error: " + str(error))

def ask_status(prompt):
    while True:
        try:
            return validate_status(input(prompt))
        except ValueError as error:
            print("Error: " + str(error))

def ask_description(prompt):
    while True:
        try:
            return validate_description(input(prompt))
        except ValueError as error:
            print("Error: " + str(error))

def show_piece(piece):
    print("[" + piece["id"] + "] " + piece["name"] + " | " + piece["category"]
          + " | " + f"{piece['price']:.2f}" + " | " + piece["status"]
          + " | Descripción: " + piece["description"])


def show_pieces(pieces, empty_message):
    if len(pieces) == 0:
        print(empty_message)
    else:
        for piece in pieces:
            show_piece(piece)


def show_data_types(catalog):
    print_section_title("Tipos de datos")
    if len(catalog) == 0:
        print("Agrega al menos una pieza para poder ver los tipos de datos.")
        return
    piece = catalog[0]
    print("catalog:", type(catalog))
    print("piece:", type(piece))
    print("categories:", type(get_categories(catalog)))
    print("id:", type(piece["id"]))
    print("name:", type(piece["name"]))
    print("price:", type(piece["price"]))
    print("status:", type(piece["status"]))

def handle_add_piece(catalog):
    print_section_title("Agregar una pieza")
    piece_id = ask_id("Identificador: ", catalog)
    name = ask_text("Nombre: ", "nombre")
    category = ask_text("Categoría: ", "categoría")
    price = ask_price("Precio: ")
    status = ask_status("Estado (disponible/reservada/vendida): ")
    description = ask_description("Descripción ('usada' o 'certificada'): ")

    piece = add_piece(piece_id, name, category, price, status, description)
    catalog.append(piece)
    print("Pieza agregada correctamente.")


def handle_show_all(catalog):
    print_section_title("Todas las piezas")
    names = list_pieces(catalog)
    if len(names) > 0:
        print("Piezas registradas (" + str(len(names)) + "): " + ", ".join(names) + "\n")
    show_pieces(catalog, "El catálogo está vacío.")


def handle_show_available(catalog):
    print_section_title("Piezas disponibles")
    available = filter_by_status(catalog, STATUS_AVAILABLE)
    show_pieces(available, "No hay piezas disponibles.")


def handle_average_price(catalog):
    print_section_title("Precio promedio")
    if len(catalog) == 0:
        print("El catálogo está vacío: no hay precio promedio.")
    else:
        print(f"Precio promedio: {get_average_price(catalog):.2f}")


def handle_search_piece(catalog):
    print_section_title("Buscar una pieza")
    piece_id = ask_text("Identificador a buscar: ", "identificador")
    piece = find_piece_by_id(catalog, piece_id)
    if piece is None:
        print("No se encontró ninguna pieza con el identificador '" + piece_id + "'.")
    else:
        show_piece(piece)


def handle_remove_piece(catalog):
    print_section_title("Eliminar una pieza")
    piece_id = ask_text("Identificador a eliminar: ", "identificador")
    if remove_piece(catalog, piece_id):
        print("Pieza eliminada correctamente.")
    else:
        print("No se pudo eliminar: no existe una pieza con el identificador '" + piece_id + "'.")


def handle_filter_status(catalog):
    print_section_title("Filtrar por estado")
    status = ask_status("Estado (disponible/reservada/vendida): ")
    pieces = filter_by_status(catalog, status)
    show_pieces(pieces, "No hay piezas en estado '" + status + "'.")

def handle_filter_price(catalog):
    print_section_title("Filtrar por precio mínimo")
    minimum = ask_number("Precio mínimo: ", "precio mínimo")
    pieces = filter_by_min_price(catalog, minimum)
    show_pieces(pieces, "No se encontraron piezas con precio superior al indicado.")

def handle_summary(catalog):
    print_section_title("Resumen por categoría")
    summary = get_catalog_summary(catalog)
    if len(summary) == 0:
        print("El catálogo está vacío.")
    else:
        for category in summary:        # recorrer un diccionario da sus claves
            print(category + ": " + str(summary[category]) + " pieza(s)")
        print("Categorías diferentes: " + str(len(summary)))

def handle_pieces_by_category(catalog):
    print_section_title("Piezas de una categoría")
    category = ask_text("Categoría: ", "categoría")
    names = get_pieces_by_category(catalog, category)
    if len(names) == 0:
        print("No hay piezas en la categoría '" + category + "'.")
    else:
        print("Piezas en '" + category + "': " + ", ".join(names))

def handle_string_exercises(catalog):
    print_section_title("Manipulación de strings")
    if len(catalog) == 0:
        print("Agrega al menos una pieza para hacer los ejercicios de strings.")
        return
    piece = catalog[0]

    concatenated = ("Pieza " + piece["id"] + ": " + piece["name"] + " ("
                    + piece["category"] + ") - " + str(piece["price"])
                    + " - " + piece["status"])
    print("Concatenación: " + concatenated)

    interpolated = (f"Pieza {piece['id']}: {piece['name']} ({piece['category']})"
                    f" - {piece['price']} - {piece['status']}")
    print("Interpolación: " + interpolated)

    tags_text = ask_text("\nEtiquetas separadas por comas (ej: retro,anime,limited): ", "etiquetas")
    tags = tags_text.split(",")
    print("Etiquetas separadas:", tags)

    print("\nDescripción original: " + piece["description"])
    print("Descripción con reemplazo: " + piece["description"].replace("usada", "certificada"))

    username = input("\nNombre de usuario: ")
    print("Sin espacios al inicio y al final: '" + username.strip() + "'")
    print("Minúsculas: " + username.lower())
    print("Mayúsculas: " + username.upper())
    print("Formato título: " + username.title())

    print("\nNombre de la pieza normalizado: " + piece["name"].strip().title())

def show_menu():
    print("\n===== MENÚ =====")
    print("1. Agregar una pieza")
    print("2. Mostrar todas las piezas")
    print("3. Mostrar piezas disponibles")
    print("4. Mostrar el precio promedio")
    print("5. Buscar una pieza por identificador")
    print("6. Eliminar una pieza")
    print("7. Salir")
    print("--- Opciones extra ---")
    print("8. Filtrar piezas por estado")
    print("9. Filtrar piezas por precio mínimo")
    print("10. Resumen de piezas por categoría")
    print("11. Piezas de una categoría")
    print("12. Ejercicios de strings")
    print("13. Ver tipos de datos")


def run_menu(catalog):
    option = ""
    while option != "7":
        show_menu()
        option = input("Elige una opción: ").strip()
        try:
            if option == "1":
                handle_add_piece(catalog)
            elif option == "2":
                handle_show_all(catalog)
            elif option == "3":
                handle_show_available(catalog)
            elif option == "4":
                handle_average_price(catalog)
            elif option == "5":
                handle_search_piece(catalog)
            elif option == "6":
                handle_remove_piece(catalog)
            elif option == "7":
                print("\nGracias por usar " + SYSTEM_NAME + ". ¡Hasta pronto!")
            elif option == "8":
                handle_filter_status(catalog)
            elif option == "9":
                handle_filter_price(catalog)
            elif option == "10":
                handle_summary(catalog)
            elif option == "11":
                handle_pieces_by_category(catalog)
            elif option == "12":
                handle_string_exercises(catalog)
            elif option == "13":
                show_data_types(catalog)
            else:
                print("Error: opción no válida. Elige un número del 1 al 13.")
        except (ValueError, TypeError) as error:
            print("Error: " + str(error))

def main():
    show_welcome()
    catalog = []            # el catálogo empieza vacío
    run_menu(catalog)

main()