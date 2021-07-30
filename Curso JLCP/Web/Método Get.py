# biblioteca Requests (Solicitações) do Python, que permite que você envie solicitações HTTP em Python.
#Uma vez que o uso de uma API implica em enviar solicitações HTTP e receber respostas, a biblioteca Requests permite que você utilize APIs no Python.
import requests

#O enderço 'http://127.0.0.1:5000' é uma API criada para estudo criada.
#Poderia ser um endereço como por exemplo de um site 

endereco = 'http://127.0.0.1:5000'

#O metodo get tem que passar (url = endereço ) por exemplo  request.get(url=google.com.br)
#Response = resposta da requisição
resposta = requests.get(url=f'{endereco}/healthcheck')
status = resposta.status_code

if status == 200:
    conteudo = resposta.json()
    #Existe um dicionário com o nome message e valor 'API is alive'
    #Exemplo: {'message': 'API is alive'}
    print(conteudo['message'])