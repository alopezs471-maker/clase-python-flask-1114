# Tarea 3 - Multiple paginas: Inicio, Informacion, Recursos, Tareas

## Objetivo

Crear un portal con **multiples paginas** conectadas.

Hasta ahora solo tenemos `/` (inicio). Ahora vamos a agregar:
- `/informacion` - Detalles de la clase
- `/recursos` - Links a documentacion
- `/tareas` - Lista de tareas entregables

## ¿Por que es importante?

Un portal real no es una sola pagina. Los usuarios navegan entre secciones.
Aprenderas a:
- Crear multiples rutas
- Pasar datos diferentes a cada ruta
- Conectarlas con un menu de navegacion

## Preparacion

1. Asegurate que Tarea 2 funciona
2. Crea dos archivos HTML nuevos: `templates/informacion.html` y `templates/recursos.html`

## Paso 1: Agregar rutas a app.py

Abre `app.py` y agrega nuevas funciones:

```python
@app.route("/informacion")
def informacion():
    datos = {
        "aula": "215",
        "profesor": "Henry Ortegon",
        "horario": "Miercoles 16:45-18:10 | Jueves 12:30-14:20",
        "objetivos": [
            "Aprender Python basico",
            "Entender Flask y aplicaciones web",
            "Construir un portal web real"
        ]
    }
    return render_template("informacion.html", **datos)

@app.route("/recursos")
def recursos():
    enlaces = [
        {"nombre": "Documentacion Flask", "url": "https://flask.palletsprojects.com"},
        {"nombre": "Tutorial Python", "url": "https://docs.python.org"},
        {"nombre": "GitHub del Profesor", "url": "https://github.com/hortegon"}
    ]
    return render_template("recursos.html", enlaces=enlaces)

@app.route("/tareas")
def tareas():
    lista_tareas = [
        {"numero": 1, "titulo": "Portal base", "fecha": "25/05/2026"},
        {"numero": 2, "titulo": "Datos dinamicos", "fecha": "30/05/2026"},
        {"numero": 3, "titulo": "Multiple paginas", "fecha": "05/06/2026"}
    ]
    return render_template("tareas.html", tareas=lista_tareas)
```

## Paso 2: Actualizar index.html con menu

En `templates/index.html`, agrega un menu de navegacion:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Portal Clase 1114</title>
</head>
<body>
    <!-- MENU DE NAVEGACION -->
    <nav>
        <ul>
            <li><a href="/">Inicio</a></li>
            <li><a href="/informacion">Informacion</a></li>
            <li><a href="/recursos">Recursos</a></li>
            <li><a href="/tareas">Tareas</a></li>
        </ul>
    </nav>

    <h1>Bienvenidos al Portal de Clase 1114</h1>
    <p>Profesor: {{ profesor }}</p>
    <p>Horario: {{ horario }}</p>
</body>
</html>
```

## Paso 3: Crear templates/informacion.html

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Informacion - Portal Clase 1114</title>
</head>
<body>
    <!-- MENU -->
    <nav>
        <ul>
            <li><a href="/">Inicio</a></li>
            <li><a href="/informacion">Informacion</a></li>
            <li><a href="/recursos">Recursos</a></li>
            <li><a href="/tareas">Tareas</a></li>
        </ul>
    </nav>

    <h1>Informacion de la Clase</h1>
    <p><strong>Aula:</strong> {{ aula }}</p>
    <p><strong>Profesor:</strong> {{ profesor }}</p>
    <p><strong>Horario:</strong> {{ horario }}</p>

    <h2>Objetivos</h2>
    <ul>
        <!-- Aqui va el bucle for (Tarea 4) -->
    </ul>
</body>
</html>
```

## Paso 4: Crear templates/recursos.html

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Recursos - Portal Clase 1114</title>
</head>
<body>
    <!-- MENU -->
    <nav>
        <ul>
            <li><a href="/">Inicio</a></li>
            <li><a href="/informacion">Informacion</a></li>
            <li><a href="/recursos">Recursos</a></li>
            <li><a href="/tareas">Tareas</a></li>
        </ul>
    </nav>

    <h1>Recursos Educativos</h1>
    <p>Enlaces utiles para aprender mas:</p>

    <!-- Aqui va el bucle for (Tarea 4) -->
</body>
</html>
```

## Paso 5: Crear templates/tareas.html

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Tareas - Portal Clase 1114</title>
</head>
<body>
    <!-- MENU -->
    <nav>
        <ul>
            <li><a href="/">Inicio</a></li>
            <li><a href="/informacion">Informacion</a></li>
            <li><a href="/recursos">Recursos</a></li>
            <li><a href="/tareas">Tareas</a></li>
        </ul>
    </nav>

    <h1>Tareas Entregables</h1>
    
    <!-- Aqui va el bucle for (Tarea 4) -->
</body>
</html>
```

## Paso 6: Verifica

Guarda todos los archivos y recarga la app. En el navegador:
- Ve a `http://127.0.0.1:5000/informacion`
- Ve a `http://127.0.0.1:5000/recursos`
- Ve a `http://127.0.0.1:5000/tareas`

El menu deberia permitirte navegar entre paginas.

## Conceptos clave

**Rutas** conectan URLs a funciones Python.

```python
@app.route("/pagina")  # La URL
def nombre_funcion():  # Que ocurre
    return render_template("pagina.html")  # Que se muestra
```

**Links** en HTML conectan las paginas:

```html
<a href="/informacion">Informacion</a>
```

## Preguntas de reflexion

1. Si tienes 10 paginas diferentes, ¿cuantas funciones necesitas en app.py?
2. ¿Que pasa si cambias el nombre de una ruta pero no actualizas los links?
3. ¿Por que es importante tener un menu consistente en todas las paginas?

## Entregable

Debes mostrar:

1. `app.py` con 4 rutas diferentes (/, /informacion, /recursos, /tareas)
2. 4 archivos HTML en `templates/` (index, informacion, recursos, tareas)
3. Un menu de navegacion en todas las paginas
4. Capturas navegando entre las 4 paginas diferentes

## Resumen

Ya tienes un portal web con **navegacion**. Las paginas estan conectadas.

En la siguiente tarea, vamos a llenar las listas de tareas y recursos usando **bucles en Jinja2**.

