import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from config.headers import headers
from logger import crawler
from utils.get_proxy import get_proxy


def requests_retry_session(
    retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504, 404), session=None,
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
    resp = requests_retry_session().get(url, headers=headers)

    return resp.text


def get_requests(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
        "cookies": 'tgw_l7_route=a37704a413efa26cf3f23813004f1a3b; _zap=429a399a-cef3-4765-bb25-7f150a18443c; _xsrf=wQiphBkFBvO1khtMEQzVZF4enEy3AVEQ; d_c0="AHDvcExeYxCPTousXDVQrutnothwaNgSGxQ=|1574326404"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1574326404; capsion_ticket="2|1:0|10:1574326437|14:capsion_ticket|44:YjQyNzhjNDg1OTNhNDBmODhhMzk1Mzc2MDI5Y2ZlODQ=|99b2a99a46876ee80f39f381be092b0f93619e15d55bf7aed1116af6caf69d96"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1574326443',
    }

    resp = requests.get(url, headers=headers)

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
