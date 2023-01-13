from pyrogram import Client, filters 

bot = Client(
    "FirstGo" ,
    api_id = 16513149,
    api_hash = "2f141cc5bbae5c37d0ed1c1b8a72c280",
    bot_token="5818099862:AAEJXeqJI7dApcWZXddmaNZCTw6cwvK_TLo"
)
@bot.on_message(filters.command('start')& filters.private)

def command1(bot, message):
    bot.send_message(message.chat.id ,"Hello ")

print("bot is working")
bot.run()   
