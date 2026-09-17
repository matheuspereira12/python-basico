from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print("Os números são:")

for i in numeros:
    print(i)
    
print(f"O maior número é {max(numeros)} e o menor número é {min(numeros)}.")