
# soma_num = 0
# while True:
#     num = abs(int(input(f'Digite um numero [999 para parar]: ')))
#     soma_num += num
#     if num == 999:
#         break

# print(f'{soma_num - 999}')


num = cont = soma = 0
num = abs(int(input(f'Digite um numero [999 para parar]: ')))
while num != 999:
    soma += num
    cont += 1
    num = abs(int(input(f'Digite um numero [999 para parar]: ')))

print(f'voce digitou {cont} digitos e a soma deles e {soma}')