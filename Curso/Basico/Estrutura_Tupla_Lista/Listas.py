'''
Listas não tem tamanho fixo e são criadas a partir de []
Listas podem mudar constantemente
'''

#Criando listas abaixo.
lista_numeros = [1,2,3,4,5] # Criei uma lista de números
lista_letras = ['a','E','x','L','n'] # Criei uma lista de letras
lista_vazia = [] # Criei uma lista vazia
lista_com_range = [list(range(11))] # Criei uma lista com um tamanho 10 elementos de 0 a 10 Exemplo 0,1,2,3,4,5,6,7,8,9,10


lista_nome = list('lucas') # Definindo a lista dess forma imprime assim -> ['l', 'u', 'c', 'a', 's'] separa cada letra em cada posição
#lista_nome = ('lucas') # Aqui a lista fica com um só valor no caso lucas
#lista_nome.split() # Esse comando separa cada letra por espaço e posso definir o caracter.Exemplo Gui Costa 2 valores 


#atribuindo variaveis

letra = str(input(f'Digite a letra que queira pesquisar na lista: '))


# O FOR abaixo procura a letra na lista5.
if letra in lista_nome:
    print(f'Achou a letra {letra} na lista {lista_nome}')#imprime a letra e depois todas as letras da lista5
else:
    print('Não achou')

'''
Para adicionar elementos na lista utilizo o comando append para adicionar 1 elemento por vez
lista_numeros = [1,99,5,27,46] # Criei uma lista de números
No append coloca o elemento como único por exemplo se colocar [1,2,4] 
vai ser um elemento do tipo lista mas com 3 número, vai adicionar uma lista dentro de uma outra lista
'''
print(f'Imprime a lista original {lista_numeros}')
lista_numeros.append(51) #Observação sempre coloca o valor no final da lista

print(f'Imprime a lista adicionando o número 51 no final: {lista_numeros}')
#vai imprimir com o número 51 junto na lista
'''
Nesse caso o extend vai adicionar os 3 número dentro da lista não vai criar uma lista nova
O extend ele não aceita só adicionar um elemento.
'''
lista_numeros.extend([10,20,40]) 
print(f'Adicionando 3 número 10,20,40 na lista: {lista_numeros}')

'''
inserir posicao do elemento
lista.insert(posicao,valor)
'''
lista_numeros.insert(2,'corinthians')# Aqui está inserindo corinthians nas posição 2
print(f'Imprime a lista com corinthians na posição 2 ->{lista_numeros}')

lista_numeros.remove('corinthians')#comando remove o valor que está na lista
print(f'Imprime a lista sem corinthians ->{lista_numeros}')

lista_numeros.pop() #Imprime a lista em ordem 
print(f'Remove ultimo elementro da lista {lista_numeros}')

lista_numeros.reverse()
print(f'Imprime lista em ordem reversa {lista_numeros}')

lista_numeros.sort()
print(f'Imprime a lista em ordem {lista_numeros}')

lista_numeros.pop(1)#Removendo o valor da posição que eu escolher.
print(f'Imprime a lista em ordem {lista_numeros}')



#Desempacotamento de listas
#Minha idéia é usar desempacotamento de lista para usar com dicionário de dados
numero1, numero2, numero3, numero4, numero5, numero6, numero7 = lista_numeros

print(f'Imprime o valor da variavel numero1 que recebeu da lista_numero: {numero1}')
print(f'Imprime o valor da variavel numero2 que recebeu da lista_numero: {numero2}')
print(f'Imprime o valor da variavel numero3 que recebeu da lista_numero: {numero3}')
print(f'Imprime o valor da variavel numero1 que recebeu da lista_numero: {numero4}')
print(f'Imprime o valor da variavel numero2 que recebeu da lista_numero: {numero5}')
print(f'Imprime o valor da variavel numero3 que recebeu da lista_numero: {numero6}')
print(f'Imprime o valor da variavel numero3 que recebeu da lista_numero: {numero7}')

lista_numeros.clear()#Removendo todos os elementeos da lista
print(f'Imprime a lista zerada {lista_numeros}')

#Lista para armazenar produtos
lista_carrinho_de_compra = []
produto1 = ['Video Game',2,'RS2550.00']
produto2 = ['Bola',1,'R$20.00']

lista_carrinho_de_compra.append(produto1)
lista_carrinho_de_compra.append(produto2)
print(lista_carrinho_de_compra)
#Nesse caso teriamos que saber o indice de cada produto, e iremos fazer atraves de dicionario de dados ou tupla