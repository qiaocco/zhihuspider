import json

from db.models import HotList
from logger import crawler


def num_str_to_int(num_str):
    if not num_str:
        return 0
    return int(num_str.replace(",", ""))


def parse_hot_list(title, html):
    all_lists = []
    try:
        data_list = json.loads(html)["data"]

        for data in data_list:
            hot_list = HotList()

            hot_list.hot_num = data["detail_text"].split(" ")[0]
            target_item = data["target"]
            hot_list.title = target_item["title"]
            hot_list.excerpt = target_item["excerpt"][:300]  # 节省空间，取前300字符
            hot_list.answer_count = target_item["answer_count"]
            hot_list.comment_count = target_item["comment_count"]
            hot_list.follower_count = target_item["follower_count"]
            hot_list.url = target_item["url"]
            hot_list.category = title
            all_lists.append(hot_list)
    except Exception:
        crawler.exception(f"error!hot_list html={html}")
    return all_lists
