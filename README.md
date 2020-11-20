1. install python 3.8 - https://www.python.org/downloads/release/python-386/
2. install pipenv
    `pip install pipenv`
3. start a pipenv shell
   
   `pipenv install --three`
    
    `pipenv shell`
4. OPTIONAL - configure things
    - in a text editor, open inventory.py
    - update `ZIP` and `RADIUS` values if desired
    - update `WAIT` to the number of seconds between inventory fetches/notifications.
5. OPTIONAL - configure twilio for sms notifications
    - register a free twilio account - https://www.twilio.com/try-twilio
    - once registered, create a trial number from https://www.twilio.com/console
    - in inventory.py, update 
        - `PHONE` with your real number
        - `TRIAL_PHONE` with your twilio trial number
        - `TWILIO_SID` with your twilio sid
        - `TWILIO_TOKEN` with your twilio token
6. run the damn thing
    `python inventory.py`

notes:
yeah, the code sucks. i wrote this really quick. i might refactor it if i have time.
