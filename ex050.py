soma_num = 0
cont = 0
for x in range(1,7):
    num = abs(int(input(f'digite o {x}° numero: ')))
    if num % 2 == 0:
        soma_num += num
        cont += 1
print(f'Voce informou {cont} numeros pares e soma desses numeros foi {soma_num}')