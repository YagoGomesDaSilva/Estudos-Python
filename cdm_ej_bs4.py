import re
import requests
from urllib.error import URLError, HTTPError #

try:
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}
    url = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,ARS-BRL',headers=headers)
    
    req = url.json()

except HTTPError as e:
    print(e.status, e.reason)

except URLError as e:
    print(e.reason)

req = str(req)

standard = re.compile(r" 'bid': '[0-9].[0-9]+'")
check = standard.findall(req)

coin = []
    
for i in check :
    coin.append(float((i.replace("'bid':","").replace("'","").strip())))

print("Bem vindo ao conversor de moedas em tempo real!\n")
money = ["dolar","euro","peso argentino"]

cont = 0
for i in coin :
    print("Atualmente 1 {} vale {} R$".format(money[cont],coin[cont]))
    cont+=1

cont = 0
for i in coin :
    print("Atualmente 1 R$ vale {} em {}".format((1/coin[cont]),money[cont]))
    cont+=1