import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
import config


dp = Dispatcher()

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text=f"Hello, {message.from_user.full_name}")

@dp.message(Command("help"))
async def handle_help(message: types.Message):
    text = "I`m a simple echo bot.\nSend me any messsage and I`ll repeat it for you."
    await message.answer(text=text)

@dp.message()
async def echo_message(message: types.Message):
    await message.bot.send_message(
        chat_id=message.chat.id,
        text="Wait a few seconds..."
    )
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply("Something new happened")


async def main():
    logging.basicConfig(level=logging.DEBUG)
    bot = Bot(config.BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())