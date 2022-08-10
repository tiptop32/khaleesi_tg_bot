from os import getenv
from aiogram import Dispatcher, executor, types

from setup import bot, logger
from webhook import app


# --------------- bot -------------------
# @bot.message_handler(commands=['help', 'start'])
# def say_welcome(message):
#     logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used /start or /help')
#     bot.send_message(
#         message.chat.id,
#         '<b>Коверкает слова. '
#         'При добавлении в группу рандомно реагирует на сообщения с негативным смысловым окрасом.</b>',
#         parse_mode='html'
#     )

dp = Dispatcher(bot)


@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")

if __name__ == '__main__':
    if getenv("IS_PRODUCTION", "False") == "True":
        app.run()
    else:
        executor.start_polling(dp, skip_updates=True)
