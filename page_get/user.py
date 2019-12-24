from config.conf import get_max_follow_page
from db.common import CommonOperate
from db.models import SeedUser, User
from logger import storage
from page_get.basic import get_page
from page_parse.user import get_detail, get_fans_or_follows

USER_HOME_URL = "https://www.zhihu.com/people/{}/activities"
FOLLOW_URL = (
    "https://www.zhihu.com/api/v4/members/{}/{"
    "}?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender"
    "%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F("
    "type%3Dbest_answerer)%5D.topics&offset={}&limit={} "
)


def get_profile(user_name):
    """
    :param user_name: 用户名
    : return  TODO
    """

    user = User.get_user_by_name(user_name)
    if user:
        storage.info(f"user {user_name} has already crawled")
        SeedUser.set_home_crawled(user_name, 1)
    else:
        storage.info(f"user {user_name} not exist, start crawling...")
        user = get_user_info_from_web(user_name)
        if user:
            SeedUser.set_home_crawled(user_name, 1)
        else:
            SeedUser.set_home_crawled(user_name, 2)

    other_crawled = SeedUser.get_seed_by_name(user_name).other_crawled

    storage.info(f"{user_name} other_crawled {other_crawled}")

    return user, other_crawled


def get_user_info_from_web(user_name):
    """从网络抓取用户信息
    :param: user_name 用户名
    :return: user entiry
    """
    if not user_name:
        return None

    url = USER_HOME_URL.format(user_name)
    html = get_page(url)

    user = get_user_detail(user_name, html)
    if user:
        CommonOperate.add_one(user)
        storage.info(f"Has stored user {user_name} info successfully")

    return user


def get_user_detail(user_name, html):
    storage.info("get_detail")

    user = get_detail(user_name, html)

    return user


def get_fans_or_followers_names(name, crawl_type):
    """
    抓取用户和粉丝
    :param name: 用户名
    :param crawl_type: 抓取类型。 followees: 关注, followers: 粉丝
    :return:
    """
    LIMIT = 20
    page = 1
    is_end = False
    max_follow_page = get_max_follow_page()

    while (not is_end) and (page < max_follow_page):
        url = FOLLOW_URL.format(name, crawl_type, (page - 1) * LIMIT, LIMIT)
        html = get_page(url)
        user_names, is_end = get_fans_or_follows(html, name)
        storage.info(
            f"get {name} {crawl_type}: user_names: {user_names}, is_end:{is_end}"
        )
        SeedUser.insert_many(user_names)

        page += 1

        storage.info(
            f"get {name} page={page}, max_follow_page={max_follow_page}, is_end={is_end}"
        )

    storage.info(f"crawle {name} fans and followers done")
