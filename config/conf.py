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
