valor_produto = abs(float(input("digite o valor do produto: R$")))
qnt_desconto = abs(float(input("Qual o desconto do produto: ")))
desconto = valor_produto*qnt_desconto/100
print(f'O produto que custava R${valor_produto} na promoçao de {qnt_desconto}% vai custar {valor_produto-desconto}')

