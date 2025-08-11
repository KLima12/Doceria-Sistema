
const form = document.querySelector('form');

function atualizarSubtotal() {
    let total = 0;
    const inputHidden = document.getElementById("inputSubtotal");

    document.querySelectorAll('.itens').forEach(container => {
        const input = container.querySelector('.amount');
        const valueElem = container.querySelector('.value');
        const unitaryPriceText = valueElem.getAttribute('data-price');
        const unitprice = parseFloat(unitaryPriceText);
        const amount = parseInt(input.value) || 0;
        
        console.log('precoUnitarioTexto:', unitaryPriceText);
        console.log('precoUnitario:', unitprice);
        console.log('quantidade:', amount);
        
        const subtotalProduto = unitprice * amount;
        console.log('subtotalProduto:', subtotalProduto);
        total += subtotalProduto;

        valueElem.textContent = `Valor: ${subtotalProduto.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL', minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
    });

    document.querySelector(".subtotal").textContent = `Total: ${total.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}`;
    inputHidden.value = total.toFixed(2);
    console.log('inputHidden.value:', inputHidden.value);
}

// Atualiza subtotal quando a página carrega
updateSubtotal();


// Garante que o subtotal seja atualizado antes de enviar
form.addEventListener('submit', function (event) {
    event.preventDefault();
    updateSubtotal();
    console.log('inputSubtotal antes do submit:', inputHidden.value);
    form.submit();
});

const inputsAmount = document.querySelectorAll('.amount')

inputsAmount.forEach(input => {
    const container = input.closest('.itens');
    const valueElem = container.querySelector('.valor');
    // Extrai o preço unitário do texto inicial (ex: "valor: R$ 60,00")
    const textValue = valueElem.textContent;
    const cleanValue = textValue.match(/[\d,.]+/)[0].replace(',', '.');
    const numericalValue = parseFloat(cleanValue);

    function atualizarValor() {
        const amount = parseInt(input.value) || 0;
        const total = amount * numericalValue;
        valorElem.textContent = `Valor: ${total.toLocaleString('pt-BR', {
            style: 'currency',
            currency: 'BRL',
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        })}`;
        updateSubtotal(); // Atualiza o subtotal após mudar a quantidade
    }

    input.addEventListener('input', updateValor);
    updateSubtotal(); // Inicializa o valor do item
});


