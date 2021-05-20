import requests # responsável por enviar requisições HTTP
import json

#requisição do tipo GET (para buscar dados) 
response = requests.get('https://osgt-cmportal.int.thomsonreuters.com/api/customer')

#Transformando em Json
content = response.json()

#Imprimir quantidade de clientes
for chave,value in enumerate(content):
    total = (chave + 1 )

print(f'Temos {total} clientes cadastrados')
totalBRP0484 = 0
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
            totalBRP0484 = totalBRP0484 + 1 
        print (f'Cliente: {name} Ambiente: {environmentCollection} TNS: {tns}')

print (f'Temos {totalBRP0484} cliente no {tnsbrp}') 