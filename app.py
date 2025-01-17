from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Cola de comandos para los clientes
commands = []

@app.route("/control", methods=["POST"])
def control():
    data = request.json
    command = data.get("command", "")
    if command:
        commands.append(command)  # Agregar el comando a la cola
        print(f"Comando recibido: {command}")
    return jsonify({"message": "Comando recibido"})

@app.route("/get_command", methods=["GET"])
def get_command():
    if commands:
        command = commands.pop(0)  # Obtener el primer comando en la cola
        return jsonify({"command": command})
    return jsonify({"command": None})

@app.route("/")
def home():
    return "Servidor Flask Activo"

if __name__ == "__main__":
    app.run(debug=True)
