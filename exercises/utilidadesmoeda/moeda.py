def aumentar(numero, exibir_formatado=False):
    if exibir_formatado:
        return f"O valor é de R$ {numero * 1.1:.2f}."
    else:
        return f"O valor é {numero * 1.1}."

def diminuir(numero, exibir_formatado=False):
    if exibir_formatado:
        return f"O valor é de R$ {numero * 0.9:.2f}."
    else:
        return f"O valor é {numero * 0.9}."


def dobro(numero, exibir_formatado=False):
    if exibir_formatado:
        return f"O valor é de R$ {numero * 2:.2f}."
    else:
        return f"O valor é {numero * 2}."


def metade(numero, exibir_formatado=False):
    if exibir_formatado:
        return f"O valor é de R$ {numero / 2:.2f}."
    else:
        return f"O valor é {numero / 2}."

