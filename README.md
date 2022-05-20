# catly_translate

Simple &amp; Easy Way For BAIDU Translation



Here's some example.

```python
>>> import catly_translate
>>> catly_translate.translate("Hello")
['你好']
>>> catly_translate.translate("Hello\nWorld")
['你好', '世界']
>>> catly_translate.translate("Hello\r\nWorld")
['你好', '世界']
```

The default setting is from English(en) to Chinese Simplified(zh).

Switchable language with change keyword 'from_lang' and 'to_lang'.

```python
>>> catly_translate.translate("你好", "zh", "en")
['Hello']
>>> catly_translate.translate("你好\n世界", from_lang="zh", to_lang="en")
['Hello', 'world']
>>> catly_translate.translate("你好", from_lang="zh", to_lang="jp")
['こんにちは']
>>> catly_translate.translate("hello", from_lang="en", to_lang="jp")
['こんにちは']
```
