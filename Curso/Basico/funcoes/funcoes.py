#Variável global
PASTEL = 'Carne'

# Declarar função comeca com def
def imprimir_boas_vindas(cliente,sexo= 'null'): #Os parametros que eu passo valor são os opcionais na chamada, sempre passo por ultimo
    print(f'Seja bem vindo {cliente},{sexo}')
    print(PASTEL)
    #Caso eu queira mudar valor var global tenho que colocar global

def adiciona_pedido(cliente,sabor,valor):
    if len(cliente) < 1:
        mensagem_de_erro = 'Putz jumento coloca o nome do cliente'
        return mensagem_de_erro
    novo_pedido = f' {cliente} pediu pastel de {sabor} e custa {valor}'
    return novo_pedido 

#Chamando as funções
imprimir_boas_vindas(cliente='Guilherme')
pedido1 = adiciona_pedido(cliente = 'Juliana',sabor='Queijo',valor='R$12.00')
print(f'{pedido1}')
print(f'{PASTEL}')

