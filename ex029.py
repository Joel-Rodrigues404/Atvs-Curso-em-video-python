velocidade = abs(int(input("qual a velocida: ")))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Voce foi multado por eceder o limite de velocidade sua multa e de {multa}R$')
else:
    print(f'Com a velocidade de {velocidade}km/h voce esta dentro do limite parabens')