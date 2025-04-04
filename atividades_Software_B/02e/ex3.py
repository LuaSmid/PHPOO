#UMC
#Eduarda e Luana 
#18/03
#Números repetidos

#Entrada
tituloo='''
                     _   _                 
 _ __ ___ _ __   ___| |_(_) ___ __ _  ___  
| '__/ _ \ '_ \ / _ \ __| |/ __/ _` |/ _ \ 
| | |  __/ |_) |  __/ |_| | (_| (_| | (_) |
|_|  \___| .__/ \___|\__|_|\___\__,_|\___/ 
         |_|                                                                         /_/                                                                                                                                                                                                                             
'''
print(tituloo)

import os
n1=int(input("Insira o primeiro número: "))
os.system('cls')
print(tituloo)

n2=int(input("Insira o segundo número: "))
os.system('cls')
print(tituloo)

n3=int(input("Insira o terceiro número: "))
os.system('cls')
print(tituloo)

n4=int(input("Insira o quarto número: "))
os.system('cls')
print(tituloo)

#Processamento e decisão
if n1 == n2:
    print(f"números repetidos: n1: {n1} e n2: {n2}")
if n1 == n3:
    print(f"números repetidos:  n1: {n1} e n3: {n3}")
if n1 == n4:
    print(f"números repetidos:  n1: {n1} e n4: {n4}")
if n2 == n3:
    print(f"números repetidos:  n2: {n2} e n3: {n3}")
if n2 == n4:
    print(f"números repetidos:  n2: {n2} e n4: {n4}")   
if n3 == n4:
    print(f"números repetidos:  n3: {n3} e n4: {n4}")

#Saída
input("Nenhum número repetido, fim do programa, pressione enter")
os.system('cls')