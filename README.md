# catly_translate

Simple &amp; Easy Way For BAIDU Translation

Here's some example.

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

The default setting is Auto language to Chinese Simplified(zh).

Switchable language by change keyword 'from_lang' and 'to_lang'.

```python
>>> catly_translate.translate("Hello", "auto", "zh")
['你好']
>>> catly_translate.translate("你好", "zh", "en")
['Hello']

```
