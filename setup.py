import setuptools
import catly_translate


setuptools.setup(
    name="catly_translate",
    version=catly_translate.__version__,
    author="CatNeverCodes",
    author_email="574469831@qq.com",
    description="Simple & Easy Way For BAIDU Translation",
    url="https://github.com/CatNeverCodes/catly_translate",
    package_dir={"":"catly_translate"},
    packages=setuptools.find_packages("catly_translate"),
    include_package_data=True,
    package_data={"": ["*.js"]},
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)