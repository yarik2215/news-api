import logging
import django_rq
from .models import News

logger = logging.getLogger("django.server")
reset_upvotes_job_id = "reset_upvotes_job"


def reset_all_upvotes():
    news = News.objects.all()
    for n in news:
        n.reset_upvotes()


def init_reset_upvotes_task():
    scheduler = django_rq.get_scheduler()
    scheduler.cron(
        "0 0 0 * * *",
        func=reset_all_upvotes,
        id=reset_upvotes_job_id,
    )
    logger.info(
        'Start task for reseting upvotes every day at 00:00:00.\n'
    )
