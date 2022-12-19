import time
import telegram
import psutil

# Telegram API
bot = telegram.Bot(token='5839085506:AAGyxBqxfhHG_pG9kr2PCtKBE6J4SSXkBVc')

# Chat ID (This is so that we send it to the right chat as one API can have multiple chats)
chat_id = 1560942074

while True:
    try:
        # Get the current CPU percentage
        cpu_percentage = psutil.cpu_percent()

        # Print the current CPU percentage
        print("Current CPU percentage: {}".format(cpu_percentage))

        # If the CPU percentage is over 5%, send a notification
        if cpu_percentage > 5.0:
            bot.send_message(chat_id=chat_id, text='CPU percentage is over 5%! Current value: {}'.format(cpu_percentage))
    except Exception as e:
        # Print any exceptions that occur
        print(e)

    # Sleep for 5 seconds before checking again
    time.sleep(5)
