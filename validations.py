STATUS_AVAILABLE = "disponible"
STATUS_RESERVED = "reservada"
STATUS_SOLD = "vendida"
ALLOWED_STATUS = [STATUS_AVAILABLE, STATUS_RESERVED, STATUS_SOLD]

WORD_USED = "usada"
WORD_CERTIFIED = "certificada"


def validate_catalog(catalog):
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")


def validate_not_empty(value, field_name):
    if value is None or str(value).strip() == "":
        raise ValueError("El campo '" + field_name + "' no puede estar vacío.")
    return str(value).strip()


def validate_number(value, field_name):
    if type(value) == int or type(value) == float:
        text = format(value, "f")
    else:
        text = str(value).strip().replace(",", ".")

    digits = text
    if digits.startswith("-"):
        digits = digits[1:]

    if digits.count(".") > 1 or not digits.replace(".", "").isdecimal():
        raise ValueError("El campo '" + field_name + "' debe ser un valor numérico.")
    return float(text)


def validate_price(price):
    number = validate_number(price, "precio")
    if number <= 0:
        raise ValueError("El precio debe ser mayor que cero.")
    return number


def validate_status(status):
    clean_status = str(status).strip().lower()
    if clean_status not in ALLOWED_STATUS:
        allowed = ", ".join(ALLOWED_STATUS)
        raise ValueError("Estado no permitido. Opciones válidas: " + allowed + ".")
    return clean_status


def validate_description(description):
    text = validate_not_empty(description, "descripción")
    lower_text = text.lower()
    if WORD_USED not in lower_text and WORD_CERTIFIED not in lower_text:
        raise ValueError("La descripción debe contener la palabra 'usada' o 'certificada'.")
    return text