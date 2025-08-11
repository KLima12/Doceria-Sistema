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

document.querySelectorAll('.btn-delete').forEach(botao => { 
    botao.addEventListener('click', async function(event) { 
        event.preventDefault();
        const favoriteId = this.dataset.favoriteId;
        console.log(favoriteId);

        const response = await fetch(`/delete-favorite/${favoriteId}/`, { 
            method: 'POST',
            headers: { 
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
        });

        if (response.ok) { 
            const elemento = document.getElementById(`favorito-${favoriteId}`);
            if (elemento) elemento.remove(); // Remove os itens na tela
        } else {
            alert("Erro ao tentar excluir o favorito.");
        }
    });
});
