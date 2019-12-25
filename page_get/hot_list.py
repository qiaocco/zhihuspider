from db.common import CommonOperate
from logger import storage
from page_get.basic import get_page
from page_parse.hot_list import parse_hot_list

HOT_LIST_URL = (
    "https://www.zhihu.com/api/v3/feed/topstory/hot-lists/{" "}?limit=50&desktop=true "
)


def get_hot_list(title):
    hot_list = get_hot_list_from_web(title)
    storage.info(f"hot_list: {hot_list}")

    return hot_list


def get_hot_list_from_web(title):
    if not title:
        return None

    url = HOT_LIST_URL.format(title)
    html = get_page(url)

    all_lists = parse_hot_list(title, html)
    if all_lists:
        CommonOperate.add_all(all_lists)
        storage.info(f"Has stored hot_list {title} info successfully")

    return all_lists
