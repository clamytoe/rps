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
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        # How mature is this project? Common values are
        #   1 - Planning
        #   2 - Pre-Alpha
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        #   6 - Mature
        #   7 - Inactive
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6.6",
    ],
    keywords="python utility",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=["pytest>=3.6.2"],
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
