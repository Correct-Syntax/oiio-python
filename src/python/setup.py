"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Prefer setuptools over distutils
from setuptools import setup
from setuptools import find_packages

setup(
    name="oiio",
    version="PACKAGE_VERSION",
    description="OpenImageIO Python package",
    url="https://github.com/Correct-Syntax/oiio-python",

    # https://pypi.org/classifiers/
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    packages=find_packages(exclude=[]),
    package_data={
        # If any package (!) contains ... files, include them:
        "": [
            "*.pyd",
            "*.dll",
            "*.so",
        ]
    },
)
