from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    API_ID = int(config("API_ID", default="123"))
    API_HASH = config("API_HASH", default=None)
    OWNER_ID = int(config("OWNER_ID", default=1344569458))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP", default=-100))
    DEV_USERS = [
        int(i)
        for i in config(
            " DEV_USER" , default=""
        ).split()
    ]
    SUDO_USERS = [ 
int(i)for i in config(
            "SUDO_USERS",
            default="",
        ).split()
    ]
    WHITELIST_USERS = [
        int(i)
        for i in config(
            "WHITELIST_USERS",
            default="",
        ).split()
    ]
    GENIUS_API_TOKEN = config("GENIUS_API",default=None)
    AuDD_API = config("AuDD_API",default=None)
    RMBG_API = config("RMBG_API",default=None)
    DB_URI = config("DB_URI", default="")
    DB_NAME = config("DB_NAME", default="")
    BDB_URI = config("BDB_URI",default=None)
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="gojo_bots_network")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="gojo_bots_network")
    VERSION = config("VERSION", default="v2.0")
    WORKERS = int(config("WORKERS", default=16))
    TIME_ZONE = config("TIME_ZONE",default='Asia/Kolkata')
    BOT_USERNAME = ""
    BOT_ID = ""
    BOT_NAME = ""
    owner_username = ""


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "6437617075:AAGD-NSUY0gMxjOYG6Yxt3M-gYqE6-koO_c"
    API_ID = 20360751  # Your APP_ID from Telegram
    API_HASH = "af00d935eaaa1063e32b0fa2c8d63c4b"  # Your APP_HASH from Telegram
    OWNER_ID = 6107573996  # Your telegram user id defult to mine
    MESSAGE_DUMP = -1001901423055  # Your Private Group ID for logs
    DEV_USERS = ['1641847702','1975547002','706493007']
    SUDO_USERS = ['6114302713','5506563973','6164270973']
    WHITELIST_USERS = ['6144607630','5196269773','6062134898']
    DB_URI = "mongodb+srv://maxshou:9uJwjoPvimWgkk4z@cluster0.zpuobzl.mongodb.net/?retryWrites=true&w=majority"  # Your mongo DB URI
    DB_NAME ="cluster0"  # Your DB name
    NO_LOAD = []
    GENIUS_API_TOKEN = "bg9TSv4mI6rHY2rtBqJWowealhHJsaefYHzhoZ2zjkJmPkEHCQxh"
    AuDD_API ="3c59823648520c0e0be1b944e4c774dc"
    RMBG_API = "xQVAaSQFJ7cYCGusww9Gmiyt"
    PREFIX_HANDLER = ["!", "/"]
    SUPPORT_GROUP = "SUPPORT_GROUP"
    SUPPORT_CHANNEL = "SUPPORT_CHANNEL"
    VERSION = "VERSION"
    TIME_ZONE = 'Asia/Kolkata'
    BDB_URI = "mongodb://atlas-sql-64de1b504b3e202dab7efc85-pafju.a.query.mongodb.net/Anon?ssl=true&authSource=admin"
    WORKERS = 8
