from logger import crawler
from page_get import get_hot_list
from tasks.workers import app


@app.task
def crawl_hot_list(title):
    if not title:
        return None

    crawler.info(f"received task crawl_hot_list {title}")
    get_hot_list(title)


@app.task
def execute_hot_list_task():
    crawler.info(f"send task hot_list")
    hot_list_title = ["total", "science", "digital", "sport", "fashion", "film"]
    for title in hot_list_title:
        app.send_task("tasks.hot_list.crawl_hot_list", args=(title,))
