print(f'digite um numero para:')
num1 = abs(int(input(f'calcular o fatorial: ')))

num2 = num1
f = 1
print(f'Calculando {num1}! ...')
while num2 > 0:
    print(f'{num2}', end='')
    print(f' x 'if num2 > 1 else (f' = '), end='')
    f = f * num2
    num2 -= 1

print(f'{f}')