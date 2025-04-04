#UMC
#Eduarda e Luana 
#18/03
#Divisão possível e impossível

#Entrada
import os
tituloo='''
██████╗ ██╗██╗   ██╗██╗███████╗ █████╗  ██████╗ 
██╔══██╗██║██║   ██║██║██╔════╝██╔══██╗██╔═══██╗
██║  ██║██║██║   ██║██║███████╗███████║██║   ██║
██║  ██║██║╚██╗ ██╔╝██║╚════██║██╔══██║██║   ██║
██████╔╝██║ ╚████╔╝ ██║███████║██║  ██║╚██████╔╝
╚═════╝ ╚═╝  ╚═══╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝                                                                                                                              
'''
print(tituloo)

n1=int(input("Insira o primeiro número: "))
os.system('cls')
print(tituloo)

n2=int(input("Insira o segundo número: "))
os.system('cls')
print(tituloo)

#Processamento e decisão


if n2 == 0:
    print("A divisão é impossível")
else:
    div=n1/n2
    print(f"A sua divisão é igual a: {div}")

#Saída
input("Fim do programa, pressione enter")
os.system('cls')


 