# Solicita os dados do financiamento e verifica se a parcela não ultrapassa 30% do salário.

print("Bem-vindo ao Simulador de Financiamento Imobiliário!\n\nInforme os dados solicitados para calcular as condições do financiamento.\n")

valor_imovel = float(input("Qual o valor do imóvel? R$ "))
salario_mensal = float(input("Informe seu salário mensal: R$ "))
prazo_anos = int(input("Quantos anos deseja pagar o financiamento? "))

if (valor_imovel / (prazo_anos * 12)) <= (salario_mensal * 0.3):
    print("Seu financiamento foi aprovado!\n\nO valor das parcelas será de R$ {:.2f}, durante o prazo escolhido.\n\nObrigado por utilizar o Simulador de Financiamento Imobiliário!".format(valor_imovel / (prazo_anos * 12)))
else:
    print("Financiamento não aprovado.\n\nO valor da parcela ultrapassa o limite de 30% do seu salário mensal.\n\nTente aumentar o prazo do financiamento ou reduzir o valor do imóvel.")
    