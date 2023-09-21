from random import randint



num_maquina = randint(1,10)
num_user = 0
par_ipar = ''
while True:
    num_user = abs(int(input(f'Digite o numero de dedos de 1 a 10: ')))
    escolha = str(input(f'Escolha par[P] ou impora[I]]')).upper().strip()
    a = num_maquina + num_user
    if a % 2 == 0:
        par_ipar = 'P'
    else:
        par_ipar = 'I'
    if escolha in 'Pp':
        print(f'voce digitou {num_user} e o outro digitou {num_maquina} {par_ipar}')
        print(f'D')

