frase = input('Digite uma frase: ').lower().strip()
print(f"""A letra "a" aparece {frase.count("a")} vezes,
a primeira vez na posição {frase.find("a")+1} 
e a ultima vez na posição {frase.rfind('a')+1}""")
