"""
Ejercicios — Clase 1: Python y Git
Parte G — Testear con pytest (G1 a G8)
"""

import pytest
from parte_c import obtener_dato_pelicula
from parte_d import aprobo, estadisticas, promedio


# ------------------------------------------------------------------
# 🟢 G1 — Tu primer test
# ------------------------------------------------------------------
def test_promedio_notas_basico():
    """Verifica que promedio([7, 4, 9, 10, 6]) devuelve 7.2 (G1)."""
    assert promedio([7, 4, 9, 10, 6]) == 7.2


# ------------------------------------------------------------------
# 🟢 G2 — Un test que falla a propósito (comentado tras verificar el fallo)
# ------------------------------------------------------------------
# Explicación G2:
# Al descomentar y correr `pytest`, pytest muestra en rojo:
#   >       assert promedio([7, 4, 9, 10, 6]) == 10.0
#   E       assert 7.2 == 10.0
#   E        +  where 7.2 = promedio([7, 4, 9, 10, 6])
# Es decir, indica exactamente qué valor devolvió la función (7.2) y contra
# qué valor esperado falló la comparación (10.0). Se deja comentado para que
# la suite de tests del repositorio quede 100% en verde.
#
# def test_promedio_falla_a_proposito():
#     assert promedio([7, 4, 9, 10, 6]) == 10.0


# ------------------------------------------------------------------
# 🟡 G3 — Varios casos, varios tests para aprobo()
# ------------------------------------------------------------------
def test_aprobo_caso_aprobado():
    """Caso que supera holgadamente el promedio de 6 (G3)."""
    assert aprobo([8, 9, 7, 10]) is True


def test_aprobo_caso_desaprobado():
    """Caso cuyo promedio no alcanza 6 (G3)."""
    assert aprobo([4, 5, 3, 5]) is False


def test_aprobo_caso_limite_exactamente_6():
    """Caso límite donde el promedio da exactamente 6.0 (G3)."""
    assert aprobo([6, 6, 6, 6]) is True


# ------------------------------------------------------------------
# 🟡 G4 — Testear un diccionario (estadisticas)
# ------------------------------------------------------------------
def test_estadisticas_diccionario_completo():
    """Verifica que estadisticas() devuelva las claves promedio, maximo y minimo con sus valores (G4)."""
    resultado = estadisticas([7, 4, 9, 10, 6])
    assert "promedio" in resultado
    assert "maximo" in resultado
    assert "minimo" in resultado
    assert resultado["promedio"] == 7.2
    assert resultado["maximo"] == 10
    assert resultado["minimo"] == 4


# ------------------------------------------------------------------
# 🟡 G5 — Testear el caso raro (.get() con clave que no existe)
# ------------------------------------------------------------------
def test_obtener_dato_pelicula_clave_inexistente():
    """Prueba que cuando falta la clave 'duracion', la función devuelve 'desconocido' (G5)."""
    ficha = {"titulo": "Inception", "anio": 2010, "director": "Christopher Nolan"}
    assert obtener_dato_pelicula(ficha, "duracion") == "desconocido"
    assert obtener_dato_pelicula(ficha, "titulo") == "Inception"


# ------------------------------------------------------------------
# 🔴 G6 — El caso límite que decidiste en D5 (lista vacía)
# ------------------------------------------------------------------
def test_promedio_lista_vacia():
    """Documenta con código que promedio([]) devuelve 0.0 sin lanzar ZeroDivisionError (G6)."""
    assert promedio([]) == 0.0


# ------------------------------------------------------------------
# 🔴 G7 — Un solo test, varios casos (@pytest.mark.parametrize)
# ------------------------------------------------------------------
@pytest.mark.parametrize(
    "notas,esperado",
    [
        ([8, 9, 10], True),       # Caso aprobado
        ([2, 4, 5], False),       # Caso desaprobado
        ([6, 6, 6], True),        # Caso límite (promedio == 6.0)
        ([5, 6, 6], False),       # Caso apenas por debajo del límite (5.67)
        ([], False),              # Caso lista vacía (promedio == 0.0)
    ],
)
def test_aprobo_parametrizado(notas: list[int], esperado: bool):
    """Corre múltiples casos de entrada/salida con un único bloque de test (G7)."""
    assert aprobo(notas) is esperado
