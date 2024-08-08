#Comando While de repetição

def repetição():

    cont = 1

    while cont <= 3:
        print(str(cont) + "a execução do laço")
        cont+=1

repetição()

#Exercicio While tabuada do X

def tabuada():
    numero = int(input("Digite o numero:"))
    cont = 1

    while cont <= 10:
        resultado = cont * numero
        print("{} x {} = {}".format(numero,cont,resultado))
        cont += 1

tabuada()

#Exercicio While Calculadora

opção = 1

while opção:
    print("---------------------")
    print("0 - Sair")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("---------------------")
    break

opção = int(input("Opção: "))

def soma():
    x = float(input("Primeiro numero:"))
    y = float(input("Segundo numero:"))
    print("Soma",x+y)

def subtração():
    x = float(input("Primeiro numero:"))
    y = float(input("Segundo numero:"))
    print("Subtração",x-y)

def multiplicação():
    x = float(input("Primeiro numero:"))
    y = float(input("Segundo numero:"))
    print("Multiplicação",x*y)

def divisão():
    x = float(input("Primeiro numero:"))
    y = float(input("Segundo numero:"))
    print("Divisão",x/y)

if(opção==1):
    soma()
if(opção==2):
    subtração()
if(opção==3):
    multiplicação()
if(opção==4):
    divisão()
    