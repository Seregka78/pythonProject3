# import telebot
# from django.core.management.base import BaseCommand
# from django.conf import settings
#
# # from telebot import TeleBot
#
# TELEGRAM_BOT_KEY='6025205370:AAH6CuxjcgHjXLuccx0UVKRCwnYNTAhG_OM'
# # Объявление переменной бота
# bot = telebot.TeleBot(TELEGRAM_BOT_KEY)
# # bot = TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)
#
# @bot.message_handler(commands=["start"])
# def start(message):
#     bot.send_message(message.chat.id, "Добро пожаловать")
#     print("бот запущен")
#
# @bot.message_handler(content_types=['text'])
# def start(message):
#     bot.send_message(message.from_user.id, 'Hello')
#     print("бот запущен")
# # Название класса обязательно - "Command"
# class Command(BaseCommand):
#   	# Используется как описание команды обычно
#     help = 'Just a command for launching a Telegram bot.'
#
#     def handle(self, *args, **kwargs):
#         bot.enable_save_next_step_handlers(delay=2) # Сохранение обработчиков
#         bot.load_next_step_handlers()				# Загрузка обработчиков
#         bot.infinity_polling()						# Бесконечный цикл бота
# bot = telebot.TeleBot(settings.API_KEY)

