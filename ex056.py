lista_idades = list()
idades = 0
maior_idade_homem = 0
homem_mais_velho = ''
mulher_menor_de_idade = 0
for x in range(1,5):
    print(f'_=_='*5, end="")
    print(f'{x}° Pessoa', end="")
    print(f'_=_='*5,)
    nome = str(input("Nome: ")).strip()
    idade = abs(int(input("Idade: ")))
    sexo = str(input("Sexo [M/F]: ")).strip().lower()
    idades += idade
    if x == 1 and sexo in "Mm":
        maior_idade_homem = idade
        homem_mais_velho = nome

    if sexo in "Mm" and idade > maior_idade_homem:
        maior_idade_homem = idade
        homem_mais_velho = nome
    
    if sexo in "Ff" and idade < 20:
        mulher_menor_de_idade += 1





media = idades/4
print(f'A media de idade do Grupo e {media}')
print(f'O homem mais velho tem {maior_idade_homem} e se chama {homem_mais_velho}')
print(f'E ao todo sao {mulher_menor_de_idade} mulheres com menos de 20 anos')
