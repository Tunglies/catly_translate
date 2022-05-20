import os
import execjs
import requests



ROOT = os.path.abspath(os.path.dirname(__file__))

js_sign = os.path.join(ROOT, "sign.js")
with open(js_sign, encoding="utf-8") as file:
    js_sign_read = file.read()


def get_sign(text):
    script = execjs.compile(js_sign_read).call("e", text)
    return script


def get_origin(text, from_lang="en", to_lang="zh"):
    url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
    sign = get_sign(text)
    payload = {
            "from": from_lang,
            "to": to_lang,
            "query": text,
            "transtype": "translang",
            "simple_means_flag": "3",
            "sign": sign,
            "token": "cdc85dad1e2fe957623b9bc2f7313790",
            "domain": "common"}
    headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'BIDUPSID=B3C026FB0ABD19E71BEB9BBC668EEA2A; PSTM=1648130971; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=B8F64E527183F2EBC58418162BC5638A:FG=1; MCITY=-%3A; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; BA_HECTOR=24ala5a0050120a4251h8cosh14; ZFY=dllBJYUQ8l:BUzqA7zaI9cM:BeFYE0JLDy8WmXs5eD23g:C; BDUSS_BFESS=d6bTJ-dTBZbVpZZFdrbzNzZHhQaUJLcWdlcWhFTjdrSmRta0xDS2F1R084YTFpRUFBQUFBJCQAAAAAAAAAAAEAAABpMnU~REpDcmFmdAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI5khmKOZIZiTU; RT="z=1&dm=baidu.com&si=4ible4eax2w&ss=l3d6go2h&sl=e&tt=6uz&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=3o66&ul=3oxm&hd=3p7h"; BAIDUID_BFESS=5049F14EB0249B116C95E4A07841F142:FG=1; delPer=0; PSINO=6; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1652782674,1652875126,1652974483,1653022520; H_PS_PSSID=36425_36454_31253_36452_36422_36166_35978_36055_36418_36345_26350_22158_36447; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1653024185; ab_sr=1.0.1_YTEyMTA2NzllMTk5MjRmOGM2NTIyOGJhZWM1ZmEzZWNhOGZiMTE3NmIwNTZkM2ZkNGU5ZDA0YmMwNzFmZDkwODI5NzcyNWFiMDU1M2Y1NGM4ZmQxNzFhYTg5NDc4M2M2Nzg1MDliMjUxYmIwNTQ1NGI4YmFlZjlmNDI0MTA0NmQ0YWRhOTg2N2NmNGM2MTEyMmNhM2RmMjBkNWJmYThmOTVjOWMzOTJmMTI2MmYyYzI5ZGQ1M2NlMDY4ZDdlNWNh; BAIDUID=E60E7E1673689E2056E064C6A83895EE:FG=1',
            'Origin': 'https://fanyi.baidu.com',
            'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'}
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()


def translate(text, from_lang="en", to_lang="zh"):
    trans_result = get_origin(text, from_lang, to_lang)["trans_result"]["data"]
    return [
        (
            i["dst"]
            .replace("\\U ", "_")
            .replace("\\U", "_")
            .replace("\\u", "_")
            .replace("\\u ", "_")
            
        ) for i in trans_result]
    

if __name__ == "__main__":
    text = "hello world"
    print(translate(text))
    text = "hello\n world"
    print(translate(text))
    text = "hello\r\nworld"
    print(translate(text))
    text = """
    hello world
    this is CatNeverCodes
    """
    print(translate(text))