primeiro_termo = int(input(f'Digite o primeiro termo: '))
razao = int(input(f'Digite a razao: '))
a = primeiro_termo
cont = 1
while cont <= 10:
    print(f'{a} -> ', end='')
    a += razao
    cont += 1

print(f'Fim')