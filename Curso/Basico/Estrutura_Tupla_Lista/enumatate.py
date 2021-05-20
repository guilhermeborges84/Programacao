cardapio =['Carne','Queijo','Pizza']

for indice,recheio in enumerate(cardapio): #O enumerate colocou indice no cardapio [0]Carne,[0]Queijo,[0]Pizza
     print(f'O indice é: {indice} e o recheio é: {recheio}')

opcao = int(input('Digite o valor desejado: '))

'''if opcao < 0 or opcao >indice:
    print("Escolha opção do cardápio")
else:
    print(f'Você escolheu {cardapio[opcao]}')'''

if opcao >=0 and opcao <=len(cardapio):
    print(f'Você escolheu {cardapio[opcao]}')
else:
    print("Escolha opção do cardápio")

    