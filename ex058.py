from random import randint

a = randint(1,10)
print(f'Acabei de pensar em um numero entre 1 e 10 sera que voce consegue adivinhar qual foi?')


palpite = 0  
while True:
    b = abs(int(input(f'qual seu palpite: ')))
    palpite += 1
    if b == a:
        print(f'Voce acertou o numero escolhido foi {a}')
        break
    elif b != a:
        if a > b:
            print(f'mais...')
        else:
            print(f'menos')


