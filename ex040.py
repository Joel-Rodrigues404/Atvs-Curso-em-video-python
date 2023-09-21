qnt = abs(int(input("digite quantos notas para formar a media: ")))
aluno = str(input("Digite o nome do aluno: "))


lista_notas = list()
cont = 1
for x in range(qnt):
    nota = abs(float(input(f'digite a {cont}° nota: ')))
    lista_notas.append(nota)
    cont += 1

soma_notas = sum(lista_notas)
media = soma_notas/qnt

if media < 5.0:
    print(f'Com a media {media} o aluno(a) {aluno} sera REPROVADO(A)')
elif 7 > media >= 5 :
    print(f'Com a media {media} o aluno(a) {aluno} ficara de RECUPERAÇAO ')
elif media >= 7.0:
    print(f'Com a media {media} o aluno(a) {aluno} sera APROVADO(A)')



