from celery.schedules import crontab
from celery import Celery
from .modules.Paeser import main as Pars
from .models import News
from celery import shared_task
from celery.schedules import crontab
from mysite.celery import celery_app
import beat


# celery_app = Celery('mysite')


@celery_app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    print('lol')
    # Calls test() every 10 seconds.
    sender.add_periodic_task(crontab(
        hour=7, minute=30, day_of_week=1),
        test.s()
    )


@celery_app.task
def test():
    print('lol')
    news = Pars()
    for n in news:
        s = News(news_text=n[1], news_url=n[0], news_hype_rate=n[2])
        s.save()