from typing import ContextManager
import requests # responsável por enviar requisições HTTP
import json

from requests.models import Response # converter para um formato de dicionário


#requisição do tipo GET (para buscar dados) 
response = requests.get('https://osgt-cmportal.int.thomsonreuters.com/api/customer')
#todos = json.loads(request.content)

content = response.json()

for dados in content:
    print(type(dados))
    #environmentCollection =  dados['environmentCollection'][0]['type']
    #print ( type(environmentCollection)) 
    #exit(1)


