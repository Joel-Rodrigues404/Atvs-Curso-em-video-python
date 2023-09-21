
num = abs(int(input(f'Quer ver a tabuada de qual valor?: ')))


cont = 1

while cont <= 10:
    print(f'{num} x {cont} = {num*cont}')
    cont += 1
    if cont == 11:
        cont=0
        num = abs(int(input(f'Quer ver a tabuada de qual valor?: ')))
        cont += 1
print(f'{cont}')
    