import random
n1 = input('Insira o nome do primeiro aluno: ')
n2 = input('Insira o nome do segundo aluno: ')
n3 = input('Insira o nome do terceiro aluno: ')
n4 = input('Insira o nome do quarto aluno: ')
print(f'O aluno selecionado é {random.choice([n1, n2, n3, n4])}')

lista = [n1, n2, n3, n4]
print(f'O escolhido é {random.choice(lista)}')
