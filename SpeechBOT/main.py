# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
import voiceBot
from dotenv import load_dotenv
load_dotenv()
update_id = None


def main():
    global update_id
    # Telegram Bot Authorization Token - Ohad's account
    bot = telegram.Bot(os.environ.get("TELEGRAM_TOKEN"))
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            voiceBot.echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1


if __name__ == '__main__':
    main()