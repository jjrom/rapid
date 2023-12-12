from setuptools import find_packages, setup

setup(
    name='rapid',
    packages=find_packages(include=['rapid']),
    version='1.0.0',
    description='resto python API',
    author='Jérôme Gasperi',
    install_requires=[
        "requests"
    ],
    setup_requires=['pytest-runner'],
)