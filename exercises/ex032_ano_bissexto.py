# Verifica se o ano informado é bissexto.

from datetime import date

ano = int(input("Digite o ano que deseja analisar. Para analisar o ano atual, digite 0: "))
if ano == 0:
    
    ano = date.today().year
    
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print("\033[1;32mO ano {} é bissexto.\033[0m".format(ano))
else:
    print("\033[1;31mO ano {} não é bissexto.\033[0m".format(ano))