import time

from .workers import app


@app.task
def crawl_user_info(name):
    time.sleep(3)
    return "crawl ok"


@app.task
def execute_user_task():
    name = "123"
    app.send_task("tasks.user.crawl_user_info", args=(name,))
