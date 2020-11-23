from lxml import etree
import requests
from bs4 import BeautifulSoup
from time import sleep
import logging
from notifications import sms
from notifications import audio
from inventory import bestbuy

WAIT = 10

def main():
    notifiers = []
    notifiers.append(sms.Twilio())
    notifiers.append(audio.Audio())

    logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.INFO, datefmt='%m/%d/%Y %I:%M:%S %p')
    bb = bestbuy.BestBuy()
    while True:
        if bb.check():
            notify([], notifiers)
        sleep(WAIT)       

def notify(inventory, notifiers):
    print("STOCK FOUND:")
    for item in inventory:
        print(item)

    for notifier in notifiers:
        notifier.notify()


if __name__ == "__main__":
    main()
