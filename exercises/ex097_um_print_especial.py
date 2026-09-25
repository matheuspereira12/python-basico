def escreva(texto):
    print(len(texto) * "-")
    print(f"{texto}")
    print(len(texto) * "-")
    
texto = input("Digite um texto:").strip()
escreva(texto=texto)