import telebot
# Chave do Bot
CHAVE_API = "5671396946:AAG3ksNePfIRhzuY1WpUd0DIzedpnM2nB1E"
# Monta a requisicao do bot
bot = telebot.TeleBot(CHAVE_API)
# Verificar todas as mensagens do bot
def verificar(mensagem):
    # Condicao para a resosta:
   #if mensagem.text = "Coe":
   #     return True
   #else:
   #    return False
    #Garante que a funcao seja verdadeira
    return True
@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.reply_to(mensagem,"Ola qual a url do produto que vc quer buscar ? ")

bot.polling()

