# Calcula a média das idades, identifica o homem mais velho e conta as mulheres com menos de 20 anos.


soma_idades = 0
homem_mais_velho = ""
maior_idade_homem = 0
mulheres_menores_20 = 0

for i in range(1, 5):
    nome = input("Digite o nome da {}ª pessoa: ".strip().format(i))
    idade = int(input("Digite a idade da {}ª pessoa: ".format(i)))
    sexo = int(input("Digite o sexo da {}ª pessoa (1 para homem, 2 para mulher): ".format(i)))
    soma_idades += idade
    if i == 1 and sexo == 1:
        homem_mais_velho = nome
        maior_idade_homem = idade
    if idade > maior_idade_homem and sexo == 1:
            homem_mais_velho = nome
            maior_idade_homem = idade
    if sexo == 2 and idade < 20:
                mulheres_menores_20 += 1
print("A média das idades das pessoas é {}.\nO nome do homem mais velho é {}.\nA quantidade de mulheres com menos de 20 anos é {}.".format(soma_idades / 4, homem_mais_velho, mulheres_menores_20))
                