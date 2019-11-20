import time

from .workers import app


@app.task
def execute_user_task():
    time.sleep(3)
    return "ok"
