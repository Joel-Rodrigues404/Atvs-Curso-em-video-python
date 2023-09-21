qnt = abs(int(input("digite quantas notas vai ter o aluno: ")))

if qnt == 0:
    print("numero deve ser diferente de zero")
else:
    soma_notas = 0
    for x in range(qnt):
        nota = float(input('digite as notas dos alunos: '))
        soma_notas += nota

    print(f'A media e {soma_notas/qnt}')