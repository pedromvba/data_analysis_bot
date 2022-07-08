'''File for testing the code'''

# pylint: disable=E1101

from src.telegram_bot import TelegramBot
from src.gdrivebot import Gdrivebot


#bot = TelegramBot()
#bot.start()

gdrivebot = Gdrivebot()

print(gdrivebot.get_data())