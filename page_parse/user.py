from lxml import etree

from db.models import User


def get_detail(user_name, html):
    user = User()
    user.name = user_name
    root = etree.HTML(html)
    headline_xpath = "//span[@class='ztext ProfileHeader-headline']/text()[1]"
    avatar_xpath = "//img[@class='Avatar Avatar--large UserAvatar-inner']/@src"
    career_xpath = "//div[@class='ProfileHeader-infoItem'][1]/text()"
    education_xpath = "//div[@class='ProfileHeader-infoItem'][2]/text()"
    user.headline = root.xpath(headline_xpath)
    user.avatar = root.xpath(avatar_xpath)[0]
    user.career = root.xpath(career_xpath)[0]
    user.education = " ".join(root.xpath(education_xpath))
    return user
