import random

l = list()
num = ['primeiro', 'segundo', 'terceiro', 'quarto']
n = 0
for x in range(4):
    aluno = input(f'{num[n]} aluno: ')
    l.append(aluno)
    n += 1
print(l)

escolhido = random.choice(l)
print(f'O aluno escolhido foi {escolhido}')
