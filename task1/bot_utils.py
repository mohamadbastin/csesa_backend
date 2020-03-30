import telepot
from telepot.loop import MessageLoop


# from telepot.api import

from .data import TOKEN
# from csesa_telegram.settings import PROXY, TELEGRAM_BOT_TOKEN


def handle(msg):
    pass


# f = telepot.api.
bot = telepot.Bot(TOKEN)

MessageLoop(bot, handle).run_as_thread()
