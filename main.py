import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config_reader import config


logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    user = message.from_user
    kb = [
        [
            types.KeyboardButton(text='🛒Товары'),
            types.KeyboardButton(text='👤Профиль'),
            types.KeyboardButton(text='🤝О нас')
        ]
    ]
    keyboard = (types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    ))
    await message.answer(
        f'<b>Добро пожаловать, {user.first_name}!</b>\n'
        'В магазине вы можете найти...\n\n\n'
        '<i>❗️Бот написан в качестве примера❗️</i>',
        reply_markup=keyboard,
        parse_mode='HTML'
    )


@dp.message(F.text.lower() == '🛒товары')
async def product(message: types.Message):
    await message.reply('Доделать')

@dp.message(F.text.lower() == '👤профиль')
async def account(message: types.Message):
    await message.reply(
        'Здесь будет информация о пользователе\n\n'
        f'<i>Имя: </i>\n'
        '...\n'
        '...\n',
        parse_mode='HTML'
    )

@dp.message(F.text.lower() == '🤝о нас')
async def about(message: types.Message):
    await message.reply(
        '<b>Раздел о нас❗️</b>\n\n'
        '<i>здесь может быть ваша информация</i>\n'
        '...\n'
        '...',
        parse_mode='HTML'
    )


admin_users = [5946765150, 'admin_username']
@dp.message(Command('admin_panel'))
async def admin(message: types.Message):
    user = message.from_user
    if message.from_user.id in admin_users:
        kb = [
        [   
            types.KeyboardButton(text='🛒Товары'),
            types.KeyboardButton(text='Добавить товар'),
            types.KeyboardButton(text='Рассылка'),
            types.KeyboardButton(text='Добавить промокод')
        ]
    ]
        keyboard = (types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    ))
        await message.reply(f'Привет, <b>{user.first_name}!</b>',reply_markup=keyboard, parse_mode='HTML')
    else:
        await message.reply('У вас нет доступа к этой команде.')


@dp.message(F.text.lower() == 'добавить товар')
async def add_product(message: types.Message):
    if message.from_user.id in admin_users:
        await message.answer('Введите название товара:')
    else:
        await message.answer('У вас нет доступа к этой команде.')






@dp.message(F.text.lower() == 'рассылка')
async def mailing(message: types.Message):
    if message.from_user.id in admin_users:
        await message.answer('Напишите текст рассылки:')
    else:
        await message.answer('У вас нет доступа к этой команде.')


@dp.message(F.text.lower() == 'добавить промокод')
async def promo(message: types.Message):
    if message.from_user.id in admin_users:
        await message.answer('Введите уникальный промокод:')
    else:
        await message.answer('У вас нет доступа к этой команде.')




async def main():
    await dp.start_polling(bot)


if __name__=='__main__':
    asyncio.run(main())
