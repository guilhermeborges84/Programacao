#Imprime 0 até 5
def loopFor():
    for x in range(0,5):
        print(x)

loopFor()


def loopEnumerate():
    dias = ["segunda","terça","quarta","quinta","sexta","sabado","domingo"]
    for indice,data in enumerate(dias):#Imprime a posição e o valor.
        print(indice,data)

loopEnumerate()