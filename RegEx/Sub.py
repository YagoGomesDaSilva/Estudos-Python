import re

texto = "yago, gomes, da, silva" #pode ser um arquivo txt tbm 

#substitui um elemento por outro,
# retonado uma lista com os elementos substituidos 

resultado = re.sub('\s','-',texto)
resultado = re.sub(',','.',resultado)

print(resultado)
