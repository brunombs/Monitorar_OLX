from bs4 import BeautifulSoup
import requests
import json
import telebot
telegram_destino = '-123456789'  #coloque o ID do telegram no lugar dos zeros.
CHAVE_API = "123456789:ABCdefGH12ABCDEF-x"  #coloque a chave API
bot = telebot.TeleBot(CHAVE_API)
bot.config['api_key'] = CHAVE_API
from time import sleep
lista = list()
total = 0
while True:
    def json_from_url(url):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        data_json = soup.find(id='initial-data').get('data-json')
        return json.loads(data_json)


    url_produtos="https://ba.olx.com.br/grande-salvador/autos-e-pecas/carros-vans-e-utilitarios/renault/clio?rs=30"
    # Pega a lista de produtos da área de eletrônicos
    data = json_from_url(url_produtos)
    def mostra_dados_do_anuncio(url):
        data = json_from_url(url)
        descricao = data['ad']['body']
        phone = data['ad']['phone']['phone']
        user = data['ad']['user']['name']
        preco = data['ad']['price']
        Local = data['ad']['location']['municipality']
        zone = data['ad']['location']['zone']
        UF = data['ad']['location']['uf']
        print('Local=',UF,',',Local,',',zone)
        print('Vendedor=',user)
        print('Telefone=',phone)
        print('Descrição=',descricao)
        print('preco=',preco)

    # Entra em cada anúncio e mostra o telefone
    adList = data['listingProps']['adList']
    for anuncio in adList:
        subject = anuncio.get('subject')
        if subject:
            print('Aguardando novos anúncios!')
            descricao = anuncio.get('subject')
            url = anuncio.get('url')
            if url in lista:
                break
            print('Descricao do produto:',descricao)
            print('URL do produto=',url)
            mostra_dados_do_anuncio(url)
            lista.append(url)
            total += 1
            anuncio = (f'Descricao do produto: {descricao}\n'
                     f'URL do produto: {url}\n'
                     f'Total: {total}')
            print(f'Total de anúncios enviados: {total}')
            bot.send_message(telegram_destino, anuncio)
            sleep(60)
