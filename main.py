import ptbot
import properties as prty
from pytimeparse import parse
from progressbar import render_progressbar


def notify_progress(secs_left, message_id, author_id, message):
    bot.update_message(author_id, message_id,
                       "Осталось {} секунд\n{}".format(secs_left, render_progressbar(parse(message),
                                                                                     parse(message) - secs_left)))


def handler_messages(author_id, message):
    message_id = bot.send_message(author_id, "Запускаю таймер.")
    bot.create_countdown(parse(message), notify_progress, message_id=message_id, author_id=author_id, message=message)
    bot.create_timer(parse(message), end_timer, author_id=author_id)


def end_timer(author_id):
    bot.send_message(author_id, "Время вышло")


if __name__ == '__main__':
    bot = ptbot.Bot(prty.TG_TOKEN)
    bot.reply_on_message(handler_messages)
    bot.run_bot()
