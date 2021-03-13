cidade = input('Digite o nome da sua cidade: ').strip().title().split()[0]
if 'Santo' in cidade:
    print('Nome da cidade começa com "Santo"')
else:
    print('Cidade não possui "Santo" no primeiro nome')
