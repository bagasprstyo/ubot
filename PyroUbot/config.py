import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "999"))

DEVS = list(map(int, os.getenv("DEVS", "7248260119").split()))

API_ID = int(os.getenv("API_ID", "1285117"))

API_HASH = os.getenv("API_HASH", "821de48a8c015e2016083f64d4d3e2fb")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7736379794:AAEa4HkoWgOi9ziK9qhomvFewFP76ZPdZTs")

OWNER_ID = int(os.getenv("OWNER_ID", "7248260119"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", " -4832634947").split()))

RMBG_API = os.getenv("RMBG_API", "no1RWHwRQwwF5XtBWufCpPck")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://bagasprastio:8lF0aWdPsN2JNQCh@bridgestone12.hexzhwt.mongodb.net/ubotdb?retryWrites=true&w=majority")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002694406555"))
