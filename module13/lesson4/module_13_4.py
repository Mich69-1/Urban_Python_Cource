#  Домашнее задание по теме "Машина состояний".

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

api = 'removed for security reasons'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    print('Получена команда /start')
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')
    await message.answer('Наберите Calories, чтобы узнать Вашу норму калорий.')

@dp.message_handler(text='Calories')
async def set_age(message):
    await message.answer('Введите Ваш возраст (лет): ')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите Ваш рост (см): ')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите Ваш вес (кг): ')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) + 5 * int(data['age']) + 5
    await message.answer('Ваша норма калорий: ' + str(calories))
    await state.finish()

@dp.message_handler()
async def all_messages(message):
    print('Получено сообщение!: ', message.text)
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)