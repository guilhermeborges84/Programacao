#Definino as variáveis
nome = str(input("Digite o seu nome: "))
cargo = str(input("Digite o seu cargo: "))
concatenado = 'Nome:' + nome + ' ,' + ' Cargo:' + cargo

#Concatenando manualmente
print(f'Valores concatenados manualmente: {nome} {cargo}')
print(f'Juntando string usando variáveis: {concatenado}')

inserir = input('Deseja inserir um novo nome e cargo? S para SIM ou N para NÃO ')

while ( inserir =='s'):
    nome = str(input("Digite o seu nome: "))
    cargo = str(input("Digite o seu cargo: "))
    concatenado =  concatenado + ',' + 'Nome: ' + nome + ',' + 'Cargo: '+ cargo
    inserir = input('Deseja inserir um novo nome e cargo? S para SIM ou N para NÃO ')
    print( concatenado )