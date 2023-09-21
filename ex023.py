num = abs(int(input("digite um numero: ")))
"""
JEITO ERRADO
"""
unidades = len(str(num))
dezena = int(num/10)
centena = int(num/100)
milhar = int(num/1000)


print(f"""
Analizando o numero {num}
unidade: {unidades}
dezena: {dezena}
centena: {centena}
milhar: {milhar}
""")

"""
JEITO CERTO
"""
num2 = abs(int(input("digite um numero: ")))

u = num2 // 1 % 10 # 1234 // 1 > 1234 % 10 = 4
d = num2 // 10 % 10 # 1234 // 10 > 123 % 10 = 3
c = num2 // 100 % 10 # 1234 // 100 > 12 % 10 = 2
m = num2 // 1000 % 10 # 1234 // 1000 > 1 % 10 = 1

print(f"""
Analizando o numero {num2}
unidade: {u}
dezena: {d}
centena: {c}
milhar: {m}
""")