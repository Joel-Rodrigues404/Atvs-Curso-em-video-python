from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')

pessoa = abs(int(input("""
Suas Opçoes
[0] PEDRA
[1] PAPEL
[3] TEZOURA
Qual e a sua jogada: """)))
if pessoa >=3 or pessoa <= 0:
    print('JOGADA ERRADA')
    exit()
maquina = randint(0,2)
sleep(1)
print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("POO!!!")
sleep(0.1)

print(f'_-_=_-'*20)
print(f'O COMPUTADOR JOGOU {itens[maquina]}')
print(f'E VOCE JOGOU {itens[pessoa]}')
print(f'_-_=_-'*20)
sleep(1.5)


if maquina == pessoa:
    print(F'EMPATE maquina jogou {itens[maquina]} e voçe jogou {itens[pessoa]}')
elif maquina == 0 and pessoa == 1 or maquina == 1 and pessoa == 2 or maquina == 2 and pessoa == 0:
    print(F'Voce ganhou maquina jogou {itens[pessoa]} e voçe jogou {itens[maquina]}')
else:
    print(F'Voce perdeu maquina jogou {itens[pessoa]} e voçe jogou {itens[maquina]}')

