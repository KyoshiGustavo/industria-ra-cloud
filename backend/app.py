from flask import Flask, jsonify
from flask_cors import CORS
import paho.mqtt.client as mqtt
import threading
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)  

equipamento_dados = {
    "id": "ROBO-01",
    "tipo": "Robô Industrial",
    "setor": "Célula de Manipulação",
    "status": "operando",
    "temperatura": 38.5,
    "horas_uso": 1240,
    "atualizacao": datetime.now().strftime("%H:%M:%S")
}

def on_connect(client, userdata, flags, rc):
    print("Conectado ao Broker MQTT com código:", rc)
    client.subscribe("industria/ROBO-01/#")

def on_message(client, userdata, msg):
    global equipamento_dados
    topico = msg.topic
    payload = msg.payload.decode("utf-8")
    
    try:
        if topico.endswith("/temperatura"):
            equipamento_dados["temperatura"] = float(payload)
        elif topico.endswith("/status"):
            equipamento_dados["status"] = str(payload)
        elif topico.endswith("/horas_uso"):
            equipamento_dados["horas_uso"] = int(payload)
            
        equipamento_dados["atualizacao"] = datetime.now().strftime("%H:%M:%S")
        print(f"[MQTT Update] {topico} -> {payload}")
    except Exception as e:
        print(f"Erro ao processar mensagem MQTT: {e}")

def iniciar_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    try:
        client.connect("mosquitto", 1883, 60)
        client.loop_forever()
    except Exception as e:
        print(f"Aviso: Não foi possível conectar ao broker MQTT ({e})")

threading.Thread(target=iniciar_mqtt, daemon=True).start()

@app.route('/api/equipamentos/<id_eq>', methods=['GET'])
def get_identificacao(id_eq):
    if id_eq == "ROBO-01":
        return jsonify({
            "id": equipamento_dados["id"],
            "tipo": equipamento_dados["tipo"],
            "setor": equipamento_dados["setor"],
            "status": equipamento_dados["status"]
        })
    return jsonify({"erro": "Equipamento não encontrado"}), 404

@app.route('/api/equipamentos/<id_eq>/telemetria', methods=['GET'])
def get_telemetria(id_eq):
    if id_eq == "ROBO-01":
        return jsonify({
            "temperatura": equipamento_dados["temperatura"],
            "horas_uso": equipamento_dados["horas_uso"],
            "status": equipamento_dados["status"],
            "atualizacao": equipamento_dados["atualizacao"]
        })
    return jsonify({"erro": "Equipamento não encontrado"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)