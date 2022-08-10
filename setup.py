import logging
from os import getenv

from aiogram import Bot
import tg_logger
from flask import Flask

# ------------- bot -------------
bot_token = getenv('BOT_TOKEN')
bot = Bot(bot_token)

# ------------- flask app -------------
app = Flask(__name__)

# ------------- logging -------------
logger = logging.getLogger("tg-bot-template")

users = [int(getenv("ADMIN_ID"))]
alpha_logger = logging.getLogger()
alpha_logger.setLevel(logging.INFO)
tg_logger.setup(alpha_logger, token=getenv("LOG_BOT_TOKEN"), users=users)

app.logger.setLevel(logging.ERROR)
tg_logger.setup(app.logger, token=getenv("LOG_BOT_TOKEN"), users=users)

# ------------- webhook -------------
ADMIN_PASSWORD = getenv('ADMIN_PASSWORD')
WEBHOOK_TOKEN = getenv('WEBHOOK_TOKEN')
