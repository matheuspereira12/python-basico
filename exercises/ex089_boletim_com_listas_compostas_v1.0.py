aluno = []
contador = 0

while True:
    aluno.append([])
    nome = input("Digite seu nome: ").strip().capitalize()
    nota1 = float(input("Digite a primeira nota: ").replace(",", "."))
    nota2 = float(input("Digite a segunda nota: ").replace(",", "."))
    aluno[contador].append(nome)
    aluno[contador].append(nota1)
    aluno[contador].append(nota2)
    contador += 1
    while True:
        continuar = input("Quer continuar? [S/N]:").strip().upper()
        if continuar == "S" or continuar == "N":
            break
    if continuar == "N":
        break
    
    
for i in aluno:
    media = (i[1] + i[2]) / 2
    print(f"A média do aluno(a) {i[0]} foi {media:.2f}.")
    while True:
        ver_notas = input("Quer ver as notas individualmente? [S/N]: ").strip().upper()
        if ver_notas == "S" or ver_notas == "N":
            break
    if ver_notas == "S":
        print(f"A primeira nota do aluno(a) {i[0]} foi {i[1]:.2f}.\nA segunda nota do aluno(a) foi {i[2]:.2f}.\n")