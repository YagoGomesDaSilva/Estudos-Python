import re
import requests
from urllib.error import URLError, HTTPError 

try:
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}
    url_dolar = requests.get('https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar&oq=cota%C3%A7%C3%A3o&aqs=chrome.0.0i131i433i512j69i57j0i131i433i512l5j0i433i512j0i512j0i131i433i512.3993j1j15&sourceid=chrome&ie=UTF-8',headers=headers)
   
    html_dolar = url_dolar.text
    
except HTTPError as e:
    print(e.status, e.reason)

except URLError as e:
    print(e.reason)


#<span class="DFlfde SwHCTb" data-precision="2" data-value="5.1594">5,16</span>

re_dolar = re.search(r'<span class="DFlfde SwHCTb" data-precision="2" data-value="(?P<dolar>.*?)">\d,\d{2}</span>',html_dolar,flags=re.DOTALL)

valor_dolar = re_dolar.group("dolar")

#print(html_dolar)
#print(re_dolar)
print(valor_dolar)





