import os
import re

import execjs
import httpx
# import requests

from urllib import parse


def instance(func):
    def wrapper(*args, **kwargs):
        if not hasattr(func, "__instance"):
            setattr(func, "__instance", func(*args, **kwargs))
        return getattr(func, "__instance")
    return wrapper


class Utils:
    @classmethod
    @instance
    def __load_sign_js(self):
        root = os.path.abspath(os.path.dirname(__file__))
        js_file = os.path.join(root, "sign.js")
        with open(js_file, encoding="utf-8") as file:
            js_read = file.read()
        return js_read

    @classmethod
    def __calculate_sign(self, text):
        js_file = self.__load_sign_js()
        context = execjs.compile(js_file)
        result = context.call("e", text)
        return result

    @classmethod
    def __format_list_str_list(self, strings):
        return [(
                i.replace("\\U ", "_")
                .replace("\\U", "_")
                .replace("\\u", "_")
                .replace("\\u ", "_")
                ) for i in strings]

    @classmethod
    def __text_urlencode(self, text):
        encode = parse.urlencode({"query": text})
        return encode.split("query=")[1]

    @classmethod
    def load_sign_js(self):
        return self.__load_sign_js()

    @classmethod
    def calculate_sign(self, text):
        return self.__calculate_sign(text)

    @classmethod
    def text_urlencode(self, text):
        return self.__text_urlencode(text)

    @classmethod
    def format_list_str_list(self, strings):
        return self.__format_list_str_list(strings)

    @classmethod
    def format_translated(self, trans):
        return self.format_list_str_list((i["dst"] for i in trans))


@instance
class Client(object):
    def __init__(self) -> None:
        super().__init__()
        # self.client = requests.Session()
        self.client = httpx.Client()
        self.client.headers = {
            "Accept": "*/*",
            "Connection": "keep-alive",
            "Acs-Token": "1658905209008_1658941773778_KtoM/F8kVSM5FqyRXd2kxe7dcVdw1Ib2Csxjj+5GIeaIZxLS5wSdnb6+pt9BwHNw6U63N8u0qKyvNVX7DbzHkgt72DzvksGtX4xkEiWEjbmHfxbENF3TQmROezTYBmgu6ga8lceA/k2YcrfGl9pyPK9gn4qaC+tjDTJGN38u+tMN47v+5R+C2zb+FDoD8LEFZCddBjmJ069Pi7jzzt8HOhFJBntD0o/3u+IhCpCEbY9d/Nb9tVgd91Xm49G8le5K0AkFsAWZz8eQZcZ2fcjabFrkd0QskcSTIAy4vbc0sORkXxxGsdz5HnGyb0IojRAr",
            "Cookie": "BAIDUID=0C95A66D7AB4D4A17AD6E98E5C3C3D07:FG=1; BAIDUID_BFESS=0C95A66D7AB4D4A17AD6E98E5C3C3D07:FG=1;",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", }

        self.token = None
        self.gtk = None

        self.__load_main_page()
        self.__load_main_page()

    def __load_main_page(self):
        url = "https://fanyi.baidu.com"
        response = self.client.get(url=url)
        self.token = re.search(pattern=r"token: '(.*)'",
                               string=response.text).group(1)
        self.gtk = re.search(pattern=r'window.gtk = "(.*)";',
                             string=response.text).group(1)

    def __langdetect(self, text):
        query = Utils.text_urlencode(text)
        url = f"https://fanyi.baidu.com/langdetect?query={query}"
        response = self.client.post(url=url).json()
        return response["lan"]

    def __translate(self, text, from_lang="auto", to_lang="zh", limite_size=5000):
        assert isinstance(text, str)
        assert len(text) < limite_size
        assert isinstance(from_lang, str)
        assert isinstance(to_lang, str)

        sign = Utils.calculate_sign(text)
        lang = self.__langdetect(text)
        if lang == "zh":
            text = Utils.text_urlencode(text)
        
        
        url = "https://fanyi.baidu.com/v2transapi"
        payload = {
            "from": from_lang,
            "to": to_lang,
            "query": text,
            "token": self.token,
            "sign": sign,
            "domain": "common",
            "transtype": "translang",
            "simple_means_flag": "3"}
        response = self.client.post(url=url, data=payload).json()

        assert "trans_result" in response.keys()

        trans_result = response["trans_result"]
        data = trans_result["data"]
        formated = Utils.format_translated(data)
        return formated

    def translate(self, text, from_lang="auto", to_lang="zh"):
        return self.__translate(text, from_lang=from_lang, to_lang=to_lang)


def translate(text: str, from_lang="auto", to_lang="zh") -> str:
    r"""
    ### Here're some basic usages.
    >>> import catly_translate
    >>> catly_translate.translate("Hello")
    ['你好']
    >>> catly_translate.translate("こんにちは")
    ['你好']
    >>> catly_translate.translate("Hello\nWorld")
    ['你好', '世界']
    >>> catly_translate.translate("こんにちは\r\n世界")
    ['你好', '世界']

    ### You can manualy specify keyword from_lang, to_lang or both.
    >>> catly_translate.translate("Hello", "en", "jp")
    ['こんにちは']
    >>> catly_translate.translate("你好", to_lang="en")
    ['Hello']
    >>> catly_translate.translate("你好", to_lang="jp")
    ['こんにちは']
    """
    client = Client()
    return client.translate(text=text, from_lang=from_lang, to_lang=to_lang)
