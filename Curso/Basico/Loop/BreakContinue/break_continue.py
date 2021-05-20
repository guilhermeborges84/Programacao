def loopBreak():
    for x in range(5,10): #O range vai de 5 até 10
        if x == 7: #Coloquei condição caso o x = 7 ele termina o loop
            break
        print(f"O valor de x é: {x}")

#Chamando função
loopBreak()

def loopContinue():
    for x in range(5,10): #O range vai de 5 até 10
        if x == 7: #Coloquei condição caso o x = 7 ele termina o loop
            continue
        print(f"O valor de x é: {x}")

loopContinue()


# O break encerra a execução á no continue interrompe somente a execução que estou e passa para o próximo.