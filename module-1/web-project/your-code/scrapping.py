import requests as rq
from bs4 import BeautifulSoup

url='http://www.congreso.es/portal/page/portal/Congreso/Congreso/Iniciativas/LeyesAprob?_piref73_1335447_73_1335446_1335446.next_page=/wc/busquedasLeyesAprobadas&anoLey=1979&selectLey=tituloListadoTodasLeyes'
html=rq.get(url)

soup=BeautifulSoup(html.text,'html.parser')

years=soup.find_all(attrs={"class": "soporte_year"})

print(years)
