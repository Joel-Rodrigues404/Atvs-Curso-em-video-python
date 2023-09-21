import math




valor_casa = abs(float(input("digite o valor da casa: ")))
salario_comprador = abs(float(input("digite qual o seu salario: ")))
anos_para_pagar = abs(int(input("em quantos anos voce vai pagar: ")))

prestacao_mensal = math.ceil((valor_casa/anos_para_pagar)/12)

if prestacao_mensal > salario_comprador:
    print(f'emprestimo NEGADO a prestaçao e maior do que voce pode pagar')
elif salario_comprador*(30/100) <= prestacao_mensal:
    print(f'A prestaçao equivale a mais de 30% de seu salario')
else:
    print(f'Emprestimo permitido')

