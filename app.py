from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

@app.route("/control", methods=["POST", "OPTIONS"])
def control():
    if request.method == "POST":
        data = request.json
        command = data.get("command", "")
        print(f"Comando recibido: {command}")
        return jsonify({"message": "Comando recibido", "command": command})
    return "OK", 200

@app.route("/")
def home():
    return "Servidor Flask Activo"

if __name__ == "__main__":
    app.run(debug=True)
