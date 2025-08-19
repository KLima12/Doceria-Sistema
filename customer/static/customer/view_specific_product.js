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

const priceText = document.getElementById('price').innerText;
// Aceita número com vírgula ou ponto
const cleanPrice = priceText.match(/[\d.,]+/)[0].replace(',', '.');
const numericalPrice = parseFloat(cleanPrice);
const input = document.getElementById('amountProduct');
const p = document.getElementById("value"); 
function updateValue() {
    const amount = parseInt(input.value) || 0;
    const total = amount * numericalPrice;
    console.log(total)
    
    p.textContent = `Valor: ${total.toLocaleString('pt-BR', {
        style: 'currency',
        currency: 'BRL',
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    })}`;
}

    input.addEventListener('input', updateValue);
    updateValue();

const favBtn = document.getElementById('favBtn');

favBtn.addEventListener('click', async() => { 
    const productId = favBtn.dataset.id; // Pegando id lá do produto no html
    const isFavorite = !favBtn.classList.contains('active'); // define o novo estado

    try { 
        const response = await fetch(`/favorited-product/${productId}/`, { 
            method:'POST',
            headers: { 
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ favorite: isFavorite })
        });

        const data = await response.json();

        if(data.status === 'ok') { 
            if (isFavorite) {
                favBtn.classList.add('active');
            } else {
                favBtn.classList.remove('active');
            }
        } else { 
            alert('Erro ao favoritar o produto');
        }

    } catch (error) { 
        alert('Erro na conexão');
    }
});


