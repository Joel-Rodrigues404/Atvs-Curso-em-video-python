import math


cat_o = abs(float(input("comprimeto do cateto oposto: ")))
cat_a = abs(float(input("comprimeto do cateto adjacente: ")))

hipotesusa = (cat_o**2 + cat_a**2) ** (1/2)

hi = math.hypot(cat_o, cat_a)

print(f'A hipotenusa e igual a {hipotesusa:.2f}')
print(f'{hi:.2f}')