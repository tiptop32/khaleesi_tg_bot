import logging
import os
import random

from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from aiogram import Bot, types

from evaluate_for_negative import evaluate_text
from replacing import replace_text

TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)


async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()


@dp.message_handler(commands='help')
async def echo(message: types.Message):
    await message.reply(
        """"Это Кхалиси! 
        - Передразнивает всех достойных того.
        - Случайно реагирует на некоторые сообщения.
        - Откликакется на свое имя в сообщениях
        - Можно натравить на чужое сообщение командой 'дракарис'
        """)


@dp.message_handler(content_types=['text'])
async def replace_message(message: types.Message):
    input_msg = message.text

    is_command_to_reply = 'дракарис' in input_msg or 'Дракарис' in input_msg

    if is_command_to_reply and message.reply_to_message is not None:
        output_msg = replace_text(message.reply_to_message.text)
        await message.reply_to_message.reply(output_msg)

    is_ref_bot = 'Кхалиси' in input_msg
    is_negative = evaluate_text(input_msg) <= -20
    if is_ref_bot or random.randint(1, 100) < 3:
        output_msg = replace_text(input_msg)
        await message.reply(output_msg)

    if len(input_msg) < 140 and is_negative:
        output_msg = replace_text(input_msg)
        await message.reply(output_msg)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )