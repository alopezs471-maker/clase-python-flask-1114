# Tarea 3 - Crear varias rutas y varias paginas en Flask

## Objetivo tecnico

Convertir la app en un mini portal con varias paginas conectadas entre si.
En esta tarea debes entender el flujo completo: `URL -> funcion Python -> plantilla HTML`.

## Preparacion

1. Ejecuta la app con `python app.py`.
2. Verifica que `http://127.0.0.1:5000/` responde correctamente.
3. Ten abierto `app.py` y la carpeta `templates/`.

## Guia paso a paso

### Paso 1: Mantener la ruta principal

No rompas la ruta `/` que ya existe. Debe seguir renderizando `index.html`.

### Paso 2: Crear la ruta `/acerca`

En `app.py`, agrega:

```python
@app.route("/acerca")
def acerca():
    return render_template("acerca.html")
```

### Paso 3: Crear la ruta `/contacto`

En `app.py`, agrega:

```python
@app.route("/contacto")
def contacto():
    return render_template("contacto.html")
```

### Paso 4: Crear las plantillas nuevas

Crea dos archivos:

1. `templates/acerca.html`
2. `templates/contacto.html`

Cada archivo debe tener estructura HTML basica y un titulo visible (`<h1>`) para distinguir la pagina.

### Paso 5: Agregar navegacion entre paginas

En `index.html`, `acerca.html` y `contacto.html`, agrega enlaces:

```html
<a href="/">Inicio</a>
<a href="/acerca">Acerca</a>
<a href="/contacto">Contacto</a>
```

Ideal: que el bloque de navegacion este en las 3 paginas.

### Paso 6: Verificar en navegador

Abre manualmente estas URLs:

1. `http://127.0.0.1:5000/`
2. `http://127.0.0.1:5000/acerca`
3. `http://127.0.0.1:5000/contacto`

Luego navega solo con los links para comprobar que todo conecta.

## Checklist de validacion

1. `app.py` contiene `/`, `/acerca` y `/contacto`.
2. Existen `index.html`, `acerca.html` y `contacto.html`.
3. Las tres paginas cargan sin error.
4. Hay navegacion entre las tres rutas.

## Errores comunes (y como corregirlos)

1. `TemplateNotFound`: la ruta existe, pero falta el archivo HTML.
   Solucion: crea el archivo dentro de `templates/` con el nombre exacto.
2. Error 404: existe el HTML, pero no la ruta en `app.py`.
   Solucion: agrega el `@app.route(...)` y su funcion.
3. Link mal escrito (por ejemplo `/contato`).
   Solucion: revisa que `href` coincida exactamente con la ruta.

## Preguntas de reflexion tecnica

1. Que parte define la URL publica: el nombre de la funcion o `@app.route(...)`?
2. Si cambias el nombre de la funcion, que debe mantenerse para no romper la URL?
3. Por que separar cada seccion en su propia plantilla mejora el proyecto?

## Entregable

1. `app.py` actualizado con las 3 rutas.
2. `templates/acerca.html` y `templates/contacto.html` creados.
3. Navegacion funcional entre las tres paginas.
4. Explicacion corta de un flujo completo, por ejemplo:
   `/contacto -> contacto() -> render_template("contacto.html") -> navegador`.
