function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Verifica se o cookie começa com o nome esperado
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

const precoTexto = document.getElementById('preco').innerText;

    // Extrai apenas o número decimal com ponto: ex: "60.00"
    const precoLimpo = precoTexto.match(/[\d.]+/)[0];
    const precoNumerico = parseFloat(precoLimpo); // agora pega corretamente ex: 180.00

    const input = document.getElementById('quantidadeProduto');
    const p = document.getElementById('valor');

    function atualizarValor() {
        const quantidade = parseInt(input.value) || 0;
        const total = quantidade * precoNumerico;

        // Formata certinho no estilo BR
        p.textContent = `Valor: ${total.toLocaleString('pt-BR', {
            style: 'currency',
            currency: 'BRL',
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        })}`;
    }

    input.addEventListener('input', atualizarValor);
    atualizarValor();

const favBtn = document.getElementById('favBtn');

favBtn.addEventListener('click', async() => { 
    favBtn.classList.toggle('active');

    const produtoId = favBtn.dataset.id;
    console.log('produtoId:', produtoId);
    const isFavorito = favBtn.classList.contains('active')

    try { 
        const response = await fetch(`/favoritar-produto/${produtoId}/`, { 
            method:'POST',
            headers: { 
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                favorito: isFavorito
            })
        });
        const data = await response.json()

        if(data.status !== 'ok') { 
            // Caso dê erro, desfaz a classe (volta o botão)
            favBtn.classList.toggle('active')
            alert('Erro ao favoritar o produto')
        }

    } catch (error) { 
        favBtn.classList.toggle('active')
        alert('Erro na conexão')
    }
});


