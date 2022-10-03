import requests
import re

cookies = {
    'JSESSIONID': '72BEDBD2C64BF77002DBDEF4BE0FCA63.appsWeb1',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://esaj.tjrn.jus.br/cpo/pg/search.do?paginaConsulta=1&localPesquisa.cdLocal=-1&cbPesquisa=NMPARTE&tipoNuProcesso=UNIFICADO&dePesquisa=maria+da+silva+neves&pbEnviar=Pesquisar',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
}

params = (
    ('processo.codigo', '010008STL0000'),
    ('processo.foro', '1'),
)

response = requests.get('http://esaj.tjrn.jus.br/cpo/pg/show.do', headers=headers, params=params, cookies=cookies, verify=False)

response = response.text

numero = re.search(r'\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}',response)
classe = re.search(r'<table cellpadding="0" cellspacing="0" border="0" width="">\s*<tr>\s*<td>\s*<span id="">\s*<span id="">(?P<classe>[^<]*?)</span>',response)
assunto = re.search(r'<div class="labelClass" style="text-align:right;font-weight:bold;;">Assunto:</div>\s*</td>\s*<td valign="">\s*<span id="">(?P<assunto>[^<]*?)</span>',response)
local_fisico = re.search(r'<div class="labelClass" style="text-align:right;font-weight:bold;;">Local F.*?sico:</div>\s*</td>\s*<td valign="">\s*<span id="">(?P<local>[^<]*?)</span>',response)
distribuicao = re.search(r'<div class="labelClass" style="text-align:right;font-weight:bold;;">Distribui.*?o:</div>\s*</td>\s*<td valign="">\s*<span id="">(?P<distr>[^<]*?)</span>',response)
valor_da_acao = re.search(r'<div class="labelClass" style="text-align:right;font-weight:bold;;">Valor da a.*?o:</div>\s*</td>\s*<td valign="">\s*<span id="">(?P<v_acao>[^<]*?)</span>',response)

#print(numero.group())
#print(classe.group('classe'))
#print(assunto.group('assunto'))
#<div class="labelClass" style="text-align:right;font-weight:bold;;">DistribuiþÒo:</div>\s*</td>\s*<td valign="">\s*<span id="">Sorteio - 28/10/2008 Ós 12:30</span>

dicionario = {
    'Numero': numero.group(),
    'Classe': classe.group('classe'),
    'Assunto': assunto.group('assunto'),
    'Local_Fisico':local_fisico.group('local'),
    'Distribuicao':distribuicao.group('distr'),
    'Valor_da_Acao':valor_da_acao.group('v_acao')
}

#print(dicionario)

lista = []
partes = re.finditer(r'<tr class="fundoClaro">\s*<td valign="top" align="right" width="141" style="padding-bottom: 5px">\s*<span\s*class="mensagemExibindo">(?P<autor>[^<]*?);</span>\s*</td>\s*<td width="\*" align="left" style="padding-bottom: 5px">\s*(?P<nome>[^<]*?)<',response,flags=re.DOTALL)

for parte in partes:
    #print(parte.group('autor'))
    #print(parte.group('nome'))

    dicionario2 = {
    'Categoria': parte.group('autor').replace(":&nbsp",""),
    'Nome': parte.group('nome').strip()
    }

    lista.append(dicionario2)
    

dicionario['lista'] = lista

print(dicionario)










