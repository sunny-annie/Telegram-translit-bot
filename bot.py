import logging
import os
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Напиши фамилию, имя и отчество, чтобы транслитерировать их'
    logging.info(f'{user_name=} {user_id} sent message: {message.text}')
    await message.reply(text)


@dp.message_handler()
async def send_translit_name(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    dict = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
            'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
            'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh',
            'ц': 'TS', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': 'ie', 'ы': 'y', 'ь': '', 'э': 'e',
            'ю': 'iu', 'я': 'ia'}
    for key in dict:
        text = text.lower().replace(key, dict[key]).title()
    logging.info(f'{user_name=} {user_id} sent message: {message.text}, got response: {text}')
    await bot.send_message(user_id, text)


if __name__ == '__main__':
    executor.start_polling(dp)
