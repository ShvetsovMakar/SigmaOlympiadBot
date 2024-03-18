from aiogram import Bot, Dispatcher

from sqlite3 import connect

# CONNECTING BOT AND DATABASE

# sigma olympiad bot token
BOT_TOKEN = "7022081530:AAHA3Y2Pi_-0tbunUScwpNokXK4-t49W6FA"

# bot and dispatcher initialization
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# cursor initialization
db = connect("main_bot/participants.db")
cur = db.cursor()

# handling
handling = {"day1": True,
            "day2": True,
            "results1": True,
            "results2": True}

choices_int = {
    "1️⃣": 1,
    "2️⃣": 2,
    "3️⃣": 3,
    "4️⃣": 4,
    "5️⃣": 5,
    "6️⃣": 6,
    "7️⃣": 7,
    "8️⃣": 8,
    "9️⃣": 9,
    "🔟": 10,
}
