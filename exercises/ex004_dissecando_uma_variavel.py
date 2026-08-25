# Analisa o tipo e as características do conteúdo armazenado na variável.

entrada = input("Digite qualquer coisa:\n")
print("O tipo de dado armazenado nessa variável é {}.\nA variável contém somente espaços? {}\nA variável contém apenas caracteres numéricos? {}\nA variável contém apenas caracteres alfabéticos? {}\nA variável contém apenas caracteres alfanuméricos? {}\nA variável está em letras minúsculas? {}\nA variável está em letras maiúsculas? {}\nA variável está capitalizada? {}\n".format(type(entrada).__name__, entrada.isspace(), entrada.isnumeric(), entrada.isalpha(), entrada.isalnum(), entrada.islower(), entrada.isupper(), entrada.istitle()))
