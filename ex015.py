km = float(input('Quantidade de km rodados: '))
dias = int(input('Numero de dias que o carro foi alugado: '))
valor = 60 * dias + 0.15 * km
print('O valor a ser pago por {} km e {} dia (s) é {}'.format(km, dias, valor))
print(f'O valor a ser pago por {km} km e {dias} é de {valor}')

