from flask import Flask, render_template

app = Flask(__name__)

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
        profesor=nombre_estudiante,
        email=email_estudiante,
        horario=horario,
        aula=aula,
        descripcion=descripcion
    )
nombre = "ale"
edad = 20

if __name__ == "__main__":
    app.run(debug=True)
