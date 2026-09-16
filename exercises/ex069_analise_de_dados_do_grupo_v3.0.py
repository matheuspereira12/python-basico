maiores_de_18 = 0
quantidade_homens = 0
mulheres_menores_de_20 = 0


while True:
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (masculino ou feminino):").strip().upper()
    if idade >= 18:
        maiores_de_18 += 1
    if "MASCULINO" in sexo:
        quantidade_homens += 1
    if idade < 20 and "FEMININO" in sexo:
        mulheres_menores_de_20 += 1                
    continuar = input("Deseja continuar? [S/N]: ").strip().upper()
    if continuar == "N":
        break
print(f"Pessoas com 18 anos ou mais: {maiores_de_18}\nHomens cadastrados: {quantidade_homens}\nMulheres com menos de 20 anos: {mulheres_menores_de_20}")