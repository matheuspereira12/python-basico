# Calcula o seno, cosseno e tangente do ângulo informado pelo usuário.

from math import sin, cos, tan, radians

angulo = radians(float(input("Digite o ângulo em graus: ")))

seno, cosseno, tangente = sin(angulo), cos(angulo), tan(angulo)
print("O valor do seno é \033[1;31m{:.2f}\033[0m\nO valor do cosseno é \033[1;34m{:.2f}\033[0m\nO valor da tangente é \033[1;35m{:.2f}\033[0m.".format(seno, cosseno, tangente))
