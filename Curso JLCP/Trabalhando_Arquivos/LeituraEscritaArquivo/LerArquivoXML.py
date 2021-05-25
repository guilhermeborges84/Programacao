#Leitura de arquivos

#Temos que abrir o arquivo com o open
#arquivo = open("C:\\Users\\6022390\OneDrive - Thomson Reuters Incorporated\Python\LeituraEscritaArquivo\Servidores.txt")
#print(arquivo)

#Para lermos o arquivo usamos a função read
#print(arquivo.read())

#Readline()  Essa função le o arquivo linha a linha
#print(arquivo.readline())

#Fechando conexão com o arquivo.
#arquivo.close()

#Abrindo arquivo com WITH não precisa fechar o arquivo.
with open("C:\\Users\\6022390\OneDrive - Thomson Reuters Incorporated\Python\LeituraEscritaArquivo\Servidores.txt") as arquivo:
    #print(arquivo.readlines())
    teste = arquivo.readlines()
    print(teste[0])

