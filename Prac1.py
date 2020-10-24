import telepot
token = '1392238011:AAFnrG1Ca91HYu-qzNwaXJ-1lrFjOhBnEQE'
TelegramBot = telepot.Bot(token)
print (TelegramBot.getMe())
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == 'text':
        bot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))
TelegramBot.message_loop(handle)
