
'''
Expressão regular exemplos:
Arquivo:
Lucas
Guilherme Costa

1-)Definir começo do texto: ^L 
Por exemplo nomes que começam com a letra L 
Retorna: L

2-)Toda letra: \w
Retorna:
Lucas
Guilherme Costa

3-)Repete ultimo comando no exemplo \w até achar caractere espaço: ^G\w+ 
Retorna:
Guilherme

4-)Espaço: ^G\w+\sCosta
Retorna:
Guilherme Costa

5-)Grupos procura L ou G: [LG]

'''
import re

with open('/home/guilherme/Estudando_Python/Python/Arquivos_Txt/familia.txt') as meu_arquivo:
    no_arquivo = meu_arquivo.read()
    busca = r'^L\w+'
    #Findall procura todos
    regex = re.findall(busca,no_arquivo)
    print(regex)
    #Search procura e só motra um resultado
    regex = re.search(busca,no_arquivo)
    print(regex.group())
    #Procura só na primeira linha
    regex = re.match(busca,no_arquivo)
    print(regex)

