#UMC
#Eduarda e Luana 
#18/03
#Números consecutivos e em ordem crescente

#Entrada
import os

#fonte calvin s

tituloo='''
┌─┐┌─┐┌┐┌┌─┐┌─┐┌─┐┬ ┬┌┬┐┬┬  ┬┌─┐┌─┐
│  │ ││││└─┐├┤ │  │ │ │ │└┐┌┘│ │└─┐
└─┘└─┘┘└┘└─┘└─┘└─┘└─┘ ┴ ┴ └┘ └─┘└─┘                                                                                                                                                                                                                                                                                                                                                                                                       
'''
print(tituloo)

n1=int(input("Insira o primeiro número: "))
os.system('cls')
print(tituloo)

n2=int(input("Insira o segundo número: "))
os.system('cls')
print(tituloo)

n3=int(input("Insira o terceiro número: "))
os.system('cls')
print(tituloo)

#Processamento
os.system('cls')
print(tituloo)
if n1 < n2 and n2 < n3 and n1 < n3 :
    print(f"números consecutivos e em ordem: n1 = {n1} , n2 = {n2} e n3 = {n3}")
else:
    print(f"Números não consecutivos e aleatórios n1 = {n1} , n2 = {n2} e n3 = {n3}")

#Saída
input("Fim do programa, pressione enter")
os.system('cls')