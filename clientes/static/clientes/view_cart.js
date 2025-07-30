
const form = document.querySelector('form');

function atualizarSubtotal() {
    let total = 0;
    const inputHidden = document.getElementById("inputSubtotal");

    document.querySelectorAll('.itens').forEach(container => {
        const input = container.querySelector('.quantidade');
        const valorElem = container.querySelector('.valor');
        const precoUnitarioTexto = valorElem.getAttribute('data-preco');
        const precoUnitario = parseFloat(precoUnitarioTexto);
        const quantidade = parseInt(input.value) || 0;
        
        console.log('precoUnitarioTexto:', precoUnitarioTexto);
        console.log('precoUnitario:', precoUnitario);
        console.log('quantidade:', quantidade);
        
        const subtotalProduto = precoUnitario * quantidade;
        console.log('subtotalProduto:', subtotalProduto);
        total += subtotalProduto;

        valorElem.textContent = `Valor: ${subtotalProduto.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL', minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
    });

    document.querySelector(".subtotal").textContent = `Total: ${total.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}`;
    inputHidden.value = total.toFixed(2);
    console.log('inputHidden.value:', inputHidden.value);
}

// Atualiza subtotal quando a página carrega
atualizarSubtotal();


// Garante que o subtotal seja atualizado antes de enviar
form.addEventListener('submit', function (event) {
    event.preventDefault();
    atualizarSubtotal();
    console.log('inputSubtotal antes do submit:', inputHidden.value);
    form.submit();
});

const inputsQuantidade = document.querySelectorAll('.quantidade')

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
    atualizarSubtotal(); // Inicializa o valor do item
});
