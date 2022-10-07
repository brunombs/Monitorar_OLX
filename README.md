<img alt="OLX Monitor" src="https://github.com/carmolim/olx-monitor/blob/main/assets/olx-monitor-banner.png"></img>

# OLX Monitor

Diariamente eu procurava por um produto específico na OLX, tinha até adicionado na barra de favoritos, resolvi buscar por uma alternativa a esse esforço repetitivo e pensei no BOT para monitorar a OLX.
Esse script serve para buscar todos os anúncios de uma página e enviar todos os anúncios para o Telegram através de um BOT. O conteúdo da mensagem irá conter o link do anúncio, descrição, preço e telefone (se houver)!

## Instalação e configuração

Para utilizar esse script você precisa ter o python devidamente instalado, ter uma conta no [Telegram](https://telegram.org/), e idealmente um computador que fique ligado 24/7 para executar o script. (É possível fazer esse processo em nuvem de forma gratuita, pode ser que mais pra frente eu ensine aqui como faz)

Se você já está familiarizado com a API do Telegram e já mexeu bom bots segue um passo-a-passo mais enxuto:

1. Clonar ou fazer download do repositório `git clone https://github.com/brunombs/Monitorar-OLX.git`
2. Incluir a URL que você quer que seja monitorada no arquivo `main.py`
3. Incluir o ID do Telegram e a Chave API no arquivo `main.py`
5. Executar o script
6. Acompanhar o andamento do script
7. Se correu tudo certo, você receberá no Telegram todos os anúncios da página existente naquele momento e quando ele rodar todos os anúncios existentes, irá notificar a cada novo anúncio que surgir.

### Configuração do Telegram

Para você poder receber as notificações pelo Telegram você precisa ter algumas coisas, um bot que terá um token e um grupo que tenho bot com que você irá criar como participante.

#### Criar seu bot

Para conseguir o seu token você precisa criar o seu próprio bot. Eu pretendo fazer um tutorial, mas enquanto isso você pode usar esse [aqui](https://www.youtube.com/watch?v=4u9JQR0-Bgc&feature=youtu.be&t=88). O vídeo é longo mas você só precisa assistir até: 3:24. Com esse vídeo você irá conseguir obter o seu token.

#### Descobrindo seu CHAT ID

Depois de criar o seu bot, crie um grupo e convite o seu bot que você acabou de criar e també um outro bot, o `@idbot`, ele vai te ajudar a descobrir o `CHAT_ID` que precisamos para enviar a notificação. 

Depois de incluir o no grupo, basta digitar `/getgroupid@myidbot` e bot irá responder com o ID do chat. 

#### Editando seu ambiênte

Dentro do repositório tem um arquivo chamado `example.env`, você precisa renomea-lo para apenas `.env` e preencher as informações que você acabou de pegar. 

| Variável          | Exemplo                                |
| ----------------- | -------------------------------------- |
| TELEGRAM_TOKEN    | Token do seu bot gerado pelo BotFather |
| TELEGRAM_CHAT\_ID | ID do seu chat                         |

### O que deve ser monitorado?

Eu não sei o que você está procurando no OLX, mas você precisa dizer para o script. A forma mais fácil de fazer isso é entrar no site do OLX, fazer uma busca, colocar os filtros que você acha necessário e copiar o endereço que o OLX vai criar.

Você pode utilizar uma ou mais pesquisas, basta apenas incluir as `URLs` no arquivo `main.py` na linha #21

#### Exemplo


```
    url_produtos="https://ba.olx.com.br/grande-salvador/autos-e-pecas/carros-vans-e-utilitarios/renault/clio?rs=30"
```


#### Dica

Quando mais específica sua busca for mais eficiente o script será, se você só buscar por iPhone, no Brasil todo, você vai receber muitas notificações por dia, não vai ser muito legal. Sugiro que coloque apenas na sua cidade, com filtro de preço e modelo. (ex: iPhone 11, na cidade de Salvador, com preço entre 2000 e 3000 e MUITO importante o filtro de ordenar pelos anúncios "MAIS RECENTES", por padrão a OLX coloca os "MAIS RELEVANTES")


## Funcionamento

O funcionamamento do script é simples. Ele percorre um `array` de `URLs` copiadas do OLX, que já contém os filtros de preço mínimo, máximo e etc, encontra os anúncios dentro dessa página e envia uma notificação para um BOT no Telegram. 


## Considerações

- Esse script foi testado com a versão brasileira do OLX, na OLX de outros países não sei se irá funcionar, não foi testado.

- No momento o script só puxa busca as informações presentes na primeira página de resultados. Num futuro penso em fazer uma alteração no `scrapper`para percorrer todas as páginas de resultado.


## Créditos do projeto para:
[Reisvmr](https://github.com/Reisvmr/Busca_OLX) que criou o script da busca na olx!
[Carmolin](https://github.com/carmolim/olx-monitor) que criou esse read.me, usei ele como base para o meu!


Eu aprimorei o script do Reismvr introduzindo o Telegram de forma funcional e a função de notificar a cada novo anúncio que surgir.
