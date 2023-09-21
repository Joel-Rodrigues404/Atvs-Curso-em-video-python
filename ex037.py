num = abs(int(input("Digite um numero inteiro: ")))
escolha = abs(int(input("""
Escolha uma das bases para conversao
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL
Sua escolha \n > """)))

if escolha == 1:
    print(f'O numero {num} em Binario e igual a {num:b}')
elif escolha == 2:
    print(f'O numero {num} em Octal e igual a {num:o}')
elif escolha == 3:
    print(f'O numero {num} em hexadecimal e igual a {num:x}')
else:
    print("voce digitou a escolha de forma errada deve escolher entre 1, 2, 3")