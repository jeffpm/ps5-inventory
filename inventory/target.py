import logging
from inventory import utils
from bs4 import BeautifulSoup


class Target():
    def __init__(self):
        self.driver = utils.get_driver()
    def check(self):
        url = "https://www.target.com/p/playstation-5-console/-/A-81114595"
        logging.info("checking target...")
        self.driver.get(url)
        html = self.driver.page_source
        soup = BeautifulSoup(str(html), 'html.parser')
        button_list = soup.find_all('button', {'data-test': 'orderPickupButton'})
        if len(button_list) > 0:
            logging.info("TARGET STOCK FOUND")
            return True
        
        return False