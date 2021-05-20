import wmi #Importando biblioteca que conecta no windows.
from locate import this_dir #Biblioteca que pega o diretório onde está executando o .py ou no caso o executável

#Caminho dos arquivos
caminho_raiz = (this_dir())
caminho_servidores= str(caminho_raiz) + '\\Servidores.ini'
comando_senha= str(caminho_raiz) + '\\Comando.ini'

#Definindo usuários e senhas
usuario_remoto = "xxxx"
senha_remoto = "yyyy"

#Abaixo estou definindo o arquivo para ler onde fica o nome dos servidores
with open(caminho_servidores,"r") as arquivo:
    #Na variável Servidores fica os dados do arquivo Servidores.ini, vai ler linha a linha no caso o nome do servidor.
    Servidores = arquivo.readlines()

for servidor in Servidores:
    #Cortando o enter do arquivo Servidores.ini
    servidor = servidor.rstrip('\n')

    #Caso queira testar posso conectar na máquina local no comando abaixo
    #localhost = wmi.WMI()

    #Conectando máquina remota
    conectar_remoto = wmi.WMI(servidor,user=usuario_remoto,password=senha_remoto)

    #Construção do Comando para criar arquivo do powershell "reset.ps1" com comando para resetar a senha do Active Directory(AD).
    comando = "powershell /c ECHO \'DSQUERY user \"\"\"\"\"cn=infra_guilherme,ou=Validacao, ou=GTM-BR-PeaPOD-QA-USERS,ou=XenApp,ou=Gtm,ou=Business Products,dc=LHTRQA,dc=loc\"\"\"\"\" -limit 0 | DSMOD user -pwd Welcome@30\' > D:\Guilherme\Resultado\\reset.ps1"
    #O comando cria o arquivo reset.ps1 no servidor remoto
    conectar_remoto.Win32_Process.Create(CommandLine=comando)

    #Executando arquivo bat para reset de senha
    conectar_remoto.Win32_Process.Create(CommandLine="powershell D:\Guilherme\Resultado\\reset.ps1 >D:\Guilherme\Resultado\\reset.txt")