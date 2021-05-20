'''
Tuplas são representadas por parenteses()
As tuplas são imutáveis:Isso significa que ao se criar uma tupla ela não muda.
Toda operação em um tupla gerar una tupla
'''

#A representação de uma tupla com 1 elemento
tupla_elemento_unico = (4,) # Podemos fazer assim também tupla_elemento_unico = 4, 
print(f'Tupla criada com 1 elemento: {tupla_elemento_unico}')

#Tupla com mais de 1 elemento
tupla_numero = (1,2,4,5,6,7,8) #Podemos fazer assim também tupla = 1,2,4,5,6,7,8
print(f'Tupla criada com mais de 1 elemento: {tupla_numero}') # Podemos concluir que tuplas são definidas pela vírgula e não pelo ()

#Tupla com range
tupla_range = tuple(range(11))
print(f'Criamos uma tupla com range de 11 {tupla_range}') #0 até 10

'''
No desempacotamento de tuplas pega os valores da tupla e 
joga em variaveis
'''
tupla_desempacotamento = ('Guilherme','Juliana','Lucas','Felipe')
pai, mae, filho, enteado = tupla_desempacotamento

print(f'Tupla desempacotamento pai: {pai}')
print(f'Tupla desempacotamento mae: {mae}')
print(f'Tupla desempacotamento filho: {filho}')
print(f'Tupla desempacotamento enteado: {enteado}')

#Adicao e remoçao de elemento na tupla não existe, pois são imutáveis.
#Os valores eu posso sobrescrever mas não alterar estrutura dela como adicionar 


tupla_carrinho = ()
tupla_produto1 = ('Bola',1,'R$20.00')
tupla_produto2 = ('Video Game',2,'R$2550.00')

tupla_carrinho = tupla_produto1 + tupla_produto2
print(tupla_carrinho)#Nesse caso pega todos os valores e joga na tupla_carrinho
tupla_carrinho = (tupla_produto1,tupla_produto2)# Nesse caso cria 3 tuplas tupla_produto1 e tupla_produto2 dentro de tupla_carrinho
print(tupla_carrinho)

#Podemos adicionar os valores da tupla na variável 
brinquedo , quantidade , valor = tupla_produto1
print(f'O brinquedo é {brinquedo} e a quantidade do brinquedo é {quantidade} e o valor é de {valor}')

