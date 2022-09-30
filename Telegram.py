import telebot
# Chave do Bot
CHAVE_API = "5671396946:AAG3ksNePfIRhzuY1WpUd0DIzedpnM2nB1E"
# Monta a requisicao do bot
bot = telebot.TeleBot(CHAVE_API)
# Verificar todas as mensagens do bot

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    print(mensagem)
    #pass
    #Responde a mensagem
    #bot.reply_to(mensagem,"Esta opção inda está em contrução")
    #Envia mensagem ao usuario
    bot.send_message(mensagem.chat.id,"Esta opção inda está em contrução")
@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.reply_to(mensagem,"Esta opção inda está em contrução")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    print(mensagem)
    bot.reply_to(mensagem,"Esta opção inda está em contrução")



############################################
def verificar(mensagem):
#Condicao para a resosta:
   #if mensagem.text = "Coe":
   #     return True
   #else:
   #    return False
#Garante que a funcao seja verdadeira
    return True
#Cria a função responsavel por coletar todas as mensagens.
@bot.message_handler(func=verificar)
def responder(mensagem):
    opcoes = """
    Ola, Como Vai?
    Qual a url do produto que vc quer buscar ?
    /opcao1 :Inserir_URL
    /opcao2 :Não defindo
    /opcao3 :Não defindo
Se você não clicar em uma opção nada irá ocorrer.. """
    bot.reply_to(mensagem,opcoes)
bot.polling()
##################
