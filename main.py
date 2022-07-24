# Aiogram imports
from aiogram import Bot, Dispatcher, executor

# Import ShipBot module
import ShipBot
from config import BOT_TOKEN

# Initialize ShipBot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Initialize handlers
ShipBot.setup(dp)

# Run executor
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_shutdown=ShipBot.on_shutdown)
