# Tienda de William Python

Programa de consola en Python para gestionar un catálogo básico de piezas coleccionables.

## Funcionalidades

- Registro de 10 piezas por terminal, con validación de datos.
- Catálogo con `id`, `name`, `category`, `price`, `status` y `description`.
- Set de categorías únicas.
- Filtros por estado y por precio mínimo.
- Reglas de publicación, revisión y piezas no vendidas.
- Manipulación de strings (concatenación, interpolación, etiquetas, normalización).
- Menú interactivo y métricas del catálogo.

## Estados permitidos

`disponible`, `reservada`, `vendida`

## Reglas de la descripción

Debe contener la palabra `usada` o `certificada`.

## Ejecución

```bash
python3 main.py
```

Requiere Python 3.8 o superior.