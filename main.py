from bs4 import BeautifulSoup
import requests
import json
#from keep_alive import keep_alive
import telebot
telegram_destino = '-123456789'  #coloque o ID do telegram no lugar dos zeros.
CHAVE_API = "123456789:ABCdefGH12ABCDEF-x"  #coloque a chave API
bot = telebot.TeleBot(CHAVE_API)
bot.config['api_key'] = CHAVE_API
from time import sleep
total = 0
while True:
    def json_from_url(url):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        data_json = soup.find(id='initial-data').get('data-json')
        return json.loads(data_json)


    url_produtos="https://ba.olx.com.br/grande-salvador/autos-e-pecas/carros-vans-e-utilitarios/renault/clio?rs=30&sf=1"
    # Pega a lista de produtos da página
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
            descricao = anuncio.get('subject')
            url = anuncio.get('url')
            precin = anuncio.get('price')
            arq = open("dados_anuncios.txt")
            linhas = arq.readlines()
            if url + '\n' in linhas:
                print(f'Título do anúncio: {descricao}')
                print('ANÚNCIO JÁ VISTO! - Aguardando novos anúncios!')
            else:
                print('ANÚNCIO NOVO:')
                with open('dados_anuncios.txt', 'a') as arquivo:
                    arquivo.write(url + '\n')
                print('Título do anúncio:',descricao)
                print('URL do anúncio:',url)
                mostra_dados_do_anuncio(url)
                lista.append(url)
                total += 1
                carro = (f'Descricao do produto: {descricao}\n'
                         f'URL do produto: {url}\n'
                         f'Preço: {precin}\n'
                         f'Total: {total}')
                print(f'Total de anúncios enviados: {total}')
                bot.send_message(telegram_destino, carro)
            if len(linhas) > 1000:
                with open('dados_anuncios.txt', 'w') as arquivo:
                    arquivo.write(url + '\n')
            sleep(2)
#keep_alive()
