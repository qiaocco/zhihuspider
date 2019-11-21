from lxml import etree

from db.common import CommonOperate
from db.models import User
from logger import storage
from page_get.basic import get_page
from page_parse.user import get_detail

USER_HOME_URL = "https://www.zhihu.com/people/{}/activities"


def get_profile(user_name):
    """
    :param user_name: 用户名
    : return  TODO
    """

    user = User.get_user_by_name(user_name)
    if user:
        storage.info(f"user {user_name} has already crawled")
    else:
        storage.info(f"user {user_name} not exist, start crawling...")
        user = get_user_info_from_web(user_name)


def get_user_info_from_web(user_name):
    """从网络抓取用户信息
    :param: user_name 用户名
    :return: user entiry
    """
    if not user_name:
        return None

    url = USER_HOME_URL.format(user_name)
    html = get_page(url)

    storage.info("get_user_detail")
    user = get_user_detail(user_name, html)


def get_user_detail(user_name, html):
    storage.info("get_detail")

    user = get_detail(user_name, html)
    # 创建用户
    CommonOperate.add_one(user)
    storage.info(f"Has stored user {user_name} info successfully")

    return user, False
