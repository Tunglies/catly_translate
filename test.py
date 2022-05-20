from src import catly_translate
print(catly_translate.translate("hello world"))
# print(catly_translate.__version__)


from src.catly_translate import translate
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

print(translate("你好", "zh", "en"))
print(translate("你好", from_lang="zh", to_lang="en"))