num = list()

for x in range(1,500,2):
    if x % 3 == 0:
        num.append(x)

soma = sum(num)
conta = len(num)
print(soma,conta)