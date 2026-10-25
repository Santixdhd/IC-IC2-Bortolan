"""
Ejercicios — Clase 1: Python y Git
Parte A — Python: tipos, variables, operaciones (A1 a A7)
"""


def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte una temperatura en grados Celsius a Fahrenheit (A3)."""
    return celsius * 9 / 5 + 32


def clasificacion_edad(edad: int) -> str:
    """Devuelve 'mayor de edad' si edad >= 18, o 'menor de edad' en caso contrario (A5)."""
    if edad >= 18:
        return "mayor de edad"
    return "menor de edad"


def convertir_distancia(km: float) -> dict:
    """Encadena la conversión km -> millas -> pies (A7)."""
    factor_km_a_millas = 0.621371
    factor_millas_a_pies = 5280

    millas = km * factor_km_a_millas
    pies = millas * factor_millas_a_pies
    return {
        "km": km,
        "millas": millas,
        "pies": pies,
    }


def main() -> None:
    print("=" * 60)
    print("PARTE A — Python: tipos, variables, operaciones")
    print("=" * 60)

    # ------------------------------------------------------------------
    # 🟢 A1 — Calculadora de promedio
    # ------------------------------------------------------------------
    print("\n--- A1: Calculadora de promedio ---")
    notas = [7, 4, 9, 10, 6]
    promedio_notas = sum(notas) / len(notas)
    estado = "Aprobó" if promedio_notas >= 6 else "Desaprobó"
    print(f"Notas: {notas}")
    print(f"Promedio: {promedio_notas}")
    print(f"Resultado: {estado}")

    # ------------------------------------------------------------------
    # 🟢 A2 — El tipo importa
    # ------------------------------------------------------------------
    print("\n--- A2: El tipo importa ---")
    cantidad = "5"
    precio = 100
    resultado_texto = cantidad * precio
    print(f"Tipo de cantidad: {type(cantidad)}")
    print(f"'5' * 100 (repite el string 100 veces): {resultado_texto}")

    # Arreglado: convertimos cantidad a entero (int) antes de multiplicar
    resultado_numerico = int(cantidad) * precio
    print(f"int('5') * 100 (multiplicación numérica real): {resultado_numerico}")

    # ------------------------------------------------------------------
    # 🟢 A3 — Conversión de temperatura
    # ------------------------------------------------------------------
    print("\n--- A3: Conversión de temperatura ---")
    for temp_c in [0, 25, 100]:
        temp_f = celsius_a_fahrenheit(temp_c)
        print(f"{temp_c} °C = {temp_f} °F")

    # ------------------------------------------------------------------
    # 🟡 A4 — Redondeo y formato
    # ------------------------------------------------------------------
    print("\n--- A4: Redondeo y formato ---")
    print(f"Promedio formateado con un solo decimal: {promedio_notas:.1f}")

    # ------------------------------------------------------------------
    # 🟢 A5 — ¿Mayor o menor de edad?
    # ------------------------------------------------------------------
    print("\n--- A5: ¿Mayor o menor de edad? ---")
    for edad_prueba in [17, 18, 0]:
        print(f"Edad {edad_prueba}: {clasificacion_edad(edad_prueba)}")

    # ------------------------------------------------------------------
    # 🟡 A6 — Par, impar, y turnos
    # ------------------------------------------------------------------
    print("\n--- A6: Par, impar, y turnos ---")
    # El operador % (módulo) devuelve el resto de la división entera.
    # Si numero % 2 == 0, es divisible por 2 (par); si da 1, es impar.
    pares = []
    impares = []
    for alumno in range(1, 31):
        if alumno % 2 == 0:
            pares.append(alumno)
        else:
            impares.append(alumno)

    print(f"Grupo par ({len(pares)} alumnos): {pares}")
    print(f"Grupo impar ({len(impares)} alumnos): {impares}")
    print(f"Total sumado: {len(pares) + len(impares)}")

    # ------------------------------------------------------------------
    # 🔴 A7 — Cadena de conversiones
    # ------------------------------------------------------------------
    print("\n--- A7: Cadena de conversiones (km -> millas -> pies) ---")
    valor_km = 10.0  # Cambiando este único valor se actualizan las 3 unidades
    conversion = convertir_distancia(valor_km)
    print(
        f"{conversion['km']} km -> "
        f"{conversion['millas']:.4f} millas -> "
        f"{conversion['pies']:.2f} pies"
    )


if __name__ == "__main__":
    main()
