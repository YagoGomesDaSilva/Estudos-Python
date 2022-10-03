import re

texto = "yago yagod tobigod yago gomes da silva ygs" #pode ser um arquivo txt tbm 
pesquisa = input('Pesquisar: ')

resultado = re.findall(pesquisa,texto)#retorna uma lista/coleção
#primeiro parametro: texto ou variavel com imput
#segundo parametro:variavel que armazenou o texto
print(resultado)
quantidade = len(resultado)
print('A quantidade é: ' + str(quantidade))

for t in resultado: 
    print(t)