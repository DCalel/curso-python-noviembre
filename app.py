from flask import Flask, request

app = Flask(__name__)

#Indicada un endpoint decorador @app.route()
@app.route('/')
def hello_world():
    return "HOLA MUNDO"

# path parameter se encierra en < >
# limitar un tipo de dato, se coloca el tipo al inicio del nombre de la variable
@app.route('/edad/<int:edad_persona>')
def mostrar_edad(edad_persona):
    if edad_persona >= 18:
        return "Es un adulto"
    else:
        return "No es un adulto"

@app.route('/saludo', methods=["POST"])
def saludar():
    return "Saludo a todos desde el POST"

@app.route('/saludo', methods=["PUT"])
def saludar_get():
    return "Saludo a todos desde el PUT"


@app.route('/users', methods=["POST"])
def registrar():
    return {
        "metodo": request.method,
        "nombre": request.form["nombre"],
        "edad": request.form["edad"],
    }

@app.errorhandler(404)
def not_found(error):
    return "Ops este endpoint no existe."

@app.route("/query")
def return_query_params():
    return request.args.get("key", "Valor-defecto")

# Servidor