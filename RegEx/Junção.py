import re

texto = "yago gomes da silva " 
pesquisa = input('Pesquisar: ')

resultado = re.search(pesquisa,texto)

if resultado != None:
    pi = resultado.start()
    pf = resultado.end()
    tam = pf - pi
    print('A string começa na posição: {} '.format(resultado.start()))
    print('A string termina ne posição: {} '.format(resultado.end()))
    print('O tamanho da string é: {} '.format(tam))
else:
    print('Não enconntrado')

resultado = re.findall(pesquisa,texto)
print(resultado)
quantidade = len(resultado)
print('A quantidade de elementos é: ' + str(quantidade))

ds = int(input('Dividir(1) ou substituir(2)? '))
if ds == 1:
    opc = input("Em qual elemento voce quer dividir o texto (se for nos 'espaços', aperte-o): ")
    resultado = re.split(opc,texto)
    print(resultado)
elif ds == 2:
    print("Aonde tem o elemento...(se for nos 'espaços', aperte-o): ")
    sub_1 = input()
    print("Subtituir por... ")
    sub_2 = input()
    resultado = re.sub(sub_1,sub_2,texto)
    print(resultado)
