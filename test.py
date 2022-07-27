# from src import catly_translate
from src.catly_translate import utils


# utils.load_sign_js()

# import catly_translate



client = utils.Client()
print(client.token, client.gtk)
# print(client.client.headers, client.client.cookies.items())
print(client.translate("hello"))

# from urllib import parse

# data = {
# "from": "en",
# "to": "zh",
# "query": "hello world",
# "transtype": "translang",
# "simple_means_flag": "3",
# "sign": "288018.34339",
# "token": "cea6c99ce31241ff66f23f8292c4c304",
# "domain": "common"}
# encode = parse.urlencode(data)
# print(encode)

# print(parse.urljoin("https://fanyi.baidu.com/v2transapi?", encode))