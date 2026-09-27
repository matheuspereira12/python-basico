def notas(*valores, situacao=True):
    if situacao:
        situacao_aluno = None
        if sum(valores) / len(valores) < 5:
            situacao_aluno = "REPROVADO"
        elif sum(valores) / len(valores) < 7:
            situacao_aluno = "RECUPERAÇÃO"
        else:
            situacao_aluno = "APROVADO"
        return {"total_notas": len(valores), "menor_nota": min(valores), "maior_nota": max(valores), "media_notas": sum(valores) / len(valores), "status": situacao_aluno}
    else:
        return {"total_notas": len(valores), "menor_nota": min(valores), "maior_nota": max(valores), "media_notas": sum(valores) / len(valores)}
    
    
lista_notas = list()
while True:
    nota = float(input("Digite a média do aluno ou 999 para encerrar: ").replace(",", "."))
    if nota== 999:
        break
    else:
        lista_notas.append(nota)
        
while True:
    consultar_situação = input("Deseja consultar a situação do aluno? Digite 'S' para sim ou 'N' para não: ").strip().upper()
    if consultar_situação == "S" or consultar_situação == "N":
        break
if consultar_situação == "S":
    resultado = notas(*lista_notas)
    print(f"Foram informadas {resultado['total_notas']} notas.\nA menor nota foi {resultado['menor_nota']}.\nA maior nota foi {resultado['maior_nota']}.\nA média foi {resultado['media_notas']:.2f}.\nA situação do aluno é {resultado['status']}.")
else:
    resultado = notas(*lista_notas, situacao=False)
    print(f"Foram informadas {resultado['total_notas']} notas.\nA menor nota foi {resultado['menor_nota']}.\nA maior nota foi {resultado['maior_nota']}.\nA média foi {resultado['media_notas']:.2f}.")
    