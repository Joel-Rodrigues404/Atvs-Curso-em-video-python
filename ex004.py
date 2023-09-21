msg = input('digite algo: ')

print(f"O tipo desta mensagem e {type(msg)}")
print(f'So tem espaços {msg.isspace()}')
print(f'So tem numeros {msg.isnumeric()}')
print(f'So tem letras {msg.isalpha()}')
print(f'E alpha numerico {msg.isalnum()}')
print(f'Esta todo em maiusculo {msg.isupper()}')
print(f'Esta toda em minuscula {msg.islower()}')
print(f'Esta capitalizada {msg.istitle()}')



