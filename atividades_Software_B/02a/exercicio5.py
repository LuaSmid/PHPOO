# Empresa UMC
# Data 27/02/2025
# Programador Eduarda e Luana
# Calculo de aumento de estoque

N = float(input("Insira o estoque atual:"))
P = float(input("Insira a porcentagem de aumento:"))
NovoEstoque = N + (N*P/100)
print ("Este é o seu novo estoque: ",NovoEstoque)
