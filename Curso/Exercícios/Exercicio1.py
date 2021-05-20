# Variáveis definidas abaixo
nome = str(input("Digite seu nome: "))
idade = str(input("Digite a idade: "))
altura = float(input("Digite a altura: "))

#Definindo minha lista vazia
atribuicao = []

#Inserindo na lista forma manual
'''
atribuicao.append('Python')
atribuicao.append('AWS')
atribuicao.append('Datadog')
'''

#Inserindo na lista usando for
'''
for tecnologia in range(3):
    atribuicao.append(input('Digite a tecnologia usando for: '))
'''

#Inserindo na lista usando while.

contador = 1
while ( contador < 4):
    atribuicao.append(input('Digite a tecnologia usando while: '))
    contador= contador +1

print(f'O seu nome é {nome}')
print(f'A sua idade é {idade} anos')
print(f'A sua altura é {altura} cm')
print(f'As tecnologias utilizada são {atribuicao}')


