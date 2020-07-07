import logging
import os
import sys
import time

from pyrogram import Client, errors

from spam.config import Config

StartTime = time.time()
log = logging.getLogger()

ENABLE = Config.ENABLE

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    logging.error("You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting.")
    quit(1)


if ENABLE:
    logger = Config.LOGGER

    # Must be filled
    if Config.user1_api_id and Config.user1_api_hash:
        user1_api_id = Config.user1_api_id
        user1_api_hash = Config.user1_api_hash

    # if Config.user2_api_id and Config.user2_api_hash:
    #     user2_api_id = Config.user2_api_id
    #     user2_api_hash = Config.user2_api_hash

    # if Config.user3_api_id and Config.user3_api_hash:
    #     user3_api_id = Config.user3_api_id
    #     user3_api_hash = Config.user3_api_hash

    # if Config.user4_api_id and Config.user4_api_hash:
    #     user4_api_id = Config.user4_api_id
    #     user4_api_hash = Config.user4_api_hash

    # if Config.user5_api_id and Config.user5_api_hash:
    #     user5_api_id = Config.user5_api_id
    #     user5_api_hash = Config.user5_api_hash

    # if Config.user6_api_id and Config.user6_api_hash:
    #     user6_api_id = Config.user6_api_id
    #     user6_api_hash = Config.user6_api_hash

    # if Config.user7_api_id and Config.user7_api_hash:
    #     user7_api_id = Config.user7_api_id
    #     user7_api_hash = Config.user7_api_hash
    
    # if Config.user8_api_id and Config.user3_api_hash:
    #     user8_api_id = Config.user8_api_id
    #     user8_api_hash = Config.user8_api_hash

    Command = Config.Command
else:
    print('Enable me first in config.py')

if user1_api_id and user1_api_hash:
    user1 = Client("user1", api_id=user1_api_id, api_hash=user1_api_hash)

# if user2_api_id and user2_api_hash:
#     user2 = Client("user2", api_id=user2_api_id, api_hash=user2_api_hash)

# if user2_api_id and user3_api_hash:
#     user3 = Client("user3", api_id=user3_api_id, api_hash=user3_api_hash)

# if user4_api_id and user4_api_hash:
#     user4 = Client("user4", api_id=user4_api_id, api_hash=user4_api_hash)

# if user5_api_id and user5_api_hash:
#     user5 = Client("user5", api_id=user5_api_id, api_hash=user5_api_hash)

# if user6_api_id and user6_api_hash:
#     user6 = Client("user6", api_id=user6_api_id, api_hash=user6_api_hash)

# if user7_api_id and user7_api_hash:
#     user7 = Client("user7", api_id=user7_api_id, api_hash=user7_api_hash)

# if user8_api_id and user8_api_hash:
#     user8 = Client("user8", api_id=user8_api_id, api_hash=user8_api_hash)