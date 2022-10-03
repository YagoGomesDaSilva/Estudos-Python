import re

texto = "yago gomes da silva " #pode ser um arquivo txt tbm 

#Divide a string de origem pelas ocorrências do padrão, 
#retornando uma lista contendo as substrings resultantes. 
resultado = re.split('\s',texto)#retira da string o elemento  informado 

print(resultado)
print(resultado[3])

for t in resultado:
    print(t)