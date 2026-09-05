# Solicita o nome e o sexo do usuário, validando a opção informada e exibindo uma mensagem personalizada.
sexo_valido = False

nome = input("Digite seu nome: ").strip().capitalize()

while not sexo_valido:
    sexo = input("Digite o sexo (M/F): ").strip().upper()
    if sexo == "M" or sexo == "F":
        sexo_valido = True
        
if sexo == "M":
    print("Olá, {}! Seu sexo é masculino.".format(nome))
else:
    print("Olá, {}! Seu sexo é feminino.".format(nome))