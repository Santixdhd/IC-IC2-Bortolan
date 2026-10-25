"""
Ejercicios — Clase 1: Python y Git
Cierre del día — Mini-proyecto integrador (H1 y H2)

Lee peliculas.csv (Parte E), calcula estadísticas usando las funciones de Parte D,
y muestra el ranking de películas ordenado de mayor a menor puntaje (Parte B).
"""

import csv
from pathlib import Path
from parte_d import estadisticas, promedio

BASE_DIR = Path(__file__).resolve().parent
RUTA_CSV = BASE_DIR / "peliculas.csv"


def cargar_peliculas(ruta_csv: Path = RUTA_CSV) -> list[dict]:
    """
    Lee el archivo CSV de películas y devuelve una lista de diccionarios
    con tipos convertidos (anio: int, puntaje: float).
    """
    peliculas = []
    with open(ruta_csv, mode="r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            peliculas.append(
                {
                    "titulo": fila["titulo"].strip(),
                    "anio": int(fila["anio"]),
                    "puntaje": float(fila["puntaje"]),
                    "genero": fila["genero"].strip(),
                }
            )
    return peliculas


def calcular_estadisticas_peliculas(peliculas: list[dict]) -> dict:
    """
    Calcula estadísticas de los puntajes de una lista de películas
    reutilizando estadisticas() de la Parte D.
    """
    if not peliculas:
        return {
            "cantidad": 0,
            "promedio": 0.0,
            "maximo": 0.0,
            "minimo": 0.0,
            "mejor_pelicula": "",
            "peor_pelicula": "",
        }

    puntajes = [p["puntaje"] for p in peliculas]
    base_stats = estadisticas(puntajes)
    mejor = max(peliculas, key=lambda p: p["puntaje"])
    peor = min(peliculas, key=lambda p: p["puntaje"])

    return {
        "cantidad": len(peliculas),
        "promedio": round(base_stats["promedio"], 2),
        "maximo": base_stats["maximo"],
        "minimo": base_stats["minimo"],
        "mejor_pelicula": mejor["titulo"],
        "peor_pelicula": peor["titulo"],
    }


def ordenar_peliculas_por_puntaje(
    peliculas: list[dict], descendente: bool = True
) -> list[dict]:
    """
    Devuelve una copia nueva de la lista de películas ordenada por puntaje
    (por defecto de mayor a menor), sin modificar la lista original (Parte B5).
    """
    return sorted(peliculas, key=lambda p: p["puntaje"], reverse=descendente)


def calcular_promedios_por_genero(peliculas: list[dict]) -> dict[str, float]:
    """
    Agrupa las películas por género y calcula el puntaje promedio de cada uno
    usando promedio() de la Parte D (Parte E5 + D1).
    """
    grupos: dict[str, list[float]] = {}
    for p in peliculas:
        genero = p["genero"]
        if genero not in grupos:
            grupos[genero] = []
        grupos[genero].append(p["puntaje"])

    return {
        genero: round(promedio(puntajes), 2)
        for genero, puntajes in grupos.items()
    }


def formatear_reporte_peliculas(peliculas: list[dict]) -> str:
    """
    Genera un reporte completo en texto con las estadísticas generales,
    el promedio por género y el ranking ordenado de mayor a menor.
    """
    stats = calcular_estadisticas_peliculas(peliculas)
    ranking = ordenar_peliculas_por_puntaje(peliculas, descendente=True)
    por_genero = calcular_promedios_por_genero(peliculas)

    lineas = [
        "=" * 60,
        "REPORTE DE PELÍCULAS — CIERRE CLASE 1 (H1)",
        "=" * 60,
        f"Total de películas : {stats['cantidad']}",
        f"Puntaje promedio   : {stats['promedio']:.2f}",
        f"Puntaje máximo     : {stats['maximo']} ({stats['mejor_pelicula']})",
        f"Puntaje mínimo     : {stats['minimo']} ({stats['peor_pelicula']})",
        "",
        "--- Promedio por género ---",
    ]

    for genero, prom in por_genero.items():
        lineas.append(f"  * {genero}: {prom:.2f}")

    lineas.append("")
    lineas.append("--- Ranking de películas (mayor a menor puntaje) ---")
    for pos, peli in enumerate(ranking, start=1):
        lineas.append(
            f"  {pos}. {peli['titulo']} ({peli['anio']}) "
            f"[{peli['genero']}] -> Puntaje: {peli['puntaje']}"
        )

    return "\n".join(lineas)


def main() -> None:
    peliculas = cargar_peliculas()
    print(formatear_reporte_peliculas(peliculas))


if __name__ == "__main__":
    main()
