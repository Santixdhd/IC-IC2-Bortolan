"""
Ejercicios — Clase 1: Python y Git
Parte C — Diccionarios (¡la forma del JSON que viene!) (C1 a C8)
"""


def obtener_dato_pelicula(pelicula: dict, clave: str, por_defecto: str = "desconocido"):
    """
    Devuelve el valor asociado a 'clave' en el diccionario 'pelicula' usando .get().
    Si la clave no existe, devuelve 'por_defecto' ('desconocido') sin lanzar KeyError (C3 / G5).
    """
    return pelicula.get(clave, por_defecto)


def buscar_por_director(peliculas: list[dict], texto_director: str) -> list[str]:
    """
    Busca películas cuyo director contenga 'texto_director' (coincidencia parcial, C5).
    Devuelve la lista de títulos que coinciden.
    """
    encontradas = []
    for p in peliculas:
        if texto_director.lower() in p["director"].lower():
            encontradas.append(p["titulo"])
    return encontradas


def contar_palabras(frase: str) -> dict[str, int]:
    """Cuenta cuántas veces aparece cada palabra en una frase (C7)."""
    conteo: dict[str, int] = {}
    for palabra in frase.lower().split():
        palabra_limpia = palabra.strip(".,;:¡!¿?")
        if palabra_limpia:
            conteo[palabra_limpia] = conteo.get(palabra_limpia, 0) + 1
    return conteo


def main() -> None:
    print("=" * 60)
    print("PARTE C — Diccionarios")
    print("=" * 60)

    # ------------------------------------------------------------------
    # 🟢 C1 — Una ficha
    # ------------------------------------------------------------------
    print("\n--- C1: Una ficha ---")
    pelicula = {
        "titulo": "Inception",
        "anio": 2009,
        "director": "Christopher Nolan",
    }
    print(f"Título de la película: {pelicula['titulo']}")

    # ------------------------------------------------------------------
    # 🟢 C2 — Agregar y cambiar
    # ------------------------------------------------------------------
    print("\n--- C2: Agregar puntaje y corregir año ---")
    pelicula["puntaje"] = 9.0
    pelicula["anio"] = 2010
    print(f"Ficha actualizada: {pelicula}")

    # ------------------------------------------------------------------
    # 🟡 C3 — Clave que no existe (.get())
    # ------------------------------------------------------------------
    print("\n--- C3: Clave que no existe ---")
    try:
        _ = pelicula["duracion"]
    except KeyError as error:
        print(f"Acceso directo pelicula['duracion'] lanzó KeyError: {error}")

    duracion = obtener_dato_pelicula(pelicula, "duracion")
    print(f"Acceso seguro con .get('duracion', 'desconocido'): {duracion}")

    # ------------------------------------------------------------------
    # 🟡 C4 — Lista de diccionarios
    # ------------------------------------------------------------------
    print("\n--- C4: Lista de 3 películas ---")
    catalogo = [
        {"titulo": "Inception", "anio": 2010, "director": "Christopher Nolan"},
        {"titulo": "Parasite", "anio": 2019, "director": "Bong Joon-ho"},
        {"titulo": "Interstellar", "anio": 2014, "director": "Christopher Nolan"},
    ]
    print("Títulos en el catálogo:")
    for item in catalogo:
        print(f" - {item['titulo']}")

    # ------------------------------------------------------------------
    # 🔴 C5 — Búsqueda por director
    # ------------------------------------------------------------------
    print("\n--- C5: Búsqueda por director ---")
    for consulta in ["Nolan", "Spielberg"]:
        resultados = buscar_por_director(catalogo, consulta)
        if resultados:
            print(f"Películas encontradas para '{consulta}': {resultados}")
        else:
            print(f"No se encontraron películas del director '{consulta}'.")

    # ------------------------------------------------------------------
    # 🟢 C6 — Combinar fichas (.update() y operador |)
    # ------------------------------------------------------------------
    print("\n--- C6: Combinar fichas ---")
    ficha_1 = {"titulo": "Dune", "anio": 2021}
    ficha_2 = {"puntaje": 8, "anio": 2024}

    combinada_1_2 = ficha_1 | ficha_2
    combinada_2_1 = ficha_2 | ficha_1
    print(f"ficha_1 | ficha_2 (gana el año de ficha_2 -> 2024): {combinada_1_2}")
    print(f"ficha_2 | ficha_1 (gana el año de ficha_1 -> 2021): {combinada_2_1}")

    # ------------------------------------------------------------------
    # 🟡 C7 — Contador de palabras
    # ------------------------------------------------------------------
    print("\n--- C7: Contador de palabras ---")
    frase = "el sensor mide temperatura y el sensor publica temperatura por mqtt"
    frecuencias = contar_palabras(frase)
    print(f"Frase: '{frase}'")
    print(f"Frecuencias: {frecuencias}")

    # ------------------------------------------------------------------
    # 🔴 C8 — Diccionario anidado (inventario de tienda)
    # ------------------------------------------------------------------
    print("\n--- C8: Diccionario anidado (inventario) ---")
    inventario = {
        "raspberry_pi": {"precio": 85000, "stock": 12},
        "sensor_dht22": {"precio": 6500, "stock": 40},
        "cable_dupont": {"precio": 2200, "stock": 100},
    }
    precio_rpi = inventario["raspberry_pi"]["precio"]
    print(f"Precio de raspberry_pi (inventario['raspberry_pi']['precio']): ${precio_rpi}")


if __name__ == "__main__":
    main()
