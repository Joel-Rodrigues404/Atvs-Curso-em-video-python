termos = abs(int(input(f'Quantos termos voce quer mostrar: ')))



cont = 3
num1 = 0
num2 = 1
print(f'{num1} > {num2}',end=' > ')
while cont <= termos:
    num3 = num1 + num2
    print(f'{num3}', end=' > ')
    num1 = num2
    num2 = num3
    cont += 1


print(f'Fim')
