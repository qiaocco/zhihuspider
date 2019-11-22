from db.models import SeedUser
from logger import crawler
from page_get import get_profile
from tasks.workers import app


@app.task
def crawl_user_info(name):
    """抓取用户及粉丝和关注者的信息
    :param name: 用户名
    :return: None
    """
    if not name:
        return None

    crawler.info(f"received task crawl_user_info {name}")
    user, is_crawled = get_profile(name)
    if not is_crawled:
        crawler.info(f"send task crawl_follower_fans {user.name}")
        app.send_task("tasks.user.crawl_follower_fans", args=(user.name,))


@app.task
def execute_user_task():
    seeds = SeedUser.get_seed_names()
    if seeds:
        for seed in seeds:
            crawler.info(f"send task crawl_user_info {seed.name}")
            app.send_task("tasks.user.crawl_user_info", args=(seed.name,))
