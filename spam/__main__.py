import asyncio
import importlib
import sys
import time
import traceback

from spam import user1
    # user2, user3, user4, user5, user6, user7, user8
from spam.modules import ALL_MODULES

BOT_RUNTIME = 0
HELP_COMMANDS = {}

loop = asyncio.get_event_loop()


async def get_runtime():
    return BOT_RUNTIME

async def reload_userbot():
    await user1.start()
    # await user2.start()
    # await user3.start()
    # await user4.start()
    # await user5.start()
    # await user6.start()
    # await user7.start()
    # await user8.start()
    for modul in ALL_MODULES:
        imported_module = importlib.import_module("spam.modules." + modul)
        importlib.reload(imported_module)

async def reinitial():
    await user1.start()
    # await user2.start()
    # await user3.start()
    # await user4.start()
    # await user5.start()
    # await user6.start()
    # await user7.start()
    # await user8.start()


async def start_bot():
    # sys.excepthook = except_hook
    print("----- Checking user and bot... -----")
    await reinitial()
    print("----------- Check done! ------------")
    # userbot
    # await user2.start()
    # await user3.start()
    # await user4.start()
    # await user5.start()
    # await user6.start()
    # await user7.start()
    # await user8.start()
    for modul in ALL_MODULES:
        imported_module = importlib.import_module("spam.modules." + modul)
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if not imported_module.__MODULE__.lower() in HELP_COMMANDS:
                HELP_COMMANDS[imported_module.__MODULE__.lower()] = imported_module
            else:
                raise Exception("Can't have two modules with the same name! Please change one")
        if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
            HELP_COMMANDS[imported_module.__MODULE__.lower()] = imported_module
    print("-----------------------")
    print("SpamProtection modules: " + str(ALL_MODULES))
    print("-----------------------")
    print("Bot run successfully!")
    await user1.idle()

if __name__ == '__main__':
    BOT_RUNTIME = int(time.time())
    loop.run_until_complete(start_bot())