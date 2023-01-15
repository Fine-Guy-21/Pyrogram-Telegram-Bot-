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
    bot.send_message(message.chat.id ,f"Welcome {message.chat.first_name} ")

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


@bot.on_message(filters.chat(Group) & filters.new_chat_members)
def welcomebot(client , message ):
   # newmembername = ""
    message.reply_text("Hello there Welcome to our Entertainment Group ")


@bot.on_message(filters.command('rmv') & filters.chat(Group2))
def command1(bot,message):
    if(message.reply_to_message):    
        owner = message.reply_to_message.text.split("Said")[0]
        id = message.reply_to_message.id
        sender = "@" + message.from_user.username + " "
        if (owner == sender) :
            bot.delete_messages(message.chat.id,message.id)
            bot.delete_messages(message.chat.id, id )
            bot.send_message(message.chat.id, " Deleted " )
        else :
#            bot.send_message(message.chat.id, f" {owner} and {sender} " )
            message.reply_text(message.chat.id, " It's not your message, Go find your Message🤨" )
            
    else :
        bot.delete_messages(message.chat.id,message.id)
        bot.send_message(message.chat.id,"You must reply to a text ")



@bot.on_message(filters.text & filters.chat(Group2))
def report_text(bot,message):
    thetext = message.text
    user ="@" + message.from_user.username 
    constr = user + " Said : \" " + thetext + " \""
    

    if(message.reply_to_message):
        user2 = message.reply_to_message.text.split("Said")[0]
        constr2 = user + " Said : \" " + thetext + " \" \n To : " + user2
        bot.delete_messages(message.chat.id, message.id)     
        bot.send_message(message.chat.id, text = constr2, reply_to_message_id = message.reply_to_message.id)
    else :
        bot.delete_messages(message.chat.id, message.id)
        bot.send_message(message.chat.id, constr )

print("bot is working")
bot.run()   