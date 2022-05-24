import os
import execjs
import requests
import warnings


def __load_sign_js():
    if not hasattr(__load_sign_js, "__instance"):
        root = os.path.abspath(os.path.dirname(__file__))
        js_file = os.path.join(root, "sign.js")
        
        with open(js_file, encoding="utf-8") as file:
            js_read = file.read()
        setattr(__load_sign_js, "__instance", js_read)

    return getattr(__load_sign_js, "__instance")


def __calculate_sign(text):
    js_file = __load_sign_js()
    script = execjs.compile(js_file).call("e", text)
    return script


def __format_list_str_list(strings):
    return [(
            i.replace("\\U ", "_")
            .replace("\\U", "_")
            .replace("\\u", "_")
            .replace("\\u ", "_")
            ) for i in strings]


def __post_translate(text, from_lang="en", to_lang="zh"):
    sign = __calculate_sign(text)
    url = f"https://fanyi.baidu.com/v2transapi?from={from_lang}&to={to_lang}&query={text}&transtype=translang&simple_means_flag=3&sign={sign}&token=cdc85dad1e2fe957623b9bc2f7313790&domain=common"
    headers = {
            'Cookie': 'BIDUPSID=B3C026FB0ABD19E71BEB9BBC668EEA2A; PSTM=1648130971; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=B8F64E527183F2EBC58418162BC5638A:FG=1; MCITY=-%3A; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; BA_HECTOR=24ala5a0050120a4251h8cosh14; ZFY=dllBJYUQ8l:BUzqA7zaI9cM:BeFYE0JLDy8WmXs5eD23g:C; BDUSS_BFESS=d6bTJ-dTBZbVpZZFdrbzNzZHhQaUJLcWdlcWhFTjdrSmRta0xDS2F1R084YTFpRUFBQUFBJCQAAAAAAAAAAAEAAABpMnU~REpDcmFmdAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI5khmKOZIZiTU; RT="z=1&dm=baidu.com&si=4ible4eax2w&ss=l3d6go2h&sl=e&tt=6uz&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=3o66&ul=3oxm&hd=3p7h"; BAIDUID_BFESS=5049F14EB0249B116C95E4A07841F142:FG=1; delPer=0; PSINO=6; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1652782674,1652875126,1652974483,1653022520; H_PS_PSSID=36425_36454_31253_36452_36422_36166_35978_36055_36418_36345_26350_22158_36447; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1653024185; ab_sr=1.0.1_YTEyMTA2NzllMTk5MjRmOGM2NTIyOGJhZWM1ZmEzZWNhOGZiMTE3NmIwNTZkM2ZkNGU5ZDA0YmMwNzFmZDkwODI5NzcyNWFiMDU1M2Y1NGM4ZmQxNzFhYTg5NDc4M2M2Nzg1MDliMjUxYmIwNTQ1NGI4YmFlZjlmNDI0MTA0NmQ0YWRhOTg2N2NmNGM2MTEyMmNhM2RmMjBkNWJmYThmOTVjOWMzOTJmMTI2MmYyYzI5ZGQ1M2NlMDY4ZDdlNWNh; BAIDUID=E60E7E1673689E2056E064C6A83895EE:FG=1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',}
    data = requests.post(url, headers=headers).json()
    return data


def __translate(text, from_lang="auto", to_lang="zh", limite_size=5000):
    if not isinstance(text, str):
        warnings.warn("translation text only support type of str")
        return text

    if len(text) > limite_size:
        warnings.warn("Baidu translation is limited to 5000 words")
        return text

    trans_result = __post_translate(text, from_lang, to_lang)
    
    if "trans_result" not in trans_result.keys():
        warnings.warn("translation faild due to somehow")
    
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