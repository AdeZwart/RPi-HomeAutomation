import os
import random
import telepot
import config
from time import sleep, localtime, strftime

# Read the API token from the config file
TOKEN = config.getConfigSetting('TelegramBot','Token')
# Read the allowed chat id's from the config file
CHATIDS = config.getConfigSetting('TelegramBot','ChatIds').split(',')

IMG_NAME='none'

CODEROOT = '/home/pi/Code'
IMGROOT = CODEROOT + '/img'
TXTROOT = CODEROOT + '/txt'

#Reference:http://unicode.org/emoji/charts/full-emoji-list.html
grinningcat = u'\U0001F63A' #ginning cat face with smiling eyes

def send_image(chat_id,bool):
    img_list=os.listdir(IMGROOT+'/static')
    img_name=img_list[random.randint(0,len(img_list)-1)]
    hide_keyboard={'hide_keyboard':True}
    if bool:
        bot.sendPhoto(chat_id,open(IMGROOT+'/static/'+img_name,'rb'),caption='',reply_markup=hide_keyboard)
        return

def handle(msg):
    chat_id=msg['chat']['id']

    if chat_id in CHATIDS:
        print(str(chat_id)+': '+msg['chat']['first_name']+' '+msg['chat']['last_name'])
        return
    
    message=msg['text']
    random_line=random.choice(open(TXTROOT+'/test.txt').readlines())+grinningcat    
    
    if message == '/linefeed@platocatbot' or message == '/linefeed':
        bot.sendMessage(chat_id, random_line)
    elif message == '/meme@platocatbot' or message == '/meme':
        send_image(chat_id,True)
    else:
        bot.sendMessage(chat_id, "Unknown command")

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

while 1:
    sleep(10)
