from src import catly_translate
from src.catly_translate import utils

client = catly_translate.utils.Client()
print(client.token)
client = catly_translate.utils.Client()
print(client.token)


# utils.load_sign_js()

# import catly_translate

print(catly_translate.translate("hello"))