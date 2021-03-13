numero = input('Digite um número de 0 à 9999: ')
if len(numero) > 4:
    print('Valor inválido, pois, não pode ser maior que 9999')
elif len(numero) == 4:
    print(f'Esse valor possui {numero[3]} unidades, {numero[2]} dezenas, {numero[1]} centenas e {numero[0]} milhar')
elif len(numero) == 3:
    print(f'Esse valor possui {numero[2]} unidades, {numero[1]} dezenas, {numero[0]} centenas')
elif len(numero) ==2:
    print(f'Esse valor possui {numero[1]} unidades, {numero[0]}')
elif len(numero) ==1:
    print(f'Esse valor possui {numero[0]} unidade')