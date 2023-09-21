peso = abs(float(input("Digite seu peso: ")))
altura = abs(float(input("digite sua altura: ")))

if altura.is_integer():
    altura = altura/100
print(altura)


imc = peso/(altura**2)


if imc <= 18.5:
    print(f'com o imc de {imc:.2f} Voce esta abaixo do peso')
elif imc <= 25:
    print(f'com o imc de {imc:.2f}Voce esta no peso ideal')
elif imc <= 30:
    print(f'com o imc de {imc:.2f}Voce esta na faixa de sobrepeso')
elif imc <= 40:
    print(f'com o imc de {imc:.2f}Voce esta na faixa de obesidade')
else:
    print(f'com o imc de {imc:.2f}Voce esta na faixa de obesidade morbida')
    
