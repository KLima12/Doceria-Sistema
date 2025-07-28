const preco = document.getElementById('preco').innerText;
const precoValor = preco.replace(/[^\d,\.]/g, ''); // remove "Preço:" e mantém números

input = document.getElementById('quantidadeProduto');
const p = document.getElementById('valor');

input.addEventListener('input', () => {
    const quantiade = parseFloat(input.value) || 0;
    const total = quantiade * preco
    p.textContent = `Valor: ${total.toLocaleString('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    })}`;
});
p.textContent = `valor: ${valor_total}`;

const input = document.getElementById('quantidadeProduto');
