from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/")
def inicio():
    # Datos del portal
    nombre_estudiante = "Alejandro"
    email_estudiante = "Alopezs471@inemkennedy.edu.co"
    horario = "Miercoles 16:45-18:10 | Jueves 12:30-14:20"
    aula = "2"
    descripcion = "Aprenderemos Python, Flask y construiremos un portal web real"
    
    # Pasar los datos a la plantilla
    return render_template(
        "index.html",
        estudiante=nombre_estudiante,
        email=email_estudiante,
        horario=horario,
        aula=aula,
        descripcion=descripcion
    )
nombre = "ale"
edad = 20
@app.route("/informacion")
def informacion():
    datos = {
        "aula": "2",
        "estudiante": "alejandro lopez",
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
        {"nombre": "GitHub del Profesor", "url": "https://github.com/hortegon"},
    {"nombre": "MDN - HTML y CSS", "url": "https://developer.mozilla.org"},
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

@app.route("/inscripcion", methods=["GET", "POST"])
def inscripcion():
    mensaje = None
    
    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        programa = request.form.get("programa")
        
        # Validacion
        if not nombre or not email or not programa:
            mensaje = "Por favor completa todos los campos."
        else:
            try:
                # Crear nuevo estudiante
                nuevo_estudiante = Estudiante(
                    nombre=nombre,
                    email=email,
                    programa=programa
                )
                
                # Guardar en BD
                db.session.add(nuevo_estudiante)
                db.session.commit()
                
                mensaje = f"Bienvenido {nombre}! Te hemos registrado."
            except Exception as e:
                db.session.rollback()
                mensaje = f"Error: Este email ya esta registrado."
    
    return render_template("inscripcion.html", mensaje=mensaje)

@app.route("/estudiantes")
def estudiantes():
    lista_estudiantes = Estudiante.query.all()
    return render_template("estudiantes.html", estudiantes=lista_estudiantes)

class Estudiante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    programa = db.Column(db.String(50), nullable=False)
    fecha_inscripcion = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return f'<Estudiante {self.nombre}>'
    



if __name__ == "__main__":
    app.run(debug=True)
