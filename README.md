#  Projeto WebAR - Monitoramento de Robô Industrial

Aplicação de Realidade Aumentada baseada na Web (WebAR) integrada a um ecossistema IoT (MQTT + REST API) para monitoramento em tempo real de equipamentos industriais.

##  Arquitetura da Solução

- **Frontend (WebAR):** HTML5, CSS3, JavaScript ES6, A-Frame e MindAR.
- **Backend (API REST):** Python 3.10 com Flask e Flask-CORS.
- **Broker MQTT:** Eclipse Mosquitto.
- **Simulador Telemetria:** Python script publicando em tópicos MQTT.
- **Orquestração:** Docker & Docker Compose.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Docker e Docker Compose instalados.

### Passos para Inicialização

1. Suba os containers da aplicação:
```bash
docker compose up --build