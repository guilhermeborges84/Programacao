import csv # importando biblioteca csv

#Aqui eu estou abrindo o arquivo no modo tipo leitura  'r'
abrir_arquivo = open('/home/guilherme/Estudando_Python/Python/Arquivos_Csv/menu.csv','r')

#Estou dizendo que a delimitador é ;
#Metodo csv.reader para ler o arquivo e limitador ; separar as colunas
arquivo_csv = csv.reader(abrir_arquivo,delimiter=';')

#For para ler o arquivo_csv.
#for tupla [sabor,valor,status] 
for [sabor,valor,status] in arquivo_csv:
    print(f'O pastel {sabor} custa {valor} e está {status}')
abrir_arquivo.close()