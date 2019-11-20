from .workers import app
import time


@app.task
def user():
    time.sleep(3)
    return "ok"
