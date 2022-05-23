from src import catly_translate
print(catly_translate.__translate("hello world"))
# print(catly_translate.__version__)


from src.catly_translate import __translate
text = "hello world"
print(__translate(text))
text = "hello\n world"
print(__translate(text))
text = "hello\r\nworld"
print(__translate(text))
text = """
hello world
this is CatNeverCodes
"""
print(__translate(text))

print(__translate("你好", "zh", "en"))
print(__translate("你好", from_lang="zh", to_lang="en"))