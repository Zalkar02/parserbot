import telebot 
#import 
bot = telebot.TeleBot('837415741:AAF27fEgvfcTdOEQGlFM24VoujPO4A6H2Iw')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text == 'hi':
   		bot.send_message(message.from_user.id, 'hello')
  
	

bot.polling()


