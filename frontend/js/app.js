const API_URL = "https://opulent-space-fiesta-6vg6w9rx469g346q7-5000.app.github.dev/api/equipamentos/ROBO-01";

function fecharPainel() {
    document.getElementById("info-panel").style.display = "none";
}

function exibirInfoEstatica(titulo, descricao) {
    const painel = document.getElementById("info-panel");
    const conteudo = document.getElementById("panel-content");
    
    conteudo.innerHTML = `
        <h3>${titulo}</h3>
        <p>${descricao}</p>
    `;
    painel.style.display = "block";
}

async function carregarTelemetria() {
    const painel = document.getElementById("info-panel");
    const conteudo = document.getElementById("panel-content");
    
    conteudo.innerHTML = `<h3> Monitoramento em Tempo Real</h3><p>A consultar serviço API...</p>`;
    painel.style.display = "block";

    try {
        const resposta = await fetch(`${API_URL}/telemetria`);
        if (!resposta.ok) throw new Error("Erro na resposta da API");
        
        const dados = await resposta.json();
        
        conteudo.innerHTML = `
            <h3> Monitoramento - ROBO-01</h3>
            <p><strong>Status:</strong> ${dados.status}</p>
            <p><strong>Temperatura:</strong> ${dados.temperatura} °C</p>
            <p><strong>Horas de Uso:</strong> ${dados.horas_uso} h</p>
            <p><strong>Última Atualização:</strong> ${dados.atualizacao}</p>
        `;
    } catch (erro) {
        console.error("Falha ao consultar a API:", erro);
        conteudo.innerHTML = `
            <h3 style="color: #ff4d4d;"> Erro de Ligação</h3>
            <p>Não foi possível consultar os dados do equipamento.</p>
            <p><small>Verifique a disponibilidade do serviço API no Codespaces e tente novamente.</small></p>
        `;
    }
}

// Configura os ouvintes de evento diretamente em cada elemento assim que carregados
window.addEventListener("DOMContentLoaded", () => {
    const associarClique = (id, acao) => {
        const el = document.getElementById(id);
        if (el) {
            el.addEventListener("click", acao);
            el.addEventListener("touchstart", (e) => {
                e.preventDefault();
                acao();
            });
        }
    };

    associarClique("hotspot-base", () => {
        exibirInfoEstatica("Base do Robô", "Estrutura de fixação e rotação do Eixo 1. Suporta toda a carga dinâmica do manipulador.");
    });

    associarClique("hotspot-braco", () => {
        exibirInfoEstatica("Braço Principal", "Segmento articulado responsável pela elevação e alcance (Eixos 2 e 3).");
    });

    associarClique("hotspot-punho", () => {
        exibirInfoEstatica("Punho Articulado", "Mecanismo de orientação final (Eixos 4, 5 e 6) de alta precisão.");
    });

    associarClique("hotspot-garra", () => {
        carregarTelemetria();
    });
});