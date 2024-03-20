#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# from django_bot.django_bot.settings import API_KEY


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_bot.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

from django.core.management.base import BaseCommand
from django.conf import settings

from telebot import TeleBot
import telebot

# API_KEY = '6025205370:AAH6CuxjcgHjXLuccx0UVKRCwnYNTAhG_OM'
bot = telebot.TeleBot(settings.API_KEY)


@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.from_user.id, 'Hello')
    bot.send_message(1677886983, 'это я')
bot.remove_webhook()
bot.polling(none_stop=True, interval=0)
# bot.polling()