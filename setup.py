import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='bleach-whitelist',
    version='0.0.10',
    packages=['bleach_whitelist'],
    include_package_data=True,
    license='BSD License',
    description='Curated lists of tags and attributes for sanitizing html',
    long_description=README,
    url="https://github.com/yourcelf/bleach-whitelist.git",
    author="Charlie DeTar",
    author_email="cfd@media.mit.edu",
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ]
)
