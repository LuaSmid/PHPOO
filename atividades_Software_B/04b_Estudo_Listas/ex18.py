#Exercício 18: Enumerar elementos (enumerate) - Mostre a posição dos nomes que possuem mais de 6 letras.
#Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio", "Ana", "Ana"]
#Luana 11251103287
#UMC - 25/04/2025

Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"] 
print(f"Minha lista: {Minha_Lista}")
for index, nome in enumerate(Minha_Lista):
    if len(nome) > 6:
        print(f"O nome {nome} na posição {index} possui mais de 6 letras.")
#O resultado é: Minha lista: ['Ana', 'Carlos', 'Beatriz', 'Eduardo', 'Sérgio']
#O nome Carlos na posição 1 possui mais de 6 letras.
#O nome Beatriz na posição 2 possui mais de 6 letras.
#O nome Eduardo na posição 3 possui mais de 6 letras.
#O nome Sérgio na posição 4 possui mais de 6 letras.
#A função enumerate() é utilizada para obter o índice e o valor de cada elemento da lista.
#Neste caso, a lista Minha_Lista contém 5 nomes, e o loop for percorre cada elemento, imprimindo sua posição e nome correspondente.
