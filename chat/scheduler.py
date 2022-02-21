from .models import Chat
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger


def delete_all_chat_objects():
    Chat.objects.all().delete()


def start():
    scheduler= BackgroundScheduler()
    scheduler.add_job(func=delete_all_chat_objects , trigger= CronTrigger(hour="21" , timezone="Iran" , minute="00"))
    scheduler.start()
