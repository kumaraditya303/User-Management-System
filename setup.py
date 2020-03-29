from distutils.core import setup
from setuptools import find_packages
setup(
    # Application name:
    name="Data Collector using SQLite3",

    # Version number (initial):
    version="0.1",

    # Application author details:
    author="Kumar Aditya",
    author_email="https://www.github.com/rahuladitya303",

    # Packages
    packages=find_packages(),

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/rahuladitya303/Data-Collector-SQLite",


    license=open("LICENSE").read(),
    description="This is Flask Project ",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',

    # Dependent packages (distributions)
    install_requires=[
        "flask",
        "flask_mail",
    ],
    python_requires='>3.0',
    platforms=['any'],
)
