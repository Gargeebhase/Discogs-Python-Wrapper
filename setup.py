import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="discogs-wrapper-python",
    version="1.0.1",
    packages=["discogs_wrapper"],
    description="This is a python API wrapper for the discogs API.",
    long_description=README,
    long_description_content_type="text/markdown",
    include_package_data=True,
    author="Gargee Bhase",
    author_email="gbhase2@gmail.com",
    license="MIT",
)