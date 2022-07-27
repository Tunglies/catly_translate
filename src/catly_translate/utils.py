import os
import re
import warnings

import execjs
import requests

from urllib import parse


def instance(func):
    def wrapper(*args, **kwargs):
        if not hasattr(func, "__instance"):
            setattr(func, "__instance", func(*args, **kwargs))
        return getattr(func, "__instance")
    return wrapper


@instance
class Client(requests.Session):
    def __init__(self) -> None:
        super().__init__()
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", }

        self.get("https://fanyi.baidu.com/")
        self.token = re.search(
            r"token: '(.*)'", self.get("https://fanyi.baidu.com/").text).group(1)


@instance
def __load_sign_js():
    root = os.path.abspath(os.path.dirname(__file__))
    js_file = os.path.join(root, "sign.js")
    with open(js_file, encoding="utf-8") as file:
        js_read = file.read()
    return js_read


def __calculate_sign(text):
    js_file = __load_sign_js()
    context = execjs.compile(js_file)
    result = context.call("e", text)
    return result


def __format_list_str_list(strings):
    return [(
            i.replace("\\U ", "_")
            .replace("\\U", "_")
            .replace("\\u", "_")
            .replace("\\u ", "_")
            ) for i in strings]


def __text_urlencode(text):
    encode = parse.urlencode({"query": text})
    return encode.split("query=")[1]


__client = Client()
__token = __client.token


def __post_translate(text, from_lang="en", to_lang="zh"):
    sign = __calculate_sign(text)
    text = __text_urlencode(text)

    url = f"https://fanyi.baidu.com/v2transapi?from={from_lang}&to={to_lang}&query={text}&transtype=translang&simple_means_flag=3&sign={sign}&token={__token}&domain=common"
    data = __client.post(url=url).json()
    return data


def __translate(text, from_lang="auto", to_lang="zh", limite_size=5000):
    if not isinstance(text, str):
        warnings.warn("translation text only support type of str")
        return text

    if len(text) > limite_size:
        warnings.warn("Baidu translation is limited to 5000 words")
        return text

    trans_result = __post_translate(text, from_lang, to_lang)
    print(trans_result)

    if not isinstance(trans_result, dict):
        raise(TypeError)

    if "trans_result" not in trans_result.keys():
        raise(KeyError)

    trans_data = trans_result["trans_result"]["data"]

    return __format_list_str_list((i["dst"] for i in trans_data))


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
    return __translate(text=text, from_lang=from_lang, to_lang=to_lang)
