#UMC
#Eduarda e Luana 
#18/03
#Direito a desconto

#Entrada
tituloo='''
┌┬┐┌─┐┌─┐┌─┐┌─┐┌┐┌┌┬┐┌─┐
 ││├┤ └─┐│  │ ││││ │ │ │
─┴┘└─┘└─┘└─┘└─┘┘└┘ ┴ └─┘                                                                                                                                                                                                                                                                                                                                                                                                       
'''
print(tituloo)
import os

idade=int(input("Insira a idade: "))


#Processamento
os.system('cls')
print(tituloo)

if idade < 16 or idade >= 60 :
    print(f"Você tem direito a desconto, idade = {idade}")
else:
    print(f"Você não tem direito a desconto, idade = {idade}")

#Saída
input("Fim do programa, pressione enter")
os.system('cls')