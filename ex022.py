nome = str(input("Digite seu nome completo: ")).strip()
maiusculo = nome.upper()
minuscula = nome.lower()
contar_nome = len(nome)-nome.count(' ')
qnt_primeiro_nome = nome.find(' ')
primeiro_nome = nome[:qnt_primeiro_nome]
cada_nome_separado = nome.split()

print(f"""
Analizando o nome {nome}
seu nome em maiusculas {maiusculo}
seu nome em minusculas {minuscula}
seu nome tem ao todo {contar_nome} letras
seu primerio nome tem {qnt_primeiro_nome} letras
seu primeiro nome e {primeiro_nome}
seu ultimo nome ou sobrenome e {cada_nome_separado[-1]}
""")