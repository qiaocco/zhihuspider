import json
import re

from lxml import etree

from db.models import User
from logger import crawler


def num_str_to_int(num_str):
    if not num_str:
        return 0
    return int(num_str.replace(",", ""))


def get_detail(user_name, html):
    user = User()
    user.name = user_name
    root = etree.HTML(html)
    headline_xpath = "//span[@class='ztext ProfileHeader-headline']/text()"
    avatar_xpath = "//img[@class='Avatar Avatar--large UserAvatar-inner']/@src"
    career_xpath = "//div[@class='ProfileHeader-infoItem'][1]/text()"
    education_xpath = "//div[@class='ProfileHeader-infoItem'][2]/text()"
    follow_xpath = "//strong[@class='NumberBoard-itemValue']"
    # approve_xpath = "//div[@class='IconGraf']/text()"
    # thanks_and_collect_xpath = "//div[@class='Profile-sideColumnItemValue']/text()"
    img_xpath = "//img[@class='Avatar Avatar--large UserAvatar-inner']/@src"

    try:
        headline_item = root.xpath(headline_xpath)
        if headline_item:
            user.headline = headline_item[0]
        avatar_item = root.xpath(avatar_xpath)
        if avatar_item:
            user.avatar = avatar_item[0]
        career_item = root.xpath(career_xpath)
        if career_item:
            user.career = career_item[0]

        user.education = " ".join(root.xpath(education_xpath))
        follow_item = root.xpath(follow_xpath)
        if follow_item:
            user.follower = num_str_to_int(follow_item[0].text)
            user.following = num_str_to_int(follow_item[1].text)
        approve_item = re.search(r"获得 (\d+(?:,\d+)) 次赞同", html)
        if approve_item:
            user.approve = num_str_to_int(approve_item.group(1))

        thanks_and_collect = re.search(r"获得 (\d+(?:,*\d+)) 次感谢，(\d+(?:,*\d+)) 次收", html)
        # thanks_and_collect = root.xpath(thanks_and_collect_xpath)[0]
        if thanks_and_collect:
            thanks_str, collect_str = thanks_and_collect.groups()
            user.thanks = num_str_to_int(thanks_str)
            user.collect = num_str_to_int(collect_str)
        else:
            user.thanks, user.collect = -1, -1

        img_item = root.xpath(img_xpath)
        if img_item:
            user.image_url = img_item[0]
    except Exception:
        crawler.exception(f"error!user_name = {user_name}")
    return user


def get_fans_or_follows(html, user_name):
    res = json.loads(html)
    user_names = list()
    for item in res["data"]:
        user_names.append(item.get("url_token"))

    is_end = res["paging"]["is_end"]
    return user_names, is_end
