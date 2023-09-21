from time import sleep

print('_-_-'*37)
print('Faça um triangulo')
print('_-_-'*37)
sleep(2)

segmento1 = abs(float(input("digite o primeiro segmento de reta: ")))
segmento2 = abs(float(input("digite o segundo segmento de reta: ")))
segmento3 = abs(float(input("digite o terceiro segmento de reta: ")))

if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento2 + segmento1:
    if segmento1 == segmento2 == segmento3:
        print(f'Com esses segmentos de reta e possivel formar um triangulo EQUILATERO')
    elif segmento1 == segmento2 != segmento3 or segmento1 == segmento3 != segmento2 or segmento2 == segmento3 != segmento1:
        print(f'Com esses segmentos de reta e possivel formar um triangulo ISOCELES')
    elif segmento1 != segmento2 != segmento3 != segmento1:
        print(f'Com esses segmentos de reta e possivel formar um triangulo ESCALENO')
else:
    print(f'Com esses segmentos de reta nao possivel formar um triangulo')
