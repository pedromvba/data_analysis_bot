from dotenv import load_dotenv
import gspread #library for accessing gsheets
import os
import json

load_dotenv()       # take environment variables from .env.
                    # Code of your application, which uses environment variables (e.g. from `os.environ` or
                    # `os.getenv`) as if they came from the actual environment.
                    # This is really useful for logins, passwords etc.

class Gdrivebot:
    
    def __init__(self):



        ''''
        Allow the connection thru the credentials informed to google services
        '''
        self.gc = gspread.service_account(filename = "/Users/pedromonteiro/Library/Mobile Documents/com~apple~CloudDocs/Python VS Code/Bot Data Analysis/data_analysis_bot/credentials.json") #filename must be a .json file



    def get_data(self):
        sh = self.gc.open_by_key('1K-ft9TcGbSShUeO43h853j7CmlPBZPoTsTvDjJ4_1s4') 
        
# spreadsheet total link = https://docs.google.com/spreadsheets/d/1K-ft9TcGbSShUeO43h853j7CmlPBZPoTsTvDjJ4_1s4/edit#gid=0
        
        worksheet = sh.sheet1 # selecting the sheet
        return worksheet.get_all_records() # This returns a list of dictionaries, get_all_values returns a list of lists.
