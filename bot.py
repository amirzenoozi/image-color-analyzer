from enum import unique
from io import StringIO
from script.utils import save_file
from datetime import datetime
from dotenv import load_dotenv
from script.analyzer import preprocess, analyze

import telebot
import os
import cv2

config = load_dotenv(".env")
app = telebot.TeleBot(os.getenv('BOT_TOKEN'))

@app.message_handler(commands=['start'])
def say_hello(messages):
    app.send_message(messages.chat.id, f'Wellcome Dear {messages.from_user.first_name}🌹')
    app.send_message(messages.chat.id, f'Here you can Analyze Your Image Based on Their Colors')
    app.send_message(messages.chat.id, f'Now send me the photo so I can tell you 😉')

@app.message_handler(content_types=['photo'])
def photo(message):
    file_info = app.get_file(message.photo[-1].file_id)
    downloaded_file = app.download_file(file_info.file_path)

    if not os.path.exists("upload"):
            os.mkdir("upload")

    if not os.path.exists("upload/telegram"):
            os.makedirs("upload/telegram")

    base_filename = file_info.file_path.split("/")
    file_parts = base_filename[1].split(".")
    date = str(datetime.timestamp(datetime.now())).replace(".", "-")
    file_name = f'{os.getcwd()}\\upload\\telegram\\{file_parts[0].replace(" ", "-")}_telebot_{date}.{file_parts[1]}'
    save_file(file_name, downloaded_file)

    
    print("Now We Are Proccessing...")
    app.send_message(message.chat.id, f'🧑🏻‍💻 Now We Are Proccessing...')

    img = cv2.imread(file_name)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    modified_image = preprocess(img)
    _, color = analyze(modified_image, args=None)
    app.reply_to(message, f'``` \n- {color[0]} \n- {color[1]} \n- {color[2]} \n- {color[3]} \n- {color[4]} \n```', parse_mode='Markdown')

if __name__ == '__main__':
    print("We Are Starting The Bot...")
    app.infinity_polling()
