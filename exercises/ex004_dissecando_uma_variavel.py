# Analisa o tipo e as características do conteúdo armazenado na variável.

cores = {"tipo" : "\033[36;40m", "pergunta" : "\033[33;40m", "resultado" : "\033[32;40m", "limpa" : "\033[0m"}

entrada = input("Digite qualquer coisa:\n")

print(
    "{}O tipo de dado armazenado nessa variável é{} {}{}{}.\n"
    "{}A variável contém somente espaços?{} {}{}{}\n"
    "{}A variável contém apenas caracteres numéricos?{} {}{}{}\n"
    "{}A variável contém apenas caracteres alfabéticos?{} {}{}{}\n"
    "{}A variável contém apenas caracteres alfanuméricos?{} {}{}{}\n"
    "{}A variável está em letras minúsculas?{} {}{}{}\n"
    "{}A variável está em letras maiúsculas?{} {}{}{}\n"
    "{}A variável está capitalizada?{} {}{}{}"
    .format(cores["pergunta"], cores["limpa"], cores["tipo"], type(entrada).__name__, cores["limpa"], cores["pergunta"], cores["limpa"], cores["resultado"], entrada.isspace(), cores["limpa"], cores["pergunta"], cores["limpa"], cores["resultado"], entrada.isnumeric(), cores["limpa"], cores["pergunta"], cores["limpa"], cores["resultado"], entrada.isalpha(), cores["limpa"], cores["pergunta"], cores["limpa"], cores["resultado"], entrada.isalnum(), cores["limpa"], cores["pergunta"], cores["limpa"], cores["resultado"], entrada.islower(), cores["limpa"], cores["pergunta"], cores["limpa"], cores["resultado"], entrada.isupper(), cores["limpa"], cores["pergunta"], cores["limpa"], cores["resultado"], entrada.istitle(), cores["limpa"])
    )
    
