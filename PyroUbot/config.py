import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "999"))

DEVS = list(map(int, os.getenv("DEVS", "5301377519").split()))

API_ID = int(os.getenv("API_ID", "29921066"))

API_HASH = os.getenv("API_HASH", "bd5462a5cdae03889276f14756ef11e1")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7737202533:AAGNkmXBWykIGy_EpeUtyXyNmHcGI8skhwQ")

OWNER_ID = int(os.getenv("OWNER_ID", "5301377519"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", " -1002356932965").split()))

RMBG_API = os.getenv("RMBG_API", "R7x6khRga3psnfbFgpfwomB3")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Johnathan:KontolXD#123@johnathansange.ggwewml.mongodb.net/?retryWrites=true&w=majority&appName=JohnathanSange")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002552768474"))
