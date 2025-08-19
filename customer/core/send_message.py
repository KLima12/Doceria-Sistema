from urllib.parse import quote


def encode_for_whatsapp(text):
    return quote(str(text))


def calculate_total(products):
    sum = 0
    for price, amount in products:
        value = price * amount
        sum += value

    return sum


def generate_whatsapp_message(product, sum):
    """
    Produtos vai vir a lista de tuplas (produtos, quantidade)
    soma: valor total do pedido
    """

    message_lines = ["Olá, estou interessado(a) nos seguintes produtos: "]
    for name, amount in product:
        print(f"Nome: {name}")
        print(f"A quantidade: {amount}")
        name_cod = encode_for_whatsapp(name)
        qtd_cod = encode_for_whatsapp(amount)
        message_lines.append(f"{name_cod} X Quantidade: {qtd_cod}")

    formatted_value = f"{sum:.2f}".replace(".", ",")
    value_cod = encode_for_whatsapp(formatted_value)

    message_lines.append(f"Valor total: R$ {value_cod}")

    message_text = "%0A".join(message_lines)
    whatsapp_url = f"https://wa.me/5581979095239?text={message_text}"
    return whatsapp_url
