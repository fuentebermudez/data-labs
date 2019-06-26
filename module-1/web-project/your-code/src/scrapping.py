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
            ley=ley.text.split(").")[0].strip()
            leyes.append(ley)
    return leyes

def get_year(ley):
    year=ley.split(",")[0][-4:]
    return year

def get_tipo_ley(ley):
    nombre_ley=ley.split(",")[0]
    len_nombre_ley=len(nombre_ley)
    tipo_ley=nombre_ley[:(len_nombre_ley-7)]
    return tipo_ley

def get_nombre_ley(ley):
    nombre_ley = ley.split(",")[0]
    return nombre_ley

url='http://www.congreso.es/portal/page/portal/Congreso/Congreso/Iniciativas/LeyesAprob?_piref73_1335447_73_1335446_1335446.next_page=/wc/busquedasLeyesAprobadas&anoLey=1979&selectLey=tituloListadoTodasLeyes'

def Extract(url,path):
    tipos_leyes=leyes = ['capaLeyOrganica', 'capaLey', 'capaRealDecretoLey', 'capaRealDecretoLeg']

    links_leyes=get_links_leyes(url)
    html_leyes=get_html_leyes(links_leyes)

    #html_leyes=get_html_leyes([r'http://www.congreso.es/portal/page/portal/Congreso/Congreso/Iniciativas/LeyesAprob?_piref73_1335447_73_1335446_1335446.next_page=/wc/busquedasLeyesAprobadas&anoLey=2019&selectLey=tituloListadoTodasLeyes'])
    leyes=[]
    for html in html_leyes:
        leyes_grupos=get_leyes_grupos(html,tipos_leyes)
        leyes_anio=get_leyes(leyes_grupos)
        leyes.append(leyes_anio)

    file=open(path + "\\leyes.txt",'a',encoding='UTF-8')
    file.write('NOMBRE_LEY;AÑO;TIPO_LEY;TITULO_LEY\n')

    for ley in leyes:
        for ley2 in ley:
            year=get_year(ley2)
            tipo_ley=get_tipo_ley(ley2)
            nombre_ley=get_nombre_ley(ley2)
            ley2=ley2.replace(";",",")
            file.write(f'{nombre_ley};{year};{tipo_ley};{ley2}\n')

