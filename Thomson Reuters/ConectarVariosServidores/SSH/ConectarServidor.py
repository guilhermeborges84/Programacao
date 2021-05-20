from typing import Sized
from PySimpleGUI import PySimpleGUI as design #Importando biblioteca para layout
import paramiko # Importando a biblioteca paramiko que tem a função para conectar via ssh
from locate import this_dir #Biblioteca que pega o diretório onde está executando o .py ou no caso o executável
from time import sleep

#Função que sobre todos os webservices com caminho /appserver/data
def subir_todos_webservices_appserver(address, command):
    try:
        #Abaixo criando o objeto estanciando o cliente.
        ssh = paramiko.SSHClient()
        #Adiciona como host conhecido.Por exemplo quando conecta temos confirmar Yes or No como host conhecido.
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #Comando para conectar no servidor
        ssh.connect(hostname=address, port= 22, username=username, password =password)
        #Executar o comando
        stdin,stdout, stderr = ssh.exec_command(command)
        stdin.close()
        #Saída do comando.
        if stdout:
            print()
            for line in stdout.readlines():
                #Guardar os comandos no arquivo Resultado.log como log.
                logResultado = ('/appserver/tomcat/'+ (line.replace('\n','/bin/./stopServer.sh\n')))
                Resultado = ('/appserver/tomcat/'+ (line.replace('\n','/bin/./stopServer.sh')))
                print(servidor)
                print(logResultado)
                with open(caminho_resultado,'a') as arquivo:
                    #Executar o comando do principal para gravar no arquivo texto o resultado
                    stdin,stdout, stderr = ssh.exec_command(command)
                    stdin.close()
                    #Escreva no arquivo o resultado
                    arquivo.writelines('echo ' +address+'\n')
                    arquivo.writelines(logResultado)
                    print(logResultado)
                    #sleep(30)
                    #Executa o resultado do comando gravado no texto
                    stdin,stdout, stderr = ssh.exec_command(Resultado)
    except Exception as error:
        print(error)

#Função que sobre todos os webservices com caminho /appdata/data
def subir_todos_webservices_appdata(address, command):
    try:
        #Abaixo criando o objeto estanciando o cliente.
        ssh = paramiko.SSHClient()
        #Adiciona como host conhecido.Por exemplo quando conecta temos confirmar Yes or No como host conhecido.
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #Comando para conectar no servidor
        ssh.connect(hostname=address, port= 22, username=username, password =password)
        #Executar o comando
        stdin,stdout, stderr = ssh.exec_command(command)
        stdin.close()
        #Saída do comando.
        if stdout:
            for line in stdout.readlines():
                #Guardar os comandos no arquivo Resultado.log como log.
                logResultado = ('/appdata/tomcat/'+ (line.replace('\n','/bin/./stopServer.sh\n')))
                Resultado = ('/appdata/tomcat/'+ (line.replace('\n','/bin/./stopServer.sh')))
                print(logResultado)
                with open(caminho_resultado,'a') as arquivo:
                    #Executar o comando do principal para gravar no arquivo texto o resultado
                    stdin,stdout, stderr = ssh.exec_command(command)
                    stdin.close()
                    arquivo.writelines('echo ' +address+'\n')
                    arquivo.writelines(logResultado)
                    print(logResultado)
                    #sleep(30)
                    #Executa o resultado do comando gravado no texto
                    stdin,stdout, stderr = ssh.exec_command(Resultado)
    except Exception as error:
        print(error)

#Função que sobre os webservices específico com caminho /appserver/data
def subir_webservice_especifico_appserver(address, command):
    try:
        #Abaixo criando o objeto estanciando o cliente.
        ssh = paramiko.SSHClient()
        #Adiciona como host conhecido.Por exemplo quando conecta temos confirmar Yes or No como host conhecido.
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #Comando para conectar no servidor
        ssh.connect(hostname=address, port= 22, username=username, password =password)
        #Executar o comando
        stdin,stdout, stderr = ssh.exec_command(command)
        stdin.close()
        #Saída do comando.
        if stdout:
            for line in stdout.readlines():
                #Guardar os comandos no arquivo Resultado.log como log.
                logResultado = ('/appserver/tomcat/'+ (line.replace('\n','/bin/./stopServer.sh\n')))
                Resultado = ('/appserver/tomcat/'+ (line.replace('\n','/bin/./stopServer.sh')))
                print(servidor)
                print(logResultado)
                with open(caminho_resultado,'a') as arquivo:
                    #Executar o comando do principal para gravar no arquivo texto o resultado
                    stdin,stdout, stderr = ssh.exec_command(command)
                    stdin.close()
                    #Escreva no arquivo o resultado
                    arquivo.writelines('echo ' +address+'\n')
                    arquivo.writelines(logResultado)
                    print(logResultado)
                    #Executa o resultado do comando gravado no texto
                    stdin,stdout, stderr = ssh.exec_command(Resultado)
    except Exception as error:
        print(error)

def subir_webservice_especifico_appdata(address, command):
    try:
        #Abaixo criando o objeto estanciando o cliente.
        ssh = paramiko.SSHClient()
        #Adiciona como host conhecido.Por exemplo quando conecta temos confirmar Yes or No como host conhecido.
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #Comando para conectar no servidor
        ssh.connect(hostname=address, port= 22, username=username, password =password)
        #Executar o comando
        stdin,stdout, stderr = ssh.exec_command(command)
        stdin.close()
        #Saída do comando.
        if stdout:
            for line in stdout.readlines():
                #Guardar os comandos no arquivo Resultado.log como log.
                logResultado = ('/appdata/tomcat/'+ (line.replace('\n','/bin/./stopServer.sh\n')))
                Resultado_stop = ('/appdata/tomcat/'+ (line.replace('\n','/bin/./stopServer.sh')))
                #Resultado_stop = ('/appdata/tomcat/'+ (line.replace('\n','/bin/./stopServer.sh')))
                with open(caminho_resultado,'a') as arquivo:
                    #Executar o comando do principal para gravar no arquivo texto o resultado
                    stdin,stdout, stderr = ssh.exec_command(command)
                    stdin.close()
                    #Escreva no arquivo o resultado
                    arquivo.writelines('echo ' +address+'\n')
                    arquivo.writelines(logResultado)
                    
                    #Executa o resultado do comando gravado no texto
                    print(f'Parando Webservice: tomcat-ws-{cliente}')
                    print( Resultado_stop )
                    #stdin,stdout, stderr = ssh.exec_command(Resultado_stop)
                    print('\n')
                    #sleep(45)
                    print(f'Subindo Webservice: tomcat-ws-{cliente}')
                    print(Resultado_stop)
                    stdin,stdout, stderr = ssh.exec_command(Resultado_stop)

    except Exception as error:
        print(error)

#Define o conteúdo da Janela
design.theme('Reddit')
tela_login_senha = [
    [design.Text('Usuário:'),design.Input(key='usuario',size=(25,1)),design.Text('Cliente:'),design.Input(key='cliente',size=(25,1))] ,
    [design.Text('Senha:  '),design.Input(key = 'senha',password_char='*',size=(25,1))],
    [design.Frame(layout=[
        [
            design.Radio('Subir todos os webservices', "webservice", default=True)
        ],
        [
            design.Radio('Subir webservices específico', "webservice", default=False)
        ]  
        ,
        [
            design.Radio('Criar ws específico', "webservice", default=False)
        ]  
                        ],
        title='Escolha a opção',title_color='red', relief=design.RELIEF_SUNKEN)
    ],
    [design.Button('Executar'),design.Button('Cancelar')],
    [design.Output(size=(75,20))]
]

#Cria a Janela
janela_login_senha = design.Window('Webservice',tela_login_senha) 

#Mostra a Janela e interage usando loop
while True:
    eventos, valores = janela_login_senha.read()
    if eventos == design.WINDOW_CLOSED or eventos == 'Cancelar':
        break
    #Recebendo os valores de usuário e senha.
    username = valores['usuario']
    password = valores['senha']
    cliente = valores['cliente']
    caminho_raiz = (this_dir())
    caminho_servidores= str(caminho_raiz) + '\\Servidores.ini'
    caminho_resultado= str(caminho_raiz) + '\\Resultado.log'    

    #Abaixo estou definindo o arquivo para ler onde fica o nome dos servidores
    with open(caminho_servidores,"r") as arquivo:
        #Na variável Servidores fica os dados do arquivo Servidores.ini, vai ler linha a linha no caso o nome do servidor.
        Servidores = arquivo.readlines()
    #Caso o botão escolhido é subir todos os webservices valores na posição 0
    if valores[0] == True:
        for servidor in Servidores:
            #Cortando o enter do arquivo Servidores.ini
            servidor = servidor.rstrip('\n')
            #Executando o comando no servidor.
            print(f'Conectando servidor: {servidor}')
            print('Executando os comandos abaixo: ')
            conexao = subir_todos_webservices_appserver(servidor,'ls /appserver/tomcat/ |grep tomcat-ws-') 
            conexao = subir_todos_webservices_appdata(servidor,'ls /appdata/tomcat/ |grep tomcat-ws-')
            print(f'Finalizado no servidor: {servidor}\n')
    elif valores[1] == True:
        print(f'Subir ws específico')
        for servidor in Servidores:
            #Cortando o enter do arquivo Servidores.ini
            servidor = servidor.rstrip('\n')
            #Executando o comando no servidor.
            print(f'Conectando servidor: {servidor}')
            print('Executando os comandos abaixo: \n')
            #conexao = subir_webservice_especifico_appserver(servidor,f'ls /appserver/tomcat/ |grep tomcat-ws-{cliente}') 
            conexao = subir_webservice_especifico_appdata(servidor,f'ls /appdata/tomcat/ |grep tomcat-ws-{cliente}')
            print(f'Finalizado no servidor: {servidor}\n')


#Encerrando execução
print('Finalizado os servidores')

#Finalizando a tela.
janela_login_senha.close()