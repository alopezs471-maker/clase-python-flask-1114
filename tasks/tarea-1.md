# Tarea 1 - Portal de Clase 1114: Estructura basica

## Objetivo

Construir la estructura inicial del **Portal de Clase 1114**. Este sera el sitio web donde estudiantes y profesor accederan a informacion de la clase.

En esta tarea vas a:
- Levantar la aplicacion Flask
- Crear la pagina de inicio
- Entender la estructura basica

## Concepto: ¿Que es el Portal de Clase?

Es una aplicacion web donde:
- Los estudiantes ven informacion de la clase
- Ven tareas disponibles
- Se pueden inscribir
- Ven calificaciones

Tu trabajo en estas 8 tareas es **construir este portal paso a paso**.

## Preparacion

1. Copia este proyecto a tu computadora
2. Abre una terminal en la carpeta del proyecto
3. Sigue los pasos del README.md para instalar dependencias

## Paso 1: Crear el entorno virtual

Windows PowerShell:
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Linux/Mac:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Verifica que veas (.venv) al inicio de tu terminal.

## Paso 2: Instalar dependencias

```powershell
pip install -r requirements.txt
```

## Paso 3: Levanta la aplicacion

```powershell
python app.py
```

Deberias ver en la terminal:
```
 * Running on http://127.0.0.1:5000
```

## Paso 4: Abre el navegador

Ve a http://127.0.0.1:5000 en tu navegador.

Deberias ver una pagina de bienvenida simple.

## Paso 5: Modifica el portal

Abre templates/index.html y cambia:

1. El <title> a: Portal Clase 1114 - Python y Flask

2. El <h1> a: Bienvenidos al Portal de Clase 1114

3. Agrega un nuevo <p> que diga:
```html
<p>Profesor: Henry Ortegon</p>
<p>Horario: Miercoles 16:45-18:10 | Jueves 12:30-14:20</p>
```

Guarda el archivo y recarga la pagina en el navegador (Ctrl+R).

Deberias ver tus cambios inmediatamente.

## Paso 6: Verifica en la terminal

En la terminal donde corre Flask, deberias ver lineas como:
```
127.0.0.1 - - [fecha hora] "GET / HTTP/1.1" 200 -
```

Eso significa que el servidor recibio la solicitud y respondo exitosamente (200 = OK).

## Preguntas de reflexion

1. ¿Que rol tiene app.py en todo esto?
2. ¿Por que necesitas el entorno virtual (.venv)?
3. ¿Donde se almacena el HTML que ves en el navegador?
4. Si cambias el HTML sin guardar, ¿se refleja el cambio en el navegador? ¿Por que?
5. ¿Que es render_template y por que Flask lo usa?

## Entregable

Debes demostrar:

1. El entorno virtual activado en la terminal
2. La aplicacion corriendo en http://127.0.0.1:5000
3. El titulo del navegador dice "Portal Clase 1114 - Python y Flask"
4. El <h1> muestra "Bienvenidos al Portal de Clase 1114"
5. Muestra el nombre del profesor y horario
6. Una captura de pantalla mostrando todo funcionando

## Resumen

Hoy activaste tu primer proyecto Flask real. El Portal de Clase apenas empieza.
En la siguiente tarea, vamos a hacer que los datos (nombre profesor, horario) vengan desde Python, no desde HTML fijo.

Eso es lo poderoso de los frameworks web: separar datos de presentacion.
