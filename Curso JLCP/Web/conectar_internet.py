import urllib.request

def ConectaInternet():
    endereco = urllib.request.urlopen("https://www.google.com")

    if endereco.getcode() == 200:
        meuDado = endereco.read()
        print(meuDado)

ConectaInternet()