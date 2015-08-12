from setuptools import setup, find_packages
from io import open

setup(
    name='MP_Sliding_Window',
    version='0.0.1',
    author='Jorge Alpedrinha Ramos',
    author_email='jalpedrinharamos@gmail.com',
    packages=find_packages(),
    license='LICENSE.txt',
    description='Multiprocessing Based Sliding window ',
    long_description=open('README.rst').read(),
    install_requires=[
    ],
)
