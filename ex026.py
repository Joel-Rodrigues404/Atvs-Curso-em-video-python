frase = str(input("digite uma frase: ")).strip().upper()
print(f"""
A letra A aparece {frase.count("A")}
A primeira letra A aparece na posiçao {frase.find('A')+1}
A ultima letra A aparece na posiçao {frase.rfind('A')+1}
""")