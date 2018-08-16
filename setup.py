"""
setup.py

Setup for installing the package.
"""
from setuptools import setup, find_packages
from os import path
from io import open

import rps

VERSION = rps.__version__
AUTHOR = rps.__author__
EMAIL = rps.__email__

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="rps",
    version=VERSION,
    description="RPS game that I created during my 100 Days of Code challenge (rps)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/clamytoe/rps",
    author=AUTHOR,
    author_email=EMAIL,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6.6",
    ],
    keywords="python utility",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=["pillow>=5.2.0", "pytest>=3.6.2"],
    license="MIT",
    entry_points={
        "console_scripts": [
            "rps=rps.app:main"
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/clamytoe/rps/issues',
        'Source': 'https://github.com/clamytoe/rps/',
    },
)
