#Primeiro tenho que abrir o arquivo
#file =open(nome do arquivo.txt,'r') r =leitura por padrão é r e não precisa passar.
#file = open('pedidos.txt')
import os
print(os.getcwd())

file = open('Udemy/musica.txt')
arquivo = file.readlines()#readline é para ler todas as linhas
for musica in arquivo:
    #print(musica)
    print(musica.replace('\n',''))# o replace uso para trocar e o \n seria o enter estou trocando para conteudo em aspas no caso nada

file.close()#Fechando arquivo