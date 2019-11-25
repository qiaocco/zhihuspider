import random
from pathlib import Path

import yaml

PROJECT_ROOT = Path.cwd()
config_path = Path(__file__).parent.joinpath("spider.yaml")
with open(config_path, encoding="utf-8") as f:
    cont = f.read()

cf = yaml.load(cont, Loader=yaml.FullLoader)


def get_db_args():
    return cf.get("db")


def get_redis_args():
    return cf.get("redis")


def get_crawl_interval():
    interval = random.randint(cf.get("min_crawl_interal"), cf.get("max_crawl_interal"))
    return interval


def get_crawl_timeout():
    return cf.get("timeout")


def get_max_follow_page():
    return cf.get("max_follow_page")
