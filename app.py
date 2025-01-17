from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit

# Inicialización de la aplicación Flask
app = Flask(__name__)
app.config["SECRET_KEY"] = "mi_clave_secreta"  # Cambiar si es necesario
CORS(app)  # Habilitar CORS para todas las rutas
socketio = SocketIO(app, cors_allowed_origins="*")

# Ruta para comandos HTTP
@app.route("/control", methods=["POST", "OPTIONS"])
def control():
    if request.method == "POST":
        data = request.json
        command = data.get("command", "")
        print(f"Comando recibido vía HTTP: {command}")
        return jsonify({"message": "Comando recibido", "command": command})
    return "OK", 200

# Ruta principal
@app.route("/")
def home():
    return "Servidor Flask con WebSocket y CORS Activo"

# Evento WebSocket: Conexión
@socketio.on("connect")
def handle_connect():
    print("Cliente conectado vía WebSocket")
    emit("message", {"data": "Conexión WebSocket establecida"})

# Evento WebSocket: Recepción de comando
@socketio.on("comando")
def handle_comando(data):
    print(f"Comando recibido vía WebSocket: {data}")
    emit("respuesta", {"message": f"Comando '{data}' procesado"})

# Ejecución de la aplicación
if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
