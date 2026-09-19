# Construir un programa en Python que funcione por consola y permita gestionar un catálogo básico de piezas coleccionables.

# El programa debe permitir registrar piezas, consultar la información del catálogo, aplicar filtros, calcular métricas y validar los datos ingresados por el usuario.

# # Reglas de negocio
# ## Estructura de datos de una pieza
# Cada pieza debe contener los siguientes datos:

# | Campo | Tipo de dato esperado | Descripción |
# |---|---|---|
# | `id` | Texto | Identificador único de la pieza |
# | `name` | Texto | Nombre de la pieza |
# | `category` | Texto | Categoría a la que pertenece |
# | `price` | Número decimal | Precio de venta o valor de referencia |
# | `status` | Texto | Estado actual de la pieza |
# | `description` | Texto | Descripción detallada de la pieza |

# Las piezas deben almacenarse dentro de una colección principal llamada `catalog`.
# La información de cada pieza debe organizarse utilizando una estructura de datos que permita asociar cada campo con su valor correspondiente.

# ## Estados permitidos
# Cada pieza solo puede tener uno de los siguientes estados:
# - `disponible` --->  la pieza puede venderse o intercambiarse.
# - `reservada` ---> la pieza está apartada temporalmente para un comprador.
# - `vendida` ---> la pieza ya fue vendida y no está disponible.

# ## La descripción
# La descripción de una pieza debe explicar brevemente las características de la pieza.
# Además, debe incluir obligatoriamente una de las siguientes palabras:
# - `usada`
# - `certificada`

# ### Ejemplos de descripciones válidas
# - Figura usada con algunos detalles de conservación.
# - Pieza certificada en caja original.
# - Carta usada en buen estado.
# - Moneda certificada por un experto.
# ### Ejemplo de descripción no válida
# - Figura roja de colección.
# La descripción anterior no contiene las palabras `usada` ni `certificada`.

# ---
# # NIVEL I – Registro de piezas y estructuras base

# ## Parte 1. Preparación del proyecto

# 1. Crear un repositorio en GitHub para el reto.
# 2. Clonar el repositorio en el equipo local.
# 3. Crear el archivo principal del programa.
# 4. Crear el archivo `README.md`.
# 5. Definir el nombre del sistema.
# 6. Mostrar un mensaje de bienvenida al iniciar el programa.

# El mensaje debe indicar que el usuario está ingresando al catálogo de piezas coleccionables.

## Parte 2. Captura de piezas por terminal

# El programa debe solicitar por terminal la información de **10 piezas coleccionables**.
# Cada pieza debe solicitar los siguientes datos:
# * Identificador.
# * Nombre.
# * Categoría.
# * Precio.
# * Estado.
# * Descripción.

