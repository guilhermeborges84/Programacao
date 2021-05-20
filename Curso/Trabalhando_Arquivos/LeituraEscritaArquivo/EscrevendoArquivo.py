#Escrevendo em arquivo devemos abrir
'''Modo de abertura
r+ =  atualização e escrita 

'''
#O parametro w significa writer ( Liberado para escrita )
with open("C:\\Users\\6022390\OneDrive - Thomson Reuters Incorporated\Python\LeituraEscritaArquivo\Ponte.rdg",'r+') as arquivo:
    arquivo.write("GUILHERME")