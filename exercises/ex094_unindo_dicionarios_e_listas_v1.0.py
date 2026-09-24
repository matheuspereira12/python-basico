pessoas = list()
media_idade = 0
mulheres = list()
pessoas_acima_media = list()



contador = 0

while True:
    pessoas.append(dict())
    pessoas[contador]["nome"] = input("Digite o nome da pessoa: ").strip().capitalize()
    while True:
        sexo = input("Digite o sexo da pessoa (M para masculino ou F para feminino): ").strip().upper()
        if sexo == "M" or sexo == "F":
            break
        print("Opção inválida! Digite apenas M para masculino ou F para feminino.\n")
    if sexo == "M":
        pessoas[contador]["sexo"] = "masculino"
    else:
        pessoas[contador]["sexo"] = "feminino"
    pessoas[contador]["idade"] = int(input("Digite a idade da pessoa: "))
    contador += 1
    while True:
        continuar = input("Deseja continuar inserindo dados? Digite S para sim ou N para não:").strip().upper()
        if continuar == "S" or continuar == "N":
            break
        print("Opção inválida! Digite apenas S para sim ou N para não.\n")
    if continuar == "N":
        break
    
    
    
    
for i in pessoas:
    media_idade += i["idade"]
    
media_idade = media_idade / len(pessoas)

for i in pessoas:
    if i["sexo"] == "feminino":
        mulheres.append(i["nome"])
        
for i in pessoas:
    if i["idade"] > media_idade:
        pessoas_acima_media.append(i["nome"])
                
mulheres = ", ".join(mulheres)
pessoas_acima_media = ", ".join(pessoas_acima_media)


print(f"Quantidade de pessoas cadastradas: {len(pessoas)}\nMédia de idade das pessoas cadastradas: {media_idade:.2f}\nMulheres cadastradas: {mulheres}\nPessoas com idade acima da média: {pessoas_acima_media}.")

