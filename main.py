import time
import requests
import json
import psutil

# Telegram API (not entirely sure what this all does but it defines send_telegram_message so that we can use it
def send_telegram_message(message: str,
                          chat_id: str,
                          api_key: str,
                          proxy_username: str = None,
                          proxy_password: str = None,
		  proxy_url: str = None):
    responses = {}

    proxies = None
    if proxy_url is not None:
        proxies = {
            'https': f'http://{username}:{password}@{proxy_url}',
            'http': f'http://{username}:{password}@{proxy_url}'
        }
        headers = {'Content-Type': 'application/json',
                   'Proxy-Authorization': 'Basic base64'}
        data_dict = {'chat_id': chat_id,
                     'text': message,
                     'parse_mode': 'HTML',
                     'disable_notification': True}
        data = json.dumps(data_dict)
        url = f'https://api.telegram.org/bot{api_key}/sendMessage'
        response = requests.post(url,
                                 data=data,
                                 headers=headers,
                                 proxies=proxies,
                                 verify=False)
        return response

while True:
    try:
        # Get the current CPU percentage
        cpu_percentage = psutil.cpu_percent()

        # If the CPU percentage is over 5%, send a notification
        if cpu_percentage > 5.0:
            send_telegram_message(text='CPU percentage is over 5%! Current value: {}'.format(cpu_percentage))
    except Exception as e:
        # Print any exceptions that occur
        print(e)

    # Sleep for 5 seconds before checking again
    time.sleep(5)

chat_id = "5839085506:AAGyxBqxfhHG_pG9kr2PCtKBE6J4SSXkBVc"
api_key = "1560942074"

send_telegram_message("Monitoring script is up and running is up and running", chat_id, api_key)
