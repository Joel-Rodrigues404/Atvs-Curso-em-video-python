while True:
    pergunta = str(input(f'Digite seu sexo: [M/F]: '))
    if pergunta not in 'MFfm':
        print(f'Digite uma escolha valida')
    elif pergunta in 'MFmf':
        if pergunta in 'mM':
            print(f'Sexo Masculino registrado')
            break
        elif pergunta in 'fF':
            print(f'Sexo feminino registrado')
            break
        