# Exibe a sequência de Fibonacci de acordo com a quantidade de termos informada pelo usuário.

quantidade_termos = int(input("Digite a quantidade de termos da sequência de Fibonacci que deseja visualizar: "))

valor_1 = 0
valor_2 = 1

contador = 0

while contador < quantidade_termos:
    print(valor_1)
    proximo_termo = valor_1 + valor_2
    valor_1 = valor_2
    valor_2 = proximo_termo
    contador += 1
    