import telebot
import wikipedia
from decouple import config

TOKEN = config('TOKEN')
BOT = telebot.TeleBot(TOKEN)

wikipedia.set_lang("ru")

@BOT.message_handler(commands=['start'])
def start(message):
    BOT.send_message(message.chat.id, 'Привет,  какую нформацию вы искали')

@BOT.message_handler(content_types=['text'])
def handle_text(message):
    BOT.send_message(message.chat.id, get_wiki(message.text))

def get_wiki(m):
    try:
        page_ = wikipedia.page(m)
        wikitext =  page_.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        
        wikitext2 = ''

        for x in wikimas:
            if (len(x.strip())>3):
                wikitext2=wikitext2 + x + '.'
        return wikimas
    except Exception:
        return 'В энцклопедии нет инвормации по вашему запросу'

BOT.polling(none_stop=True, interval=0)