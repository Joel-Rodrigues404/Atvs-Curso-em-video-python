from datetime import date

ano_atual = date.today().year

maior = 0
menor = 0
for x in range(7):
    ano_nascimento = abs(int(input(f'em que ano a {x}° pessoa nasceu: ')))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maior += 1
    elif idade < 18:
        menor += 1

print(f'Ao todo tivemos {maior} maiores de idade')
print(f'Ao todo tivemos {menor} menores de idade')

