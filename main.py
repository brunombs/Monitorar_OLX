#!/usr/bin/env python3
# WebScraping para OLX em Python3
# Vinicius Reis
from bs4 import BeautifulSoup
import requests
import json

def json_from_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    data_json = soup.find(id='initial-data').get('data-json')
    #print(data_json)
    return json.loads(data_json)
#Teste

# Função que recebe url do anúncio
# e mostra nome do vendedor, telefone,
# descrição do produto e preço
#url_produtos='https://rj.olx.com.br/rio-de-janeiro-e-regiao/autos-e-pecas/motos/suzuki/boulevard?pe=30000&ps=10000'
url_produtos="https://rj.olx.com.br/rio-de-janeiro-e-regiao?q=ps5"
# Pega a lista de produtos da área de eletrônicos
data = json_from_url(url_produtos)
def mostra_dados_do_anuncio(url):
    data = json_from_url(url)
    descricao = data['ad']['body']
    phone =  data['ad']['phone']['phone']
    user = data['ad']['user']['name']
    preco = data['ad']['price']
    Local = data['ad']['location']['municipality']
    zone = data['ad']['location']['zone']
    UF =  data ['ad']['location']['uf']
    print('Local= ',UF,',',Local,',',zone)
    print('Vendedor=',user)
    print('Telefone=',phone)
    print('Descrição=',descricao)
    print('preco=',preco)

# Entra em cada anúncio e mostra o telefone
adList = data['listingProps']['adList']
for anuncio in adList:
    subject = anuncio.get('subject')
    if subject:
        print('------------------------')
        descricao = anuncio.get('subject')
        url = anuncio.get('url')
        print('Descricao do produto:',descricao)
        print('URL do produto=',url)
        mostra_dados_do_anuncio(url)
