'''
Dicionarios representado por {} e contém chave e valor separados por 2 pontos :
Não pode ter chaves repetidas, caso passe o mesmo nome ele atualiza o valor e não cria uma nova.
'''
#Exemplo
dicionario_paises = {
    'BR':'Brasil','EUA':'Estados Unidos','CH':'Chile'
    }
print(f'Imprime os países do dicionario {dicionario_paises}')

dicionario_paises =dict(BR = 'Brasil',EUA = 'Estados Unidos',CH ='Chile')
print(f'Imprime os países do dicionario {dicionario_paises}')

#Busca na estrutura se existe uma chave retornando true or false
pais = dicionario_paises.get('BR')
print(f'Imprime o pais: {pais}')

#Checar se existe a chave no dicionario
print('BR' in dicionario_paises)#Retorna true se existir

#Utilizando tuplas em dicionarios
#A taupla não tem o seu valor alterado

dicionario_localizacao ={
    'Toquio': (52454255,2514265),
    (142563,2565632) : 'Chile'
    }

print(dicionario_localizacao)

#Adicionando no dicionario de dados
dicionario_lucro = {
    'Janeiro': 2500,
    'Feveiro':3000,
    'Março':4000,
    'Abril':152,
    'Maio':500,
    'Junho':650,
    'Julho':890,
    'Agosto':320,
}
print(dicionario_lucro)#Imprime os valores de lucro
dicionario_lucro['Setembro'] = 700 #Adicionando o mes de setembro no dicionario
print(dicionario_lucro)

#Remover chave
dicionario_lucro.pop('Setembro')#Remove o mes de Setembro
del dicionario_lucro['Agosto']#Outra forma de remover no caso removendo Agosta
print(dicionario_lucro)#imprime sem o mes Setembro
 #As diferenças é que no pop eu consigo guardar o valor removido em uma var usando o poop
Janeiro = dicionario_lucro.pop('Janeiro')
print(f'Valor removido: {Janeiro}')


carrinho = []#Defini carrinho como Lista vazia

#Abaixo defini os 2 tipos de produtos como estrutura de dados
produto1 = {'Nome':'Video Game','Quantidade':'2','Preco':'RS2550.00'}
produto2 = {'Nome':'Bola','Quantidade':'1','Preco':'R$20.00'}

carrinho.append(produto1)
carrinho.append(produto2)

print(f'Aqui temos um carrinho do tipo lista com 2 produtos do tipo estruturas de dados: {carrinho}')

#Retornando todas as chaves do dicionario, diferente do get que retorna true or false
chaves = produto1.keys()
print(f'Imprimindo todas as chaves: {chaves}')

valor_chave = produto1.values()# Retorna o valor da chave do item
print(f'Imprimindo os valores das chaves {valor_chave}')

valores = produto1.items()#Retorna a chave e o valor do item
print(f'{valores}')

for chaves,valor_chave in valores:
    #print(chaves)
    #print(valor_chave)
    print(f'A chave é: {chaves} e tem o valor de: {valor_chave}')

produto1.pop