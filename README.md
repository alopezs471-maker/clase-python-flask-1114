# Portal de Clase 1114 - Python y Flask

## Clase 1114 - Introducción a Python y Flask

**Profesor:** Henry Ortegon (Kyrbot Innovations)  
**Horario:** Miércoles 16:45-18:10 | Jueves 12:30-14:20  
**Aula:** 215  
**Email Profesor:** henry@kyrbot.com

---

## Que es este proyecto

Es el **Portal Web oficial de Clase 1114** donde estudiantes y profesor acceden a:
- Información de la clase
- Tareas entregables
- Calificaciones
- Recursos educativos
- Sistema de inscripción

**Los alumnos van a construirlo paso a paso en 8 tareas**, aprendiendo:
- Rutas y plantillas Flask
- Datos dinamicos con Jinja2
- Multiples paginas
- Bucles y listas
- Formularios
- Base de datos SQLite
- Autenticacion y sesiones
- CRUD (Create, Read, Update, Delete)

## El Portal incluye

- Pagina de inicio con info de la clase
- Formulario de inscripcion para estudiantes
- Base de datos de estudiantes inscritos
- Login para Profesor y Estudiantes
- Panel del Profesor: crear, editar, eliminar tareas
- Panel del Estudiante: ver tareas asignadas
- Sistema de permisos por rol

## Requisitos

- Python 3.8+
- Terminal
- Editor de codigo (VS Code, PyCharm, etc)

## Instalacion rapida

1. Copia la carpeta a tu computadora
2. Abre terminal en la carpeta

Crear entorno virtual (Windows):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

O en Linux/Mac:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instala dependencias:
```powershell
pip install -r requirements.txt
```

4. Ejecuta el portal:
```powershell
python app.py
```

5. Abre http://127.0.0.1:5000 en tu navegador

## Las 8 Tareas + BONUS

| # | Tarea | Que aprendes | Entrega |
|---|-------|-------------|---------|
| 1 | Portal base | Levantar Flask, HTML, rutas basicas | Captura funcionando |
| 2 | Datos dinamicos | Jinja2, variables de Python en HTML | app.py + index.html |
| 3 | Multiple paginas | Varias rutas, menu de navegacion | 4 HTML + app.py |
| 4 | Listas y bucles | For en Jinja2, mostrar listas | Tablas dinamicas |
| 5 | Formularios | Recibir datos del usuario | Formulario inscripcion |
| 6 | Base de datos | SQLite, guardar datos persistentes | BD + Portal |
| 7 | Autenticacion | Login, sesiones, roles (Profesor vs Estudiante) | Login funcional |
| 8 | CRUD completo | Crear, editar, eliminar tareas | Portal completo |
| **9** | **Diseño CSS** | **Bootstrap, diseño profesional** | **Portal visualmente atractivo** |

## Estructura del proyecto

```
clase-python-flask-1114/
├── app.py              # Aplicacion principal
├── requirements.txt    # Dependencias
├── portal.db          # Base de datos (se crea)
├── templates/         # Plantillas HTML
│   ├── index.html
│   ├── login.html
│   ├── panel_profesor.html
│   ├── panel_estudiante.html
│   └── ...mas templates
└── tasks/             # Consignas de trabajo (8 tareas)
    ├── tarea-1.md
    ├── tarea-2.md
    └── ... tarea-8.md
```

## Como iniciar cada tarea

1. Lee la consigna en `tasks/tarea-X.md`
2. Sigue los pasos paso a paso
3. Modifica `app.py` y `templates/`
4. Verifica en el navegador en http://127.0.0.1:5000
5. Entrega evidencia (capturas, archivos modificados)

## Datos de prueba (a partir de Tarea 7)

**Profesor:**
- Usuario: `henry`
- Contraseña: `password123`

## Lo que vas a aprender

- Backend web con Python y Flask
- Frontend HTML con Jinja2
- Bases de datos relacionales (SQLite)
- Autenticacion y sesiones
- Operaciones CRUD
- Arquitectura MVC
- Seguridad (hashing de contraseñas)
- Desarrollo de aplicaciones web reales

## Fechas importantes

- **Tarea 1-2:** Semana 1 (Bases de Flask)
- **Tarea 3-4:** Semana 2 (Rutas y listas)
- **Tarea 5-6:** Semana 3-4 (Formularios y BD)
- **Tarea 7-8:** Semana 5 (Autenticacion y CRUD)

## Contacto

- **Profesor:** henry@kyrbot.com
- **GitHub:** https://github.com/hortegon
- **Kyrbot:** https://kyrbot.com

## Proximamente

- Agregar calificaciones
- Sistema de entregas de trabajos
- Notificaciones por email
- Interfaz mejorada con CSS
- Deploy en internet (Heroku, PythonAnywhere)
- API REST

---

**Portal de Clase 1114 - Introducción a Python y Flask**  
Diseño y contenido: Henry Ortegon (Kyrbot Innovations)
