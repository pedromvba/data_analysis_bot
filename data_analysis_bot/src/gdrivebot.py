from dotenv import load_dotenv
import gspread #library for accessing gsheets
import os
import json

load_dotenv()       # take environment variables from .env.
                    # Code of your application, which uses environment variables (e.g. from `os.environ` or
                    # `os.getenv`) as if they came from the actual environment.
                    # This is really useful for logins, passwords etc.

class Gdrivebot():
    
    CREDENTIALS = json.loads(os.getenv('GDRIVE_BOT_CREDENTIALS'))

    
     
    def __init__(self):

        ''''
        Allow the connection thru the credentials informed to google services
        '''
        self.gc = gspread.service_account(filename=CREDENTIALS) #filename must be a .json file

    #def getdata():