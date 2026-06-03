# Tarea 2 - Datos dinamicos: Profesor, horario desde Python

## Objetivo

En Tarea 1, los datos (profesor, horario) estaban **hardcodeados** en HTML.
Ahora vamos a sacarlos desde **Python y enviarlos a la plantilla**.

Esto es lo que hace poderoso a Flask: separar datos de presentacion.

## ¿Por que es importante?

Si cambias el horario de la clase en 3 meses, ¿donde lo cambias?
- Forma vieja (Tarea 1): Editar HTML manualmente
- Forma nueva (Tarea 2): Cambiar una variable en Python

La forma nueva **escala mejor**.

## Preparacion

1. Asegurate que la Tarea 1 funciona (el portal levanta sin errores)
2. Ten abierto `app.py` en tu editor

## Paso 1: Ver el codigo actual

En `app.py` deberias tener algo asi:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```

## Paso 2: Agregar variables en Python

Modifica la funcion `inicio()` para crear variables:

```python
@app.route("/")
def inicio():
    # Datos del portal
    nombre_profesor = "Henry Ortegon"
    email_profesor = "henry@kyrbot.com"
    horario = "Miercoles 16:45-18:10 | Jueves 12:30-14:20"
    aula = "215"
    descripcion = "Aprenderemos Python, Flask y construiremos un portal web real"
    
    # Pasar los datos a la plantilla
    return render_template(
        "index.html",
        profesor=nombre_profesor,
        email=email_profesor,
        horario=horario,
        aula=aula,
        descripcion=descripcion
    )
```

## Paso 3: Usar variables en HTML

Abre `templates/index.html` y reemplaza los datos fijos por variables Jinja2:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portal {{ profesor }}</title>
</head>
<body>
    <h1>Bienvenidos al Portal de Clase 1114</h1>
    
    <h2>Informacion de la clase</h2>
    <p><strong>Profesor:</strong> {{ profesor }}</p>
    <p><strong>Email:</strong> {{ email }}</p>
    <p><strong>Horario:</strong> {{ horario }}</p>
    <p><strong>Aula:</strong> {{ aula }}</p>
    <p><strong>Descripcion:</strong> {{ descripcion }}</p>
</body>
</html>
```

## Paso 4: Guarda y verifica

1. Guarda `app.py`
2. Flask deberia auto-reiniciar (veras mensajes en la terminal)
3. Recarga el navegador (Ctrl+R)

Deberias ver los mismos datos, pero ahora **vienen desde Python**.

## Paso 5: Prueba el cambio

Cambia una variable en `app.py`. Por ejemplo:

```python
nombre_profesor = "Prof. Henry - Kyrbot Innovations"
```

Guarda, y verifica que el cambio aparece en el navegador.

**Eso demuestra que los datos vienen desde Python, no del HTML.**

## Conceptos clave

**Jinja2** es el motor de plantillas que Flask usa.

En HTML escribes `{{ variable }}` para mostrar valores de Python.

Ejemplo:
```python
# En Python
nombre = "Ana"
edad = 25

# En HTML con Jinja2
<p>Nombre: {{ nombre }}</p>
<p>Edad: {{ edad }}</p>

# Resultado en navegador
Nombre: Ana
Edad: 25
```

## Preguntas de reflexion

1. ¿Cual es la diferencia entre escribir datos en HTML vs guardarlos en variables Python?
2. Si el profesor cambia mañana, ¿cuantos archivos necesitas editar con este enfoque?
3. ¿Que ventaja tiene usar `{{ }}` en lugar de escribir texto fijo?
4. ¿Donde se ejecuta Jinja2: en la computadora del usuario o en el servidor?

## Entregable

Debes mostrar:

1. El archivo `app.py` con al menos 5 variables (profesor, email, horario, aula, descripcion)
2. El archivo `templates/index.html` usando `{{ }}` para mostrar esas variables
3. Una captura del navegador mostrando los datos dinamicos
4. Evidencia de que cambiar una variable en Python se refleja en el navegador

## Resumen

Ahora entiendes la **separacion de responsabilidades**:
- Python maneja los datos
- HTML maneja la presentacion
- Jinja2 conecta ambos

En la siguiente tarea, vamos a agregar **mas paginas** al portal (Informacion, Recursos, Tareas).

