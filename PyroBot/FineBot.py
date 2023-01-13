from site import getusersitepackages
from pyrogram import Client, filters 

bot = Client(
    "FirstGo" ,
    api_id = 16513149,
    api_hash = "2f141cc5bbae5c37d0ed1c1b8a72c280",
    bot_token="5836107188:AAG21vssOh_3emRT52Ivi6JJXwoQ-bANkqc"
)
@bot.on_message(filters.command('start')& filters.private)

def command1(bot, message):
    bot.send_message(message.chat.id ,"Hello ")

@bot.on_message(filters.command('greet'))

def command1(bot, message):
    bot.send_message(message.chat.id ,"Hello There")

@bot.on_message(filters.command('help'))

def command1(bot, message):
    bot.send_message(message.chat.id ,"/greet  - Greets the person who sends greet   ")

@bot.on_message(filters.command('who'))

def command1(bot, message):
    message.reply_text("I am FineBot")

@bot.on_message(filters.command('myid'))

def command1(bot, message):
    
    bot.send_message(message.chat.id, str(message.chat.id))

  
print("bot is working")
bot.run()   