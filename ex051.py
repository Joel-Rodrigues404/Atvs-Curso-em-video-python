print("=--="*17)
print(f'10 TERMOS DE UMA PA')
print("=--="*17)

primeiro_termo = abs(int(input("Primeiro termo: ")))
razao = abs(int(input("Razao: ")))
decimo_termo = primeiro_termo + (10 - 1)* razao

for x in range(primeiro_termo, decimo_termo + razao ,razao):
    print(f'{x}',end=" -> ")
print("...")
