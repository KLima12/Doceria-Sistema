from clientes.models import *
from urllib.parse import quote


def codificar_para_whatsapp(texto):
    return quote(str(texto))


def calcular_total(produtos):
    soma = 0
    for preco, quantidade in produtos:
        valor = preco * quantidade
        soma += valor

    return soma


def gerar_mensagem_whatsapp(produtos, soma):
    """
    Produtos vai vir a lista de tuplas (produtos, quantidade)
    soma: valor total do pedido
    """

    message_lines = ["Olá, estou interessado(a) nos seguintes produtos: "]
    for nome, quantidade in produtos:
        nome_cod = codificar_para_whatsapp(nome)
        qtd_cod = codificar_para_whatsapp(quantidade)
        message_lines.append(f"{nome_cod} X Quantidade: {qtd_cod}")

    valor_formatado = f"{soma:.2f}".replace(".", ",")
    valor_cod = codificar_para_whatsapp(valor_formatado)

    message_lines.append(f"Valor total: R$ {valor_cod}")

    message_text = "%0A".join(message_lines)
    whatsapp_url = f"https://wa.me/5581979095239?text={message_text}"
    return whatsapp_url
