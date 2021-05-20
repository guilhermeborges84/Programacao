from typing import Sized
from PySimpleGUI import PySimpleGUI as design #Importando biblioteca para layout
import paramiko # Importando a biblioteca paramiko que tem a função para conectar via ssh
from locate import this_dir #Biblioteca que pega o diretório onde está executando o .py ou no caso o executável
import requests # responsável por enviar requisições HTTP
import json

#requisição do tipo GET (para buscar dados) 
response = requests.get('https://osgt-cmportal.int.thomsonreuters.com/api/customer')

#Transformando em Json
content = response.json()


#Define o conteúdo da Janela
design.theme('Reddit')
tela_login_senha = [
    [design.Text('Banco:'),design.Input(key='banco',size=(20,1))],
    [design.Frame(layout=[
        [
            design.Radio('Quantidade de clientes cadastrados', "webservice", default=True)
        ],
        [
            design.Radio('Clientes cadastrados no banco', "webservice", default=False)
        ]                 ],
        title='Escolha a opção',title_color='red', relief=design.RELIEF_SUNKEN)
    ],
    [design.Button('Mostrar'),design.Button('Cancelar')],
    [design.Output(size=(125,20))]
]
#Cria a Janela
janela_login_senha = design.Window('CM Portal',tela_login_senha) 

#Mostra a Janela e interage usando loop
while True:
    eventos, valores = janela_login_senha.read()
    if eventos == design.WINDOW_CLOSED or eventos == 'Cancelar':
        break
    #Recebendo os valores de banco ou mostrar todos.
    username = valores['banco']

    #Imprimir quantidade de clientes
    for chave,value in enumerate(content):
        total = (chave + 1 )

    print(f'Temos {total} clientes cadastrados')
    totalBRP0484 = 0
    nometnsbrp = []
    for dados in content:
        #Nome do cliente
        name =  dados['name']
        #Ambiente do cliente
        for tamanho in range(len(dados['environmentCollection'])):
            #environmentCollection = PRODUÇÃO / Qualidae / Projeto é o ambiente
            environmentCollection =  dados['environmentCollection'][tamanho]['type']
            '''
            dbInstanceId = é o TNS no caso passado o ID
            Por exemplo o id 42309020 é o tns BRP0484
            dbInstanceId = 42309020 (BRP0484)
            '''
            tns = dados['environmentCollection'][tamanho]['dbInstanceId']
            if tns == 42309020:
                tnsbrp = 'BRP0484'
                
                nometnsbrp.append(dados['name'])
                totalBRP0484 = totalBRP0484 + 1 
            #print (f'Cliente: {name} Ambiente: {environmentCollection} TNS: {tns}')
    print (f'Temos {totalBRP0484} cliente no {tnsbrp}')
    print ( f'{nometnsbrp}')


#Finalizando a tela
janela_login_senha.close()

