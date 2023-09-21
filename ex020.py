import random

l = list()
posicao = ['primeiro','segundo','terceiro','quarto']
n = 0
for x in range(4):
    aluno = str(input(f'{posicao[n]} aluno: '))
    l.append(aluno)
    n += 1

random.shuffle(l)
print(l)

