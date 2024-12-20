#  Домашнее задание по теме "Методы отправки сообщений".

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = 'removed for security reasons'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    print('Получена команда /start')
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')

@dp.message_handler()
async def all_messages(message):
    print('Получено сообщение!: ', message.text)
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)