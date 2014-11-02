from setuptools import setup, find_packages

setup(
    name = 'sleep-after',
    version = '0.1.0',
    author = 'Alfred Dominic',
    author_email = 'alfie.2012@gmail.com',
    packages = find_packages(exclude=[]),
    scripts = ['sleep-after'],
    url = 'https://github.com/alfie-max/sleep-after',
    description = 'Program to put your system to sleep/suspend',
    long_description = open('README.md').read(),
)
