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