from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='apache-airflow-testing',  # Required
    version='0.0.1',
    description='',

    classifiers=[
        'Programming Language :: Python :: 3.4'
    ],

    packages=find_packages(include=['dags']),  # Required

    install_requires=['pytest'],
)