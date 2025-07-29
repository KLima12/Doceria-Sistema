const inputsQuantidade = document.querySelectorAll('.quantidade');

function atualizarSubtotal() {
    let total = 0;
    let soma = 0
    document.querySelectorAll('.itens').forEach(container => {
        const input = container.querySelector('.quantidade');
        console.log(input)
        const valorElem = container.querySelector('.valor');
        // Extraindo o preço unitário do texto inicial (ex: "valor: R$ 60,00")
        const valorTexto = valorElem.textContent;
        const valorLimpo = valorTexto.match(/[\d,.]+/)[0].replace(',', '.');
        const valorNumerico = parseFloat(valorLimpo);
        total += valorNumerico;
    });
    const subtotal = document.querySelector(".subtotal");
    subtotal.textContent = `Total: ${total.toLocaleString('pt-BR', {
        style: 'currency',
        currency: 'BRL',
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    })}`;
}

inputsQuantidade.forEach(input => {
    const container = input.closest('.itens');
    const valorElem = container.querySelector('.valor');
    // Extrai o preço unitário do texto inicial (ex: "valor: R$ 60,00")
    const valorTexto = valorElem.textContent;
    const valorLimpo = valorTexto.match(/[\d,.]+/)[0].replace(',', '.');
    const valorNumerico = parseFloat(valorLimpo);

    function atualizarValor() {
        const quantidade = parseInt(input.value) || 0;
        const total = quantidade * valorNumerico;
        valorElem.textContent = `Valor: ${total.toLocaleString('pt-BR', {
            style: 'currency',
            currency: 'BRL',
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        })}`;
        atualizarSubtotal(); // Atualiza o subtotal após mudar a quantidade
    }

    input.addEventListener('input', atualizarValor);
    atualizarValor(); // Inicializa o valor do item
});

// Inicializa o subtotal na carga da página
atualizarSubtotal();