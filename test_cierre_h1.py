"""
Ejercicios — Clase 1: Python y Git
Tests del Cierre del día (H1 y H2)

Cubre cada función de cierre_h1.py para asegurar que cualquier regresión
o cambio accidental sea detectado automáticamente por pytest.
"""

from pathlib import Path
from cierre_h1 import (
    calcular_estadisticas_peliculas,
    calcular_promedios_por_genero,
    cargar_peliculas,
    formatear_reporte_peliculas,
    ordenar_peliculas_por_puntaje,
)


PELICULAS_PRUEBA = [
    {"titulo": "Peli A", "anio": 2020, "puntaje": 8.0, "genero": "Drama"},
    {"titulo": "Peli B", "anio": 2022, "puntaje": 10.0, "genero": "Ciencia Ficcion"},
    {"titulo": "Peli C", "anio": 2019, "puntaje": 6.0, "genero": "Drama"},
]


def test_cargar_peliculas_convierte_tipos_correctamente(tmp_path: Path):
    """
    Cubre cargar_peliculas().
    Justificación H2: Si alguien olvida convertir 'anio' a int o 'puntaje' a float
    al leer el CSV, este test falla inmediatamente verificando tipos y valores.
    """
    csv_temporal = tmp_path / "test_peliculas.csv"
    csv_temporal.write_text(
        "titulo,anio,puntaje,genero\nInception,2010,9.0,Ciencia Ficcion\n",
        encoding="utf-8",
    )

    peliculas = cargar_peliculas(csv_temporal)
    assert len(peliculas) == 1
    assert peliculas[0]["titulo"] == "Inception"
    assert isinstance(peliculas[0]["anio"], int)
    assert peliculas[0]["anio"] == 2010
    assert isinstance(peliculas[0]["puntaje"], float)
    assert peliculas[0]["puntaje"] == 9.0
    assert peliculas[0]["genero"] == "Ciencia Ficcion"


def test_calcular_estadisticas_peliculas_valores_exactos():
    """
    Cubre calcular_estadisticas_peliculas() con datos conocidos (H1 / H2).
    Justificación H2: Detecta errores en el cálculo de promedio, máximo, mínimo
    o en la identificación del título de la mejor/peor película.
    """
    stats = calcular_estadisticas_peliculas(PELICULAS_PRUEBA)
    assert stats["cantidad"] == 3
    assert stats["promedio"] == 8.0
    assert stats["maximo"] == 10.0
    assert stats["minimo"] == 6.0
    assert stats["mejor_pelicula"] == "Peli B"
    assert stats["peor_pelicula"] == "Peli C"


def test_calcular_estadisticas_peliculas_lista_vacia():
    """
    Cubre calcular_estadisticas_peliculas([]) (caso borde H2).
    Justificación H2: Verifica que una lista vacía no dispare ValueError en max()/min()
    ni ZeroDivisionError en el promedio.
    """
    stats = calcular_estadisticas_peliculas([])
    assert stats["cantidad"] == 0
    assert stats["promedio"] == 0.0
    assert stats["maximo"] == 0.0
    assert stats["minimo"] == 0.0
    assert stats["mejor_pelicula"] == ""


def test_ordenar_peliculas_por_puntaje_no_muta_original():
    """
    Cubre ordenar_peliculas_por_puntaje().
    Justificación H2: Detecta si el ordenamiento quedó invertido (menor a mayor en vez
    de mayor a menor) o si se modificó la lista original in-place.
    """
    copia_original = list(PELICULAS_PRUEBA)
    ordenadas = ordenar_peliculas_por_puntaje(PELICULAS_PRUEBA, descendente=True)

    assert [p["titulo"] for p in ordenadas] == ["Peli B", "Peli A", "Peli C"]
    assert PELICULAS_PRUEBA == copia_original


def test_calcular_promedios_por_genero():
    """
    Cubre calcular_promedios_por_genero().
    Justificación H2: Verifica que las películas del mismo género se agrupen
    y promedien bien (Drama: (8.0 + 6.0)/2 = 7.0; Ciencia Ficcion: 10.0).
    """
    promedios = calcular_promedios_por_genero(PELICULAS_PRUEBA)
    assert promedios == {
        "Drama": 7.0,
        "Ciencia Ficcion": 10.0,
    }


def test_formatear_reporte_peliculas_incluye_datos_clave():
    """
    Cubre formatear_reporte_peliculas().
    Justificación H2: Si alguien rompe el armado del reporte final o borra una sección,
    verifica que el texto resultante contenga las estadísticas y el ranking.
    """
    texto = formatear_reporte_peliculas(PELICULAS_PRUEBA)
    assert "Total de películas : 3" in texto
    assert "Puntaje promedio   : 8.00" in texto
    assert "1. Peli B (2022)" in texto
    assert "3. Peli C (2019)" in texto
