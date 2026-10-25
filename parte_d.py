"""
Ejercicios — Clase 1: Python y Git
Parte D — Funciones (D1 a D6)
"""


def promedio(notas: list[int | float]) -> float:
    """
    Calcula el promedio de una lista de números (D1).
    Decisión de diseño para lista vacía (D5 / G6): si la lista está vacía,
    devuelve 0.0 en lugar de lanzar ZeroDivisionError.
    """
    if not notas:
        return 0.0
    return sum(notas) / len(notas)


def aprobo(notas: list[int | float], minimo: float = 6) -> bool:
    """
    Usa promedio(notas) por dentro y devuelve True si alcanza el umbral 'minimo' (D2 y D4).
    Por defecto el umbral de aprobación es 6.
    """
    return promedio(notas) >= minimo


def estadisticas(notas: list[int | float]) -> dict[str, float]:
    """
    Devuelve un diccionario con 'promedio', 'maximo' y 'minimo' de la lista (D3 / G4).
    Si la lista está vacía, devuelve los tres valores en 0.0.
    """
    if not notas:
        return {"promedio": 0.0, "maximo": 0.0, "minimo": 0.0}
    return {
        "promedio": promedio(notas),
        "maximo": max(notas),
        "minimo": min(notas),
    }


def reporte(notas: list[int | float]) -> str:
    """
    Usa estadisticas(notas) por dentro y devuelve un texto formateado (D6), ej.:
    'Promedio: 7.2 | Máximo: 10 | Mínimo: 4'
    """
    stats = estadisticas(notas)
    return (
        f"Promedio: {stats['promedio']:.1f} | "
        f"Máximo: {stats['maximo']} | "
        f"Mínimo: {stats['minimo']}"
    )


def main() -> None:
    print("=" * 60)
    print("PARTE D — Funciones")
    print("=" * 60)

    notas_alumno_1 = [7, 4, 9, 10, 6]
    notas_alumno_2 = [5, 5, 4, 6]

    # ------------------------------------------------------------------
    # 🟢 D1 — Encapsular promedio(notas)
    # ------------------------------------------------------------------
    print("\n--- D1: Función promedio(notas) ---")
    print(f"Promedio de {notas_alumno_1}: {promedio(notas_alumno_1)}")
    print(f"Promedio de {notas_alumno_2}: {promedio(notas_alumno_2)}")

    # ------------------------------------------------------------------
    # 🟡 D2 — ¿Aprobó?
    # ------------------------------------------------------------------
    print("\n--- D2: Función aprobo(notas) ---")
    print(f"¿Aprobó alumno 1 ({notas_alumno_1})?: {aprobo(notas_alumno_1)}")
    print(f"¿Aprobó alumno 2 ({notas_alumno_2})?: {aprobo(notas_alumno_2)}")

    # ------------------------------------------------------------------
    # 🔴 D3 — Estadísticas en un diccionario
    # ------------------------------------------------------------------
    print("\n--- D3: Función estadisticas(notas) ---")
    print(f"Estadísticas alumno 1: {estadisticas(notas_alumno_1)}")

    # ------------------------------------------------------------------
    # 🟢 D4 — Parámetro por default en aprobo(notas, minimo=6)
    # ------------------------------------------------------------------
    print("\n--- D4: Parámetro por default (minimo=6 vs minimo=8) ---")
    print(f"Alumno 1 con minimo por defecto (6): {aprobo(notas_alumno_1)}")
    print(f"Alumno 1 pasando minimo=8: {aprobo(notas_alumno_1, minimo=8)}")

    # ------------------------------------------------------------------
    # 🟡 D5 — Que no explote con la lista vacía
    # ------------------------------------------------------------------
    print("\n--- D5: Lista vacía promedio([]) ---")
    print(f"promedio([]) devuelve de forma segura: {promedio([])}")

    # ------------------------------------------------------------------
    # 🔴 D6 — Reporte combinado
    # ------------------------------------------------------------------
    print("\n--- D6: Función reporte(notas) ---")
    print(reporte(notas_alumno_1))


if __name__ == "__main__":
    main()
