n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
lista = sorted([n1,n2,n3])
print(f'O maior número é {lista[2]} e o menor número é {lista[0]}')

if n1>n2 and n1>n3:
    print(f'O maior número é {n1}')
if n1<n2 and n1<n3:
    print(f'O menor número é {n1}')
if n2>n1 and n2>n3:
    print(f'O maior número é {n2}')
if n2>n1 and n2<n3:
    print(f'O menor número é {n2}')
if n3>n2 and n3>n1:
    print(f'O maior número é {n3}')
if n3<n2 and n3<n1:
    print(f'O menor número é{n3}')
