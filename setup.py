from setuptools import setup, find_packages


with open('ReadMe.md') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    license = f.read()

setup(
    name='Data_Collector_MySQL',
    version='1.0',
    description='Python Flask Project',
    long_description=readme,
    author='Kumar Aditya',
    url='https://github.com/rahuladitya303/Data-Collector-MySQL',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)