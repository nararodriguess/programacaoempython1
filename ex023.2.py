numero = int(input('Digite um número: '))
n1 = numero // 1 % 10
n2 = numero // 10 % 10
n3 = numero // 100 % 10
n4 = numero // 1000 % 10
print(f"""O número {numero} possui:'
      Unidades: {n1}
      Dezenas: {n2}
      Centenas: {n3}
      Milhar: {n4}""")
