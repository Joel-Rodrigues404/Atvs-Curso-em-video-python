soma_num = 0
while True:
    num = abs(int(input(f'Digite um numero [999 para parar]: ')))
    if num == 999:
        break
    soma_num += num
    

print(f'{soma_num}')