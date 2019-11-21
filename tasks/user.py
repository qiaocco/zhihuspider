import time

from db.operates import SeedUserOperate

from .workers import app


@app.task
def crawl_user_info(name):
    time.sleep(3)
    print(name)
    return "crawl ok"


@app.task
def execute_user_task():
    seeds = SeedUserOperate.get_seed_names()
    if seeds:
        for seed in seeds:
            app.send_task("tasks.user.crawl_user_info", args=(seed.name,))
