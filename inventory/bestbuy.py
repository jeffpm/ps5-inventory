import logging
from inventory import utils
from bs4 import BeautifulSoup
class BestBuy():
    def __init__(self):
        self.driver = utils.get_driver()
    def check(self):
        url = "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
        logging.info("checking best buy...")
        self.driver.get(url)
        html = self.driver.page_source

        soup = BeautifulSoup(str(html), 'html.parser')
        button_list = soup.find_all('button', {'class': 'add-to-cart-button'})
        if len(button_list) != 1:
            logging.error("could not find the best buy add to cart button")
            return False
        
        if button_list[0].text != "Sold Out":
            logging.info("BEST BUY STOCK FOUND")
            return True
        else:
            return False
