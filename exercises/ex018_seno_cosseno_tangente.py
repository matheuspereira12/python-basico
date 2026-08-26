# Calcula o seno, cosseno e tangente do ângulo informado pelo usuário.

from math import sin, cos, tan, radians

angulo = radians(float(input("Digite o ângulo em graus: ")))

seno, cosseno, tangente = sin(angulo), cos(angulo), tan(angulo)
print("O valor do seno é {:.2f}\nO valor do cosseno é {:.2f}\nO valor da tangente é {:.2f}.".format(seno, cosseno, tangente))
