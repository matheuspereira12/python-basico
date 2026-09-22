pessoa = [[], []]

while True:
    nome = input("Digite o nome da pessoa: ").strip().capitalize()
    peso = float(input("Digite o peso da pessoa: ").replace(",", "."))
    pessoa[0].append(nome)
    pessoa[1].append(peso)
    while True:
        continuar = input("Deseja continuar cadastrando nome e peso? [S/N]: ").strip().upper()
        if continuar == "S" or continuar == "N":
            break
    if continuar == "N":
        break
    
print(f"Foram cadastradas {len(pessoa[0])} pessoas.\nO menor peso registrado foi de {min(pessoa[1])} kg.\nO maior peso registrado foi de {max(pessoa[1])} kg.")
