import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "6782633403").split()))

API_ID = int(os.getenv("API_ID", "24527689"))

API_HASH = os.getenv("API_HASH", "113d91ecebac3b6e4cda8952c5bb0de3")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8324363627:AAH1Dh01wITkv3i6F7jB83WRxT_DlUNOYrg")

OWNER_ID = int(os.getenv("OWNER_ID", "6782633403"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002312835928").split()))

RMBG_API = os.getenv("RMBG_API", "Y8mKMpDEsaZsvRikj4xk8xRR")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://storefansx28:storefansx28@cluster0.uczmgas.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002312835928"))
