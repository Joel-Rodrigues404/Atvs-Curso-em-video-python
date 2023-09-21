print(f'=-=-'*17,end=' ')
print(f'Loja JOEL',end=' ')
print(f'=-=-'*17)

valor_compras = abs(float(input("digite o valor das compras: ")))
escolha = abs(int(input("""
Formas de Pagamento
[1] a vista dinheiro/cheque
[2] a vista cartao
[3] 2x no cartao
[4] 3x ou mais no cartao
Qual e a opçao: """)))

if escolha == 1:
    valor = valor_compras - valor_compras*(10/100)
    print(f'pagando a vista voce tem 10% de deconto assim o valor fica {valor}R$')

elif escolha == 2:
    valor = valor_compras - valor_compras*(5/100)
    print(f'pagando a vista com cartao voce tem 5% de deconto assim o valor fica {valor}R$')

elif escolha == 3:
    valor = valor_compras/2
    print(f'pagando parcelado em 2x no cartao cada parcela deve ficar de {valor}R$')
elif escolha == 4:
    parcela = abs(int(input("em quantas parcelas voce vai pagar: ")))
    valor = valor_compras + valor_compras*(20/100)
    print(f'pagando parcelado em {parcela}x no cartao cada parcela deve ficar de {valor/parcela}R$')
else:
    print(f'Voce digitou algo errado na escolha da forma de pagamento')
