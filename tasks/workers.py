from celery import Celery

app = Celery("zhihu")
app.config_from_object("config.celeryconfig")
