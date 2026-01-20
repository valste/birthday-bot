from apscheduler.schedulers.background import BackgroundScheduler
from bot.logging import setup_logging


def start_scheduler(job_callable) -> BackgroundScheduler:
    setup_logging()
    scheduler = BackgroundScheduler()
    scheduler.add_job(job_callable, "cron", hour=6, minute=0)
    scheduler.start()
    return scheduler
