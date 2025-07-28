// Seleciona todos os inputs de quantidade
const inputsQuantidade = document.querySelectorAll('.quantidade');

inputsQuantidade.forEach(input => {
    // Pega o container do item inteiro
    const container = input.closest('.itens');
    // Pega o elemento que mostra o preço unitário
    const valorElem = container.querySelector('.valor');

    // Extrai o texto do preço (ex: "valor: R$ 60,00")
    const valorTexto = valorElem.textContent;
    // Usa expressão regular para extrair número (com vírgula ou ponto)
    const valorLimpo = valorTexto.match(/[\d.]+/)[0];
    const valorNumerico = parseFloat(valorLimpo);

    function atualizarValor() {
        const quantidade = parseInt(input.value) || 0;
        const total = quantidade * valorNumerico;

        // Atualiza o texto do elemento `.valor` no formato moeda BR
        valorElem.textContent = `Valor: ${total.toLocaleString('pt-BR', {
            style: 'currency',
            currency: 'BRL',
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        })}`;
    }

    // Atualiza o valor quando o input mudar e na inicialização
    input.addEventListener('input', atualizarValor);
    atualizarValor();
});
