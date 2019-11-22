import re

from lxml import etree

from db.models import User


def num_str_to_int(num_str):
    if not num_str:
        return 0
    return int(num_str.replace(",", ""))


def get_detail(user_name, html):
    user = User()
    user.name = user_name
    root = etree.HTML(html)
    headline_xpath = "//span[@class='ztext ProfileHeader-headline']/text()[1]"
    avatar_xpath = "//img[@class='Avatar Avatar--large UserAvatar-inner']/@src"
    career_xpath = "//div[@class='ProfileHeader-infoItem'][1]/text()"
    education_xpath = "//div[@class='ProfileHeader-infoItem'][2]/text()"
    follow_xpath = "//strong[@class='NumberBoard-itemValue']"
    approve_xpath = "//div[@class='IconGraf']/text()"
    thanks_and_collect_xpath = "//div[@class='Profile-sideColumnItemValue']/text()"
    img_xpath = "//img[@class='Avatar Avatar--large UserAvatar-inner']/@src"

    user.headline = root.xpath(headline_xpath)
    user.avatar = root.xpath(avatar_xpath)[0]
    user.career = root.xpath(career_xpath)[0]
    user.education = " ".join(root.xpath(education_xpath))
    follow = root.xpath(follow_xpath)
    user.follower = num_str_to_int(follow[0].text)
    user.following = num_str_to_int(follow[1].text)
    user.approve = num_str_to_int(root.xpath(approve_xpath)[1])
    thanks_and_collect = root.xpath(thanks_and_collect_xpath)[0]
    thanks_str, collect_str = thanks_and_collect.split("，")
    user.thanks = num_str_to_int(re.search(r"\d+(?:,\d+)?", thanks_str).group())
    user.collect = num_str_to_int(re.search(r"\d+(?:,\d+)?", collect_str).group())
    user.image_url = root.xpath(img_xpath)[0]

    return user
