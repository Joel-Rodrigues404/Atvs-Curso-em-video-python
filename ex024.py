cidade = str(input("Em que cidade voce nasceu: ")).strip().upper()
print("A palavra santo esta na cidade")

print(cidade[:5].upper() == 'SANTO')
print('SANTO' in cidade)