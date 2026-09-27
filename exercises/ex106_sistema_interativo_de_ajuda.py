def exibir_ajuda(comando):
    return help(comando)



print("Seja bem-vindo ao Sistema Interativo de Ajuda em Python!\nAqui você poderá consultar e aprender sobre comandos da linguagem Python.\n")
while True:
    comando_python = input("Digite o comando Python que deseja consultar ou digite 'fim' para encerrar o programa: ").strip()
    if comando_python == "fim":
        break
    else:
        exibir_ajuda(comando=comando_python)