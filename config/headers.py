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
    "Cookies": 'tgw_l7_route=a37704a413efa26cf3f23813004f1a3b; _zap=429a399a-cef3-4765-bb25-7f150a18443c; _xsrf=wQiphBkFBvO1khtMEQzVZF4enEy3AVEQ; d_c0="AHDvcExeYxCPTousXDVQrutnothwaNgSGxQ=|1574326404"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1574326404; capsion_ticket="2|1:0|10:1574326437|14:capsion_ticket|44:YjQyNzhjNDg1OTNhNDBmODhhMzk1Mzc2MDI5Y2ZlODQ=|99b2a99a46876ee80f39f381be092b0f93619e15d55bf7aed1116af6caf69d96"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1574326443',
}
