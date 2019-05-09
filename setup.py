import io
from os import path
from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    README = f.read()

# This call to setup() does all the work
setup(
    name="tikz2graphml",
    version="1.1.1",
    description="Convert Latex Tikz code into yed graphml",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ysahil97/tikz-to-yed-graphml",
    author="Harsh Agarwal",
    author_email="harshaga97@gmail.com",
    # license="Apache License 2.0",
    # classifiers=[
    #     "License :: OSI Approved :: MIT License",
    #     "Programming Language :: Python :: 3",
    #     "Programming Language :: Python :: 3.7",
    # ],
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    include_package_data=True,
    install_requires=[
        "colour==0.1.5",
        "numpy==1.16.2",
        "networkx==2.3",
        "matplotlib==3.0.3",
        "pylatexenc==1.4",
        "antlr4-python3-runtime==4.7.2"
    ],
    entry_points={
        "console_scripts": [
            "tikz2graphml=tikz2graphml.__main__:main",
        ]
    }
)
