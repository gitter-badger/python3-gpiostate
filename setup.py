from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup

classifiers = ['Development Status :: Beta',
               'Operating System :: POSIX :: Linux',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development']

setup(
    name             = 'gpiostate',
    version          = '0.1b',
    author           = 'scott snyder',
    author_email     = 'scott@growmaster420.com',
    py_modules       = ['ez_setup'],
    url              = 'https://github.com/growmaster420/python3-gpiostate',
    keywords         = 'gpiostate',
    packages         = find_packages()
)