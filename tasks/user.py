from db.models import SeedUser
from logger import crawler
from page_get import get_fans_or_followers_names, get_profile
from tasks.workers import app


@app.task
def crawl_follower_fans(name):
    """
    抓取用户粉丝信息
    :param name: 用户名
    :return:
    """
    seed = SeedUser.get_seed_by_name(name)
    if seed.other_crawled == 0:
        get_fans_or_followers_names(name, "followees")  # 关注
        get_fans_or_followers_names(name, "followers")  # 粉丝

    SeedUser.set_other_crawled(name, 1)


@app.task
def crawl_user_info(name):
    """抓取用户首页的信息
    :param name: 用户名
    :return: None
    """
    if not name:
        return None

    crawler.info(f"received task crawl_user_info {name}")
    user, other_crawled = get_profile(name)
    if not other_crawled:
        crawler.info(f"send task crawl_follower_fans {user.name}")
        app.send_task("tasks.user.crawl_follower_fans", args=(user.name,))


@app.task
def execute_user_task():
    seeds, is_exists = SeedUser.get_seed_names()
    if is_exists:
        for seed in seeds:
            crawler.info(f"send task crawl_user_info {seed.name}")
            app.send_task("tasks.user.crawl_user_info", args=(seed.name,))
    else:
        crawler.info("find no user, abort")
