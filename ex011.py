largura_parede = abs(float(input("largura da parede: ")))
altura_parede = abs(float(input("altura da parede: ")))
area = largura_parede * altura_parede
tinta = area/2
print(f'A parede de dimençao igual a {largura_parede}x{altura_parede} e sua area e igual a {area}m²')
print(f'E a quantidade de tinta neçessaria para pintar e {tinta}')