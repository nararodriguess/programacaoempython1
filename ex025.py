nome = str(input('Digite o nome: ').strip().lower())
print(f'Seu nome possui Silva? {"silva" in nome}')

cond = ('silva' in nome)
if cond != True:
    print('Não possui Silva no nome')
else:
    print('Esse nome possui Silva no nome')


