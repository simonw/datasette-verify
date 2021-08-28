from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-verify",
    description="Verify that SQLite files can be opened using Datasette",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-verify",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-verify/issues",
        "CI": "https://github.com/simonw/datasette-verify/actions",
        "Changelog": "https://github.com/simonw/datasette-verify/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_verify"],
    entry_points={"datasette": ["verify = datasette_verify"]},
    install_requires=["datasette>=0.59a2"],
    extras_require={"test": ["pytest"]},
    tests_require=["datasette-verify[test]"],
    python_requires=">=3.6",
)
