#UMC
#Eduarda e Luana 
#18/03
#Números pares e ímpares

#Entrada
import os

tituloo='''
                                             _                           
    ____  ____ ______   ____  __  __   (_)___ ___  ____  ____ ______
   / __ \/ __ `/ ___/  / __ \/ / / /  / / __ `__ \/ __ \/ __ `/ ___/
  / /_/ / /_/ / /     / /_/ / /_/ /  / / / / / / / /_/ / /_/ / /    
 / .___/\__,_/_/      \____/\__,_/  /_/_/ /_/ /_/ .___/\__,_/_/     
/_/                                            /_/                                                                                                                                                                                                                             
'''
print(tituloo)
numero=int(input("Insira um número: "))

#Processamento e decisão
os.system('cls')
print(tituloo)
if numero%2 ==0:
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} é ímpar")

#Saída
input("Fim do programa, pressione enter")
os.system('cls')
