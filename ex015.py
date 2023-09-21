dias_alugados = abs(int(input("quantidade de dias aludos: ")))
km_rodados = abs(int(input("quantidade de quilometros rodados: ")))

valor_aluguel = dias_alugados*60
valor_km_rodados = km_rodados*0.15

print(f"""
O carro foi alugado por {dias_alugados} dias e andou {km_rodados}kms o valor a ser pago e {valor_aluguel+valor_km_rodados}
""")



