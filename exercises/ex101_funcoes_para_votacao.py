def verifica_voto(idade):
    if idade < 16:
        return "proibido"
    elif idade <18:
        return "facultativo"
    elif idade < 70:
        return "obrigatório"
    else:
        return "facultativo"
    
idade = int(input("Digite sua idade: "))
print(f"Para você, o voto é {verifica_voto(idade=idade)}.")