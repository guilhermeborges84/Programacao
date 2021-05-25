# Caso apresente algum erro ele cai no except e depois continua o programa
try:
    with open('Python/Arquivos_Txt/tentativa.txt') as file:
        print('Arquivo aberto')
except Exception as meu_erro:
    print('Dançou não achou o arquivo tentativa.txt')

print('Continua o programa')