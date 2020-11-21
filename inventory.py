from lxml import etree
import requests
from bs4 import BeautifulSoup
from time import sleep
import logging
from twilio.rest import Client

ZIP = "23238"
SKU = "207-43-0001"
RANGE = "25"
WAIT = 10
PHONE = "+1<your-phone>"
TRIAL_PHONE = "+1<your-trial-phone>"
TWILIO_SID = "<your-twilio-sid>"
TWILIO_TOKEN = "<your-twilio-token>"

def main():
    logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.INFO, datefmt='%m/%d/%Y %I:%M:%S %p')

    while True:
        inventory = check_inventory()
        if len(inventory) > 0:
            notify(inventory)
        else:
            logging.info("no stock found")
        sleep(WAIT)
       
def check_inventory():
    available = []
    url = f"https://popfindr.com/results?pid={SKU}&zip={ZIP}&range={RANGE}&webpage=target"
    logging.info(f"checking: {url}")
    r = requests.get(url)
    html_string = r.text
    soup = BeautifulSoup(html_string, 'lxml')
    try:
        table = soup.find_all('table')[1]
    except:
	    logging.info("site error, no inventory table returned")
	    return available

    for tr in table.find_all('tr')[1:]:
        td = [th.get_text(strip=True) for th in tr.find_all('th')]
        if int(td[2]) > 0:
            available.append(td)
    return available

def notify(inventory):
    print("STOCK FOUND:")
    for item in inventory:
        print(item)

    account_sid = TWILIO_SID
    auth_token = TWILIO_TOKEN
    client = Client(account_sid, auth_token)
    try:
        message = client.messages \
            .create(
                    body="PS5 STOCK FOUND.",
                    from_=TRIAL_PHONE,
                    to=PHONE
                )
    except:
        logging.info("couldn't send twilio message")

if __name__ == "__main__":
    main()
