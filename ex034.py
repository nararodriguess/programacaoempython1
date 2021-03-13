salario = float(input('Digite o seu salário: '))
if salario > 1250:
    novo = salario * (1 + 0.1)
else:
    novo = salario * (1 + 0.15)
print(f'Seu salário era R${salario:.2f} reais, agora será R${novo:.2f} reais')
