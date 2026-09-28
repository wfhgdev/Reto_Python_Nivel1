# Tienda de William Python

Aplicación de consola en Python para la gestión interactiva de un catálogo de piezas coleccionables. Desarrollada de forma modular con validaciones robustas de datos y manejo de excepciones.

---

## 📁 Estructura del Proyecto

El proyecto está organizado en módulos para separar la interfaz de usuario, la lógica de negocio y las validaciones:

```text
├── main.py          # Punto de entrada, menú interactivo y controladores de interfaz (CLI)
├── catalog.py       # Lógica del catálogo (agregar, listar, buscar, filtrar y métricas)
├── validations.py   # Reglas de negocio y validación de tipos, campos y valores permitidos
└── readme.md        # Documentación del proyecto
```

---

## 🚀 Funcionalidades y Opciones del Menú

La aplicación cuenta con un menú interactivo con 13 opciones divididas en operaciones principales y utilidades extra:

### Operaciones Principales
1. **Agregar una pieza**: Registro guiado con validación campo por campo y prevención de IDs duplicados.
2. **Mostrar todas las piezas**: Listado completo de nombres registrados y detalles de cada pieza.
3. **Mostrar piezas disponibles**: Vista filtrada de piezas con estado `disponible`.
4. **Mostrar el precio promedio**: Cálculo automático del valor promedio de las piezas en el catálogo.
5. **Buscar una pieza por identificador**: Búsqueda por `id`.
6. **Eliminar una pieza**: Eliminación segura por `id` con confirmación de existencia.
7. **Salir**: Finaliza la ejecución del programa.

### Opciones Extra y Utilidades
8. **Filtrar piezas por estado**: Búsqueda según estado (`disponible`, `reservada`, `vendida`).
9. **Filtrar piezas por precio mínimo**: Lista piezas cuyo precio supera el valor indicado.
10. **Resumen de piezas por categoría**: Conteo de piezas por categoría y total de categorías únicas.
11. **Piezas de una categoría**: Lista los nombres de piezas pertenecientes a una categoría específica.
12. **Ejercicios de strings**: Demostración de manipulación de cadenas (concatenación, interpolación `f-string`, división con `.split()`, reemplazo con `.replace()`, `.strip()`, `.lower()`, `.upper()` y `.title()`).
13. **Ver tipos de datos**: Inspección en tiempo de ejecución de las estructuras y tipos de datos (`list`, `dict`, `set`, `float`, `str`).

---

## 📋 Estructura de una Pieza

Cada elemento del catálogo almacena los siguientes campos:

| Campo | Tipo | Reglas y Validaciones |
| :--- | :--- | :--- |
| `id` | `str` | Obligatorio, único en el catálogo. |
| `name` | `str` | Obligatorio, texto no vacío. |
| `category` | `str` | Obligatorio, texto no vacío. |
| `price` | `float` | Numérico, estrictamente mayor que cero (`> 0`). |
| `status` | `str` | Permitidos: `disponible`, `reservada`, `vendida`. |
| `description` | `str` | Obligatorio; debe contener la palabra `usada` o `certificada`. |

---

## ⚙️ Requisitos y Ejecución

- **Python**: Versión 3.8 o superior (sin dependencias externas).

### Ejecutar el programa

```bash
python main.py
```

O en sistemas basados en Unix/Linux/macOS:

```bash
python3 main.py
```