import telebot
import parser


bot = telebot.TeleBot('837415741:AAF27fEgvfcTdOEQGlFM24VoujPO4A6H2Iw')
news = parser.main() # v etu peremennuy vash metod pixnite pls


@bot.message_handler(commands=['start', 'help'])
def main(message):
    for k,v in news.items():
        bot.send_message(message.chat.id, f'{k}) {v}')

@bot.message_handler(content_types=["text"])
def choose_news(message):
    if message.text.lower() == 'finish':
        bot.send_message(message.chat.id, 'good bye')
    else:
        bot.send_message(message.chat.id, parser.title(news[int(message.text)]))



bot.polling()