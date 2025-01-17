#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = config("27886867", default=None, cast=int)
API_HASH = config("1db614ec07489cf356faaf6547709c27", default=None)
BOT_TOKEN = config("7798107233:AAE3yqJrbsWlgEwfw85nsgzvSaFRnlqd20g", default=None)
SESSION = config("1BVtsOKEBu7Miet6L4AdbC7XLUuz2ffa6zpvtZyQic7fjQJYsEt6hYrGJe60UnCMea7b-56_IUIIB2QcKq7qCPvKmKQOjeuzOts_9eM7xzsL97dNIyp1kaRc7XKlZDayoSKpkCi6OB2-SqLaEhRgOeJn2C-R91WdR2IR4igN77yh_JAgyoxeiwZ8gDg4p65E5kJzo6ggiGx5YiyZNRJeQrsCofPMzClCi2DIilPfQQG9t5GqMyJY6GwW0_m4sdgKwNXNFtTSSW7rDvp4t7J8NEM2gjoMn9gqwQbLmtjAj9qYrvrtjzsWrdTFwceSKdnUuquHGGujs9Kj2zufkuWO7aYRRbQJYJuI=", default=None)
FORCESUB = config("-1002294570357", default=None)
AUTH = config("AUTH", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
