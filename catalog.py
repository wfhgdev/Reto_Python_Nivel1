import validations

def add_piece(piece_id, name, category, price, status, description):
    clean_id = validations.validate_not_empty(piece_id, "identificador")
    clean_name = validations.validate_not_empty(name, "nombre")
    clean_category = validations.validate_not_empty(category, "categoría")
    validations.validate_not_empty(price, "precio")
    validations.validate_not_empty(status, "estado")

    clean_price = validations.validate_price(price)
    clean_status = validations.validate_status(status)
    clean_description = validations.validate_description(description)

    piece = {
        "id": clean_id,
        "name": clean_name,
        "category": clean_category,
        "price": clean_price,
        "status": clean_status,
        "description": clean_description,
    }
    return piece

def list_pieces(catalog):
    validations.validate_catalog(catalog)
    names = []
    for piece in catalog:
        names.append(piece["name"])
    return names


def find_piece_by_id(catalog, piece_id):
    validations.validate_catalog(catalog)
    wanted_id = str(piece_id).strip()
    for piece in catalog:
        if piece["id"] == wanted_id:
            return piece
    return None


def piece_exists(catalog, piece_id):
    return find_piece_by_id(catalog, piece_id) is not None


def remove_piece(catalog, piece_id):
    try:
        validations.validate_catalog(catalog)
        piece = find_piece_by_id(catalog, piece_id)
        if piece is None:
            raise ValueError("Pieza no encontrada: " + str(piece_id))
        catalog.remove(piece)
        return True
    except (ValueError, TypeError):
        return False

def get_catalog_summary(catalog):
    validations.validate_catalog(catalog)
    summary = {}
    for piece in catalog:
        category = piece["category"]
        if category in summary:
            summary[category] += 1
        else:
            summary[category] = 1
    return summary


def get_categories(catalog):
    validations.validate_catalog(catalog)
    categories = set()
    for piece in catalog:
        categories.add(piece["category"])
    return categories


def get_pieces_by_category(catalog, category):
    validations.validate_catalog(catalog)
    wanted_category = str(category).strip().lower()
    names = []
    for piece in catalog:
        if piece["category"].lower() == wanted_category:
            names.append(piece["name"])
    return names


def get_average_price(catalog):
    try:
        validations.validate_catalog(catalog)
        if len(catalog) == 0:
            raise ValueError("El catálogo está vacío: no se puede calcular el promedio.")
        total = 0
        for piece in catalog:
            total += piece["price"]
        return total / len(catalog)
    except (ValueError, TypeError):
        return 0

def filter_by_status(catalog, status):
    validations.validate_catalog(catalog)
    clean_status = validations.validate_status(status)
    result = []
    for piece in catalog:
        if piece["status"] == clean_status:
            result.append(piece)
    return result


def filter_by_min_price(catalog, min_price):
    validations.validate_catalog(catalog)
    minimum = validations.validate_number(min_price, "precio mínimo")
    result = []
    for piece in catalog:
        if piece["price"] > minimum:
            result.append(piece)
    return result