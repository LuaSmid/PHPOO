#UMC
#Eduarda Beatriz Nogueira e Luana Felix Smid de Campos
#01/04
#Atividade 6 - Apartamento de férias

#Entrada/Repetição

import os
COR = '\033[1;30;42m'
FIM = '\033[0m'
cor = '\033[7;30;46m'
fim = '\033[0m'
imp = "Dados"
apt = "Apartamento"
total = "Total"
pessoa = "Pessoas"
tipo1 = "Diária 1"
tipo2 = "Diária 2"

tituloo='''
███████╗███████╗██████╗ ██╗ █████╗ ███████╗
██╔════╝██╔════╝██╔══██╗██║██╔══██╗██╔════╝
█████╗  █████╗  ██████╔╝██║███████║███████╗
██╔══╝  ██╔══╝  ██╔══██╗██║██╔══██║╚════██║
██║     ███████╗██║  ██║██║██║  ██║███████║
╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝'''
print(f"{cor}{tituloo}{fim}")

print("-------------------------------------------------------------------")
print(f"|{COR}    {pessoa}     |{COR}         {tipo1}       |{COR}       {tipo2}        {FIM}|")
print("|-----------------------------------------------------------------|")
print(f"|      1         |        R$20,00        |        R$25,00         |")
print("|-----------------------------------------------------------------|")
print(f"|      2         |        R$28,00        |        R$34,00         |")
print("|-----------------------------------------------------------------|")
print(f"|      3         |        R$35,00        |        R$42,00         |")
print("|-----------------------------------------------------------------|")
print(f"|      4         |        R$42,00        |        R$50,00         |")
print("|-----------------------------------------------------------------|")
print(f"|      5         |        R$48,00        |        R$57,00         |")
print("|-----------------------------------------------------------------|")
print(f"|      6         |        R$53,00        |        R$63,00         |")
print("-------------------------------------------------------------------")

nome=str(input("Insira o nome: "))
os.system('cls')
print(f"{cor}{tituloo}{fim}")

print("-------------------------------------------------------------------")
tel=str(input("Insira o telefone: "))
os.system('cls')

print(f"{cor}{tituloo}{fim}")
print("-------------------------------------------------------------------")
cpf=str(input("Insira o cpf: "))
os.system('cls')

print(f"{cor}{tituloo}{fim}")
print("-------------------------------------------------------------------")

while True:
    try:
        tipo=int(input("Insira o tipo da diária: "))
    except:
        print("Valor inválido.")
        opt=input("Pressione C para entrar novamente ou S para finalizar: ")
        if opt=="S" or opt=="s":
            break
    else:
        os.system('cls')
        print(f"{cor}{tituloo}{fim}")
        print("-------------------------------------------------------------------")
        if tipo not in [1,2]:
            print("Valor incorreto, insira um valor de 1 a 2: ")
           
        else:
            break
                
while True:
    try:
        pessoas=int(input("Insira a quantidade de pessoas: "))
    except:
        print("Valor inválido.")
        opt=input("Pressione C para entrar novamente ou S para finalizar: ")
        if opt=="S" or opt=="s":
            break
    else:
        os.system('cls')
        print(f"{cor}{tituloo}{fim}")
        print("-------------------------------------------------------------------")
        if pessoas not in [1,2,3,4,5,6]:
            print("Limite de pessoas ultrapassado, insira um valor de 1 a 6: ")
        else:
            break

dias=int(input("Insira quantos dias irá ficar: "))
os.system('cls')

#Processamento/Estrutura de Decisão

if pessoas == 1 and tipo == 1:
    precoApt = (20*pessoas)*dias
elif pessoas == 1 and tipo == 2:
    precoApt = (25*pessoas)*dias

elif pessoas == 2 and tipo == 1:
    precoApt = (28*pessoas)*dias
elif pessoas == 2 and tipo == 2:
    precoApt = (34*pessoas)*dias

elif pessoas == 3 and tipo == 1:
    precoApt = (35*pessoas)*dias
elif pessoas == 3 and tipo == 2:
    precoApt = (42*pessoas)*dias

elif pessoas == 4 and tipo == 1:
    precoApt = (42*pessoas)*dias
elif pessoas == 4 and tipo == 2:
    precoApt = (50*pessoas)*dias

elif pessoas == 5 and tipo == 1:
    precoApt = (48*pessoas)*dias
elif pessoas == 5 and tipo == 2:
    precoApt = (57*pessoas)*dias

elif pessoas == 6 and tipo == 1:
    precoApt = (53*pessoas)*dias
elif pessoas == 6 and tipo == 2:
    precoApt = (63*pessoas)*dias

#Saída
print(f"{cor}{tituloo}{fim}")
print("-------------------------------------------------------------------")
print(f"|{COR}           {imp}            |{COR}     {apt}     |{COR}    {total}     {FIM}|")
print("|-----------------------------------------------------------------|")
print(f"| Nome: {nome[:20]:<20} | Diária: {tipo:<11} | R$ {precoApt:<9} |")
print("|-----------------------------------------------------------------|")
print(f"| Tel: {tel[:20]:<20}  | {'':<19} | {'':<12} |")
print("|-----------------------------------------------------------------|")
print(f"| CPF: {cpf[:20]:<20}  | {'':<19} | {'':<12} |")
print("|-----------------------------------------------------------------|")
print(f"| Pessoas: {pessoas:<14}    | {'':<19} | {'':<12} |")
print("|-----------------------------------------------------------------|")
print(f"| Dias: {dias:<17}    | {'':<19} | {'':<12} |")
print("-------------------------------------------------------------------")

input("Fim do programa, pressione enter")
os.system('cls')
print(f"{cor}{tituloo}{fim}")