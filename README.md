# catly_translate

Simple &amp; Easy Way For Baidu Translation

Here're some basic usages.

```python
>>> import catly_translate
>>> catly_translate.translate("Hello")
['你好']
>>> catly_translate.translate("こんにちは")
['你好']
>>> catly_translate.translate("Hello\nWorld")
['你好', '世界']
>>> catly_translate.translate("こんにちは\r\n世界")
['你好', '世界']
```

The default setting is auto language to Chinese Simplified(zh).

```python
def translate(text: str, from_lang="auto", to_lang="zh") -> str:
    ...
```

from_lang=auto is suitable in most case, try change when translation not as expected.

You can also manualy specify keyword from_lang, to_lang or both.

```python
>>> catly_translate.translate("Hello", "en", "jp")
['こんにちは']
>>> catly_translate.translate("你好", to_lang="en")
['Hello']
>>> catly_translate.translate("你好", to_lang="jp")
['こんにちは']
```

\# Note: Max string length is 5000 per translation due to Baidu API limit. 
