#Comanado para instalar o plugin do telegram
# pip install python-telegram-bot

#importando bibliotecas do telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler

#importando bibliotecas do SO
import os

#Função para quando o bot receber o comando start
def start(update,context):
    message = 'Seja bem vindo Guilherme'
    context.bot.send_message(chat_id=update.effective_chat.id, text = message)


def comando_invalido(update,context):
    message = 'Comando inválido'
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


token = os.getenv('TOKEN_TG')
print(token)

def main():
    print('Iniciando bot')
    updater = Updater(token = 1234, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start',start))
    #iniciar o bot
    updater.start_polling()
    updater.idle()

main()

