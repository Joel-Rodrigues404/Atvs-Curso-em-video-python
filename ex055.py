
l = list()
for x in range(1,6):
    peso = abs(float(input(f'O peso da {x}° pessoa: ')))
    l.append(peso)

print(f'O maior peso foi {max(l,key=float)}')
print(f'O menor peso foi {min(l,key=float)}')