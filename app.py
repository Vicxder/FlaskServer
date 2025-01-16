from flask import Flask, request, jsonify
from flask_cors import CORS  # Importar Flask-CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

@app.route('/control', methods=['POST'])
def control():
    data = request.json  # Recibir datos JSON del frontend
    command = data.get('command')
    if command:
        print(f"Comando recibido: {command}")
        return jsonify({"status": "success", "command": command}), 200
    else:
        return jsonify({"status": "error", "message": "Comando no proporcionado"}), 400

if __name__ == '__main__':
    app.run(debug=True)
