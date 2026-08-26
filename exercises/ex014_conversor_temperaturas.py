# Converte a temperatura de Celsius para Fahrenheit.


temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))
temperatura_fahrenheit = (temperatura_celsius * 1.8) + 32
print("A temperatura {:.1f}°C equivale a {:.1f}°F.".format(temperatura_celsius, temperatura_fahrenheit))
