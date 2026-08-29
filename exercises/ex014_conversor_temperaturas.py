# Converte a temperatura de Celsius para Fahrenheit.


temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))
temperatura_fahrenheit = (temperatura_celsius * 1.8) + 32
print("A temperatura \033[1;34m{:.1f}\033[0m°C equivale a \033[1;31m{:.1f}\033[0m°F.".format(temperatura_celsius, temperatura_fahrenheit))
