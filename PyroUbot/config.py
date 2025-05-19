import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "999"))

DEVS = list(map(int, os.getenv("DEVS", "1986099968").split()))

API_ID = int(os.getenv("API_ID", "21370336"))

API_HASH = os.getenv("API_HASH", "d63f22a973f14fedc07c45595306842a")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7736379794:AAEa4HkoWgOi9ziK9qhomvFewFP76ZPdZTs")

OWNER_ID = int(os.getenv("OWNER_ID", "1986099968"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", " -4885252371").split()))

RMBG_API = os.getenv("RMBG_API", "no1RWHwRQwwF5XtBWufCpPck")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://bagasprstyo999000:<tEfT0suIAPrSM6Lm>@bridgestone12.hexzhwt.mongodb.net/")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002504273075"))
