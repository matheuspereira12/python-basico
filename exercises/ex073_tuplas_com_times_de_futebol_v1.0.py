times_brasileirao = ("Athletico-PR", "Flamengo", "Grêmio", "Santos", "Botafogo", "Fluminense", "Bahia", "Palmeiras", "Coritiba", "Cruzeiro", "Vitória", "São Paulo", "Internacional", "Remo", "Bragantino", "Atlético-MG", "Vasco", "Mirassol", "Chapecoense", "Ceará")


print("Os 5 primeiros colocados são:")

for i in times_brasileirao[0:5]:
    print(i)
    
print("Os últimos 4 colocados são:")
for i in times_brasileirao[16:]:
    print(i)
    
print("Os times em ordem alfabética são:")
for i in sorted(times_brasileirao):
    print(i)
    
print(f"A Chapecoense está na {times_brasileirao.index('Chapecoense') + 1}ª posição.")