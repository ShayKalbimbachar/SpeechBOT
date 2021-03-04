from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def start(bot):
    bot.message.reply_text(main_menu_message(),
                           reply_markup=main_menu_keyboard())


def main_menu(bot, update):
    bot.callback_query.message.edit_text(main_menu_message(),
                                         reply_markup=main_menu_keyboard())


def error(update, context):
    print(f'Update {update} caused error {context.error}')


def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Hebrew 🇮🇱', callback_data='iw')],
                [InlineKeyboardButton('English 🇺🇸', callback_data='en-us')],
                [InlineKeyboardButton('Russian 🇷🇺', callback_data='ru')],
                [InlineKeyboardButton('Arabic 🇦🇪', callback_data='ar')]
                ]
    return InlineKeyboardMarkup(keyboard)


def main_menu_message():
    return 'Please choose your preferred language'
