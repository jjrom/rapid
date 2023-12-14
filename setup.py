from setuptools import find_packages, setup

setup(
    name='jjromrapid',
    packages=find_packages(include=['rapid']),
    version='0.0.3',
    description='resto python API',
    author='Jérôme Gasperi',
    install_requires=[
        "requests"
    ]
)