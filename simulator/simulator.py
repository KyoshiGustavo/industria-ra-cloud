import paho.mqtt.client as mqtt
import time
import random

BROKER = "mosquitto"
PORT = 1883
TOPIC_BASE = "industria/ROBO-01"

def conectar_broker():
    client = mqtt.Client()
    while True:
        try:
            client.connect(BROKER, PORT, 60)
            print("Simulador conectado ao Broker MQTT!")
            return client
        except Exception as e:
            print(f"Aguardando broker MQTT... ({e})")
            time.sleep(2)

def rodar_simulacao():
    client = conectar_broker()
    horas_uso = 1240

    while True:
        temp = round(random.uniform(35.0, 48.0), 1)
        status = random.choice(["operando", "operando", "operando", "em manutencao"])
        horas_uso += 1

        client.publish(f"{TOPIC_BASE}/temperatura", temp)
        client.publish(f"{TOPIC_BASE}/status", status)
        client.publish(f"{TOPIC_BASE}/horas_uso", horas_uso)

        print(f"[Simulador MQTT] Temp: {temp}C | Status: {status} | Horas: {horas_uso}")
        
        time.sleep(5) 

if __name__ == "__main__":
    rodar_simulacao()