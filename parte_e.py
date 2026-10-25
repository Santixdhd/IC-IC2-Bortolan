"""
Ejercicios — Clase 1: Python y Git
Parte E — Leer datos de un archivo (CSV) (E1 a E5)
"""

import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_CSV = BASE_DIR / "peliculas.csv"
RUTA_FILTRADAS_CSV = BASE_DIR / "filtradas.csv"


def leer_lineas_crudas(ruta: Path = RUTA_CSV) -> list[str]:
    """Lee el archivo CSV y devuelve la lista de líneas de texto sin saltos finales (E1)."""
    with open(ruta, mode="r", encoding="utf-8") as archivo:
        return [linea.strip() for linea in archivo if linea.strip()]


def leer_peliculas_csv(ruta: Path = RUTA_CSV) -> list[dict]:
    """
    Lee peliculas.csv y convierte tipos numéricos (anio -> int, puntaje -> float)
    porque todo dato leído de un CSV entra inicialmente como str (E2).
    """
    peliculas = []
    with open(ruta, mode="r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            peliculas.append(
                {
                    "titulo": fila["titulo"],
                    "anio": int(fila["anio"]),
                    "puntaje": float(fila["puntaje"]),
                    "genero": fila["genero"],
                }
            )
    return peliculas


def sumar_puntajes(peliculas: list[dict]) -> float:
    """Suma la columna puntaje ya convertida a float (E2)."""
    return round(sum(p["puntaje"] for p in peliculas), 2)


def reporte_csv(peliculas: list[dict]) -> dict:
    """
    Calcula cantidad de películas, puntaje promedio y el título de la mejor puntuada (E3).
    """
    if not peliculas:
        return {"cantidad": 0, "promedio": 0.0, "mejor_puntuada": ""}

    cantidad = len(peliculas)
    promedio_puntaje = round(sum(p["puntaje"] for p in peliculas) / cantidad, 2)
    mejor = max(peliculas, key=lambda p: p["puntaje"])
    return {
        "cantidad": cantidad,
        "promedio": promedio_puntaje,
        "mejor_puntuada": mejor["titulo"],
        "mejor_puntaje": mejor["puntaje"],
    }


def filtrar_por_genero_y_guardar(
    peliculas: list[dict],
    genero_elegido: str,
    ruta_salida: Path = RUTA_FILTRADAS_CSV,
) -> list[dict]:
    """
    Filtra las películas del género elegido y escribe un nuevo CSV (filtradas.csv) (E4).
    """
    filtradas = [
        p for p in peliculas if p["genero"].lower() == genero_elegido.lower()
    ]
    with open(ruta_salida, mode="w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(
            archivo, fieldnames=["titulo", "anio", "puntaje", "genero"]
        )
        escritor.writeheader()
        escritor.writerows(filtradas)
    return filtradas


def promedio_por_genero(peliculas: list[dict]) -> dict[str, float]:
    """
    Agrupa las películas por categoría (genero) y devuelve {genero: puntaje_promedio} (E5).
    """
    acumulado: dict[str, list[float]] = {}
    for p in peliculas:
        genero = p["genero"]
        if genero not in acumulado:
            acumulado[genero] = []
        acumulado[genero].append(p["puntaje"])

    return {
        genero: round(sum(puntajes) / len(puntajes), 2)
        for genero, puntajes in acumulado.items()
    }


def main() -> None:
    print("=" * 60)
    print("PARTE E — Leer datos de un archivo (CSV)")
    print("=" * 60)

    # ------------------------------------------------------------------
    # 🟡 E1 — Leer y mostrar
    # ------------------------------------------------------------------
    print("\n--- E1: Leer y mostrar peliculas.csv línea por línea ---")
    for linea in leer_lineas_crudas():
        print(f"  {linea}")

    # ------------------------------------------------------------------
    # 🟡 E2 — Cuidado: todo viene como texto
    # ------------------------------------------------------------------
    print("\n--- E2: Suma de puntajes convirtiendo texto a float ---")
    peliculas = leer_peliculas_csv()
    suma_total = sumar_puntajes(peliculas)
    print(f"Suma total de puntajes ({len(peliculas)} películas): {suma_total}")

    # ------------------------------------------------------------------
    # 🔴 E3 — Reporte del CSV
    # ------------------------------------------------------------------
    print("\n--- E3: Reporte general ---")
    datos_reporte = reporte_csv(peliculas)
    print(f"Cantidad de películas: {datos_reporte['cantidad']}")
    print(f"Puntaje promedio: {datos_reporte['promedio']}")
    print(
        f"Mejor puntuada: {datos_reporte['mejor_puntuada']} "
        f"({datos_reporte['mejor_puntaje']})"
    )

    # ------------------------------------------------------------------
    # 🟡 E4 — Filtrar y guardar en filtradas.csv
    # ------------------------------------------------------------------
    print("\n--- E4: Filtrar por género y guardar en filtradas.csv ---")
    genero_objetivo = "Ciencia Ficcion"
    filtradas = filtrar_por_genero_y_guardar(peliculas, genero_objetivo)
    print(
        f"Se guardaron {len(filtradas)} películas de '{genero_objetivo}' "
        f"en {RUTA_FILTRADAS_CSV.name}:"
    )
    for f in filtradas:
        print(f"  - {f['titulo']} ({f['anio']}) -> Puntaje: {f['puntaje']}")

    # ------------------------------------------------------------------
    # 🔴 E5 — Agrupar por categoría (promedio por género)
    # ------------------------------------------------------------------
    print("\n--- E5: Puntaje promedio por género ---")
    promedios_genero = promedio_por_genero(peliculas)
    for gen, prom in promedios_genero.items():
        print(f"  - {gen}: {prom}")


if __name__ == "__main__":
    main()
