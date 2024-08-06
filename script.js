var btnEntrar = document.querySelector("#entrar")
var btnSair = document.querySelector("#sair")

var body = document.querySelector("body");

btnEntrar.addEventListener("click", function () {
    body.className = "entrar-js"
});

btnSair.addEventListener("click", function () {
    body.className = "sair-js"
});


function mostrarSenhaPrimary() {
    var inputPassPrimary = document.getElementById('msgCriptografada-primary')
    var btnShowPassPrimary = document.getElementById('btn-msgCriptografada-primary')

    if (inputPassPrimary.type === 'password') {
        inputPassPrimary.setAttribute('type', 'text')
        btnShowPassPrimary.classList.replace('bi-eye-fill', 'bi-eye-slash-fill')
    } else if (inputPassPrimary.type === 'text') {
        inputPassPrimary.setAttribute('type', 'password')
        btnShowPassPrimary.classList.replace('bi-eye-slash-fill', 'bi-eye-fill')
    }
}

function mostrarSenhaSecond() {
    var inputPassSecond = document.getElementById('msgDescriptografada-second')
    var btnShowPassSecond = document.getElementById('btn-msgDescriptografada-second')

    if (inputPassSecond.type === 'password') {
        inputPassSecond.setAttribute('type', 'text')
        btnShowPassSecond.classList.replace('bi-eye-fill', 'bi-eye-slash-fill')
    } else if (inputPassSecond.type === 'text') {
        inputPassSecond.setAttribute('type', 'password')
        btnShowPassSecond.classList.replace('bi-eye-slash-fill', 'bi-eye-fill')
    }
}

function btnInfoEnterEsquerda() {
    var btnInformacoes = document.getElementById('btnInformacoesEsquerda')
    var btnInfo = document.getElementById('informacoesEsquerdaFront')

    if (btnInfo.type === 'password') {
        btnInfo.setAttribute('type', 'text')
        btnInformacoes.setAttribute('src', 'imagens/info-circle-fill.png')

    } else if (btnInfo.type === 'text') {
        btnInfo.setAttribute('type', 'password')
        btnInformacoes.setAttribute('src', 'imagens/info-circle.png')
    }
}

function btnInfoOutEsquerda() {
    var btnInformacoes = document.getElementById('btnInformacoesEsquerda')
    var btnInfo = document.getElementById('informacoesEsquerdaFront')

    if (btnInfo.type === 'password') {
        btnInfo.setAttribute('type', 'text')
        btnInformacoes.setAttribute('src', 'imagens/info-circle-fill.png')

    } else if (btnInfo.type === 'text') {
        btnInfo.setAttribute('type', 'password')
        btnInformacoes.setAttribute('src', 'imagens/info-circle.png')
    }
}

function btnInfoEnterDireita() {
    var btnInformacoes = document.getElementById('btnInformacoesDireita')
    var btnInfo = document.getElementById('informacoesDireita')

    if (btnInfo.type === 'password') {
        btnInfo.setAttribute('type', 'text')
        btnInformacoes.setAttribute('src', 'imagens/info-circle-fill.png')
    } else if (btnInfo.type === 'text') {
        btnInfo.setAttribute('type', 'password')
        btnInformacoes.setAttribute('src', 'imagens/info-circle.png')
    }
}

function btnInfoOutDireita() {
    var btnInformacoes = document.getElementById('btnInformacoesDireita')
    var btnInfo = document.getElementById('informacoesDireita')

    if (btnInfo.type === 'password') {
        btnInfo.setAttribute('type', 'text')
        btnInformacoes.setAttribute('src', 'imagens/info-circle-fill.png')

    } else if (btnInfo.type === 'text') {
        btnInfo.setAttribute('type', 'password')
        btnInformacoes.setAttribute('src', 'imagens/info-circle.png')
    }
}

function abrirDireita() {
    var infoimage = document.getElementById('popup')
    infoimage.style.display = 'block';
    infoimage.style.animation = 'slideInfoDireita 1.8s'
    var btninfo = document.getElementById('myRect')
    btninfo.setAttribute('fill', 'black')
    var transicaoTexto = document.getElementById('infoTextoEsquerda')
    transicaoTexto.style.animation = 'transicaoTextoEsquerda 1.8s'
}

function abrirEsquerda() {
    var infoimage = document.getElementById('popup')
    infoimage.style.display = 'block';
    infoimage.style.animation = 'slideInfoEsquerda 1.8s'
    var btninfo = document.getElementById('myRect')
    btninfo.setAttribute('fill', 'black')
    var btnInfoFront = document.getElementById('informacoesEsquerdaFront')
    btnInfoFront.style.visibility = 'hidden'
    var transicaoTexto = document.getElementById('infoTextoEsquerda')
    transicaoTexto.style.animation = 'transicaoTextoDireita 1.8s'
}

function fecharDireita() {
    var infoimage = document.getElementById('popup')
    infoimage.style.display = 'none';
    infoimage.style.animation = 'slideInfoDireita 1s'
    var btninfo = document.getElementById('myRect')
    btninfo.setAttribute('fill', 'white')
}

function toggleVisibility(elementosASeremExibidos, elementosASeremOcultados) {
    elementosASeremExibidos.forEach(function(id) {
        var elemento = document.getElementById(id);
        if (elemento) {
            elemento.style.visibility = 'visible';
        }
    });
    elementosASeremOcultados.forEach(function(id) {
        var elemento = document.getElementById(id);
        if (elemento) {
            elemento.style.visibility = 'hidden';
        }
    });
}

function proximaPagina(paginaAtual, paginaSeguinte) {
    var elementosExibir = ['conteudoInfo' + paginaSeguinte, 'informacoesEsquerdaBackVoltarPaginaAnterior' + paginaSeguinte, 'botaoVoltarPaginaAnterior' + paginaSeguinte, 'topicosInfo' + paginaSeguinte, 'topicoImagem' + 'pagina' + paginaSeguinte, 'mudarCorBotaoPaginaProxima1' + paginaSeguinte];
    var elementosOcultar = ['conteudoInfo' + paginaAtual, 'informacoesEsquerdaBackVoltarPaginaAnterior' + paginaAtual, 'botaoVoltarPaginaAnterior' + paginaAtual, 'informacoesEsquerdaBackVoltar' + paginaAtual, 'botaoVoltar' + paginaAtual, 'topicosInfo' + paginaAtual, 'topicoImagem' + paginaAtual, 'pagina' + paginaAtual, 'mudarCorBotaoPaginaProxima' + paginaAtual];
    toggleVisibility(elementosExibir, elementosOcultar);
}

function paginaAnterior(paginaAtual, paginaAnterior) {
    var elementosExibir = ['conteudoInfo' + paginaAnterior, 'informacoesEsquerdaBackVoltarPaginaAnterior' + paginaAnterior, 'botaoVoltarPaginaAnterior' + paginaAnterior, 'topicosInfo' + paginaAnterior, 'topicoImagem' + 'pagina' + paginaAnterior, 'mudarCorBotaoPaginaProxima1' + paginaAnterior];
    var elementosOcultar = ['conteudoInfo' + paginaAtual, 'informacoesEsquerdaBackVoltarPaginaAnterior' + paginaAtual, 'botaoVoltarPaginaAnterior' + paginaAtual, 'informacoesEsquerdaBackVoltar' + paginaAtual, 'botaoVoltar' + paginaAtual, 'topicosInfo' + paginaAtual, 'topicoImagem' + paginaAtual, 'pagina' + paginaAtual, 'mudarCorBotaoPaginaProxima' + paginaAtual];
    toggleVisibility(elementosExibir, elementosOcultar);
}

//Função para mudar de cor o botão Anterior
function mudarCorBotaoAnterior(idBotao, idSvg) {
    var btnAnterior = document.getElementById(idBotao);
    var btnAnteriorSvg = document.getElementById(idSvg);

    if (btnAnterior.type === 'password') {
        btnAnterior.setAttribute('type', 'text');
        btnAnteriorSvg.setAttribute('fill','black')
    } else if (btnAnterior.type === 'text') {
        btnAnterior.setAttribute('type', 'password');
        btnAnteriorSvg.setAttribute('fill','white')
    }
}


//Função para mudar de cor o botão Próximo
function mudarCorBotaoProxima(idBotao, idSvg) {
    var btnProximo = document.getElementById(idBotao);
    var btnProximoSvg = document.getElementById(idSvg);

    if (btnProximo.type === 'password') {
        btnProximo.setAttribute('type', 'text');
        btnProximoSvg.setAttribute('fill','black')
    } else if (btnProximo.type === 'text') {
        btnProximo.setAttribute('type', 'password');
        btnProximoSvg.setAttribute('fill','white')
    }
}