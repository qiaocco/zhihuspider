import time

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from config.conf import get_crawl_interval, get_crawl_timeout
from config.headers import headers
from logger import crawler
from utils.get_proxy import get_proxy


def requests_retry_session(
    retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504), session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


def get_page(url):
    crawler.info("the crawling url is {url}".format(url=url))
    # proxies = get_proxy()
    REQUEST_INTERVAL = get_crawl_interval()
    REQUEST_TIMEOUT = get_crawl_timeout()

    time.sleep(REQUEST_INTERVAL)
    crawler.info(f"sleep {REQUEST_INTERVAL}")

    resp = requests_retry_session().get(url, headers=headers, timeout=REQUEST_TIMEOUT,)

    return resp.text


if __name__ == "__main__":
    # response = requests_retry_session().get("https://httpbin.org/gets")
    # print(response.text)

    # s = requests.Session()
    # s.auth = ("user", "pass")
    # s.headers.update({"x-test": "true"})

    # response = requests_retry_session(session=s).get("https://www.peterbe.com")
    from lxml import etree

    url = "https://www.zhihu.com/people/laike9m/activities"
    html = get_requests(url)
    root = etree.HTML(html)
    headline_xpath = "//span[@class='ztext ProfileHeader-headline']/text()[1]"
    avatar_xpath = "//img[@class='Avatar Avatar--large UserAvatar-inner']/@src"
    career_xpath = "//div[@class='ProfileHeader-infoItem'][1]/text()"
    education_xpath = "//div[@class='ProfileHeader-infoItem'][2]/text()"
    headline = root.xpath(headline_xpath)
    avatar = root.xpath(avatar_xpath)[0]
    career = root.xpath(career_xpath)[0]
    education = " ".join(root.xpath(education_xpath))
