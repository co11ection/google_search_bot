import requests
from bs4 import BeautifulSoup, Tag
import telebot
from decouple import config
import lxml

TOKEN = config('TOKEN')
BOT = telebot.TeleBot(TOKEN)

@BOT.message_handler(commands=['start'])
def start(message):
    BOT.send_message(message.chat.id, 'Привет,  какую нформацию вы искали')

@BOT.message_handler(content_types=['text'])
def handle_text(message):
    BOT.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHxwtj7w6Ql2Fj01jQBXTuyJ-0WcraFAACYhUAAiKjwUn70vs57W5Ifi4E')
    message = BOT.send_message(message.chat.id, search_google(message.text))

def search_google(message):
    URL = f'https://www.google.com/search?q={message}'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0, win64; x64) AppleWebKit/537.36 (KHTML., like Gecko) Chrome/68.0.3029.10 Safari/537.3"}
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    cards = soup.find_all('div', class_ = 'yuRUbf')
    data = []
    card: Tag
    for card in cards:
        try:
            title = card.find("h3").text
            link = card.find('a').get("href")
            data.append(f"{title} <---> {link}\n")
        except:
            pass
        
    result = '\n'.join(data)
    if result:
        return result
    return 'Информаия не доступна'


BOT.polling(none_stop=True, interval=0)