salario = abs(float(input("digite o valor de seu salario: ")))

if salario >= 1250.0:
    novo_salario = salario + salario*(10/100)
else:
    novo_salario = salario + salario*(15/100)

print(f'\033[31mSeu novo salario e {novo_salario}R$')
print()