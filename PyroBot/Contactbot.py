import pyrogram
from pyrogram import Client , filters

bot = Client(
    "FirstGo2" ,
    api_id = 16513149,
    api_hash = "2f141cc5bbae5c37d0ed1c1b8a72c280",
    bot_token="5914131615:AAG0p2EVNr26tEC4mVAzF9qQ4SmjZ9zounA"
)
Group_id = -1001698691465

@bot.on_message(filters.text & filters.private)
def messagesender(bot,message):
    text = message.text
    message.forward(Group_id)

@bot.on_message(filters.chat(Group_id))
def replyanswer(bot,message):
    text = message.text
    if message.reply_to_message :
        Customer_id = message.reply_to_message.from_user.id
        bot.send_message( chat_id = Customer_id, text=text)

print("Bot is working! ")
bot.run()
