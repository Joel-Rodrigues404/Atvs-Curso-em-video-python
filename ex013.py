salario_func = abs(float(input("digite o salario do funcionario: ")))
salario_acrecimo = abs(float(input("digite quantos porcento de acrecimo de salario: ")))

print(f'um funcionario que ganhava {salario_func} com {salario_acrecimo}% de aumento passou a receber R${salario_func + salario_func*(salario_acrecimo/100)}')