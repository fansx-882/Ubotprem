import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "1714407109").split()))

API_ID = int(os.getenv("API_ID", "23524337"))

API_HASH = os.getenv("API_HASH", "77a7094ef80a4296f5d4f54638e833fa")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8276692772:AAHksYZp8fyls08qztxoNLtHL5R9fokHYZI")

OWNER_ID = int(os.getenv("OWNER_ID", "1714407109"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002312835928").split()))

RMBG_API = os.getenv("RMBG_API", "Y8mKMpDEsaZsvRikj4xk8xRR")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://storefansx28:storefansx28@cluster0.uczmgas.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002312835928"))
