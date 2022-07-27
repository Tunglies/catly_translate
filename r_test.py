import requests
requests = requests.Session()

url = "https://fanyi.baidu.com/langdetect"
payload = "query=hello"
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
print(response.headers)
print(response.cookies.items())


url = "https://miao.baidu.com/abdr?_o=https%3A%2F%2Ffanyi.baidu.com"
payload = "{\"data\":\"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\",\"key_id\":\"560c28f2c82243fd\",\"enc\":2}"
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Cookie': 'BAIDUID=1E9F5A1717C3CEB1A9B887B36B41F4E7:FG=1; BAIDUID_BFESS=1E9F5A1717C3CEB1A9B887B36B41F4E7:FG=1; ab_sr=1.0.1_ODE3Y2E3MjhiYTNhMjQyODMyMWE2Y2Q0NDg3YzFlNTIzMWQ4MzJkNTA4YzAxYTEyZWM1MjQ1ZTE5MzIyYjVkYmNiNTM0ZmQ4ZjNiYjA2Y2EzNDljMjIzODY1YjAyZTZhYzg1ZTRiNTUzYzJiNjVkYzQ0ODhmMDBkZjJlMTIyZTAxNTk0ZDI5ZjdlYjY2ODA4MDk4MWNmOWJlOTUzYmM0MA==; ab_bid=3baf4f564fdaf680fe2f553e1aa0f2ea3b64; ab_jid=3baf4f564fdaf680fe2f553e1aa0f2ea3b64; ab_jid_BFESS=3baf4f564fdaf680fe2f553e1aa0f2ea3b64'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
print(response.headers)
print(response.cookies.items())


url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
payload = "from=en&to=zh&query=hello&transtype=translang&simple_means_flag=3&sign=54706.276099&token=29748beea4bafeaab162686e49b3caea&domain=common"
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Acs-Token': '1658905209008_1658943264651_KtoM/F8kVSM5FqyRXd2kxe7dcVdw1Ib2Csxjj+5GIeaIZxLS5wSdnb6+pt9BwHNw6U63N8u0qKyvNVX7DbzHkgt72DzvksGtX4xkEiWEjbmHfxbENF3TQmROezTYBmgu6ga8lceA/k2YcrfGl9pyPK9gn4qaC+tjDTJGN38u+tMN47v+5R+C2zb+FDoD8LEFZCddBjmJ069Pi7jzzt8HOhHIMjpxS+2y2mb1uUBHdcntThhSWXg6dvCUyKNu6sbbRtVgIuuA9SCQIkxYFnSlIU3b0+kvmQhHnwS5TdzJSxtaa9CeQjhx26oBH/MoV6wu',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'ab_sr=1.0.1_YzAwZmYyOGY0NDI4NjRiOWJiYTRkMDUyMzZiNDA2YmUwNjIxYTc3MzE1NTk3ZTVlYzFkMGY3ZWRmMGQ5ZTEzNjYyOTQ0Y2E0OGZjZTVmZDRhZWIzNTZjZWUxMjRjOTk4MGViZTAzYzcyZTNhZTViYzU4Y2E0NGZlZDAyMjhjMWRmMzJmOGExYzZmOTMyYTRlZDRhNTBhZWQwN2Q4Y2ZkZg==; BAIDUID=99208733CEFDA039A5AEA0BD92DB2520:FG=1; BAIDUID_BFESS=99208733CEFDA039A5AEA0BD92DB2520:FG=1; BAIDUID=1E9F5A1717C3CEB1A9B887B36B41F4E7:FG=1; BAIDUID_BFESS=1E9F5A1717C3CEB1A9B887B36B41F4E7:FG=1; ab_sr=1.0.1_ODE3Y2E3MjhiYTNhMjQyODMyMWE2Y2Q0NDg3YzFlNTIzMWQ4MzJkNTA4YzAxYTEyZWM1MjQ1ZTE5MzIyYjVkYmNiNTM0ZmQ4ZjNiYjA2Y2EzNDljMjIzODY1YjAyZTZhYzg1ZTRiNTUzYzJiNjVkYzQ0ODhmMDBkZjJlMTIyZTAxNTk0ZDI5ZjdlYjY2ODA4MDk4MWNmOWJlOTUzYmM0MA==',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
print(response.headers)
print(response.cookies.items())

url = "https://fanyi.baidu.com/track"
payload = 'key=web_error_report&params=%7B%22information%22%3A%22errno%3A%20998%20en%20zh%20hello%22%7D&sign=08d6e19ac34e02baf61d8a71d5fcd6a2'
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'ab_sr=1.0.1_YzAwZmYyOGY0NDI4NjRiOWJiYTRkMDUyMzZiNDA2YmUwNjIxYTc3MzE1NTk3ZTVlYzFkMGY3ZWRmMGQ5ZTEzNjYyOTQ0Y2E0OGZjZTVmZDRhZWIzNTZjZWUxMjRjOTk4MGViZTAzYzcyZTNhZTViYzU4Y2E0NGZlZDAyMjhjMWRmMzJmOGExYzZmOTMyYTRlZDRhNTBhZWQwN2Q4Y2ZkZg==; BAIDUID=99208733CEFDA039A5AEA0BD92DB2520:FG=1; BAIDUID_BFESS=99208733CEFDA039A5AEA0BD92DB2520:FG=1; BAIDUID=1E9F5A1717C3CEB1A9B887B36B41F4E7:FG=1; BAIDUID_BFESS=1E9F5A1717C3CEB1A9B887B36B41F4E7:FG=1; ab_sr=1.0.1_ODE3Y2E3MjhiYTNhMjQyODMyMWE2Y2Q0NDg3YzFlNTIzMWQ4MzJkNTA4YzAxYTEyZWM1MjQ1ZTE5MzIyYjVkYmNiNTM0ZmQ4ZjNiYjA2Y2EzNDljMjIzODY1YjAyZTZhYzg1ZTRiNTUzYzJiNjVkYzQ0ODhmMDBkZjJlMTIyZTAxNTk0ZDI5ZjdlYjY2ODA4MDk4MWNmOWJlOTUzYmM0MA==',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
print(response.headers)
print(response.cookies.items())

url = "https://fanyi.baidu.com/"
response = requests.request("get", url)
print(response.text)
print(response.headers)
print(response.cookies.items())

url = "https://fanyi.baidu.com/langdetect"
payload = "query=hello"
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'ab_sr=1.0.1_YzAwZmYyOGY0NDI4NjRiOWJiYTRkMDUyMzZiNDA2YmUwNjIxYTc3MzE1NTk3ZTVlYzFkMGY3ZWRmMGQ5ZTEzNjYyOTQ0Y2E0OGZjZTVmZDRhZWIzNTZjZWUxMjRjOTk4MGViZTAzYzcyZTNhZTViYzU4Y2E0NGZlZDAyMjhjMWRmMzJmOGExYzZmOTMyYTRlZDRhNTBhZWQwN2Q4Y2ZkZg==; BAIDUID=99208733CEFDA039A5AEA0BD92DB2520:FG=1; BAIDUID_BFESS=99208733CEFDA039A5AEA0BD92DB2520:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1658835806,1658892296,1658918117,1658942571; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1658943265; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=1E9F5A1717C3CEB1A9B887B36B41F4E7:FG=1; BAIDUID_BFESS=1E9F5A1717C3CEB1A9B887B36B41F4E7:FG=1; ab_sr=1.0.1_ODE3Y2E3MjhiYTNhMjQyODMyMWE2Y2Q0NDg3YzFlNTIzMWQ4MzJkNTA4YzAxYTEyZWM1MjQ1ZTE5MzIyYjVkYmNiNTM0ZmQ4ZjNiYjA2Y2EzNDljMjIzODY1YjAyZTZhYzg1ZTRiNTUzYzJiNjVkYzQ0ODhmMDBkZjJlMTIyZTAxNTk0ZDI5ZjdlYjY2ODA4MDk4MWNmOWJlOTUzYmM0MA==',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}
response = requests.request("get", url)
print(response.text)
print(response.headers)
print(response.cookies.items())

url = "https://miao.baidu.com/abdr?_o=https%3A%2F%2Ffanyi.baidu.com"
payload = "{\"data\":\"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\",\"key_id\":\"560c28f2c82243fd\",\"enc\":2}"
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Cookie': 'ab_jid=4a09d38d96ddbe8e2434be3dfe8a39979de9; ab_bid=4a09d38d96ddbe8e2434be3dfe8a39979de9; ab_sr=1.0.1_YzAwZmYyOGY0NDI4NjRiOWJiYTRkMDUyMzZiNDA2YmUwNjIxYTc3MzE1NTk3ZTVlYzFkMGY3ZWRmMGQ5ZTEzNjYyOTQ0Y2E0OGZjZTVmZDRhZWIzNTZjZWUxMjRjOTk4MGViZTAzYzcyZTNhZTViYzU4Y2E0NGZlZDAyMjhjMWRmMzJmOGExYzZmOTMyYTRlZDRhNTBhZWQwN2Q4Y2ZkZg==; ab_jid_BFESS=4a09d38d96ddbe8e2434be3dfe8a39979de9; BAIDUID=99208733CEFDA039A5AEA0BD92DB2520:FG=1; BAIDUID_BFESS=99208733CEFDA039A5AEA0BD92DB2520:FG=1; BAIDUID=1E9F5A1717C3CEB1A9B887B36B41F4E7:FG=1; BAIDUID_BFESS=1E9F5A1717C3CEB1A9B887B36B41F4E7:FG=1; ab_sr=1.0.1_ODE3Y2E3MjhiYTNhMjQyODMyMWE2Y2Q0NDg3YzFlNTIzMWQ4MzJkNTA4YzAxYTEyZWM1MjQ1ZTE5MzIyYjVkYmNiNTM0ZmQ4ZjNiYjA2Y2EzNDljMjIzODY1YjAyZTZhYzg1ZTRiNTUzYzJiNjVkYzQ0ODhmMDBkZjJlMTIyZTAxNTk0ZDI5ZjdlYjY2ODA4MDk4MWNmOWJlOTUzYmM0MA==; ab_bid=3baf4f564fdaf680fe2f553e1aa0f2ea3b64; ab_jid=3baf4f564fdaf680fe2f553e1aa0f2ea3b64; ab_jid_BFESS=3baf4f564fdaf680fe2f553e1aa0f2ea3b64',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}
print(response.text)
print(response.headers)
print(response.cookies.items())


url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
payload = "from=en&to=zh&query=hello&simple_means_flag=3&sign=54706.276099&token=0978a5de984ac79a7b3c45cf8c92651f&domain=common"
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Acs-Token': '1658905209008_1658943265655_KtoM/F8kVSM5FqyRXd2kxe7dcVdw1Ib2Csxjj+5GIeaIZxLS5wSdnb6+pt9BwHNw6U63N8u0qKyvNVX7DbzHkgt72DzvksGtX4xkEiWEjbmHfxbENF3TQmROezTYBmgu6ga8lceA/k2YcrfGl9pyPK9gn4qaC+tjDTJGN38u+tMN47v+5R+C2zb+FDoD8LEFZCddBjmJ069Pi7jzzt8HOhHIMjpxS+2y2mb1uUBHdcntThhSWXg6dvCUyKNu6sbbnCjZMQ8Uzcvg2BGm7/q3xSaXjtLBpT6YLhutUlzdwjaF7PrPgEDYlhuv5azhXd2u',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'ab_sr=1.0.1_YzAwZmYyOGY0NDI4NjRiOWJiYTRkMDUyMzZiNDA2YmUwNjIxYTc3MzE1NTk3ZTVlYzFkMGY3ZWRmMGQ5ZTEzNjYyOTQ0Y2E0OGZjZTVmZDRhZWIzNTZjZWUxMjRjOTk4MGViZTAzYzcyZTNhZTViYzU4Y2E0NGZlZDAyMjhjMWRmMzJmOGExYzZmOTMyYTRlZDRhNTBhZWQwN2Q4Y2ZkZg==; BAIDUID=99208733CEFDA039A5AEA0BD92DB2520:FG=1; BAIDUID_BFESS=99208733CEFDA039A5AEA0BD92DB2520:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1658835806,1658892296,1658918117,1658942571; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1658943265; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=1E9F5A1717C3CEB1A9B887B36B41F4E7:FG=1; BAIDUID_BFESS=1E9F5A1717C3CEB1A9B887B36B41F4E7:FG=1; ab_sr=1.0.1_ODE3Y2E3MjhiYTNhMjQyODMyMWE2Y2Q0NDg3YzFlNTIzMWQ4MzJkNTA4YzAxYTEyZWM1MjQ1ZTE5MzIyYjVkYmNiNTM0ZmQ4ZjNiYjA2Y2EzNDljMjIzODY1YjAyZTZhYzg1ZTRiNTUzYzJiNjVkYzQ0ODhmMDBkZjJlMTIyZTAxNTk0ZDI5ZjdlYjY2ODA4MDk4MWNmOWJlOTUzYmM0MA==',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

print(response.text)
print(response.headers)
print(response.cookies.items())
print(response.json())
