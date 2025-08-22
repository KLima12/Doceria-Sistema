function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

const csrftoken = getCookie('csrftoken');

document.querySelectorAll('.products').forEach(product => {
  const input  = product.querySelector('.amountProduct');
  const p = product.querySelector('.value');
  const addBtn = product.querySelector('.addProduct');
  const favBtn = product.querySelector('.favBtn');

  // ADICIONAR AO CARRINHO
  addBtn.addEventListener('click', async (e) => {
    e.preventDefault();
    cart = document.querySelector('.cart')
    if (cart) { 
      cart.style.color = 'green';
    }
    const idProduct = input.dataset.id;
    const amount = parseInt(input.value) || 1;

    try {
      const response = await fetch(`/add-to-cart/${idProduct}/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ amount })
      });

      if (!response.ok) {
        const txt = await response.text();
        throw new Error(`HTTP ${response.status}: ${txt}`);
      }

      const data = await response.json();
      console.log('Resposta JSON:', data);

      if (data.status === 'ok') {
        alert('✅ Produto adicionado ao carrinho');
      } else {
        alert('⚠️ Erro: ' + (data.mensagem || 'Falha ao adicionar'));
      }
    } catch (err) {
      console.error('Erro na requisição:', err);
      alert('Erro na conexão: ' + err.message);
    }
  });

  windows.addEventListener('load', async () => { 
    const cartIcon = document.querySelector('.cart');
    try {
      const response = await fetch('/cart-status/')
      const data = await response.json();

      if (data.hasProducts) { 
        cartIcon.classList.add('active_green')
      } else { 
        cartIcon.classList.remove('active_green')
      }
    } catch(err) { 
      console.error('Erro ao verificar o carrinho: ', err)
    }
  })

  // ATUALIZA TOTAL (preço x quantidade)
  const priceText    = p.innerText;
  const cleanPrice   = priceText.match(/[\d.,]+/)[0].replace(',', '.');
  const basePrice    = parseFloat(cleanPrice);

  function updateValue() {
    const amount = parseInt(input.value) || 0;
    const total = amount * basePrice;
    p.textContent = `Valor: ${total.toLocaleString('pt-BR', {
      style: 'currency',
      currency: 'BRL',
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    })}`;
  }

  input.addEventListener('input', updateValue);
  updateValue();

  // FAVORITO
  favBtn.addEventListener('click', async () => {
    const productId  = favBtn.dataset.id;
    const isFavorite = !favBtn.classList.contains('active');

    try {
      const response = await fetch(`/favorited-product/${productId}/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ favorite: isFavorite })
      });

      if (!response.ok) {
        const txt = await response.text();
        throw new Error(`HTTP ${response.status}: ${txt}`);
      }

      const data = await response.json();
      if (data.status === 'ok') {
        favBtn.classList.toggle('active', isFavorite);
      } else {
        alert('Erro: ' + (data.mensagem || 'Falha ao favoritar'));
      }
    } catch (err) {
      console.error(err);
      alert('Erro na conexão: ' + err.message);
    }
  });
});


