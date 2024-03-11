import requests
import time

TOKEN = 'TOKEN'
URL = 'https://api.telegram.org/bot'


def get_updates(offset=0):
    result = requests.get(f'{URL}{TOKEN}/getUpdates?offset={offset}').json()
    return result['result']


def send_message(chat_id, text):
    requests.get(f'{URL}{TOKEN}/sendMessage?chat_id={chat_id}&text={text}&parse_mode=html&reply_markup={{"keyboard":+[[{{"text":+"/start"}},+{{"text":+"/stop"}},+{{"text":+"/status"}}],+[{{"text":+"/help"}}]],+"resize_keyboard":+true}}')


def run():
    update_id = get_updates()[-1]['update_id'] # Присваиваем ID последнего отправленного сообщения боту
    while True:
        time.sleep(1)
        messages = get_updates(update_id) # Получаем обновления
        for message in messages:
            # Если в обновлении есть ID больше чем ID последнего сообщения, значит пришло новое сообщение
            if update_id < message['update_id']:
                update_id = message['update_id'] # Присваиваем ID последнего отправленного сообщения боту
                print(f"ID пользователя: {message['message']['chat']['id']}, Сообщение: {message['message']['text']}")
                send_message(message['message']['chat']['id'], "<b><i>" + message['message']['text'] + '</i></b>')



if __name__ == '__main__':
    run()
