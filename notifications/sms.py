from twilio.rest import Client
import logging


PHONE = "+1<your-phone>"
TRIAL_PHONE = "+1<your-trial-phone>"
TWILIO_SID = "<your-twilio-sid>"
TWILIO_TOKEN = "<your-twilio-token>"

class Twilio():
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)
    def notify(self):
        try:
            message = self.client.messages \
                .create(
                        body="PS5 STOCK FOUND.",
                        from_=TRIAL_PHONE,
                        to=PHONE
                    )
        except:
            logging.info("couldn't send twilio message")