import random

first_num = random.randint(55, 62)
third_num = random.randint(0, 3200)
fourth_num = random.randint(0, 140)


class FakeChromeUA:
    os_type = [
        "(Windows NT 6.1; WOW64)",
        "(Windows NT 10.0; WOW64)",
        "(X11; Linux x86_64)",
        "(Macintosh; Intel Mac OS X 10_12_6)",
    ]

    chrome_version = "Chrome/{}.0.{}.{}".format(first_num, third_num, fourth_num)

    @classmethod
    def get_ua(cls):
        return " ".join(
            [
                "Mozilla/5.0",
                random.choice(cls.os_type),
                "AppleWebKit/537.36",
                "(KHTML, like Gecko)",
                cls.chrome_version,
                "Safari/537.36",
            ]
        )


headers = {
    "User-Agent": FakeChromeUA.get_ua(),
    "Cookies": 'tgw_l7_route=5966d81f231983c5ed4f6d32ecde8ac5; _zap=46573718-fe42-4030-abac-90ef946efb09; _xsrf=8594c9c6-7b2e-4df2-86b6-94f48883b2a5; d_c0="AOBujCeJaBCPTv7Z59FfVCxq4e2G04lHKig=|1574673183"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1574673189; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1574673189',
}
