import pyrogram
from site import getusersitepackages
from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from gtts import gTTS
import time

bot = Client(
    "FirstGo" ,
    api_id = 16513149,
    api_hash = "2f141cc5bbae5c37d0ed1c1b8a72c280",
    bot_token="5836107188:AAG21vssOh_3emRT52Ivi6JJXwoQ-bANkqc"
)
Inlinebuttons = [
    [
     InlineKeyboardButton('🔈 Channel',url='https://t.me/Ready_players_Please'),
     InlineKeyboardButton('👥 Group', url='https://t.me/+EcySgpoTodk1ZTk0')
    ],
    [InlineKeyboardButton('🧑‍💻Contact',url='https://t.me/fine_guy_21')]
]

@bot.on_message(filters.command('start'))
def command1(bot, message):
        text = f"Hello There {message.from_user.first_name}"
        reply_markup = InlineKeyboardMarkup(Inlinebuttons)
        bot.send_chat_action(message.chat.id,enums.ChatAction.TYPING)
        message.reply(text = text,reply_markup = reply_markup,disable_web_page_preview = True)

@bot.on_message(filters.command('help'))
def command1(bot, message):
    bot.send_chat_action(message.chat.id ,enums.ChatAction.TYPING)
    bot.send_message(message.chat.id ,
        text = """
             \n<b>/start</b>(private) - \" Starting The Bot \"      
             \n<b>/Getid</b> - \" get your telegram id , reply to get other people id \"
             \n<b>/bully</b> - \" bully a replied user(slap,kick,mock) \"
             \n<b>/speak</b> - \" reply a text to get text to speech feature \"
             \n<b>/animate</b> - \" reply to a text and it will start writing out the text letters one by one \"
              \nFor any inquiry  \ncontact - @Fine_Guy_21 
        
               """
    )

@bot.on_message(filters.command('Getid')&filters.command('getid'))
def command1(bot, message):
    bot.send_chat_action(message.chat.id ,enums.ChatAction.TYPING)
    if(message.reply_to_message):
     bot.send_message(message.chat.id, f"The Id of {message.reply_to_message.from_user.first_name} is : " + str(message.reply_to_message.from_user.id ))
    else:
     bot.send_message(message.chat.id, f"The Id of {message.from_user.first_name} is : "+str(message.from_user.id))

@bot.on_message(filters.command('bully') & filters.command('Bully'))
def slap(bot,message):
    bot.send_chat_action(message.chat.id ,enums.ChatAction.TYPING)
    user = message.from_user.first_name
    if (message.reply_to_message):
        if (message.reply_to_message.from_user.id == message.from_user.id ):
            message.reply ("Self harming is dangerous. 🧐 ")
        else:
            user2 = message.reply_to_message.from_user.first_name
            bot.send_message(message.chat.id,user + " Lay a hand on " + user2 + "'s face")
    else:
        mes = bot.send_message(message.chat.id,"Either reply to some one or i'll slap you")
        time.sleep(5)
        bot.edit_message_text(chat_id=message.chat.id,message_id=mes.id,text=f"Hey {user},Take this 👊")
        bot.send_message(message.chat.id,"👊")


@bot.on_message(filters.command('speak') & filters.command('Speak'))
def speak(bot,message):
    if (message.reply_to_message) :
        if(message.reply_to_message.text):
            text=message.reply_to_message.text
            voice=gTTS(text=text,lang='en')
            bot.send_chat_action(message.chat.id ,enums.ChatAction.RECORD_AUDIO)
            text2 = message.reply("Generating audio... please wait! ")
            voice.save("voice.mp3")
            bot.delete_messages(message.chat.id,text2.id)
            bot.send_chat_action(message.chat.id ,enums.ChatAction.UPLOAD_AUDIO)
            bot.send_voice(message.chat.id,"voice.mp3")
        else:
            message.reply("It only works on <b> Texts </b>")
    else :
        message.reply(" <b>Reply</b> the <b>text</b>")
        


Group = "Chatswar"
Group2 = -1001881740609
Group3 = -1001673884695


@bot.on_message(filters.command('animate') & filters.command('Bully'))
def stringfun(client , message):
    bot.send_chat_action(message.chat.id ,enums.ChatAction.TYPING)
    if(message.reply_to_message) :
        text = message.reply_to_message.text
        if len(text) <= 12 : 
            mes = bot.send_message(message.chat.id, text)
            text2 = " "
            
            for x in text:
                if x == " " :
                    text2 = text2 + "_"
                else :
                    text2 = text2 + x
                bot.edit_message_text(chat_id = message.chat.id, message_id=mes.id, text = text2)
                time.sleep(1)  
        else :
            message.reply("The text Should not have morethan 12 letters ")  
    else:
        bot.send_message(message.chat.id," Reply to a message" )

@bot.on_message(filters.chat(Group) & filters.new_chat_members)
def welcomebot(client , message ):
    message.reply_text("Hello there Welcome to our Entertainment Group ")


@bot.on_message(filters.command('rmv') & filters.chat(Group))
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
   
@bot.on_message(filters.text & filters.chat(Group))
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