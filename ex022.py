nome = str(input('Digite o seu nome: ')).strip()
print(f'Seu nome em letras maiúsculas: {nome.upper()}')
print(f'Seu nome em letras minúsculas: {nome.lower()}')
print(f'Seu nome com as iniciais maiúsculas: {nome.title()}')
print(f'Seu nome possui {len(nome)-nome.count(" ")} letras')


print(f'Seu nome tem {len(nome.replace(" ", ""))} letas')
# ou
# import re
# tiraespaco2 = re.sub(r'\s+', '', nome)
# print(f'Seu nome tem {len(tiraespaco2)} letras')

print(f'Seu primeiro nome é {(nome.split()[0])} e possui {len(nome.split()[0])} letras')
