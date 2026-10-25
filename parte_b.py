"""
Ejercicios — Clase 1: Python y Git
Parte B — Listas (B1 a B8)
"""


def estadisticas_con_for(puntajes: list[int | float]) -> tuple[float, float, float]:
    """Calcula (mayor, menor, promedio) recorriendo la lista con un for (B3)."""
    mayor = puntajes[0]
    menor = puntajes[0]
    suma = 0

    for p in puntajes:
        if p > mayor:
            mayor = p
        if p < menor:
            menor = p
        suma += p

    promedio = suma / len(puntajes)
    return mayor, menor, promedio


def filtrar_mayores_a(puntajes: list[int | float], umbral: float = 100) -> list[int | float]:
    """Devuelve una lista nueva con los valores estrictamente mayores al umbral (B4)."""
    filtrados = []
    for p in puntajes:
        if p > umbral:
            filtrados.append(p)
    return filtrados


def promedio_movil_3(lecturas: list[int | float]) -> list[float]:
    """
    Calcula el promedio móvil de a 3 elementos consecutivos (ventana deslizante, B8).
    Tiene 2 elementos menos que la lista original porque cada ventana requiere 3 elementos
    consecutivos (i, i+1, i+2), por lo que la última ventana empieza en len(lecturas) - 3.
    """
    promedios = []
    for i in range(len(lecturas) - 2):
        ventana = lecturas[i : i + 3]
        promedios.append(round(sum(ventana) / 3, 2))
    return promedios


def main() -> None:
    print("=" * 60)
    print("PARTE B — Listas")
    print("=" * 60)

    # ------------------------------------------------------------------
    # 🟢 B1 — Playlist
    # ------------------------------------------------------------------
    print("\n--- B1: Playlist ---")
    playlist = [
        "De Música Ligera",
        "Bohemian Rhapsody",
        "Stairway to Heaven",
        "Imagine",
        "Smells Like Teen Spirit",
    ]
    print(f"Playlist completa: {playlist}")
    print(f"Primera canción (índice 0): {playlist[0]}")
    print(f"Última canción (índice -1): {playlist[-1]}")

    # ------------------------------------------------------------------
    # 🟢 B2 — Sumar a la lista
    # ------------------------------------------------------------------
    print("\n--- B2: Sumar a la lista ---")
    playlist.append("Hotel California")
    playlist.append("Persiana Americana")
    print(f"Playlist actualizada: {playlist}")
    print(f"Cantidad de canciones ahora (len): {len(playlist)}")

    # ------------------------------------------------------------------
    # 🟡 B3 — El más alto y el más bajo
    # ------------------------------------------------------------------
    print("\n--- B3: El más alto y el más bajo ---")
    puntajes = [120, 45, 300, 80, 210]
    mayor_for, menor_for, prom_for = estadisticas_con_for(puntajes)
    print(f"Con bucle for -> Mayor: {mayor_for} | Menor: {menor_for} | Promedio: {prom_for}")

    mayor_fn = max(puntajes)
    menor_fn = min(puntajes)
    prom_fn = sum(puntajes) / len(puntajes)
    print(f"Con max()/min() -> Mayor: {mayor_fn} | Menor: {menor_fn} | Promedio: {prom_fn}")

    # ------------------------------------------------------------------
    # 🟡 B4 — Filtrar
    # ------------------------------------------------------------------
    print("\n--- B4: Filtrar mayores a 100 ---")
    mayores_a_100 = filtrar_mayores_a(puntajes, 100)
    print(f"Lista nueva (> 100): {mayores_a_100}")
    print(f"Lista original intacta: {puntajes}")

    # ------------------------------------------------------------------
    # 🔴 B5 — Ranking (ordenar de mayor a menor)
    # ------------------------------------------------------------------
    print("\n--- B5: Ranking (mayor a menor) ---")
    # sorted(lista, reverse=True) devuelve una COPIA nueva ordenada sin modificar la original.
    # lista.sort(reverse=True) ordena la lista EN SU LUGAR (in-place) y devuelve None.
    ranking_copia = sorted(puntajes, reverse=True)
    print(f"Copia ordenada con sorted(..., reverse=True): {ranking_copia}")
    print(f"Original sin modificar: {puntajes}")

    # ------------------------------------------------------------------
    # 🟢 B6 — Al revés (slicing [::-1])
    # ------------------------------------------------------------------
    print("\n--- B6: Playlist al revés con slicing [::-1] ---")
    playlist_invertida = playlist[::-1]
    print(f"Playlist invertida: {playlist_invertida}")
    print(f"Playlist original intacta: {playlist}")

    # ------------------------------------------------------------------
    # 🟡 B7 — Sin repetidos (set)
    # ------------------------------------------------------------------
    print("\n--- B7: Sin repetidos usando set() ---")
    con_repetidos = [3, 5, 3, 8, 5, 1, 8, 8]
    sin_repetidos = list(set(con_repetidos))
    print(f"Original con repetidos: {con_repetidos}")
    print(f"Sin repetidos (list(set(...))): {sin_repetidos}")

    # ------------------------------------------------------------------
    # 🔴 B8 — Promedio móvil (ventana deslizante de 3 elementos)
    # ------------------------------------------------------------------
    print("\n--- B8: Promedio móvil (ventana deslizante de 3) ---")
    lecturas = [20.0, 21.5, 22.0, 24.0, 23.5, 25.0, 26.5, 24.0, 22.5, 21.0]
    promedios_ventana = promedio_movil_3(lecturas)
    print(f"Lecturas originales ({len(lecturas)} elementos): {lecturas}")
    print(f"Promedios móviles de a 3 ({len(promedios_ventana)} elementos): {promedios_ventana}")
    print(
        "Explicación: tiene 2 elementos menos (10 - 2 = 8) porque cada promedio agrupa "
        "3 posiciones consecutivas (0-1-2 hasta 7-8-9)."
    )


if __name__ == "__main__":
    main()
