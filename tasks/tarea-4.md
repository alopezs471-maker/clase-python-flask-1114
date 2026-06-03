# Tarea 4 - Listas dinamicas: Bucles for en Jinja2

## Objetivo

Mostrar **listas** de tareas y recursos usando bucles `{% for %}` en Jinja2.

Hasta ahora pasamos datos simples (strings). Ahora vamos a pasar **listas** y recorrerlas en HTML.

## ¿Por que es importante?

Si tienes 100 tareas, no vas a escribir 100 lineas de HTML. Los bucles automatizan eso.

## Preparacion

1. Asegurate que Tarea 3 funciona
2. Los datos ya existen en `app.py` (listas de tareas, enlaces, objetivos)

## Paso 1: Agregar bucles en tareas.html

En `templates/tareas.html`, reemplaza el comentario con:

```html
<table border="1">
    <thead>
        <tr>
            <th>Numero</th>
            <th>Titulo</th>
            <th>Fecha entrega</th>
        </tr>
    </thead>
    <tbody>
        {% for tarea in tareas %}
        <tr>
            <td>{{ tarea.numero }}</td>
            <td>{{ tarea.titulo }}</td>
            <td>{{ tarea.fecha }}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
```

**Explicacion:**
- `{% for tarea in tareas %}` - Recorre cada tarea de la lista
- `{{ tarea.numero }}` - Accede a la propiedad `numero` de esa tarea
- `{% endfor %}` - Termina el bucle

## Paso 2: Agregar bucles en recursos.html

En `templates/recursos.html`:

```html
<ul>
    {% for enlace in enlaces %}
    <li>
        <a href="{{ enlace.url }}">{{ enlace.nombre }}</a>
    </li>
    {% endfor %}
</ul>
```

## Paso 3: Agregar bucles en informacion.html

En `templates/informacion.html`:

```html
<h2>Objetivos de la clase</h2>
<ul>
    {% for objetivo in objetivos %}
    <li>{{ objetivo }}</li>
    {% endfor %}
</ul>
```

## Paso 4: Verifica

Guarda todo y recarga las paginas:
- `/tareas` deberia mostrar una tabla con las 3 tareas
- `/recursos` deberia mostrar una lista de enlaces
- `/informacion` deberia mostrar los objetivos

## Paso 5: Agrega mas datos

En `app.py`, en la funcion `recursos()`, agrega mas enlaces:

```python
enlaces = [
    {"nombre": "Documentacion Flask", "url": "https://flask.palletsprojects.com"},
    {"nombre": "Tutorial Python", "url": "https://docs.python.org"},
    {"nombre": "GitHub del Profesor", "url": "https://github.com/hortegon"},
    {"nombre": "MDN - HTML y CSS", "url": "https://developer.mozilla.org"}
]
```

Recarga la pagina. Deberia verse el nuevo enlace automaticamente, **sin cambiar HTML**.

**Eso es el poder de los bucles: agregar datos sin modificar el template.**

## Conceptos clave

**Diccionarios en Python:**

```python
enlace = {
    "nombre": "Flask",
    "url": "https://flask.com"
}
```

En HTML accedes con `{{ enlace.nombre }}` o `{{ enlace['nombre'] }}`

**Listas de diccionarios:**

```python
enlaces = [
    {"nombre": "Flask", "url": "..."},
    {"nombre": "Python", "url": "..."}
]
```

En HTML:
```html
{% for enlace in enlaces %}
    {{ enlace.nombre }}
{% endfor %}
```

## Preguntas de reflexion

1. Si tienes 50 tareas en la lista, ¿cuantas lineas de HTML necesitas escribir?
2. ¿Que pasa si accedes a una propiedad que no existe, como `{{ tarea.profesor }}`?
3. ¿Como cambarias el bucle si quisieras mostrar solo las primeras 5 tareas?

## Entregable

Debes mostrar:

1. `tareas.html` con un bucle `{% for %}` mostrando todas las tareas en una tabla
2. `recursos.html` con un bucle mostrando todos los enlaces
3. `informacion.html` con un bucle mostrando todos los objetivos
4. Una captura de cada pagina mostrando los datos dinamicos en bucles
5. Evidencia de que agregar un item a la lista en Python se refleja en HTML

## Resumen

Ya entiendes bucles en Jinja2. Esto es fundamental para mostrar datos reales.

En la siguiente tarea, vamos a agregar un **formulario** para que estudiantes se inscriban en la clase.

