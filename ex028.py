import random
from time import sleep

print(f"-=-="*37)
print(f'VOU PENSAR EM UM NUMERO ENTRE 0 E 5. TENTE ADIVINHAR ...')
print(f"-=-="*37)

maquina = random.randint(0,5)
num = int(input("Em que numero eu pensei: "))
print(f'PENSANDO ...')
sleep(2)
if num == maquina:
    print("VOCE ACERTOU")
    print(f'PENSEI NO NUMERO {maquina}')
else:
    print("VOCE ERROU")
    print(f'PENSEI NO NUMERO {maquina}')

