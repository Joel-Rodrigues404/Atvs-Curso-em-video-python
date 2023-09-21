"""
JEITO FACIL
"""

num1 = int(input('digite um numero: '))
num2 = int(input('digite um numero: '))

soma = (num1 + num2)

print(f'A soma entre {num1} e {num2} e {soma}')



"""
JEITO DIFICIL
"""
pergunta = int(input('digite quantos numeros deseja somar: '))
lista = list()
for x in range(pergunta):
    a = int(input("digite um numero: "))
    lista.append(a)
print(f'A soma dos numeros e {sum(lista)}')
