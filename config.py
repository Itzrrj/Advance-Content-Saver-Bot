from os import environ 

class Config:
    API_ID = environ.get("API_ID", "27886867")
    API_HASH = environ.get("API_HASH", "1db614ec07489cf356faaf6547709c27")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7798107233:AAE3yqJrbsWlgEwfw85nsgzvSaFRnlqd20g") 
    BOT_SESSION = environ.get("BOT_SESSION", "1BVtsOKEBu7Miet6L4AdbC7XLUuz2ffa6zpvtZyQic7fjQJYsEt6hYrGJe60UnCMea7b-56_IUIIB2QcKq7qCPvKmKQOjeuzOts_9eM7xzsL97dNIyp1kaRc7XKlZDayoSKpkCi6OB2-SqLaEhRgOeJn2C-R91WdR2IR4igN77yh_JAgyoxeiwZ8gDg4p65E5kJzo6ggiGx5YiyZNRJeQrsCofPMzClCi2DIilPfQQG9t5GqMyJY6GwW0_m4sdgKwNXNFtTSSW7rDvp4t7J8NEM2gjoMn9gqwQbLmtjAj9qYrvrtjzsWrdTFwceSKdnUuquHGGujs9Kj2zufkuWO7aYRRbQJYJuI=") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://cphdlust:cphdlust@cphdlust.ydeyw.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "cphdlust")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7059757087').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
