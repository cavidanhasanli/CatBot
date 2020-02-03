import re
from flask import Flask, request
import telegram
from telebot.credentials import bot_token, bot_user_name, URL

global bot
global TOKEN

TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)


@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id


    text = update.message.text.encode('utf-8').decode()

    if text == "salam":

        bot_welcome = """
        Aleykum Salam
       """

        bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)

    if text == "kredit":

        bot_name_surname = """
            zehmet olmasa ad ve soyadinizi qeyd edin.Qeyd: Ad ve soyad
            biri birinden bir space arali olsun.
        """
        bot.sendMessage(chat_id=chat_id, text=bot_name_surname, reply_to_message_id=msg_id)

    splt = text.split(' ')
    if len(splt) >= 2:

        bot_question = """
            sizin emek haqqi kartiniz ve yaxudda pensiya kartiniz varmi?
            beli ve yaxud xeyir cavabi verin zehmet olmasa.
        """
        bot.sendMessage(chat_id=chat_id, text=bot_question, reply_to_message_id=msg_id)

    if text == "beli":

            bot_yes = """
                Zehmet olmasa telefon nomrenizi qeyd edin.Numune: +994555555555
            """
            bot.sendMessage(chat_id=chat_id, text=bot_yes, reply_to_message_id=msg_id)

    if type(text) == int or len(text) == 11:
        bot_message = """
            Isteyiniz qeyde alindi tesekkurler
        """
        bot.sendMessage(chat_id=chat_id, text=bot_message, reply_to_message_id=msg_id)

    # if type(text) != int:
    #     bot_message = """
    #         Zehmet olmasa duzgun cavab verin.
    #     """
    #     bot.sendMessage(chat_id=chat_id, text=bot_message, reply_to_message_id=msg_id)
    if text == "xeyir":

        bot_no = """
            Tessufki siz bizden kredit ala bilmersiniz.
        """
        bot.sendMessage(chat_id=chat_id, text=bot_no, reply_to_message_id=msg_id)

    # else:
    #     try:
    #         # clear the message we got from any non alphabets
    #         text = re.sub(r"\W", "_", text)
    #         # create the api link for the avatar based on http://avatars.adorable.io/
    #         url = "https://api.adorable.io/avatars/285/{}.png".format(text.strip())
    #         # reply with a photo to the name the user sent,
    #         # note that you can send photos by url and telegram will fetch it for you
    #         bot.sendPhoto(chat_id=chat_id, photo=url, reply_to_message_id=msg_id)
    #     except Exception:
    #         # if things went wrong
    #         bot.sendMessage(chat_id=chat_id,
    #                         text="There was a problem in the name you used, please enter different name",
    #                         reply_to_message_id=msg_id)

    return 'ok'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/')
def index():
    return '.'


if __name__ == '__main__':
    app.run(threaded=True)
