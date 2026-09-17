produtos = ("Arroz", "R$ 25,90", "Feijão ", "R$ 8,50", "Leite", "R$ 5,99", "Café", "R$ 18,90", "Açúcar", "R$ 4,79")

for i in range(1, len(produtos) + 1):
    if i % 2 == 1:
        print(f"{produtos[i - 1]:-<30}", end="")
    else:
        print(f"{produtos[i - 1]:->15}")