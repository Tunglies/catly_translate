import setuptools
from src.catly_translate import __version__


setuptools.setup(
    name="catly_translate",
    version=__version__,
    author="CatNeverCodes",
    author_email="574469831@qq.com",
    description="Simple & Easy Way For BAIDU Translation",
    url="https://github.com/CatNeverCodes/catly_translate",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data=True,
    package_data={"src": ["sign.js"]},
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
)