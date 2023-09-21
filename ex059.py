num1 = abs(int(input(f'Digite o primeiro valor: ')))
num2 = abs(int(input(f'Digite o segundo valor: ')))


while True:
    escolha = abs(int(input(f"""
    [1] Somar
    [2] multiplicar
    [3] maior 
    [4] novos numeros
    [5] sair programa
    >>>>>>> Qual é a sua opçao? """)))
    if escolha == 1:
        print(f'A soma entre {num1} e {num2} e {num1 + num2}')
    elif escolha == 2:
        print(f'A multiplicaçao entre {num1} e {num2} e {num1 * num2}')
    elif escolha == 3:
        if num1 > num2:
            print(f'O primeiro numero e maior')
        elif num1 == num2:
            print(f'Os nunmeros sao iguais')
        else:
            print(f'O segundo numero e maior')
    elif escolha == 4:
        num1 = abs(int(input(f'Digite o primeiro valor: ')))
        num2 = abs(int(input(f'Digite o segundo valor: ')))
    elif escolha == 5:
        print(f'saindo...')
        break