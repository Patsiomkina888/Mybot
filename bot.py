import logging
from apscheduler.schedulers.background import BackgroundScheduler
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)
logging.getLogger("apscheduler.scheduler").setLevel(
    logging.WARNING
)  # спрятано сообщение  в логах "INFO:apscheduler.scheduler:Scheduler started."

# Настройки прокси: добавляется словарь
# PROXY = {
#     "proxy_url": settings.PROXY_URL,
#     "urllib3_proxy_kwargs": {'username': settings.PROXY_USERNAME, "password": settings.PROXY_PASSWORD},
# }


def greet_user(update, context):
    print("Вызван/start")
    update.message.reply_text(
        "Привет, дорогой пользователь! Ты вызвал команду /start. Ай-да молодец!"
    )


def talk_to_me(update, context):
    usertext = update.message.text
    print(usertext)
    update.message.reply_text(usertext)


def main():
    mybot = Updater(
        settings.API_KEY,
        use_context=True,
        # request_kwargs=PROXY,
    )
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
