import io
import re

from setuptools import setup

__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
    io.open('{{cookiecutter.package_name}}/__init__.py', encoding='utf_8_sig').read()
).group(1)

setup(
    name='{{cookiecutter.package_name}}',
    version=__version__,
    author='{{cookiecutter.author}}',
    packages=['{{cookiecutter.package_name}}'],
    long_description=open('README.md').read(),
    package_data={'{{cookiecutter.package_name}}': ['py.typed']}
)

