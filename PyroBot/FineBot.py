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
    message.reply_text("Hello There")

@bot.on_message(filters.command('help'))

def command1(bot, message):
    bot.send_message(message.chat.id ,"/greet  - Greets the person who sends greet   ")

@bot.on_message(filters.command('who'))

def command1(bot, message):
    message.reply_text("I am FineBot")

@bot.on_message(filters.command('myid'))

def command1(bot, message):
    
    bot.send_message(message.chat.id, str(message.from_user.id))

Group = "Chatswar"
Group2 = -1001881740609
Welcome_Message = "Hello there Welcome to our group"

@bot.on_message(filters.chat(Group) & filters.new_chat_members)
def welcomebot(client , message ):
    message.reply_text(Welcome_Message)


@bot.on_message(filters.text & filters.chat(Group2) & filters.private)
def delete_text(bot,message):
    thetext = message.text
    user = message.from_user.first_name 
    constr = user + " Said : \" " + thetext + " \""
    bot.delete_messages(message.chat.id, message.id)     
    bot.send_message(message.chat.id, constr )



print("bot is working")
bot.run()   