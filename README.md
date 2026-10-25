# Ingeniería en Computación 2 — Clase 1: Python y Git

Repositorio con la resolución completa de los ejercicios de la **Clase 1 (Python, Git y pytest)** y el mini-proyecto integrador de cierre (**H1 / H2**).

---

## Estructura del proyecto

| Archivo | Descripción |
| :--- | :--- |
| `parte_a.py` | **Parte A** (A1–A7): Tipos, variables, operaciones, módulo `%` y cadena de conversiones. |
| `parte_b.py` | **Parte B** (B1–B8): Listas, recorridos con `for`, filtrado, ordenamiento, slicing `[::-1]`, `set()` y promedio móvil. |
| `parte_c.py` | **Parte C** (C1–C8): Diccionarios, `.get()`, listas de dicts, búsqueda por director, unión con `|`, contador de palabras e inventario anidado. |
| `parte_d.py` | **Parte D** (D1–D6): Funciones `promedio()`, `aprobo()`, `estadisticas()` y `reporte()`, incluyendo manejo de lista vacía. |
| `parte_e.py` | **Parte E** (E1–E5): Lectura de `peliculas.csv`, conversión de tipos, reporte, filtrado hacia `filtradas.csv` y promedio por género. |
| `GUIA_GIT_PARTE_F.md` | **Parte F** (F1–F8): Guía paso a paso de comandos Git en equipo y flujo de ramas + Pull Requests por Parte. |
| `test_promedio.py` | **Parte G** (G1–G8): Tests automáticos con `pytest` (`assert`, casos límite, diccionarios, `.get()` y `@pytest.mark.parametrize`). |
| `cierre_h1.py` | **Cierre H1**: Script integrador que lee `peliculas.csv`, calcula estadísticas y muestra el ranking ordenado. |
| `test_cierre_h1.py` | **Cierre H2**: Suite completa de tests con `pytest` que cubre todas las funciones de `cierre_h1.py`. |
| `peliculas.csv` | Dataset de películas con columnas `titulo,anio,puntaje,genero`. |
| `filtradas.csv` | CSV generado al filtrar películas por género (`Ciencia Ficcion`). |
| `notas-equipo.md` | Archivo de notas del equipo (ejercicio F1). |
| `.gitignore` | Reglas para ignorar el entorno virtual (`venv/`) y archivos temporales (ejercicio F3). |
| `requirements.txt` | Dependencias del proyecto (`pytest`). |

---

## Cómo configurar el entorno (venv)

1. **Clonar el repositorio y entrar a la carpeta:**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```

2. **Crear el entorno virtual (`venv`):**
   ```bash
   python -m venv venv
   ```

3. **Activar el entorno virtual:**
   - **En Windows (PowerShell):**
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - **En Windows (CMD):**
     ```cmd
     venv\Scripts\activate.bat
     ```
   - **En Linux / macOS / Raspberry Pi:**
     ```bash
     source venv/bin/activate
     ```

4. **Instalar las dependencias (`pytest`):**
   ```bash
   pip install -r requirements.txt
   ```

---

## Cómo correr el script del cierre (H1) y cada parte

Para ejecutar el **mini-proyecto integrador del cierre (H1)**:
```bash
python cierre_h1.py
```

Para ejecutar los ejercicios de cada parte individualmente:
```bash
python parte_a.py
python parte_b.py
python parte_c.py
python parte_d.py
python parte_e.py
```

---

## Cómo correr los tests automáticos (`pytest`)

Con el entorno virtual activado, ejecutar desde la raíz del repositorio:
```bash
pytest -v
```

O para correr un archivo de tests específico:
```bash
pytest test_promedio.py -v
pytest test_cierre_h1.py -v
```
