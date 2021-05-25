#Definindo lista de números
lista_numeros = []
tem_na_lista = False

for numeros in range(10):
    #Recebendo o número que o usuário digitar
    numero = input('Digite o número para inserir: ')
    tem_na_lista = False
    #Percorrendo a lista para verificar se existe o número que irá inserir
    for posicao_lista in range(len(lista_numeros)):
        #Se estiver o número na lista não insere
        if numero == lista_numeros[posicao_lista]:
            tem_na_lista = True
    
    #Caso o número inserido na lista não tem ele insere 
    if tem_na_lista == False:
        lista_numeros.append(numero)

print(lista_numeros)
