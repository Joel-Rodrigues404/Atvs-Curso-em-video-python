frase = str(input("digite uma frase: ")).upper().strip()

frase2 = frase.replace(" ","")

frase_reverse = frase2[::-1]
print(frase_reverse)
if frase2 == frase_reverse:
    print("e um palindromo")
    print(f'A palavra {frase} A frase ao contrario {frase_reverse}')

