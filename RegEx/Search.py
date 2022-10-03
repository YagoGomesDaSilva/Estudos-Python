import re

texto = "yago gomes da silva " #pode ser um arquivo txt tbm 
pesquisa = input('Pesquisar: ')

resultado = re.search(pesquisa,texto)#indica se foi encontrado ou não
#primeiro parametro: texto ou variavel com imput
#segundo parametro:variavel que armazenou o texto

if resultado != None:
    pi = resultado.start()
    pf = resultado.end()
    tam = pf - pi
    print('começa: {} '.format(resultado.start()))
    print('termina: {} '.format(resultado.end()))
    print('tamanho: {} '.format(tam))
else:
    print('Não enconntrado')