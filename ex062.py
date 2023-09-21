primeiro_termo = int(input(f'Digite o primeiro termo: '))
razao = int(input(f'Digite a razão: '))


soma = primeiro_termo
cont = 1
total = 10
termos_a_mais = 10
while termos_a_mais != 0:
    while cont <= total:
        print(f'{soma} -> ', end='')
        soma += razao
        cont += 1
    print(f'Pausa')
    termos_a_mais = abs(int(input(f'Quantos termos a mais voce deseja: ')))
    total += termos_a_mais
