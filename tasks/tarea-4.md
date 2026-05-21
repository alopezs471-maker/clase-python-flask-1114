# Tarea 4 - Mostrar listas con Jinja en Flask

## Objetivo tecnico

Agregar la pagina `/recursos` y mostrar una coleccion de datos con un bucle de Jinja.
La meta es pasar de variables sueltas a renderizar listas completas.

## Preparacion

Antes de empezar, valida que la tarea 3 funciona:

1. `/`
2. `/acerca`
3. `/contacto`

Si alguna ruta falla, arreglala primero y luego continua.

## Guia paso a paso

### Paso 1: Crear la ruta `/recursos`

En `app.py`, agrega una nueva funcion con su decorador.

### Paso 2: Definir la lista en Python

Dentro de esa funcion, crea una lista con minimo 4 elementos.
Ejemplo:

```python
recursos = [
    "Entorno virtual",
    "Rutas en Flask",
    "Plantillas HTML",
    "Variables con Jinja"
]
```

### Paso 3: Enviar la lista a la plantilla

Retorna `render_template` pasando la variable:

```python
return render_template("recursos.html", recursos=recursos)
```

### Paso 4: Crear `templates/recursos.html`

Crea el archivo y agrega estructura HTML basica.
Incluye un titulo como `<h1>Recursos de clase</h1>`.

### Paso 5: Recorrer la lista con Jinja

En `recursos.html`, usa un `<ul>` con bucle:

```html
<ul>
  {% for recurso in recursos %}
    <li>{{ recurso }}</li>
  {% endfor %}
</ul>
```

Ese bloque debe generar un `<li>` por cada elemento de la lista de Python.

### Paso 6: Integrar navegacion

Agrega enlace a `/recursos` desde `index.html`, `acerca.html` y `contacto.html`.
Tambien incluye links de regreso desde `recursos.html` al resto de paginas.

### Paso 7: Verificar en navegador

1. Abre `http://127.0.0.1:5000/recursos`.
2. Comprueba que se vean los 4 (o mas) elementos.
3. Cambia un texto en la lista de `app.py`, guarda y recarga.
4. Verifica que el cambio aparece en la pagina.

## Checklist de validacion

1. Existe la ruta `/recursos` en `app.py`.
2. Existe `templates/recursos.html`.
3. La lista tiene al menos 4 elementos en Python.
4. El HTML usa `{% for %}` y `{{ recurso }}`.
5. La pagina muestra la lista correctamente.
6. Hay navegacion entre todas las paginas del mini portal.

## Errores comunes (y como corregirlos)

1. Error de sintaxis en Jinja: olvidar `%` o llaves.
   Solucion: revisa el formato exacto de `{% for ... %}` y `{% endfor %}`.
2. Nombre inconsistente: en Python `recursos`, en HTML `items`.
   Solucion: usa el mismo nombre en ambos lados.
3. Lista fuera de la funcion o mal indentada.
   Solucion: verifica indentacion dentro de la funcion de la ruta.
4. La pagina carga, pero no muestra elementos.
   Solucion: confirma que la lista no este vacia y que el bucle este dentro del `<ul>`.

## Preguntas de reflexion tecnica

1. Que cambia entre renderizar una variable simple y renderizar una lista?
2. Donde se ejecuta el bucle de Jinja: en el navegador o en Flask?
3. Que ventaja aporta este patron para casos reales (productos, tareas, alumnos)?

## Entregable

1. `app.py` con ruta `/recursos` funcional.
2. `templates/recursos.html` creado.
3. Lista de minimo 4 recursos definida en Python.
4. Lista mostrada con bucle `{% for %}` en HTML.
5. Navegacion hacia y desde la pagina de recursos.
6. Explicacion corta del flujo:
   `lista en Python -> render_template -> bucle Jinja -> HTML final en navegador`.
