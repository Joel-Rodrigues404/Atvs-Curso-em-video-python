pergunta = 'sS'
cont = 0
soma = 0
maior = 0
menor = 0
while pergunta in 'sS':
    num = abs(float(input(f'Digite um numero: ')))
    pergunta = str(input(f'Quer continuar [S/N]: ')).upper().strip()[0]
    soma += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    

print(f'A media e {soma/cont} numeros digitados foi {cont}')
print(f'maior {maior} menor {menor}')



