ano = abs(int(input("Digite o ano que dejesa saber se e bissexto ou n: ")))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#  2000 % 4 == 500 resto 0 TRUE
#  2000 % 100 == 20 resto 0 FALSE
#  2000 % 400 == 5 resto 0 TRUE
    print(f'O ano {ano} e Bissexto')
else:
    print(f'O ano {ano} N e Bissexto')