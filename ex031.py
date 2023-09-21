distancia = abs(int(input("digite a distancia da viagem: ")))

# if distancia <= 200:
#     valor = distancia * 0.50
#     print(f'Com {distancia}km de distancia voce deve pagar {valor}R$')
# else:
#     valor = distancia * 0.45
#     print(f'Com {distancia}km de distancia voce deve pagar {valor}R$')

valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'Com {distancia}km de distancia voce deve pagar {valor}R$')