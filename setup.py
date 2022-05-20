import os
import requests
import setuptools



version = requests.get("https://pypi.org/pypi/catly-translate/json").json()["info"]["version"]
v0, v1, v2 = map(int, version.split("."))
if v2 < 10:
    v2 += 1
else:
    v1 += 1
    v2 = 0
if v1 > 10:
    v0 += 1
    v1 = 0
version = ".".join(map(str, [v0, v1, v2]))

with open("src/catly_translate/__version.py", "w+") as file:
    file.write(f'version = "{version}"')

with open("requirements.txt", encoding="UTF-8") as file:
    install_requires = [i[:-1] for i in file.readlines()]
    
if os.path.isdir("build"):
    os.removedirs("build")
if os.path.isdir("dist"):
    os.removedirs("dist")

setuptools.setup(
    name="catly_translate",
    version=version,
    author="CatNeverCodes",
    author_email="574469831@qq.com",
    description="Simple & Easy Way For BAIDU Translation",
    long_description=open("README.md", encoding="utf-8"),
    url="https://github.com/CatNeverCodes/catly_translate",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
    package_data={
        "": ["*.js"]
    },
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    install_requires=install_requires,
    keywords=["translate", "translation", "baidu", "BAIDU", "百度翻译", "baidu translate"]
)