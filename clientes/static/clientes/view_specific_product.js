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