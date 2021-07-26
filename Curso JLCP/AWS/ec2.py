#Lista = []

#Dicionario = {}
'''Dicionarios representado por {} e contém chave e valor separados por 2 pontos :
Não pode ter chaves repetidas, caso passe o mesmo nome ele atualiza o valor e não cria uma nova.'''

#Para usar Boto3, primeiro devemos importar e indiciar qual tipo de serviço estamos usando.
import boto3
teste = 'teste1'
Instancia = boto3.client('ec2')

#Me mostra as informações da minhas instâncias 
TodasInstancias = Instancia.describe_instances()

#print(TodasInstancias)

for informacoes in TodasInstancias['Reservations']:
    for instance in informacoes['Instances']:
        nomeInstancia = instance['KeyName']
        statusInstancia = instance['State']['Name']
        print(f'O nome da minha instancia é {nomeInstancia} o estado dela é {statusInstancia}')