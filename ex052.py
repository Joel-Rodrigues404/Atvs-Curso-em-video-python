num = abs(int(input("digite um numero: ")))

lista = list()
cont = 0
for x in range(1, num+1):
    if num % x == 0:
        lista.append(x)
        cont += 1
if len(lista) == 2:
    print(f'O numero {num} e primo')
    print(f'E e divisivel por {lista}')
else:
    print(f'O numero {num} n e primo e foi divisivel {len(lista)}')
    print(f'E e divisivel por {lista}')

