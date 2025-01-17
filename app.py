from flask import Flask, request, jsonify
from flask_cors import CORS
import paho.mqtt.publish as publish

app = Flask(__name__)
CORS(app)  # Habilitar CORS

# Ruta para recibir comandos y enviarlos vía MQTT
@app.route("/control", methods=["POST"])
def control():
    data = request.json
    command = data.get("command", "")
    if command:
        try:
            # Publicar el comando en el tema MQTT
            publish.single("auto_rc/control", command, hostname="broker.emqx.io")
            print(f"Comando enviado vía MQTT: {command}")
            return jsonify({"message": "Comando enviado vía MQTT", "command": command})
        except Exception as e:
            print(f"Error al publicar en MQTT: {e}")
            return jsonify({"message": "Error enviando comando", "error": str(e)}), 500
    return jsonify({"message": "No se recibió ningún comando"}), 400

@app.route("/")
def home():
    return "Servidor Flask con MQTT Activo"

if __name__ == "__main__":
    app.run(debug=True)
