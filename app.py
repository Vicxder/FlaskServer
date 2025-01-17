from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

# Inicializar SocketIO
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/control", methods=["POST", "OPTIONS"])
def control():
    if request.method == "POST":
        data = request.json
        command = data.get("command", "")
        print(f"Comando recibido vía HTTP: {command}")
        # Emitir el comando a través de SocketIO a los clientes conectados
        socketio.emit("command", {"command": command})
        return jsonify({"message": "Comando recibido", "command": command})
    return "OK", 200

@app.route("/")
def home():
    return "Servidor Flask-SocketIO Activo"

# Evento de conexión de SocketIO
@socketio.on('connect')
def handle_connect():
    print("Cliente conectado vía SocketIO")
    emit("message", {"info": "Conexión establecida"})

# Evento de desconexión de SocketIO
@socketio.on('disconnect')
def handle_disconnect():
    print("Cliente desconectado")

if __name__ == "__main__":
    socketio.run(app, debug=True)
