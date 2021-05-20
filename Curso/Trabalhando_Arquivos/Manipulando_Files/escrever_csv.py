import csv

#'w' = escrita
meu_arquivo =  open('/home/guilherme/Estudando_Python/Python/Arquivos_Csv/pedidos.csv','w',newline='',encoding='utf-8')

escreva = csv.writer(meu_arquivo,delimiter=';')
cabecalho = ['id','cliente','valor']
escreva.writerow(cabecalho)#Metodo que vai escrever na linha o que está entre ()

pedido1 = ['01','Guilherme','R$15.00']
escreva.writerow(pedido1)

pedido2 = ['02','Juliana','R$23.00']
escreva.writerow(pedido2)

pedido3 = ['03','Lucas','R$34.00']
escreva.writerow(pedido3)

pedido4 = ['04','Felipe','R$5.00']
escreva.writerow(pedido4)

meu_arquivo.close()