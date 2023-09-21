distancia = abs(float(input("Digite uma distancia em metros: \n > ")))

if distancia == 0:
    print("O valor deve ser diferente de zero")
else:
    dm = distancia * 10
    cm = distancia * 100
    mm = distancia * 1000
    km = distancia / 1000
    hm = distancia / 100
    dam = distancia / 10

print(f"""
A distancia {distancia} corresponde a
{dm}dm
{cm}cm
{mm}mm
{km}km
{hm}hm
{dam}dam
""")



