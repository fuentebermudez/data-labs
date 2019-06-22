import requests as rq
from bs4 import BeautifulSoup


def get_links_leyes(url_parlamento):
    url_todas_leyes = '&selectLey=tituloListadoTodasLeyes'

    html = rq.get(url_parlamento)
    soup=BeautifulSoup(html.text,'html.parser')
    years=soup.find_all(attrs={"class": "soporte_year"})

    links=[year.find_all('a') for year in years]

    links_leyes=[]
    for link in links[0]:
        href=link.get('href')
        href=href + url_todas_leyes
        links_leyes.append(href)
    return links_leyes

def get_html_leyes(links):

    html_leyes = []
    for link in links:
        print(link)
        html = rq.get(link)
        #soup = BeautifulSoup(html.text, 'html.parser')
        html_leyes.append(html.text)
    return html_leyes

def get_leyes_grupos(html_ley_anio,tipos_leyes):
    soup=BeautifulSoup(html_ley_anio,'html.parser')
    leyes_tipo=[]
    for grupo in tipos_leyes:
        leyes_grupo = soup.find_all('div', {'id': grupo})
        leyes_tipo.append(leyes_grupo)
    return leyes_tipo

def get_leyes(leyes_grupos):
    leyes=[]

    for grupo in leyes_grupos:
        leyes_html = grupo[0].find_all('li')
        for ley in leyes_html:
            ley=ley.text.split(").")[0]
            leyes.append(ley)
    return leyes

url='http://www.congreso.es/portal/page/portal/Congreso/Congreso/Iniciativas/LeyesAprob?_piref73_1335447_73_1335446_1335446.next_page=/wc/busquedasLeyesAprobadas&anoLey=1979&selectLey=tituloListadoTodasLeyes'
tipos_leyes=leyes = ['capaLeyOrganica', 'capaLey', 'capaRealDecretoLey', 'capaRealDecretoLeg']

links_leyes=get_links_leyes(url)
html_leyes=get_html_leyes(links_leyes)

#html_leyes=get_html_leyes([r'http://www.congreso.es/portal/page/portal/Congreso/Congreso/Iniciativas/LeyesAprob?_piref73_1335447_73_1335446_1335446.next_page=/wc/busquedasLeyesAprobadas&anoLey=2019&selectLey=tituloListadoTodasLeyes'])
leyes=[]
for html in html_leyes:
    leyes_grupos=get_leyes_grupos(html,tipos_leyes)
    leyes_anio=get_leyes(leyes_grupos)
    leyes.append(leyes_anio)

for ley in leyes:
    for ley2 in ley:
        print(ley2)

