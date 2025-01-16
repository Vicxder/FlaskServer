from flask import Flask, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Habilitar CORS para WebSockets

@app.route('/control', methods=['POST'])
def control():
    data = request.json
    command = data.get('command', 'Ninguno')
    print(f"Comando recibido: {command}")

    # Emitir el comando a todos los clientes conectados
    socketio.emit('command', {'command': command})
    return {'status': 'success', 'command': command}, 200

@socketio.on('connect')
def handle_connect():
    print("Cliente conectado")
    emit('message', {'status': 'Conexión establecida'})

@socketio.on('disconnect')
def handle_disconnect():
    print("Cliente desconectado")

if __name__ == "__main__":
    socketio.run(app, debug=True)
