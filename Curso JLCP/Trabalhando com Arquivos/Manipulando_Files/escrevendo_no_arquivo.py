familia = ['Guilherme','Lucas','Juliana','Felipe']
file = open('/home/guilherme/Estudando_Python/Udemy/Arquivos_Txt/familia.txt','w')#O w parametro de escrita substitui
for pessoas in familia:
    print(f'Colocamos mais um na familia {familia}')
    file.write(f'{pessoas}\n')

amigos = ['Denis','Rafael','Thiago']
file = open('/home/guilherme/Estudando_Python/Udemy/Arquivos_Txt/familia.txt','a')#O a parametro de inserir
for pessoas in amigos:
    print(f'Colocamos mais um na familia {amigos}')
    file.write(f'{pessoas}\n')

file.close()#Necessario fechar o arquivo.