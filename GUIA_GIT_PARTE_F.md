# Guía Práctica — Parte F (Git en equipo) y Entrega por Pull Requests

Esta guía resume los comandos exactos para realizar la **Parte F (F1 a F8)** y para entregar cada Parte mediante **ramas + Pull Requests (PR)** en tu repositorio individual `IC-IC2-apellido-fecha_de_la_practica`.

---

## 1. Cómo entregar los ejercicios en tu repo individual (Flujo Rama -> PR -> Merge)

Según `consignas.md`, **no** se hace push directo a `main` para los ejercicios individuales, sino **un Pull Request por cada Parte**:

```bash
# 1. Inicializar o clonar tu repo individual (ej. IC-IC2-apellido-2026-10-24)
git clone https://github.com/<tu-usuario>/IC-IC2-apellido-2026-10-24.git
cd IC-IC2-apellido-2026-10-24

# 2. Crear y pasar a la rama de la Parte A
git checkout -b parte-a
git add parte_a.py .gitignore
git commit -m "Resuelve ejercicios de la Parte A (tipos, variables y operaciones)"
git push -u origin parte-a
# -> Ir a GitHub, abrir el Pull Request de `parte-a` hacia `main` y apretar "Merge pull request".

# 3. Volver a main, actualizar y crear la rama de la Parte B
git checkout main
git pull origin main
git checkout -b parte-b
git add parte_b.py
git commit -m "Resuelve ejercicios de la Parte B (listas y promedio movil)"
git push -u origin parte-b
# -> Abrir PR en GitHub y mergear a `main`.

# 4. Repetir para Parte C, Parte D, Parte E, Parte G y Cierre H:
#    - Rama `parte-c`: agrega `parte_c.py`
#    - Rama `parte-d`: agrega `parte_d.py`
#    - Rama `parte-e`: agrega `peliculas.csv`, `filtradas.csv` y `parte_e.py`
#    - Rama `parte-g`: agrega `requirements.txt` y `test_promedio.py`
#    - Rama `cierre-h`: agrega `cierre_h1.py`, `test_cierre_h1.py` y `README.md`
```

---

## 2. Resolución paso a paso de la Parte F (en el repo del equipo)

### 🟢 F1 — El ciclo completo
```bash
git clone <URL_REPO_EQUIPO>
cd <CARPETA_REPO_EQUIPO>
# Crear o editar notas-equipo.md con los nombres del grupo
git add notas-equipo.md
git commit -m "Agrega notas-equipo.md con los integrantes del grupo"
git push origin main
# El compañero ejecuta en su máquina:
git pull origin main
```

### 🟢 F2 — Mensajes que sirven
Hacer commits atómicos y descriptivos, y verificar el historial:
```bash
git log --oneline
```

### 🟡 F3 — `.gitignore`
Crear el entorno virtual y asegurarse de que `.gitignore` incluya `venv/`:
```bash
python -m venv venv
git status
# Como `venv/` está en `.gitignore`, Git no intenta subir la carpeta del entorno virtual.
```

### 🔴 F4 — Provocar y resolver un merge conflict
1. Dos integrantes editan **la misma línea** de `notas-equipo.md`, hacen `git add notas-equipo.md` y `git commit -m "..."`.
2. El primero hace `git push origin main`.
3. El segundo intenta `git push origin main` (Git lo rechaza) y ejecuta `git pull origin main`.
4. Git marca el conflicto en el archivo:
   ```text
   <<<<<<< HEAD
   Versión local
   =======
   Versión que vino de GitHub
   >>>>>>> <hash-del-commit>
   ```
5. Borrar las marcas `<<<<<<<`, `=======`, `>>>>>>>`, dejar el texto acordado y cerrar el conflicto:
   ```bash
   git add notas-equipo.md
   git commit -m "Resuelve conflicto de merge en notas-equipo.md"
   git push origin main
   ```

### 🔴 F5 — Volver atrás
Ver el historial de commits y consultar o revertir un cambio que rompió algo:
```bash
git log --oneline
# Para ver cómo estaba un commit anterior sin borrar historia:
git show <hash-del-commit>
# Para crear un commit que deshaga el commit roto de forma segura:
git revert <hash-del-commit>
```

### 🟢 F6 — Una rama propia
```bash
git checkout -b rama-prueba-integrante
# Editar notas-equipo.md agregando una línea
git add notas-equipo.md
git commit -m "Agrega firma en rama separada"
git checkout main
# Al volver a main, el cambio hecho en `rama-prueba-integrante` no está en `main`.
```

### 🟡 F7 — Traer la rama de vuelta (`merge`)
```bash
git checkout main
git merge rama-prueba-integrante
# Ahora el cambio de la rama se unió a `main`.
```

### 🔴 F8 — Guardar sin commitear (`git stash`)
```bash
# Hacés un cambio en un archivo pero todavía no querés commitearlo:
git stash
# Ahora el directorio de trabajo queda limpio para cambiar de rama:
git checkout otra-rama
git checkout main
# Recuperás tu cambio a medio hacer intacto:
git stash pop
```
