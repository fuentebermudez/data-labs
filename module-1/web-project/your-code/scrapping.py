import requests as rq
from bs4 import BeautifulSoup

url='http://www.congreso.es/portal/page/portal/Congreso/Congreso/Iniciativas/LeyesAprob?_piref73_1335447_73_1335446_1335446.next_page=/wc/busquedasLeyesAprobadas&anoLey=1979&selectLey=tituloListadoTodasLeyes'
url_todas_leyes='&selectLey=tituloListadoTodasLeyes'
html=rq.get(url)

soup=BeautifulSoup(html.text,'html.parser')

years=soup.find_all(attrs={"class": "soporte_year"})

links=[year.find_all('a') for year in years]

links_leyes=[]
for link in links[0]:
    href=link.get('href')
    href=href + url_todas_leyes
    links_leyes.append(href)

leyes=['capaLeyOrganica','capaLey','capaRealDecretoLey','capaRealDecretoLeg']
leyes_titulos=[]
for link in links_leyes:
    print(link)
    for grupo in leyes:
        html=rq.get(link)
        soup = BeautifulSoup(html.text, 'html.parser')
        leyes_grupo=soup.find_all('div',{'id':grupo})
        for ley_tipo in leyes_grupo:
            ley=ley_tipo.find('li')
            print(ley.text.split(").")[0])