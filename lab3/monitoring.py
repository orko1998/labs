import requests
import json
import logging
from time import sleep

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)


def main(url):
    try:
        r = requests.get(url)
        data = json.loads(r.content)
    except Exception as err:
        logging.error("ERROR: \n%s", err)
        print("ERROR: \n", err, flush=True)
    else:
        logging.info("Сервер доступний. Час на сервері: %s", data['date'])
        logging.info("Запитувана сторінка: : %s", data['current_page'])
        logging.info("Відповідь сервера місти наступні поля:")
        for key in data.keys():
            logging.info("Ключ: %s, Значення: %s", key, data[key])

if __name__ == '__main__':
    while True:
        main("http://localhost:8000/health")
        sleep(60)

