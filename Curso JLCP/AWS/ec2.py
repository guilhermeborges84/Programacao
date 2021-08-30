#Lista = []
#Dicionario = {}
'''Dicionarios representado por {} e contém chave e valor separados por 2 pontos :
Não pode ter chaves repetidas, caso passe o mesmo nome ele atualiza o valor e não cria uma nova.'''

#Para usar Boto3, primeiro devemos importar e indiciar qual tipo de serviço estamos usando.
import boto3
Instancia = boto3.client('ec2')

#Informação importante:
#É necessário ter instalado o AWS CLI na máquina que está tentando conectar no AWS

#Me mostra as informações da minhas instâncias 
TodasInstancias = Instancia.describe_instances()


#print(TodasInstancias)
#print(TodasInstancias["Reservations"])

#Guardando os valores do dicionário Reservations
Reservations = TodasInstancias["Reservations"]

print(TodasInstancias)

'''for listaReservations in Reservations:
    for listaInstances in listaReservations["Instances"]:
        print(listaInstances["ImageId"])
'''
