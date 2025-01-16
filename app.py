from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta para recibir comandos
@app.route('/control', methods=['POST'])
def control():
    data = request.json  # Recibe el JSON enviado desde el cliente
    command = data.get('command')
    if command:
        print(f"Comando recibido: {command}")
        return jsonify({"status": "success", "command": command}), 200
    else:
        return jsonify({"status": "error", "message": "Comando no proporcionado"}), 400

if __name__ == '__main__':
    app.run(debug=True)

