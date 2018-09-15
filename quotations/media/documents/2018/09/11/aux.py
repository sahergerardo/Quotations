# encoding: utf-8
from bs4 import BeautifulSoup
from googletrans import Translator
import urllib2
translator = Translator()

contador = 0


def escribir(url):
    try:
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = urllib2.Request(url, headers=hdr)
        page = urllib2.urlopen(req)
        html = BeautifulSoup(page, 'html.parser')
        nombre = html.find('h1', {'id': 'prd-name'}).getText().replace('\"', '')
        sku = html.find('table', {'class': 'prd-attributes mtl'}).find('td').getText().strip()
        descripcion = html.find('div', {'class': 'prd-description prm'}).getText().replace('\"', '').strip()
        imagen = html.find('div', {'class': 'jcarousel'}).find_all('img')
        images = "\""
        for image in imagen:
            images = images + image['src'].replace('-cart', '') + ","
        images = images[0:len(images) - 1] + '"'
        price = int(html.find('span', {'id': 'prd-price'}).getText().split(' ')[0].replace(',', ''))
        categoria = "Ropa"
        linees = sku + ",\"" + nombre + "\",,\"" + descripcion + "\"," + "1," + str(int(price)) + "," + images + ",\"" + categoria + "\""
        f = open('ropa1.txt', "a")
        f.write("\n" + linees.encode('utf-8'))
        f.close()
        print "Funciona --> " + url
        global contador
        contador = contador + 1
        print contador
    except Exception:
        print 'err0r'
        pass


def getLinks(url):
    try:
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = urllib2.Request(url, headers=hdr)
        page = urllib2.urlopen(req)
        html = BeautifulSoup(page, 'html.parser')
        links = html.find_all('a', {'class': 'itm-link'})
        for link in links:
            escribir("https://www.osom.com/" + link['href'])
    except Exception:
        print "No Funciona" + url
        pass


file = open('linksropa1.txt', 'r')
while True:
    line = file.readline()
    if not line:
        break
    veces = int(line.split(",")[1])
    base = line.split(",")[0]
    for vez in range(1, veces):
        url = base + str(vez)
        getLinks(url)
