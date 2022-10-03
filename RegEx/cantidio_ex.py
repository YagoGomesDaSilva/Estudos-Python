import re
import requests
# https://curlconverter.com/

headers = {
    'authority': 'www.oficinadanet.com.br',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'popUserDataV2=1; _gid=GA1.3.106883681.1645576575; __gads=ID=a0f71575fd9fd4ee:T=1645576575:S=ALNI_ManA3szsFqS2ahq1j8VCebrf55mpA; _ga_JVKGH8SCBW=GS1.1.1645576574.1.1.1645576940.0; _ga=GA1.3.1115973352.1645576575; _gat_UA-676692-1=1',
    'if-modified-since': 'Wed, 23 Feb 2022 00:18:27 GMT',
}

response = requests.get('https://www.oficinadanet.com.br/games/30289-os-melhores-jogos-de-pc',headers=headers).text

padrao = re.findall(r'<h3>.*?</h3>\s*<p>.*?</p>',response,flags=re.DOTALL)

lista = []

for jogo in padrao:
    
    re_jogo = re.search(r'<h3>(?P<titulo>.*?)</h3>\s*<p>(?P<descr>.*?)</p>',jogo,flags=re.DOTALL)
    titulo = re_jogo.group("titulo")
    descricao = re_jogo.group("descr")
    
    dicionario = {
        'titulo': titulo, 
        'descricao' : descricao
    }
    lista.append(dicionario)
    
print(lista)