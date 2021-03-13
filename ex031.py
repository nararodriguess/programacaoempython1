distancia = float(input('Digite a distância da viagem: '))
if distancia <= 200:
    print(f'O preço médio da sua passagem é de R$ {distancia*0.50} reais')
else:
    print(f'O preço médio da sua passagem é de R$ {distancia * 0.45} reais')

# modelo 02
preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print(preco)