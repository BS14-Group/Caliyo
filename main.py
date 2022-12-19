import time
import telegram
import psutil

# Telegram API
bot = telegram.Bot(token='5839085506:AAGyxBqxfhHG_pG9kr2PCtKBE6J4SSXkBVc')

# Chat ID (This is so that we send it to the right chat as one API can have multiple chats)
chat_id = 1560942074

while True:
    # Get the current CPU percentage
    cpu_percentage = psutil.cpu_percent()

    # If the CPU percentage is over 5%, send a notification
    if cpu_percentage > 5.0:
        bot.send_message(chat_id=chat_id, text='CPU percentage is over 5%! Current value: {}'.format(cpu_percentage))
    
    # Sleep for 10 Sec before checking again
    time.sleep(10)
