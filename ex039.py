from datetime import date

ano_nascimento = abs(int(input("Digite o ano de seu nascimento: ")))
data_atual = date.today().year
idade = data_atual - ano_nascimento

if idade < 18:
    print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em 2022')
    print(f'Ainda faltan {18 - idade} ano para seu alistamento')
    print(f'E seu alistamento sera em {(18-idade) + data_atual}')

elif idade == 18:
    print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em 2022')
    print(f'Esse e seu ano de alistamento voce deve se alistar imediatamente')

else:
    print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em 2022')
    print(f'Voce ja deveria ter se alistado a {idade - 18} anos')
    print(f'seu alistamento foi em {data_atual - (idade - 18)}')
