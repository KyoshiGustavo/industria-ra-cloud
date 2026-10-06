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

A aplicação conta com renderização de elementos 3D rastreados por visão computacional (MindAR). Devido às variações de suporte ao evento de raycasting WebGL em ecossistemas móveis (especialmente em navegação tátil mobile), foi implementada uma interface Overlay 2D responsiva no ecrã. Esta abordagem garante acesso universal às informações estáticas dos eixos e aos dados de telemetria em tempo real via API REST, cumprindo todos os requisitos de usabilidade do projeto.