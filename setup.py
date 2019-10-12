from setuptools import setup, find_packages
from os import path
from io import open

with open(path.join('README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PythonClienforApiSelectel',
    version='0.0.1',
    description='Sorry, it`s first version ...',
    long_description=f.read("README.md"),
    author='We all the AUTHOR',
    author_email=None,
    license=None,
    url='https://github.com/xRocketPowerx/python-sel-dedicated',
    packages=find_packages(exclude=["tests.*", "tests"]),
    classifiers=[
        "Development Status :: Pre - complete",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python, GO",
        "Framework :: Requests, Swagger",
    ]
)
