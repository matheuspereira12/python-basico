parenteses = []

expressao = input("Digite uma expressão matemática com parênteses: ")


for i in expressao:
    if i == "(":
        parenteses.append("(")
    elif i == ")":
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(")")
            break
        
if len(parenteses) == 0:
    print("A expressão é válida.")
else:
    print("A expressão não é válida.")