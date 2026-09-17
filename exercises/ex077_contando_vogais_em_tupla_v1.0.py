palavras = ("casa", "carro", "mesa", "livro", "bola", "gato", "janela", "escola", "banana", "sapato")
for i in palavras:
    print(f"Na palavra {i} temos:", end="")
    for letra in i:
        if letra.lower() in "aeiou":
            print(letra, end="")
    print("")