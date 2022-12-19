import time
import psutil
import telegram

#chat_id = "1560942074"
#api_key = "5839085506:AAGyxBqxfhHG_pG9kr2PCtKBE6J4SSXkBVc"

bot = telegram.Bot(token="5839085506:AAGyxBqxfhHG_pG9kr2PCtKBE6J4SSXkBVc")

while True:
    try:
        # Get the current CPU percentage
        cpu_percentage = psutil.cpu_percent()

        # Print the CPU percentage
        print('System CPU load is {} %'.format(cpu_percentage))

        # If the CPU percentage is over 1%, send a notification
        if cpu_percentage > 0.5:
            bot.sendMessage(chat_id=1560942074, text="CPU percentage is over 1%! Current value: {}".format(cpu_percentage))
            #the break can be removed if we want to continuously run the script
            break

        # Sleep for 5 second before checking again
        time.sleep(5)
    except Exception as e:
        # Print any exceptions that occur
        print(e)
	
