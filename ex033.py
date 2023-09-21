num1 = abs(int(input("digite o primeiro valor: ")))
num2 = abs(int(input("digite o segundo valor: ")))
num3 = abs(int(input("digite o terceiro valor: ")))

menor = num1
if num2<num1 and num2<num3:
    menor = num2
elif num3<num2 and num3<num1:
    menor = num3

maior = num1
if num2>num1 and num2>num3:
    maior = num2
elif num3>num2 and num3>num1:
    maior = num3

print(f'O maior valor e {maior}')
print(f'O menor valor e {menor}')