from datetime import date

ano_atual = date.today().year
ano_de_nascimento = abs(int(input("digite seu ano de nascimento: ")))
idade = ano_atual - ano_de_nascimento

print(f'O atleta tem {idade} anos')

if idade <= 9:
    print(f'Classificaçao MIRIN')
elif idade <=14:
    print(f'Classificaçao INFANTIL')
elif idade <= 19:
    print(f'Classificaçao JUNIOR')
elif idade <= 25:
    print(f'Classificaçao SENIOR')
elif idade > 25:
    print(f'Classificaçao MASTER')
