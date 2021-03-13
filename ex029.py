km = int(input('Quantos Km por hora está o carro: '))
if km > 80:
    print(f'Você foi multado e o valor da multa é de {((km-80)*7):.2f} reais')
print('Dirija com cuidado! Boa viagem.')
